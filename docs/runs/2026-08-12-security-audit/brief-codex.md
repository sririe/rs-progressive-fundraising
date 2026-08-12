# Wave 1 security lane — recon · Codex

Read `/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-security-audit/WAVE1-SHARED-CONTEXT.md`
first — canon, stakes, fuel plan, evidence/severity/redaction rules, and the recon floor all bind you.

## Your lenses: (1) Crypto & secrets-at-rest, (3) Export/egress, (4) Injection & input

You are the deep-code finder. Be exhaustive across these three lenses; a sibling Claude lane owns
authZ/access-scoping, WordPress-intake authZ, audit-log, and config.

**Lens 1 — Crypto & secrets-at-rest.** `src/lib/card-secrets.ts`, `card-fields.ts`, `password.ts`,
`session-cookie.ts`, `session-token.ts` (+ the migration `…_card_secret_encryption_export_tracking`).
Cipher/mode, IV/nonce generation and reuse, authenticated-encryption vs malleable, key derivation and
storage, the Wave 0 **fail-closed gap** (does a missing/default `CARD_VAULT_ENCRYPTION_KEY` ever
silently encrypt real data outside `NODE_ENV==='production'`?), password hashing cost/algorithm,
timing-safe compares. Answer Doug **Q5** (who can decrypt full card numbers/PINs) with code evidence.

**Lens 3 — Export/egress.** `export-csv.ts`, `merchant-output-export.ts`,
`src/app/requests/[requestNumber]/exports/[exportId]/route.ts` + `…/work-file/route.ts`. Doug **Q7**:
password-ZIP strength + who sets it, expiry, download authorization + tracking, deletion policy, and
**verify in code** that CSV formula-injection is actually neutralized on both import and export (Wave 0
claimed it — confirm the sanitizer covers `= + - @ TAB CR` and is applied on every egress path). Check
for unauthenticated or IDOR-able export download and path traversal on the work-file route.

**Lens 4 — Injection & input.** The Walmart activated-result CSV path (`walmart-preparation.ts`,
`src/app/requests/[requestNumber]/walmart-preparation/route.ts`,
`src/app/card-vault/generation/walmart-preparation/route.ts`) — **design QA found two 500s here**
(file-upload import `ERROR 777059612`; note create-order 500 too). Determine whether the 500 masks an
unhandled parse/validation path that is also a DoS or injection vector, and whether malformed rows can
corrupt vault state. Also: SQL/Prisma raw queries, XSS in rendered card data, file-upload type/size
validation, and **SSRF** via the configurable Fiserv/integration URL (can an operator or intake caller
point it at internal endpoints?).

## Method
- Static read is primary. Local dynamic execution is allowed if you need to confirm a runtime
  behavior (e.g., feed a crafted CSV to the parser locally) — label it locally-executed, do NOT hit
  the live Render host.
- Every finding: file:line + mechanism + concrete exploit scenario + fix direction + confidence
  (confirmed / candidate). Redact real secrets to masked fingerprints.

## Deliverable
`/Users/spencer/projects-work/rs-progressive-fundraising/docs/runs/2026-08-12-security-audit/findings-codex.md`
(structure per WAVE1-SHARED-CONTEXT §Deliverable). Sentinel when complete:
`security-codex.done` (one line: findings path). Blocked → `security-codex.blocked`. Start now.
