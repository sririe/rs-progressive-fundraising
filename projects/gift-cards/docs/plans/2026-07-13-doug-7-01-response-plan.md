---
title: "Doug 7/1 pre-signing asks — response plan & punch list"
type: plan
category: internal
date: 2026-07-13
status: active
source: "Doug email 2026-07-01 (thread 19e9a0905b082b87, msg 19f1fe2bb8d479a1); nudge 7/8; Spencer holding reply 7/8"
related:
  - 2026-07-13-support-maintenance-agreement-draft.md
  - 2026-07-13-merchant-flow-diagrams.html
  - 2026-06-29-sow-amendment-plan.md
---

# Doug 7/1 pre-signing asks — response plan & punch list

Doug (7/1): "We want to get moving on this and get this SOW signed, but there are two items we would
like before signing and several comments/questions clarified." He nudged again 7/8; Spencer replied
7/8 that the updated SOW, a proposed S&M Agreement, and the diagrams would come together. **Nothing
had actually shipped as of 7/13** — the v2 SOW was last edited 6/29 and no S&M doc existed. This
session builds the package.

## The two pre-signing gates

| # | Ask | Status (2026-07-13) |
|---|---|---|
| G1 | Known monthly/quarterly S&M fee before signing | **Drafted** — `2026-07-13-support-maintenance-agreement-draft.md`; pricing number needs Spencer's word ($800/mo recommended) |
| G2 | Workflow diagrams promised to Lloyd | **Drafted** — `2026-07-13-merchant-flow-diagrams.html` (7 diagrams: overview + 6 merchant patterns); export to PDF after review |

## The eight clarification questions — proposed answers

Most are already answered by the v2 SOW text or the SA; three need a decision or a small SOW edit.

**Q1 — "Confirm you support all current merchants, although you wrote 'Confirming the first set of merchants…'"**
Answer: Yes — Phase 1 covers all of Progressive's current active merchants. "Confirming the first
set" refers to the Phase 1A kickoff step of validating each merchant's current file format against
real examples before configuration, not to a subset of merchants.
*Optional SOW edit:* change "the first set of merchant file formats" → "the file formats and
fulfillment patterns for Progressive's current active merchants." Low risk; recommend making it.

**Q2 — Partially filled orders: status in the vault? What order/invoice statuses exist?**
Answer: Yes — an order can be partially allocated/fulfilled and the vault shows that state. Statuses
tracked per order: payment status (unpaid/paid, updated manually), fulfillment status (open →
allocated [full or partial] → exported/delivered → closed), plus void/archive. Invoice records stay
in QuickBooks (per SOW, out of scope) — the vault tracks payment *status*, not invoices.
*Needs Tim confirmation:* exact status vocabulary is a Phase 1A kickoff item — say so plainly
("final status names are confirmed with your team in kickoff").

**Q3 — Who converts existing inventory to the import format: Progressive or Redstamp?**
Answer: Per the SOW, Redstamp supports one agreed initial import batch *after Progressive has
normalized it to the approved format*, and the importer's supplier-aware mapping absorbs the current
file shapes — so most current files should import with mapping rather than manual conversion.
Redstamp can quote cleanup help beyond that from S&M hours.
*Tone note:* don't make Doug feel dumped on; lead with "the importer is built to read your current
supplier files as they are."

**Q4 — Inventory reports: included?**
Answer: Inventory *visibility* is included (counts by merchant/denomination, searchable views,
statuses). If "reports" means exportable/printable inventory reports, that's a small addition —
recommend just saying yes: a simple inventory export (CSV) is included; scheduled/custom reporting
is Phase 2.
*Small SOW edit recommended:* add "inventory summary export (CSV)" to the Card Vault scope bullet.

**Q5 — What card data reaches the customer (e.g., Amazon serial number, not just claim code)?**
Answer: The per-merchant customer-facing field list is confirmed against Lloyd's known-good examples
during Phase 1A — the canonical record preserves all delivered fields (incl. Amazon serial numbers),
so whatever the known-good file contains, the export can contain. Commit to matching current
known-good outputs field-for-field as the acceptance baseline.

**Q6a — Customer-ready file = password-protected Excel (URLs+data) OR password-protected ZIP of PDFs?**
Answer: Yes, exactly those two modes (Mode A / Mode B in our model), chosen per order/brand rule.
The diagrams show this directly.

**Q6b — New merchants fitting an existing pattern shouldn't require Redstamp config; or give Progressive a self-serve config UI.**
This is the one real scope negotiation in the list. Current SOW position (deliberate, 6/23):
new-pattern-fit merchants are a *small Redstamp back-end setup* (config + mapping + end-to-end
validation) handled under S&M — because a mis-mapped cash-equivalent card file is a real risk, we
validate before a merchant goes live. A Progressive-facing self-serve merchant-configuration UI is
buildable but is new Phase 1 scope (import-mapping UI was deliberately deferred to 2nd pass).
**Proposed line:** keep validation with Redstamp in Phase 1 (it's included in S&M, typically 2–4
hrs/merchant, no change order), and name the self-serve mapping UI as a Phase 2 candidate once the
patterns have been stable in production.
*Needs Spencer's word — this is a posture call.*

**Q7 — Track "Support Requests" in Order Activity History.**
Answer: Reasonable and cheap — add "support/issue notes recorded against an order" to the activity
list (quarantine/replacement events are already in the invalid-card workflow). Recommend accepting.
*Small SOW edit recommended.*

**Q8 — Post-launch bugs: do we pay? And who owns the software?**
Answer (bugs): Warranty period per SA (15 business days) free; after that, defect fixes are covered
within the S&M agreement's included hours — bug fixes are never change orders. (Draft S&M §03 says
exactly this.)
Answer (ownership): Per the Services Agreement — Progressive owns the deliverables upon payment of
all invoices; Redstamp retains its pre-existing background IP with a perpetual license to
Progressive. Plain-English: "once paid, the vault is yours."
*Confirm Spencer is comfortable stating the SA IP position this plainly (hosting/ops custody is
separate from ownership).*

## Punch list to signature

| # | Item | Owner | State |
|---|---|---|---|
| 1 | S&M pricing number ($800/mo rec.) | **Spencer** | decision |
| 2 | Q6b posture (self-serve config → Phase 2) | **Spencer** | decision |
| 3 | Diagram PDF review + export | Spencer (review) | draft built |
| 4 | Three small SOW edits (Q1 wording, Q4 CSV export, Q7 support-request activity) | Claude → gog docs, highlight yellow | ready to run on approval |
| 5 | S&M agreement → branded Google Doc → #am-pm-review | Claude/Stephanie | after #1 |
| 6 | Doug reply email (all answers + attachments) | drafted, Spencer sends | staged as Gmail draft |
| 7 | Firm timeline dates | Spencer + Tim sync | outstanding since 6/29 (Tim was out wk of 6/30) — SOW keeps relative dates, so NOT blocking |
| 8 | D-15 export-password mechanism | Spencer + Tim | deferred, not blocking (System Bind keeps export protection in V1) — but Q6a answer touches passwords; keep answer at "password-protected," no mechanism detail |
| 9 | Stephanie: PM approval → Dropbox Sign after Doug OKs package | Stephanie | waiting on package |

Doug's last message (7/8) is friendly but this is the third nudge. The package should go out this
week; every answer above is designed to close, not reopen, discussion.
