---
title: "Mario Walkthrough — Session 2 Notes: Digital Fulfillment Operations & Walmart Process"
type: discovery
category: meeting-notes
date: 2026-03-27
status: complete
format: structured-notes
participants:
  progressive:
    - Mario (Digital card operator — demo lead)
    - Doug B. (Owner — heavy involvement, strategic context)
    - Elena (Admin — referenced, not present)
  redstamp:
    - Spencer R.
    - Tim L.
    - Danny (Director of Operations — on-site observer)
tags: [knowledge-transfer, mario-walkthrough, digital-fulfillment, walmart, order-intake, invoicing, quickbooks, encryption, email-delivery, volume, seasonality, pain-points, risk-posture, fundstream, edmonton-food-bank, skate-canada, self-service]
key_insights:
  - Order intake flows through Formidable Forms (website) or legacy email order forms; Elena prints and places on Mario's desk
  - Physical trigger to fulfill is hard copy invoice marked "PAID" (red stamp) + "R" (reconciled) — nothing ships until paid
  - Walmart is the exception flow — just-in-time issuance via Lloyd-built Excel template + PowerShell + Walmart Virtual GC Activation tool
  - Only ~5 of 28 digital merchant folders require in-house generation (Walmart, Loblaws, Shoppers, Amazon, plus 1–2 others)
  - Typical volume is 1–3 digital orders/day (15–20/month); Nov–Dec peaks at 5–10/day
  - Per-order processing time is 5–10 minutes typical; edge cases like Skate Canada (15 merchants, 1–2 cards each) take ~60 minutes
  - Mario has been doing this solo for ~2 months; leaving in ~1 month — single point of failure risk
  - Doug explicitly stated willingness to accept some risk to simplify and scale digital workflows
  - Doug sees competitive advantage in people/service over tech-only providers (Fundstream called out as "slowest supplier" with weaker service)
  - Preference shift to default URL delivery; reduce customer choice to cut friction
  - Large client Edmonton Food Bank did $300–$400K digital last year — big orders are typically one merchant, one denomination
  - Mario's top pain points are copy/paste across spreadsheets and repetitive email templating
  - Mario suggested self-service for small orders (1–3 cards) to remove manual burden
key_decisions:
  - Spencer to email Lloyd (cc Doug) to request secure Google Drive access to scripts/templates
  - Danny to brain dump on-site observations into documented workflow
  - Team to propose initial streamlining options with risk trade-offs for Doug's review
  - Mario to update Walmart March monthly report before month-end
related:
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-notes.md
  - projects/gift-cards/docs/discovery/2026-03-27-mario-handoff-session2-transcript.md
  - projects/gift-cards/docs/discovery/2026-01-29-client-discovery-call.md
---

## End-to-End Digital Order Workflow

### Order intake and triggers
- Website orders via Formidable Forms; legacy email order forms still used by some
- Elena prints the form email; places hard copy on Mario's desk
- Mario creates invoice in QuickBooks; always CCs himself and Doug for digital orders
- Physical trigger to fulfill: hard copy invoice on desk marked "PAID" (red stamp) and "R" when reconciled
- When Doug away (Palm Springs): Elena covers invoicing trigger/admin

### Invoicing specifics
- Taxes/discounts applied at invoicing (province-specific taxes not handled on order form)
- Some clients have standing discounts; Elena annotates on printed form
- Invoice email is labeled and filed under Mario's Gmail e-card folder for tracking

### Payment dependency
- Nothing is fulfilled until invoice is paid ("we're selling money")
- Exception for known clients if payment confirmation is imminent (noted by Doug)

---

## Walmart Digital E-Card Process (Exception Flow)

### Why different
- Direct integration with Walmart virtual GC activation; just-in-time issuance
- Requires a special Lloyd-built Excel template and PowerShell scripts

### Steps
- Download invoice; move into specific Google Drive folder structure for scripts
- Run PowerShell to generate a base Excel export (invoice-aligned)
- Copy/paste into Walmart-specific template (set denomination; replicate rows to match quantity, e.g., 100 x $50)
- Validate row count via Excel "Count" to confirm quantity
- Use Walmart Virtual GC Activation tool to generate card numbers + PINs into the same template
- Update monthly Walmart activation tracking sheet:
  - Record first and last card numbers for each activation
  - Sequential numbers; last 4 obfuscated in reporting
- Generate PDFs via Lloyd's PDF generator using the "invoice-based" sheet tabs:
  - Tabs per denomination: 25 / 50 / 100 / "Variable"
  - Validate tabs to ensure values routed correctly
- Client delivery options:
  - Preferred: URLs (historically most clients)
  - This case: Encrypted ZIP of PDFs per client request
    - Use 7-Zip command with naming convention and per-file encryption
    - Password = invoice number without "CPN"/dashes (e.g., 10454152)
    - Send two emails:
      - Email 1: ZIP + invoice PDF, instructions
      - Email 2: Password only
- Physical invoice note: record fulfillment timestamp and "Mario" initials

### Reliability and checks
- Failures during activation: none reported so far
- Validation before send: tedious to check balances; not done card-by-card
- Walmart balance/usage lookups possible via Walmart API if full 16 digits available; otherwise Walmart assists

---

## Standard Digital Fulfillment (Non-Walmart)

### Merchants and inputs
- Two patterns:
  - Merchant provides URLs/PDFs with challenge codes (e.g., Tim Hortons, Chapters/Indigo, CashStar brands, Loblaws/Shoppers)
  - Merchant provides numbers only; Lloyd's tool generates PDFs
- Only ~5 of 28 digital merchant folders require in-house generation (Walmart, Loblaws, Shoppers, Amazon, plus 1–2 others). Uber, Petro-Canada legacy no longer relevant; now via Fundstream for Petro-Canada with links

### Process
- Use PowerShell script to generate card-number spreadsheets from invoice
- For URL/PDF merchants: forward merchant-provided assets with optional Progressive encryption
- For numbers-only: transform to PDFs via generator, then deliver as URLs or encrypted PDFs per policy

### Edge cases
- Skate Canada monthly: 15 merchants; 1–2 cards each; 60+ minutes per order
- Legacy order forms cause denomination/product mismatches; client is notified; invoice becomes confirmation
- Consolidation anomaly: multi-line, mixed-denomination order requiring manual grouping—first time seen in 5 years

---

## Volume, Timing, and Seasonality

### Daily/weekly
- Typical: 1–3 digital orders/day (15–20 per month)
- March mini-rush (government/funding year-end); 20–25 invoices pending payment at time of meeting

### Peak season
- Nov–Dec: 5–10 digital orders/day typical
- Walmart physical activations: twice weekly Jan–Oct; daily Nov–Dec
- Processing time per digital order:
  - Typical: 5–10 minutes to fulfill once paid (complexity-dependent)
  - Edge multi-merchant, low-qty orders can take ~60 minutes

---

## Risk, Service, and Strategy

### Risk posture
- Doug willing to accept some risk to simplify and scale digital workflows
- Goal: streamline steps; reduce manual handling; maintain client trust
- Concern: becoming de facto helpdesk for end recipients; preference to equip client-side admin without Progressive becoming first-line support

### Service philosophy
- High-touch "5-star" service expected on large orders (e.g., Edmonton Food Bank $300–$400K last year)
- Competitive advantage: people/service over tech-only providers (e.g., Fundstream "slowest supplier," weaker service)
- Preference shift: default to URLs; reduce choice to cut friction; still accommodate PDFs/ZIPs if required

### Data and integration
- Reporting needs from clients: know if cards were received/redeemed
- Today: redemption status available only via merchant integration (Walmart supports; others vary)
- Variability in merchant integration depth limits centralized reporting

---

## Roles, Access, and Knowledge Transfer

### People
- Elena: admin; prints orders; marks paid/reconciled; can cover Doug; handles payment posting
- Mario: primary digital fulfillment; 2 months in role; leaving in ~1 month
- Doug: owner; orders inventory; approves access; business rules
- Lloyd: built scripts/templates; highly competent; not focused on ease-of-use; owner of Google Drive/script structure

### Access
- Google Drive (Lloyd-owned) access currently limited to Lloyd, Mario, Doug
- Red Stamp needs secure access to scripts/folders; action: email Lloyd with Doug cc/approval

### Risk to operations
- Single point of failure: only Mario can run end-to-end digital fulfillment internally
- Need to streamline so newcomers can learn quickly; reduce manual, error-prone steps

---

## Pain Points and Opportunities

### Manual, error-prone steps
- Copy/paste across multiple spreadsheets and tools
- Repetitive email templating per client (two-message flow for ZIP/password)
- Handling many small, multi-merchant orders
- Lack of automated "paid" trigger from QuickBooks to fulfillment queue
- Folder clutter; no archive cadence
- Password sharing out-of-band and per order

### Opportunities (high-level)
- Auto-generate fulfillment sheets/templates from invoice data
- Centralize merchant adapters; abstract per-merchant differences behind one workflow
- Default URL delivery; auto-zip/encrypt only when flagged
- Template-driven, prefilled emails; one-click send + separate password channel automations
- Month-end Walmart ledger auto-population from activation events
- Self-serve micro-orders (1–3 cards) for trusted clients; keep bulk via managed flow
- Clear archive protocol for per-order artifacts
- Training playbook with screenshots and step-by-step (5th-grade reading level goal)

---

## Notable Specifics and Examples

### Example order processed
- Children's Aid Society of Ottawa
  - Walmart digital: 100 x $50 = $5,000
  - Delivery: encrypted ZIP of PDFs; password = invoice number (sans CPN/dashes)
  - Two emails sent: ZIP+invoice; then password
  - Note added to physical invoice: date/time, fulfilled by Mario

### Large client references
- Edmonton Food Bank: $300–$400K digital last year; Walmart/Loblaws, typically single denomination
- Another group: ~$500K plastic; asks for redeemed/not redeemed reporting (Walmart API used when possible)

### Merchant mix requiring in-house generation
- Approx. 5 of 28 digital folders: Walmart, Loblaws, Shoppers, Amazon, plus 1–2 more
- Petro-Canada: moved to Fundstream; Progressive receives links now

---

## Action Items
- Spencer: Email Lloyd (cc Doug) to request secure access to Lloyd's Google Drive scripts/templates
- Team: Confirm whether Walmart activation PowerShell requires internet/Walmart connectivity during generation
- Danny: Brain dump on-site observations into documented workflow (with screenshots if available)
- Team: Propose initial streamlining options with risk trade-offs for Doug's review (URL default, email automation, monthly ledger automation, archive protocol)
- Mario: Update Walmart March monthly report with orders 204–205 before month-end
