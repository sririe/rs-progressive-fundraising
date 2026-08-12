# Wave 1 security findings — Claude lane (AuthN/AuthZ · WordPress-intake authZ · Audit/config/infra)

- **Target:** `/Users/spencer/projects-work/progressive-card-vault/app` @ `08c0c74` (verified HEAD).
- **Lenses:** (2) AuthN/AuthZ/access-scoping, (4-WP) WordPress signed-intake authZ, (5) Audit-log integrity + config/infra.
- **Method:** static source read (primary) + three local, non-network dynamic checks (labeled *local-exec* below). No traffic to the Render host. Read-only; no edits/branches.
- **Headline:** The access-control boundary is **well-built** — no P0 in my lenses. Card secrets decrypt in exactly two role-gated, audited download routes; every page and server action enforces its own `requireUser`/`requireRole`; the audit log has no app-level update/delete path; prod CSP and fail-closed secrets are real. Findings are availability, config-integrity, WordPress-intake hardening, and defense-in-depth.

---

## 1. Coverage

### Inspected (lens 2 — AuthN/AuthZ)
- `src/lib/auth.ts`, `session-token.ts`, `session-cookie.ts`, `permissions.ts`, `card-scope.ts`, `password.ts`, `login-attempts.ts`.
- `src/app/api/auth/login/route.ts`, `src/app/logout/route.ts`, `src/proxy.ts` (this Next fork's middleware — see §4 N1).
- **Every** route handler under `src/app/**/route.ts` (9 total) and **every** server action file (`src/app/**/actions.ts`, 9 files) — auth guard on each enumerated below.
- Every `page.tsx` (18) checked for a `requireUser`/`requireRole` guard.

### Inspected (lens 4-WP — WordPress intake)
- `src/app/api/integrations/wordpress/formidable/orders/route.ts`, `.../test/route.ts`.
- `src/lib/integrations/request-signature.ts`, `wordpress-connections.ts`.
- PHP mu-plugin `wordpress/mu-plugins/pro-gift-cards-vault-handoff.php` (full read).

### Inspected (lens 5 — audit/config/infra)
- `AuditLog`/`LoginAttempt` models (`prisma/schema.prisma`) + all `auditLog.create` writers (grep-enumerated) + mutation search.
- `next.config.ts`, `src/proxy.ts`, `render.yaml`, `scripts/seed-if-enabled.ts`, `src/lib/feature-flags.ts`, `src/lib/testing-package.ts`, `src/app/current-testing-instructions/**`.

### Could not fully cover / out of scope
- Runtime behavior on the live Render/Postgres box (not attacked, per lane floor). Prod uses `schema.postgres.prisma`; I read the sqlite `schema.prisma` — model shape assumed equivalent (not diffed line-by-line).
- Crypto internals of `card-secrets.ts`/`card-fields.ts`, CSV/Walmart parsing, export-crypto — **owned by the Codex lane**; I only traced their authZ entry points.

### Local-exec checks (no network)
- **LX1** — Node repro of the login `next` open-redirect normalization (finding P2-3). 
- **LX2** — confirmed Next.js version `16.2.6` and `PROXY_FILENAME = 'proxy'` in `node_modules/next/dist/lib/constants.js` (proves `src/proxy.ts` is the live middleware → N1 disposition).
- **LX3** — grep-enumeration of guards, `auditLog` mutations, `console.*`, raw SQL, and `WORDPRESS_INTAKE_ENABLED` usage.

---

## 2. Findings

### P0
None in lenses 2 / 4-WP / 5.

### P1

| id | lens | file:line | mechanism | exploit scenario | fix direction | confidence |
|----|------|-----------|-----------|------------------|---------------|------------|
| C-P1-1 | 2 | `src/lib/login-attempts.ts:20-28,62-88` | Lockout uses an **IP-independent** `account:<login>` key that trips after 8 failures in 15 min → 10-min lock, in addition to the per-IP key. | Unauthenticated attacker POSTs 8 bad passwords for `redstamp` (admin username is documented/guessable) → admin locked out 10 min. Repeat forever = **sustained denial of admin access** to a cash-equivalent vault. Needs no credentials, no elevated access. IP rotation does not help the defender because the lock is account-scoped by design. | Keep the account key but (a) don't hard-block on it — degrade to increasing delay / CAPTCHA for the account track while only the per-IP track hard-locks; or (b) exempt a break-glass admin path; or (c) shorten account lock + alert on repeated account locks. | confirmed (code-read) |
| C-P1-2 | 4-WP / 5 | `render.yaml:` `WORDPRESS_INTAKE_ENABLED=false` vs `src` (0 refs) | The intake kill-switch env var is **never read** anywhere in `src/`. `orders/route.ts` + `test/route.ts` are gated only by the HMAC signature, not by this flag. | Ops set `WORDPRESS_INTAKE_ENABLED=false` believing intake is disabled, but any caller with a valid connection/env HMAC secret can still inject orders. False sense of a disabled surface; widens the exploitable window for C-P2-2/3 (leaked WP secret). | Enforce the flag: early-return 404/503 from both intake routes when `WORDPRESS_INTAKE_ENABLED !== "true"`, or remove the var so config doesn't imply a control that doesn't exist. | confirmed (grep: 0 usages) |

### P2

| id | lens | file:line | mechanism | exploit scenario | fix direction | confidence |
|----|------|-----------|-----------|------------------|---------------|------------|
| C-P2-1 | 2 | `src/app/api/auth/login/route.ts:22-24,108-109` + `login/page.tsx:61` | `getSafeNextPath` allows any `next` starting with `/` and not `//`. `getPublicUrl` feeds it to `new URL(next, base)`, which **normalizes a leading `/\`** (slash-backslash) into `//` → host takeover. | Victim clicks `…/login?next=/\evil.com`; page reflects it into the hidden `next` field; on successful login the 303 redirects to `https://evil.com/`. Post-auth **open redirect** for phishing / credential-harvest credibility. `/\/evil.com` also works. | Validate against `new URL(candidate, base)` and require the resolved `.origin` to equal the app origin; reject backslashes; or allow only a known path allowlist. | confirmed (LX1: `/\evil.com` → `https://evil.com/`) |
| C-P2-2 | 4-WP | `src/lib/integrations/request-signature.ts:27-65` | HMAC verify checks a ±5-min timestamp window but has **no nonce/replay store**. Any captured signed body is replayable verbatim within the window. | Attacker on-path (or with WP request logs) replays a signed intake POST. **Blast radius is bounded**: `createFulfillmentRequestRecord` is idempotent on `@@unique([sourceSystem, sourceEntryId])`, so replay of the same body is a no-op. Risk is latent — any future reuse of `verifySignedPayload` without a DB idempotency key would be replayable. | Add a short-lived seen-nonce cache (or persist `(connectionId, timestamp, signature)` for the window) and reject repeats. Document that replay-safety currently depends on downstream idempotency. | confirmed (code-read) |
| C-P2-3 | 4-WP / 5 | `wordpress/mu-plugins/pro-gift-cards-vault-handoff.php:73-88,113-122,460-465` | The intake HMAC secret is stored in the WP **`wp_options` table in plaintext** unless `PGC_VAULT_HANDOFF_SECRET` is defined in wp-config/env. The admin UI itself states "Treat database/options access as access to this vault connection." (Wave 0 N3/N4.) | Anyone with WP DB/options read (a WP SQLi elsewhere, a leaked backup, a rogue plugin) recovers the HMAC secret → can forge signed intake requests. **Bounded:** intake only *creates* draft/unpaid orders; it returns no card data and cannot allocate/export (those need an authenticated operator). Impact = order-queue pollution / integrity, not card disclosure. | Prefer the `PGC_VAULT_HANDOFF_SECRET` constant path (documented) for all non-local sites; store options-based secrets encrypted; rotate on suspicion via the app's `regenerateConnectionSecret`. | confirmed (PHP read) |
| C-P2-4 | 2 | `src/lib/login-attempts.ts:11-18` | `getTrustedClientIp` trusts client-settable headers (`cf-connecting-ip`, `true-client-ip`, `x-real-ip`) with no proof they were set by the trusted proxy. | An attacker hitting the Render origin directly can spoof these to fragment the per-IP throttle track. **Mitigated:** the account-scoped key (C-P1-1) still hard-locks, so this does *not* enable password brute-force — it only defeats per-IP granularity and aids the C-P1-1 lockout DoS. | Derive the client IP only from the header your actual edge (Render/Cloudflare) guarantees, and only trust it when the request arrives via that edge; ignore inbound copies otherwise. | confirmed (code-read) |
| C-P2-5 | 4-WP | `src/app/api/integrations/wordpress/formidable/orders/route.ts:51-58,126-132` | Bearer fallback compares secrets with `providedSecret === acceptedSecret` — **non-constant-time** — unlike the HMAC path's `timingSafeEqual`. | Timing side-channel on the intake secret. **Gated:** only reachable when `WORDPRESS_INTAKE_ALLOW_BEARER_FALLBACK==="true"` (staging sets it `false`), so not exploitable as configured. | Use `crypto.timingSafeEqual` on equal-length buffers for the bearer compare too, or drop the bearer fallback. | confirmed (code-read) |
| C-P2-6 | 4-WP | `orders/route.ts:99-125,180-201` + `wordpress-connections.ts:141-155` | The env-secret path (no `x-pgc-connection-id` header) verifies the signature against `WORDPRESS_INTAKE_SECRET` but **skips `isSiteAllowed`** (that check is `if (connection && …)`). Also `isSiteAllowed` returns `true` when the connection has no `siteUrl` set. | A holder of the env secret can post from any origin (no site pinning). Requires the real (Render-generated) secret, so not exploitable without it — defense-in-depth gap that widens if the env secret leaks. | Require a stored connection for all non-legacy intake; enforce a site allowlist even on the env path; treat an empty `siteUrl` as "deny" rather than "allow-any" for production connections. | confirmed (code-read) |

### P3 / hardening (one-liners)
- **Login user-enumeration timing oracle** — `login/route.ts:89-96`: `!user || !user.active || !verifyPassword(...)` short-circuits before scrypt for missing/inactive accounts (and missing logins run 2 `findUnique`s vs 1), so response time distinguishes account states. Mitigated by lockout. Fix: always run a dummy scrypt.
- **SameSite=lax** on the session cookie (`session-cookie.ts:10`) — acceptable, but sensitive downloads lean on `sec-fetch-site` (`http-security.ts:24-34`), which is absent for non-browser clients (fine for CSRF, since CSRF needs a browser). Consider `SameSite=strict` for the session cookie.
- **Staging DB reset on every deploy** — `render.yaml` + `seed-if-enabled.ts`: `autoDeployTrigger: checksPass` + `SEED_DATABASE_ON_DEPLOY=true` reseeds staging each deploy. Well-guarded against prod, but destructive on staging if it ever holds real data.
- **Intake error verbosity** — `orders/route.ts:261-284` returns `error.message` to the (authenticated) caller; low risk but avoid echoing internal messages.

---

## 3. Answers to Doug's security spec

**Q5 — Who can decrypt / view full card data?**
Only roles **admin** and **operations**, and only via two routes, both of which decrypt at the download boundary:
- `src/app/requests/[requestNumber]/exports/[exportId]/route.ts:28-31,85-98` (customer CSV)
- `.../exports/[exportId]/work-file/route.ts:32-35,84-94` (Lloyd work file, additionally behind `LLOYD_WORK_FILES_ENABLED`)

`finance` and `viewer` receive `403` at both. `decryptCardSecret` is called in **exactly** these two routes (plus the admin-only WordPress *connection* secret, not card data) — grep-confirmed across `src/`. The UI everywhere else renders only masked values (`cardNumberMasked`/`pinMasked`/`lastFour`); there is **no "reveal full card in UI" path**.

**Q6 — Is *viewing* sensitive card data audited?**
Yes, because "viewing full data" == "downloading". Both decrypt routes write an `AuditLog` (`sensitive_data.export_downloaded` / `sensitive_data.work_file_downloaded`) with actor, request, and timestamp; the export route does it atomically inside the `$transaction` with the status changes, and the work-file route `await`s the audit write before returning (a failed audit write fails the download). There is no separate, un-audited decrypt path to leave unlogged.

**Q7 — Export file security.**
There is **no stored password-protected ZIP with an expiry**. An `ExportPackage` is a DB record; the sensitive CSV is **generated live per GET** and streamed with `Cache-Control: private, no-store`, `X-Content-Type-Options: nosniff`, and a sanitized `Content-Disposition` filename. Access controls on each download: (1) middleware cookie gate, (2) `getCurrentUser` + `canAccessRole(["admin","operations"])`, (3) `rejectCrossSiteSensitiveRequest` (blocks `sec-fetch-site: cross-site`), (4) audit + `downloadCount`/`downloadedByName` tracking, and allocation status advances to `downloaded`. `exportId` is a cuid and must match its `requestNumber`. **Gaps vs a "secure package" model:** no download-count cap, no link expiry, no password on the file itself — re-download is unlimited for any admin/operations user (each is audited). Formula-injection neutralization lives in `merchant-output-export.ts`/`export-csv.ts` — **deferred to the Codex lane** to verify.

---

## 4. Wave 0 open-thread dispositions

- **N1 (CSP) — RESOLVED, present in prod.** CSP is **not** in `next.config.ts`; it is injected by the Next 16 middleware `src/proxy.ts:31-64` (`nextWithProductionCsp`), which sets a nonce-based policy (`default-src 'self'; base-uri 'self'; frame-ancestors 'none'; object-src 'none'; form-action 'self'; script-src 'self' 'nonce-…' 'strict-dynamic'; …`). **LX2** confirms Next `16.2.6` treats `proxy.ts` as the middleware entrypoint (`PROXY_FILENAME='proxy'`), so it runs. Caveat: CSP is applied **only when `NODE_ENV==='production'`** (`proxy.ts:46`) — dev/preview builds ship no CSP. Tim's "production CSP configured" claim is **accurate**. (Minor: `style-src 'unsafe-inline'`.)
- **N2 (fail-closed) — from the authZ/startup side: session secret fails closed.** `session-token.ts:72-83` **throws** in production if `AUTH_SESSION_SECRET` is missing or one of the known unsafe defaults, so no session can be minted/verified with a weak key in prod (fail-closed). `render.yaml` provides it via `generateValue: true`. (The `card-secrets.ts` encryption-key fail-closed gap is the Codex lane's; I did not re-audit crypto internals.)
- **N3/N4 (PHP plaintext secret) — CONFIRMED, blast radius bounded.** See C-P2-3: the mu-plugin keeps the HMAC secret in `wp_options` plaintext by default; the app-side stores it encrypted (`wordpress-connections.ts:98,115-125`). A leaked secret enables **forged order injection only** — no card-data read, no allocation/export — because those require an authenticated operator. Combine with C-P1-2 (kill-switch is a no-op) for the true exposure window.

---

## 5. Positive controls worth recording
- No Next.js `middleware`-name file, but `src/proxy.ts` provides a cookie-presence gate + prod CSP; **every** data page independently calls `requireUser`/`requireRole`, so the presence-only gate is backstopped (the one `NO-GUARD` page, `closed-requests/page.tsx`, only `redirect()`s to a guarded page).
- `AuditLog` has **no** `update`/`delete`/`deleteMany` anywhere in `src/` (grep-confirmed) — append-only from the app; no authenticated suppression/tamper path, no "clear audit" feature.
- No `$queryRaw`/`$executeRaw` in `src/` (all Prisma parameterized); no `console.*` in `src/lib` or `src/app` (no server-side secret/stack logging via console).
- Path traversal in the hidden QA-pack download is properly blocked (`testing-package.ts:54-66`: `path.resolve` + `startsWith(root + sep)`), and the route + page are `requireRole(["admin"])` and flag-gated. So `/current-testing-instructions` is authz-gated, not merely unlinked.
- Session model: role is re-read from DB in `getCurrentUser` (not trusted from the token) and `active` is re-checked, so role changes and deactivations take effect on the next request.
