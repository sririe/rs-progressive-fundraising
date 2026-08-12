# Wave 1 security lane — recon · Claude

Read `/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-security-audit/WAVE1-SHARED-CONTEXT.md`
first — canon, stakes, fuel plan, evidence/severity/redaction rules, and the recon floor all bind you.

## Your lenses: (2) AuthN/AuthZ/access-scoping, (4-WP) WordPress-intake authZ, (5) Audit-log + config/infra

You are the access-control and boundary finder. Be exhaustive; a sibling Codex lane owns crypto,
export-crypto, and CSV/Walmart parsing internals.

**Lens 2 — AuthN / AuthZ / access scoping.** `src/lib/auth.ts`, `card-scope.ts`,
`src/app/api/auth/login/route.ts`, any middleware, and **every** API/route handler under
`src/app/**/route.ts` (enumerate them). The core questions for a cash-equivalent vault:
- **IDOR:** can an authenticated user read/allocate/export another client's cards, orders, or export
  packages by manipulating an id in the URL/body? Check each route's ownership/scope enforcement, not
  just authentication.
- **Privilege escalation / role scoping:** roles are `redstamp` (admin), `elaine` (operations),
  `mario` (finance). Can a non-admin reach card *secrets*, user management, or sensitive exports?
  Map the permission model (`card-scope.ts`) to actual route enforcement.
- Session fixation, cookie/session flags, login throttle bypass (Wave 0 said throttling is
  DB-backed + account-aware — verify it can't be bypassed by casing/whitespace/enumeration).
- Doug **Q5** (who can decrypt/view full card data — from the authZ side) and **Q6** (is *viewing*
  sensitive card data audited, or only allocation/export actions?).

**Lens 4-WP — WordPress signed-intake authZ.** `src/app/api/integrations/wordpress/formidable/*`
routes + the PHP mu-plugin `wordpress/mu-plugins/pro-gift-cards-vault-handoff.php`. The HMAC handshake:
constant-time signature compare? replay protection (nonce/timestamp window)? Can a forged or replayed
signed request inject orders or read data? Wave 0 flagged the WP HMAC secret can live in the options
table in plaintext (N3/N4) — assess blast radius.

**Lens 5 — Audit-log integrity & config/infra.** `AuditLog` / `LoginAttempt` models and their writers:
is sensitive-data *viewing* logged (Doug Q6), can audit entries be suppressed/tampered by an
authenticated user, do secrets/PII leak into logs or error responses (the design-QA 500s expose
`ERROR <code>` — check server-side log verbosity)? Config: resolve Wave 0's **N1** (is CSP genuinely
absent or injected via middleware — Tim claims prod CSP configured), **N2 fail-closed** from the authz/
startup side, cookie flags (HttpOnly/Secure/SameSite), `render.yaml` secret handling, and the
`/current-testing-instructions` + `…/package-file/route.ts` exposure (is the hidden QA pack
authz-gated or just unlinked?).

## Method
- Static read is primary; local dynamic execution allowed to confirm a runtime behavior (label it),
  never against the live Render host.
- Every finding: file:line + mechanism + concrete exploit scenario + fix direction + confidence
  (confirmed / candidate). Redact real secrets.

## Deliverable
`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-security-audit/findings-claude.md`
(structure per WAVE1-SHARED-CONTEXT §Deliverable). Sentinel when complete:
`security-claude.done` (one line: findings path). Blocked → `security-claude.blocked`. Start now.
