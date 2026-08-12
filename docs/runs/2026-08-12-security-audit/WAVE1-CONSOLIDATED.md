# Wave 1 security audit — consolidated & verified (Progressive Card Vault)

**Date:** 2026-08-12 · **Source:** `progressive-card-vault/app` @ `08c0c74` (GitLab rs-dev) ·
**Scope:** static source + local non-network dynamic. **Not** live pen-test of the Render host.

## Method (three lineages, cross-verified)
- **Finders:** Codex/OpenAI (crypto, export-crypto, injection) + Claude/Opus-4.8 (authZ, WordPress
  intake, audit, config). Full-source, read-only.
- **Verifier:** Gemini 3.1 Pro via Cursor (Google — third lineage) adversarially refuted the six
  load-bearing findings from finding-local snippets only. Verdicts: **F1–F4, F6 CONFIRMED; F5 PARTIAL
  (narrowed).** No false positives survived.
- Grok excluded from source (data-exposure ruling). Wave 0 (deterministic secret/dep/config scan)
  was clean; this wave is the semantic audit.

## Bottom line
**No P0.** The core encryption and access-control boundaries are sound: AES-256-GCM authenticated,
fresh IV per field, unknown-version ciphertext fails closed; card secrets decrypt in exactly two
role-gated + audited download routes with no UI reveal path; audit log is append-only (no
update/delete in code); Prisma parameterized throughout, no raw SQL / XSS sink / SSRF fetch; prod CSP
real (via `src/proxy.ts`); session secret fails closed in prod.

**Nine P1s** — none remotely exploitable by an anonymous outsider against current staging, but several
are real money/availability risks under an insider, a compromised operator session, or a
misconfigured deploy. Ranked by real-world exploitability below.

---

## P1 — ranked by exploitability × impact

### 1. C-06 · Walmart import has no reconciliation → bad cards can be allocated to customers
**Impact: value loss.** `walmart-preparation.ts`, `inventory-import-service.ts`,
`requests/[requestNumber]/actions.ts:490-651`. Imported activated-result rows are validated only for
field presence, a permissive success status, and a catalog vendor/type match — **never reconciled**
against the order's own preparation file (expected idempotency keys, denominations, quantities).
Rows become globally `available` and can advance the order to `ready_to_allocate`. A malicious or
compromised **Operations** user (or an honest wrong-file upload) can inject attacker-chosen or
inactive card numbers/PINs that get allocated to paying customers.
**Confidence:** Codex confirmed + **Gemini CONFIRMED**. Needs an authenticated Operations account (→ P1, not P0).
**Fix:** persist expected prep rows; transactionally reconcile request identity, idempotency key,
denomination, quantity, uniqueness, and an explicit Fiserv success status before a card goes
`available`; reject extra/missing/cross-request rows; review state for partial results.

### 2. C-01 · Encryption key enforcement not fail-closed
**Impact: offline card-data disclosure under misconfig.** `card-secrets.ts:16-41`, `session-token.ts:72-101`,
`render.yaml`. Enforcement is gated on `NODE_ENV==='production'`: outside prod a missing key silently
uses a hardcoded fallback (and card encryption can fall back to `AUTH_SESSION_SECRET`); *in* prod, any
non-placeholder string — even one character — is accepted and SHA-256'd into the AES key, with **no
entropy floor**. A preview/manual deploy touching real data, or a weak prod key, yields DB ciphertext
a reader can decrypt offline. **Current Render staging is safe only because its config sets a
generated key.**
**Confidence:** Codex confirmed (+ local safe-dummy exec) + **Gemini CONFIRMED**.
**Fix:** require explicit high-entropy `CARD_VAULT_ENCRYPTION_KEY` + separate `AUTH_SESSION_SECRET`
in every non-fixture environment; enforce decoded key length; fail at startup, not first use; allow
local constants only behind an explicit localhost/test-DB opt-in.

### 3. C-03 · Exports are an indefinitely reusable decryption capability (= Doug's Q7 gap)
**Impact: repeat credential disclosure; SOW-relevant.** `exports/[exportId]/route.ts:67-116`,
`schema.prisma`. An export record has **no expiry, revocation, one-time-use, or deletion state**;
every authorized GET regenerates plaintext card/PIN CSV live from ciphertext. Months post-delivery, a
compromised Admin/Operations session + an old export URL re-yields the credentials. There is **no
password-protected ZIP with expiry** — the model Doug's Q7 assumed. Downloads are role-gated, bound to
the request, no-store, and audited, but unlimited.
**Confidence:** Both lanes + **Gemini CONFIRMED**.
**Fix:** short-lived, revocable, ideally one-time download grants; stop regeneration after
delivery/expiry; if password-ZIP is the agreed control, strong random per-package password out-of-band
(never filename-derived) + defined retention/deletion. **Surface to the client as a Q7 design decision.**

### 4. C-04 · Work-file route bypasses the download-state machine → double-spend (dormant)
**Impact: value loss; currently dormant.** `work-file/route.ts:70-124`, `actions.ts:1024-1040`,
`feature-flags.ts`. The Lloyd work-file route decrypts full credentials + audits, but does **not**
update `downloadCount`/`downloadedAt`/allocation state that cancellation-safety relies on. With
`LLOYD_WORK_FILES_ENABLED=true`, Operations downloads live cards while the order looks never-downloaded;
an Admin then cancels → cards return to available inventory → reallocation/double-spend. **Flag is
false on staging**, so dormant there.
**Confidence:** Codex confirmed state-machine mismatch (candidate for deployed exploit) + **Gemini CONFIRMED**.
**Fix:** route all sensitive downloads through one atomic state-transition service; cancellation must
inspect any sensitive-download event, not one endpoint's counter. Keep the flag off until fixed.

### 5. C-P1-1 · Account-scoped login lockout → unauthenticated admin-lockout DoS
**Impact: availability, trivial trigger.** `login-attempts.ts:20-28,62-88`. Lockout uses an
IP-independent `account:<login>` key that hard-locks after 8 failures/15min for 10min. An
unauthenticated attacker POSTing bad passwords for the guessable `redstamp` username can hold the
admin locked out indefinitely; IP rotation doesn't help the defender.
**Confidence:** Claude confirmed + **Gemini CONFIRMED**.
**Fix:** keep the account key but degrade to increasing delay / CAPTCHA on the account track (only
per-IP hard-locks), or add a break-glass admin path, or shorten + alert on repeated account locks.

### 6. C-P1-2 · WordPress intake kill-switch is a no-op
**Impact: false sense of a disabled surface.** `WORDPRESS_INTAKE_ENABLED` is set in `render.yaml` but
**read nowhere in `src/`** (grep: 0 usages). The intake routes are gated only by the HMAC signature.
Ops could believe intake is disabled while it stays open to any holder of the HMAC secret.
**Confidence:** Claude confirmed (grep). (Not in the Gemini set — mechanical, unambiguous.)
**Fix:** enforce the flag (early 404/503 when not `"true"`) or remove the var.

### 7. C-02 · Password hashing below current OWASP scrypt minimum
`password.ts:1-19`. `scryptSync` uses Node defaults (N=2^14) and stores no cost/version, materially
below OWASP's current scrypt guidance. After a user-table leak, cheaper offline cracking → a cracked
Operations/Admin password opens the full-card export boundary. Salt + timing-safe compare are correct.
**Fix:** Argon2id (or calibrated scrypt), encode all params per hash, rehash-on-login when stale.

### 8. C-05 · Quadratic CSV parse → import DoS
`inventory-import.ts:335-447`. Per row the parser rescans the whole accumulated issues array
(`issues.some(...)`), so malformed input is O(rows × issues). Locally: 8,000 bad rows = 1.35s vs 27ms
at 1,000; a sub-1MB payload can hold >100k tiny rows and tie up the event loop. Repeatable by a
malicious/compromised Operations account. **Confidence:** Codex confirmed + local timing.
**Fix:** row-local error flag; cap rows/issues/field-length/bytes; bounded error threshold; streaming parser.

### 9. C-07 · CSV-injection neutralization misses full-width formula initiators (narrowed)
`export-csv.ts:1-24`. Sanitizer apostrophe-prefixes ASCII `= + - @` (incl. leading whitespace). Codex
flagged TAB/CR/LF too — **Gemini refuted that part**: the regex consumes `\s\t\r\n` as leading
whitespace, so those are handled. The **real, confirmed** gap is **full-width variants** (e.g. `＝`),
which pass through unescaped on both import and export. Spreadsheet/locale-dependent.
**Confidence:** Codex candidate → **Gemini PARTIAL** (narrowed to full-width). **Fix:** neutralize the
full target-spreadsheet prefix set incl. full-width variants; add LibreOffice/Excel behavioral tests.

---

## P2 (defense-in-depth) — brief
Post-login open redirect via `/\` slash-backslash normalization (`login/route.ts`, confirmed local
exec); WordPress HMAC replay window ±5min with no nonce store (bounded by downstream idempotency);
PHP mu-plugin keeps HMAC secret in `wp_options` plaintext by default (Wave 0 N3/N4 — order-injection
only, no card read); spoofable client-IP headers fragment the per-IP throttle; non-constant-time
bearer-secret compare (gated off on staging); env-secret intake path skips `isSiteAllowed`; single
SHA-256-derived key reused for GCM + HMAC fingerprints (no HKDF domain separation / key rotation);
one corrupted ciphertext can 500 a whole export (no per-record quarantine); Fiserv URL accepts any
HTTPS host incl. loopback (Admin-planted client-side link, not server SSRF).

## Doug's security spec — answered with code evidence
- **Q5 (who can decrypt/view full card data):** Admin + Operations only, via two audited download
  routes; Finance/Viewer 403; no UI reveal path. Offline: anyone with both DB ciphertext **and** the
  encryption key (running app process / infra operator with Render-secret + DB access).
- **Q6 (is viewing audited):** Yes — "viewing full data" == "downloading," and both routes write an
  `AuditLog` before returning (export route atomically in-transaction; work-file audits but skips the
  canonical state fields → C-04). Append-only log, no suppression path.
- **Q7 (export file security):** **Gap vs the question's premise.** No password-ZIP, no expiry, no
  deletion — live-generated CSV, role-gated + audited + no-store, but unlimited re-download (C-03).
  This is a design decision to put to the client, not just a bug.

## The two design-QA 500s (engineering dispositions)
- **Walmart upload-500 (`777059612`):** the fixture parses cleanly locally; the upload branch diverges
  at `getUploadedTextFile` (`File.text()`), 1MB check applied post-decode. Most likely upload
  transport/runtime/deploy handling — **not** a malicious parse/injection path; did not corrupt state.
- **Create-order 500 (`294045514`):** most likely a **request-number race** (read-then-create on the
  unique order number in `fulfillment-request-service.ts`). No raw SQL, no card data in the error path.

## Recommended remediation order
Insider/config money-risk first: **C-06 → C-01 → C-03 → C-04**, then availability **C-P1-1 → C-P1-2**,
then **C-02 → C-05 → C-07** and the P2 set. C-01, C-03, and C-04 are also the items to confirm as
production-deploy gates before go-live (Wave 0's "confirm before production" list).

## Artifacts
Finder reports: `findings-codex.md`, `findings-claude.md`. Wave 0: `WAVE0-REPORT.md`. Verification:
`../../../scratchpad/security-verify-1/gemini-verdicts.txt` (session-local).
