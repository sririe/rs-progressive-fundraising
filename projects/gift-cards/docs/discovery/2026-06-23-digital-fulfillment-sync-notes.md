---
title: "Progressive Digital Fulfillment Sync — Meeting Notes (Supernormal AI summary)"
type: discovery
category: meeting-notes
date: 2026-06-23
status: complete
format: notes
notes_provenance: "Supernormal default AI summary — machine-generated, NOT a human-witnessed note. Weight below the transcript and below human artifacts; verify before quoting as fact."
participants:
  progressive:
    - Doug Beers (dbeers@progressivefundraising.ca)
    - Lloyd Scrubb (lscrubb@progressivefundraising.ca)
  redstamp:
    - Spencer Ririe
    - Tim Lemke (tim@redstamp.com)
    - Stephanie Lamon (stephanie.lamon@redstamp.com)
referenced_not_present:
  - James (role unconfirmed)
  - Candace (Redstamp design)
  - Kaitlin Gordeyko (Redstamp design)
capture_tool: Supernormal
source_capture: "second-brain/Incoming/2026-06-29-1039-data-model-and-normalization-approach.md (manual web-UI copy, captured 2026-06-29)"
related:
  - projects/gift-cards/docs/discovery/2026-06-23-digital-fulfillment-sync-transcript.md
  - projects/gift-cards/docs/plans/2026-05-27-progressive-secure-card-vault-sow-draft.md
  - projects/gift-cards/docs/plans/2026-06-10-phase1-sow-reconciliation.md
  - projects/gift-cards/docs/plans/2026-06-18-phase1-vault-normalization-design-note.md
---

# Data model and normalization approach

### Data model and normalization approach
**Canonical card record design**
- Normalize all incoming inventory to a single, canonical vault schema
- Fields: merchant/brand (e.g., Tim Hortons), supplier, source system, credential, recipient name, recipient email, customer, order reference, invoice reference, date, status, provenance
- Status values: available, allocated, fulfilled, quarantined, need replacement, voided
- Provenance tracking: import batch ID, source file name, row number

**Credential patterns by merchant family**
- Amazon: claim code secret
- CashStar merchants (most): URL + secret/challenge
- Fairmont/Winners: URL
- PC Allocation: URL + account number + PIN
- Chapters: raw numbers requiring barcode/art output
- Walmart: activation/generation flow; no pre-stored inventory

**Rationale vs pass-through**
- Normalize on ingest to support inventory, allocation, audit, and uniform client outputs
- Import UI will allow field mapping verification before commit
- Robust to weekly vendor file header/column changes; reduce brittleness

### Import and inventory workflows
**Import flow**
- Upload CSV/XLSX from vendor
- Mapping screen: show source columns → vault fields; adjust if vendor template shifts
- Validate, then commit to vault with full provenance

**Inventory handling**
- Store minimal redemption data needed; hide internal normalization from clients
- Support quarantining and replacements without losing audit history
- Allocation links specific card rows to orders, preserving who fulfilled and when

### Fulfillment and output generation
**Order allocation and packaging**
- Multi-merchant orders supported; allocate across normalized inventory
- Generate consistent outputs per merchant requirements
- Simple, uniform client-facing files; only redemption essentials

**PDF and barcode generation**
- Support server-side PDF generation when required (e.g., Walmart, Amazon, Chapters)
- Preference to avoid PDFs where possible to reduce failure points
- Chapters need barcode/“card” artifacts; Amazon/Walmart historically needed generated visuals due to lack of card art

### Walmart-specific flow
**Current operational model**
- No pre-inventory; submit activation request with denominations
- Walmart returns live virtual cards (activation + inquiry combined)
- After payment: activate/generate, receive live cards, then distribute

**Vault integration**
- Treat as on-demand generation:
  - Receive order → run activation workflow externally → ingest returned cards to vault → allocate/package with rest of order
- Future possibility: explore direct API integration to remove manual step (post–V1)

### UX, roles, and usability
**Operator experience**
- Goal: simple, obvious flows for Doug and team
- Clear steps: Import → Review/Map → Commit → Allocate → Generate → Deliver
- Visibility: who fulfilled, what was sent, to whom, when; quick lookup for customer disputes

**Design involvement**
- Candace and Caitlin to support intuitive UX and clear on-screen guidance
- Keep flows streamlined; no overdesign; meet acceptance criteria with clarity

### Hosting, security, and infrastructure
**Hosting approach**
- Managed cloud (AWS or equivalent), 99.9% uptime class; no on-prem servers
- Monthly hosting cost; nominal relative to project

**System Bind relationship**
- Today: System Bind manages URL generation/hosting of assets/ZIPs
- V1: keep System Bind in place while vault launches
- Post-V1: assess consolidating URL generation/artifact hosting into vault stack to reduce dependencies

### Change management and extensibility
**New merchants/vendors**
- Add merchant metadata; test one sample import to validate mapping
- Only change order if a truly novel credential type appears beyond existing patterns

**Vendor format drift**
- Handled via import mapping UI; removing unused columns should not require changes
- Maintain flexible ingestion engine to avoid brittle dependencies

### Timelines and next steps
**SOW updates**
- Red Stamp to deliver a modified Statement of Work
- All changes highlighted in yellow
- Include visual diagrams of 5–6 common merchant flows: source file → vault mapping → output

**Schedule**
- Confirm timeline after internal sync (Tim on vacation next week)
- Target: deliver quickly with proper QA; mindful of October peak/Blackout window

### Decisions
**Agreed principles**
- Normalize all inventory on ingest
- Provide mapping verification UI on import
- Keep outputs minimal and merchant-appropriate; support PDFs where necessary
- Maintain System Bind for V1; consider replacement later
- Walmart handled as on-demand activation; ingest post-activation

### Open questions
**Items to finalize**
- Hosting vendor selection and whether routed via System Bind billing
- Scope and priority of PDF/barcode generation per merchant at V1
- Exact V1 timeline after Spencer/Tim sync

### Action Items
- Spencer: Deliver revised SOW with yellow-highlighted changes; correct banner brand/system bind naming; include visual workflow diagrams for common merchants.
- Tim + Spencer: Align on hosting architecture recommendation and share with Lloyd; confirm timeline post-vacation.
- Lloyd: Review proposed workflows/diagrams and hosting plan; confirm comfort with import mapping and normalization approach.
- Doug: Confirm which merchants require PDF/barcode artifacts at V1 (e.g., Chapters, Amazon/Walmart expectations).
- Spencer + Tim: Define Walmart activation-hand-off steps and vault ingest sequence for clarity in SOW.
- Spencer: Coordinate with System Bind on potential hosting/billing alignment; assess future consolidation feasibility (post-V1).
