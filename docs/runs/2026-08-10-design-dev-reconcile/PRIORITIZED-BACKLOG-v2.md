---
title: Progressive Card Vault — Prioritized backlog v2 (executable)
date: 2026-08-11
status: ready-for-Tim
audience: Tim / Codex builder
supersedes: PRIORITIZED-BACKLOG.md (v1 — adversarial FAIL; do not use)
sources:
  - DESIGN-QA-REPORT.md (PASS adversarial 2026-08-11)
  - ADVERSARIAL-REVIEW.md + ADVERSARIAL-REVIEW-DESIGN-QA-REPORT.md
  - Product ruling Spencer+Kaitlin 2026-08-10 (Walmart prep as order step)
app_commit: 6241988b1a0f3c42924339d9eafba703ad1ecfc8
staging: https://progressive-gift-cards-card-vault-staging.onrender.com/
figma: https://www.figma.com/design/Ztv1YtEx1S19i0w4bdHgo4/Digital-Gift-Card-Fulfillment-Design
---

# Prioritized backlog v2 — executable for Tim / Codex

**Use this file.** Ignore `PRIORITIZED-BACKLOG.md` (v1).

**Implement-against:** Figma **Screens** frames listed per slice + Tim `docs/application-style-guide.md`.  
**Not source:** Figma Design Direction historical screenshots / most Design Direction comments.

**Fixture walkthrough (UAT gate):** `PGC-1027` (Walmart / needs_generation) and `PGC-1026` (non-Walmart).

**After each UI staging deploy:** 3–8 bullets in `#progressive-fundraising` (routes, Figma nodes, remaining gaps).

---

## Do not build (closed by design QA)

| Topic | Why closed |
| --- | --- |
| Broad shell / token redesign | Already close to Screens |
| Rebuild Orders filter | Four categories already work (payment, progress, client, merchant) |
| Card Vault table rewrite / broken-icon hunt | Structure close; merchant logos load |
| “Make Paid green” color pass | Paid is already green; fix **labels** |
| Design Direction comment sweep | Polluted / stale |
| Login pixel pass | No canonical Screens frame; already coherent |

---

## Slice 1 — P0 · `lane/walmart-order-preparation-step`

### Product intent
Walmart card preparation is part of the **order workflow**, not a vault side-quest. ~High share of Progressive volume. Operators must not lose order context.

### Locked constraints
- App does **not** open or automate Fiserv.
- App **prepares** work file → operator activates externally → app **imports** activated result.
- Copy never says “you will be taken to Fiserv.”
- Prefer **inline conditional step** on order detail (report default). Nested order-scoped route is OK if inline is blocked — keep order chrome/context.
- Keep `/card-vault/generation` as **admin/batch** only; not primary order CTA.

### Current defect (evidence)
- Staging `/requests/PGC-1027`: progress rail **Paid → Allocated** with no Card Preparation stage.
- Detached red “Merchant preparation required” + link to `/card-vault/generation`.
- Allocated step highlights while preparation still blocks allocation.
- Code: `src/app/requests/[requestNumber]/page.tsx` (`workflowSteps`, generation card).

### Figma (layout/state only — not Fiserv fantasy copy)
- `601:450`, `601:823`, `601:1196`, `601:1573` — Walmart Orders 1–4  
- Place **Card Preparation** between **Paid** and **Allocated** when any line has `vendor.requiresGeneration`.

### Build notes (load-bearing)
- **Do not** reuse post-allocation export/work-file builders as the pre-allocation contract (`merchant-output-export.ts` / `vendor-work-files.ts` assume allocations).
- Need a **dedicated order-line-item work-file builder** (or deliberate new contract) validated against Progressive’s Walmart/Fiserv template when available.
- **Do** extract activated-result import from `card-vault/generation/actions.ts` into a shared service; order wrapper validates against order reference / line requirements and returns to that order.
- Prefill order # / denomination × qty from line items; notes optional.
- After successful matching import → inventory ready → `ready_to_allocate`; order-scoped audit event.
- Non-error chrome for prep step (not red “error” card for a normal Walmart path).

### Acceptance
1. On `PGC-1027` (or equivalent), rail shows **Card Preparation** after Paid when generation required.  
2. From that step: download work file + import activated result without using vault nav as primary path.  
3. Order context retained (order number, line items visible).  
4. After valid import, request can proceed to allocate; Allocated is not “current” while prep still required.  
5. `/card-vault/generation` no longer the primary CTA from order detail.  
6. Staging-only test generation remains gated / secondary if still present.

### Likely loci
- `src/app/requests/[requestNumber]/page.tsx`
- `src/app/requests/[requestNumber]/actions.ts`
- new order prep component + download route under requests
- extract service from `src/app/card-vault/generation/actions.ts`
- `src/lib/inventory-import-service.ts`
- new prep builder beside merchant-output stack

---

## Slice 2 — P0 · `lane/semantic-order-status-pills`

### Product intent
Operators must read **real** payment and fulfillment states at a glance on Dashboard, Orders list, and order header.

### Current defect (evidence)
- `paid` → display label **`Completed`** (style guide + Figma + payment control use **Paid**).
- Many fulfillment states → **`In Progress`** (Needs Generation, Ready to Allocate, Allocated, etc. indistinguishable).
- Colors/tones are largely fine; **labels** are wrong.
- Code: `src/lib/format.ts`; `getPaymentPill` / `getOrderStatusPill` in `src/app/fulfillment/page.tsx`; consumers on `/`, `/fulfillment`, order detail.

### Figma
- Pills: `421:1868` Final Pills; Design System Pills `296:13711`
- Orders list: `601:2640`
- Order detail header: `601:123`
- Dashboard: `564:1152`

### Build notes
- Separate **display label** from **visual tone**.
- Key tones by raw domain state (or small tone enum); labels stay semantic.
- Minimum distinguishable labels: **Paid**, **Needs Generation**, **Ready to Allocate**, **Allocated** / **Cards Allocated**, **Export created**, **Closed** (match Figma wording where Screens show it).
- Align filter option text for payment that currently says “Completed” for value `paid`.
- Keep green Success treatment for Paid.

### Acceptance
1. Paid order shows **Paid** (green), never payment label **Completed**, on list + detail + dashboard.  
2. `needs_generation` order shows **Needs Generation** (or Screens-exact synonym), not generic **In Progress**, on list + detail + dashboard.  
3. Filter payment options use the same semantic labels.  
4. No broad color redesign; tones remain coherent with style guide.

### Likely loci
- `src/lib/format.ts`
- `src/app/fulfillment/page.tsx`
- `src/app/page.tsx`
- `src/app/requests/[requestNumber]/page.tsx`

---

## Slice 3 — P1 · `lane/order-detail-disclosure-defaults`

### Defect
`Allocated Cards` and `Order Activity` use `defaultOpen={hasExportPackage}` — long troubleshooting surface steals focus from workflow rail when export exists.

### Figma / style guide
Supporting disclosures collapsed by default; active workflow rail stays primary.

### Acceptance
- Both disclosures **closed** on initial load even when export/activity exist.
- Headers still show counts so operators know when to expand.
- Do not change timeline checkmarks, client keylines, or rail layout.

### Locus
- `src/app/requests/[requestNumber]/page.tsx` (`defaultOpen={hasExportPackage}` → false / omit)

---

## Slice 4 — P1 · `lane/operator-language-cleanup` (tiny)

| Current (visible) | Target |
| --- | --- |
| `Search requests, customers, status, or merchant` | `Search orders, customers, status, or merchant` |
| Vault CTA `Generate Cards` | `Card Preparation` or `Prepare / import cards` (match Screens) |
| Any remaining operator-facing “Generate Cards” / “Card Generation” as primary path | Preparation / import language |

Do **not** rename internal Prisma/`request` identifiers for cosmetics.

### Loci
- `src/app/fulfillment/orders-overview.tsx`
- `src/app/card-vault/page.tsx`
- skim `src/app/card-vault/generation/page.tsx` for operator-visible generate wording only

---

## Builder order (binding)

```text
1. lane/walmart-order-preparation-step     (P0)
2. lane/semantic-order-status-pills        (P0)
3. Staging walkthrough PGC-1027:
   Paid → prepare work file → external activation boundary → import → ready_to_allocate
   + confirm semantic labels on /, /fulfillment, order header
4. lane/order-detail-disclosure-defaults   (P1)
5. lane/operator-language-cleanup          (P1)
6. Changelog note in #progressive-fundraising
```

Ship **1 and 2 before Progressive UAT walkthrough**. 4–5 only if 1–2 green or trivial parallel.

---

## PR / agent hygiene

- Branch names: `lane/<slice-slug>` (no host-branded prefixes).
- One slice per PR; do not mix Walmart workflow restructure with pill renames.
- No product commits from recon-only agents.
- If blocked on Walmart work-file template fields: file `.blocked` with exact unknown fields + partial UI that still owns the step.

---

## Human decisions (only if builder hits them)

| Question | Default if silent |
| --- | --- |
| Inline step vs nested `/requests/[n]/prepare` | **Inline** panel (report default) |
| Exact Figma synonym for Allocated pill | Prefer Screens wording; fall back to “Allocated” |
| Staging test-generation UI on generation page | Hide/gate behind non-prod flag; never order CTA |

---

## Evidence index

| Doc | Role |
| --- | --- |
| `DESIGN-QA-REPORT.md` | Visual + staging recon (PASS) |
| `ADVERSARIAL-REVIEW-DESIGN-QA-REPORT.md` | Gate on that report |
| `ADVERSARIAL-REVIEW.md` | Gate on pack v1 (historical FAIL) |
| `SESSION-BRIEF.md` | Session context |
| Voice 1:1 + morning sync transcripts | Product ruling + team process |
