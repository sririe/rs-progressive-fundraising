# Wave 1 — adversarial security source audit (Progressive Card Vault)

The Card Vault stores **cash-equivalent credentials** (gift-card numbers, PINs, claim codes,
redemption URLs). A vulnerability here is a theoretical "drain the account." Treat every finding at
that stakes level. This wave is a **static source + local dynamic** audit — NOT live pen-testing of
the deployed Render staging box (that's a separate authorization class; do not attack the live host).

## Fuel plan (operator ruling 2026-08-12)
- **Finders:** Codex (OpenAI) + Claude (Anthropic) — both already handle this repo.
- **Verifier:** Gemini-via-Cursor is the third-lineage adversarial verifier, invoked by AUR2 on
  candidate findings using **finding-local snippets only** — it does not crawl the full source.
- **Grok is excluded** from the source entirely (data-exposure ruling; frozen review lane).
- No-self-review: every confirmed finding is refuted by a **different lineage** than the lane that
  found it.

## Target
`/Users/spencer/projects-work/progressive-card-vault/app` @ `08c0c74`
(GitLab `git@gitlab.com:rs-dev/progressive-gift-cards-card-vault.git`). Next.js App Router + Prisma
(14 models) + a PHP mu-plugin (`wordpress/mu-plugins/pro-gift-cards-vault-handoff.php`), Render deploy
(`render.yaml`). **Read-only** — no branches, no edits, no PRs.

## Build on Wave 0 (already done — do NOT re-run)
`WAVE0-REPORT.md`: gitleaks (full history + worktree) clean of real secrets; `npm audit` 0/0/0/0/0;
no default/fallback encryption key reachable in production (guarded by `NODE_ENV==='production'`,
staging `render.yaml` sets a Render-generated real key). **Open threads Wave 1 must go deeper on:**
- **N2 fail-closed gap:** `card-secrets.ts` + `session-token.ts` gate dev fallback keys on
  `NODE_ENV==='production'` rather than failing closed whenever the key is missing/default. Does any
  path let a missing/weak key silently encrypt real data? Is the prod guard actually load-bearing?
- **N1 CSP:** `next.config.ts` sets headers but no Content-Security-Policy. Tim's 8/12 report claims
  "production CSP configured" — is CSP injected elsewhere (middleware), or genuinely absent?
- **N3/N4 PHP:** the mu-plugin mirrors the fallback-secret pattern; webhook HMAC secret can sit in
  the WP options table in plaintext.

## Threat lenses (assigned per-brief; be exhaustive within yours)
1. **Crypto & secrets-at-rest** — `card-secrets.ts`, `card-fields.ts`, `password.ts`,
   `session-cookie.ts`, `session-token.ts`. Algorithm/mode, IV/nonce reuse, key derivation, key
   management, the fail-closed gap, password hashing, timing.
2. **AuthN / AuthZ / access scoping** — `auth.ts`, `card-scope.ts`, `api/auth/login/route.ts`,
   middleware, every API route under `src/app/**/route.ts`. **IDOR** (can one client/role read
   another's cards/exports via id manipulation?), privilege escalation (can finance/`mario` read card
   secrets?), missing authz checks, session fixation, throttle bypass. Doug's Q5/Q6: who can decrypt
   full card numbers, and is *viewing* sensitive data audited.
3. **Export / egress** — `export-csv.ts`, `merchant-output-export.ts`,
   `requests/[n]/exports/[id]/route.ts`, `.../work-file/route.ts`. Doug Q7: password-ZIP strength,
   expiry, download authz/tracking, deletion, CSV formula-injection (Wave 0 said import/export
   neutralize — verify the code actually does), path traversal, unauthenticated export download.
4. **Injection & input** — the WordPress signed-intake bridge
   (`api/integrations/wordpress/formidable/*` + the PHP plugin HMAC handshake: constant-time compare?
   replay/nonce? timestamp window?), Walmart activated-result CSV upload
   (`walmart-preparation*`, the two 500s from design QA — is the 500 masking an unhandled parse path
   that's also a DoS/injection vector?), SQL/Prisma raw queries, XSS in rendered card data, file-upload
   validation, SSRF via the configurable Fiserv/integration URLs.
5. **Audit-log integrity & config/infra** — `AuditLog` / `LoginAttempt` models: is sensitive-data
   *viewing* logged (not just allocation/export)? Can logs be tampered/suppressed? Do secrets leak
   into logs/errors? Config: CSP (N1), session/cookie flags (HttpOnly/Secure/SameSite), the
   fail-closed gap (N2), `render.yaml` secret handling, the `/current-testing-instructions` route
   exposure, error verbosity (the design-QA 500s dump `ERROR <code>` — do server logs leak stack/secrets?).

## Evidence & severity
- Every finding: **file:line + exact mechanism + a concrete exploit/failure scenario** (inputs →
  bad outcome). No hand-waving. State provenance: code-read vs locally-executed.
- **P0** = exploitable path to card-data disclosure/theft, auth bypass, or account-drain; or a
  fail-open on the crypto/authz boundary. **P1** = real weakness needing a chain or elevated access;
  hardening the client should not ship without. **P2/P3** = defense-in-depth, brief.
- **Redaction:** never write a real secret value into any file — type + file:line + masked
  fingerprint only. This is cash-equivalent.
- **Adversarial mindset:** you are trying to steal card data or drain value. Assume a malicious
  authenticated low-privilege user AND a malicious WordPress-intake caller.

## Recon lane floor (read-only)
1. No commits/branches/PRs/edits to the app repo. Only writes: your findings file + sentinel in the
   security-audit run dir.
2. Do NOT attack the live Render host. Local dynamic testing (build/run locally) is allowed if you
   need to confirm a runtime behavior; note it as locally-executed.
3. Sentinel `security-<fuel>.done` (one line: findings path) only after the findings file is complete.
   Blocked → `security-<fuel>.blocked` with exact command + error.
4. A false "done" or invented/unverified-exploit finding benches the fuel (COLLECTIVE-CONTRACT).
   Mark low-confidence findings as "candidate — needs verification," don't inflate them to P0.

## Deliverable structure
1. Coverage — files/lenses inspected, what you could/couldn't cover, local-exec vs read-only.
2. P0 / P1 tables — id | lens | file:line | mechanism | exploit scenario | fix direction |
   confidence (confirmed / candidate).
3. Answers to Doug's security spec Q5 (who can decrypt/view full card data), Q6 (is viewing audited),
   Q7 (export file security) — with code evidence.
4. Wave 0 open-thread dispositions (N1 CSP, N2 fail-closed, N3/N4 PHP).
5. P2/P3 hardening one-liners.
