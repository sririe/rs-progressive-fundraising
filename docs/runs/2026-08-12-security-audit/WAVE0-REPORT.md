# Wave 0 — Security Recon (Mechanical/Deterministic)

**Target:** `/Users/spencer/projects-work/progressive-card-vault/app` (local checkout of `git@gitlab.com:rs-dev/progressive-gift-cards-card-vault.git`)
**HEAD at scan time:** `08c0c749a013ce153f625c70c1b189e6b1147600` (2026-08-12 15:57:31 -0400), 144 commits total (143 reachable ancestors scanned by gitleaks)
**Run date:** 2026-08-12
**Scope:** Read-only. Secret scanning, dependency audit, static config posture. No semantic vuln analysis (Wave 1).

---

## 1. Coverage

| # | Check | Command | Tool / version | Exit code | Status |
|---|---|---|---|---|---|
| 1a | Secret scan, full git history | `gitleaks detect --source . --report-format json --report-path gitleaks-history.json --redact` | gitleaks 8.30.1 | 0 | Ran. 143 commits, ~2.12 MB scanned. **0 leaks.** |
| 1b | Secret scan, worktree (uncommitted) | `gitleaks detect --source . --no-git --report-format json --report-path gitleaks-worktree.json --redact` | gitleaks 8.30.1 | 0 | Ran. ~421.46 MB scanned (includes `node_modules`, `.next/dev`). **14 leaks found** — see §2, all resolved as noise/false-positive, see below. |
| 1c | Repeat of 1b with `-i .gitignore` | same, `-i .gitignore` | gitleaks 8.30.1 | 0 | Ran but **not meaningful** — gitleaks' `-i` flag expects a `.gitleaksignore` fingerprint file, not a `.gitignore` glob file; every glob line logged `Invalid .gitleaksignore entry`, so it re-scanned the identical file set and reproduced the same 14 findings. Confirmed manually instead (see §2). |
| 2 | Deep history check, crown-jewel files | `git log --all --oneline -- <file>`, `git ls-files \| grep -iE '\.env\|\.pem\|\.key$\|secret'` | git | 0 | Ran on `src/lib/card-secrets.ts`, `src/lib/password.ts`, `src/lib/session-token.ts`, `prisma/schema.prisma`, and `.env*` paths. No `-S` pattern search needed — see reasoning in §3. |
| 3 | Node dependency audit | `npm audit --json` | npm 11.17.0 / node v22.13.1 (repo-pinned; local node v26.4.0 used to invoke npm) | 0 | Ran. 847 total deps (737 prod, 111 optional). **0 vulnerabilities at any severity.** stderr log empty — no partial/offline-audit warning. |
| 4 | PHP mu-plugin dependency posture | manual read of `wordpress/mu-plugins/pro-gift-cards-vault-handoff.php` (665 lines, only file in the dir) | n/a (no composer.json, no vendor/) | n/a | Ran. Single flat PHP file, zero third-party dependencies, zero vendored libraries — no dependency surface to audit. Logic review deferred to Wave 1 per scope. |
| 5a | `.gitignore` coverage | read `.gitignore`; `git ls-files \| grep -iE '\.env\|\.pem\|\.key$\|secret'` | n/a | n/a | Ran. Covers `.env*`, `*.pem`, `/prisma/dev.db*`. No env/pem/key files tracked. |
| 5b | `render.yaml` secret posture | read | n/a | n/a | Ran. |
| 5c | `next.config.ts` security headers | read | n/a | n/a | Ran. |
| 5d | `.env.example` | `find . -iname ".env.example"` | n/a | n/a | Ran. **Not present in repo** — no example file to check placeholders on. |
| 5e | `src/lib/card-secrets.ts` default/fallback key | read | n/a | n/a | Ran — this is the highest-value check per the brief. |
| 5f | Session/auth secret handling | read `src/lib/auth.ts`, `src/lib/password.ts`, `src/lib/session-token.ts` | n/a | n/a | Ran. |

**Gaps, stated honestly:**
- No dependency-confusion / typosquat check was performed on the 847 npm packages beyond what `npm audit` covers (that's a known-CVE database check, not a supply-chain provenance check). Out of scope for a mechanical Wave 0 pass but worth naming if Spencer wants it later.
- `git log -p --all -S'<pattern>'` deep-content history search for hardcoded key constants was not run as a separate step. Rationale: `card-secrets.ts` and `session-token.ts` history is only 4-6 commits each (listed above), and reading the full current+historical logic directly (below) already surfaces the exact fallback-key mechanism and shows it was hardened, not weakened, over time (commit messages: "Harden production security defaults", "Harden production readiness docs and secrets", "Harden sensitive request handling"). If Spencer wants literal `-S` proof that no *stronger* secret was ever committed and later stripped, that's a 5-minute follow-up, but the current code path is the one that matters for risk today.
- I did not open the local `.env` file (present on disk, 426 bytes, confirmed **not** git-tracked). Reading live local secret material was out of scope for a static config-posture check and unnecessary once tracking status was confirmed — flagging that instead of reading it, per the redaction spirit of this task.
- `render.yaml` only defines a `-staging` service. No production `render.yaml` service block was found in this file — if a separate prod service/config exists elsewhere (Render dashboard, a different branch), it wasn't in scope of this checkout and should be confirmed by Spencer/Wave 1.

---

## 2. Findings

### P0 — none found.

### P1 — none found.

### Notes

**N1 — No Content-Security-Policy header.** `next.config.ts` sets `X-Content-Type-Options`, `X-Frame-Options: DENY`, `Referrer-Policy: no-referrer`, `Permissions-Policy`, and HSTS (production-only). It does **not** set a `Content-Security-Policy` header. For an internal admin vault handling cash-equivalent card credentials, a CSP would meaningfully reduce XSS blast radius (e.g., exfiltrating a decrypted card number rendered client-side). Not a P0/P1 because there's no evidence of an XSS vector here (that's Wave 1's job to find) — this is a missing defense-in-depth layer, not a demonstrated hole.
*Fix direction:* add a `Content-Security-Policy` (even a conservative `default-src 'self'` starting point) to the `securityHeaders` array in `next.config.ts`.

**N2 — Encryption/session-key fallback logic is sound but depends entirely on `NODE_ENV==='production'` being set correctly at runtime.** `src/lib/card-secrets.ts` and `src/lib/session-token.ts` both: (a) require `CARD_VAULT_ENCRYPTION_KEY` / `AUTH_SESSION_SECRET` to be present and non-default when `process.env.NODE_ENV === "production"`, throwing otherwise; (b) fall back to a hardcoded dev-only value (`local-card-vault-development-key`, `local-development-session-secret-change-before-production`) when `NODE_ENV` is anything else. This is the correct pattern, and `render.yaml` (staging service) confirms `NODE_ENV: production` is set explicitly alongside `CARD_VAULT_ENCRYPTION_KEY: generateValue: true` and `AUTH_SESSION_SECRET: generateValue: true` — so on the deploy path actually reviewed, the guard is armed and the key is a real generated secret, not the fallback. Flagging as a note rather than clean because: this is a single environment-variable trust boundary — if any deploy target ever runs the built app without `NODE_ENV=production` set (a misconfigured second Render service, a manual `npm start` on a box, a container without the env var propagated), the app will silently use the hardcoded dev key/secret rather than failing closed. A cash-equivalent vault's encryption key should arguably fail closed on "key is missing or default" *regardless* of `NODE_ENV`, not only when `NODE_ENV==='production'`.
*Fix direction (optional hardening, not urgent given current render.yaml):* consider gating on "is `CARD_VAULT_ENCRYPTION_KEY` unset/default" rather than "is `NODE_ENV` production", so any environment lacking a real key fails the same way.

**N3 — PHP mu-plugin has an equivalent local-only hardcoded fallback secret**, same pattern: `pgc_vault_handoff_default_settings()` sets `'secret' => wp_get_environment_type() === 'local' ? 'local-formidable-handoff-secret' : ''`. WordPress's `wp_get_environment_type()` defaults to `'production'` unless explicitly configured otherwise (via `WP_ENVIRONMENT_TYPE` in `wp-config.php` or env var), so this fails safe by default — same shape as N2, same caveat (depends on the environment-type constant being correctly *unset or explicit* rather than accidentally `'local'` in a real deployment).

**N4 — Webhook shared secret can live in the WordPress options table (plaintext) if not set via `wp-config.php`/env constant.** The plugin's own admin UI is honest about this ("Secret source: WordPress options. Treat database/options access as access to this vault connection."). This is a webhook-signing secret (HMAC key for order handoff), not card credential material — lower stakes than the vault's encryption key — but worth Wave 1 confirming whether the constant-based path (`PGC_VAULT_HANDOFF_SECRET` in `wp-config.php`) is actually what's configured in the live WordPress deployment, vs. the options-table fallback.

### Gitleaks worktree scan — 14 hits, all resolved as noise (not a finding)

All 14 hits from the `--no-git` worktree scan are inside `.next/dev/` (Next.js's local dev build cache):
- `generic-api-key` hits (7): Next.js's own internal `previewModeSigningKey` / `previewModeEncryptionKey` / `encryption.key` fields in `.next/dev/prerender-manifest.json` and `.next/dev/cache/.rscinfo` — these are framework-generated dev-server artifacts, not application secrets, and are regenerated per local build.
- `github-oauth` hits (4) and `sourcegraph-access-token` hits (3): all inside minified/bundled `.next/dev/cache/turbopack/**` and `.next/dev/static/chunks/node_modules_*.js.map` — pattern matches against bundled third-party library code and sourcemaps, not real committed tokens.

Confirmed via `git ls-files | grep -cE '^\.next/'` → **0** tracked files, and `.gitignore` contains `/.next/`. This directory is local-only build output, never committed, never deployed as source (Render's `buildCommand` runs `npm run render:build` fresh). No redaction of an actual secret value was needed here — `--redact` was used and the JSON already stores literal `"REDACTED"` for every `Secret`/`Match` field, so nothing sensitive is in `gitleaks-worktree.json` either.

**Recommendation for future scans:** exclude `.next/` and `node_modules/` from worktree gitleaks runs (a proper `.gitleaksignore` fingerprint file, not the attempted `.gitignore` reuse) to avoid the 2m17s scan time and this noise on every re-run.

---

## 3. Clean list (don't re-run these)

- **Full git history (143 commits) — zero secrets.** No API keys, tokens, passwords, or private keys ever committed, per gitleaks history scan.
- **No `.env` file, `.pem` file, or key file has ever been tracked in git**, at any point in history (`git log --all --oneline --diff-filter=A -- '.env*' '**/.env*'` returned nothing; `git ls-files` grep for env/pem/key/secret only matches the appropriately-named `card-secrets.ts`/`card-secrets.test.ts` source files and a migration file, none of which are secret material).
- **`.gitignore` is correctly scoped**: `.env*`, `*.pem`, `/prisma/dev.db*`, `/node_modules`, `/.next/` all covered.
- **`npm audit`: 0 vulnerabilities** across 847 dependencies (0 critical, 0 high, 0 moderate, 0 low, 0 info). No CRITICAL/HIGH advisories to list.
- **`prisma/schema.prisma`**: `DATABASE_URL` is read from env (`env("DATABASE_URL")`), no hardcoded connection string/credentials in the schema file itself, across its full history.
- **`render.yaml`**: all secrets (`AUTH_SESSION_SECRET`, `CARD_VAULT_ENCRYPTION_KEY`, `WORDPRESS_INTAKE_SECRET`, `SEED_ADMIN_PASSWORD`) are either `generateValue: true` (Render-managed random value) or `sync: false` (manually set out-of-band, never in the YAML) — none inline/plaintext. `NODE_ENV: production` is explicit.
- **`src/lib/password.ts`**: `scrypt` with per-password random salt, 64-byte key length, `timingSafeEqual` for comparison. No hardcoded password/salt.
- **`src/lib/auth.ts` / role model**: no secrets, straightforward role-gate logic reading from the signed session token.
- **PHP mu-plugin dependency surface**: none (no composer, no vendored libraries) — nothing to audit at the dependency layer; all admin actions have `current_user_can( 'manage_options' )` + nonce checks (`check_admin_referer`) at a glance, though full logic review is Wave 1's job.
- **`next.config.ts`**: `poweredByHeader: false`, X-Frame-Options DENY, nosniff, no-referrer, restrictive Permissions-Policy, HSTS in production — solid baseline (missing only CSP, see N1).

---

## Raw scan output in run directory

- `gitleaks-history.json` / `gitleaks-history.log`
- `gitleaks-worktree.json` / `gitleaks-worktree.log`
- `gitleaks-worktree-src-only.json` / `gitleaks-worktree-src-only.log` (the `-i .gitignore` rerun; identical results, see §1)
- `npm-audit.json` / `npm-audit.stderr.log`
