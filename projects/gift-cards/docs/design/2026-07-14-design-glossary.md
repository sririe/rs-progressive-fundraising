---
title: "Card Vault — Design Glossary"
type: reference
category: internal-design
date: 2026-07-14
status: living
audience: internal (design team, Tim, Spencer) — not client-sent
---

# Card Vault — Design Glossary

**Status:** v0 — seeded 2026-07-14. **Rulings live here and only here** — the string inventory's §1 is
a worklist that points at this table, never a second record. Candace/Kaitlin propose, Hannah ratifies.
Once a term is ruled, **every surface writes to it**: UI strings, docs, design specs, and any
AI-generated material. This file is the standing fix for machine-optimized naming.

## Ruled (inherited from Tim's style guide — ratified as glossary law)

| Term | Ruling | Why |
|------|--------|-----|
| **Request** | The internal fulfillment record is always a *request*. | Style guide, Content Style §Terminology. |
| **Cancel** (never "delete") | Requests are cancelled and retained, never deleted. | Records and audit history are preserved — the word carries the behavior. |
| **Downloaded internally** vs **Delivered to customer** | Two distinct events, never conflated. | Downloading an export ≠ the customer having the file; the security model depends on the distinction. |
| **Activation boundary** | The app *prepares* merchant work files and *imports activated results*. Only Progressive *activates* — always outside the app. UI copy may say "activated result import"; it must never imply the app performs activation. | Contractual boundary (style guide + Doug's requirements), stated as an actor rule so legitimate phrases like "Walmart Activated Result" stay legal. |
| **Official merchant capitalization** | Brand names render as the brand writes them (Loblaws, Walmart, Amazon). | Style guide. |
| **Merchant** (not Vendor or Supplier) | The word for Amazon, Walmart, Loblaws etc., everywhere in the UI (~30 current "Vendor" strings to migrate). Locked external CSV headers (`Gift Card Vendor`) remain as documented format exceptions. | Ruled from canon 2026-07-14: the vault normalization design note uses *merchant* exclusively (24–0), the client-facing workflows doc says *Merchant*, and Tim's capitalization rule already says "official *merchant* capitalization." **Open task, not an open ruling:** confirm on the next client call that operators don't need a "supplier" exception; Hannah confirms this record. |

## Open rulings (worklist mirrored from inventory §1 — decide in order)

| # | Term | Question | Default + evidence | Ruling (by, date) |
|---|------|----------|--------------------|-------------------|
| 2 | Client / Customer | Account entity vs requesting party — one word, or a ruled split (Client = the organization; "customer delivery" = the handoff act) | Tim's rule: consistent within a section. App currently mixes across sections. | |
| 3 | Fulfillment / Requests | One name for the area — nav says "Fulfillment Requests," list title "Fulfillment," dashboard "Digital Gift Card Fulfillment," detail eyebrow "Fulfillment request" | "Request" is the ruled record name; the area name should contain it. | |
| 4 | Denomination | Keep the industry word, or plainer? | Industry + Lloyd's materials use it. Confirm with operators on the next call — don't assume. | |
| 5 | Allocate | The word for reserving cards to a request | **Default: keep.** Lloyd's 7/14 email uses "allocation" unprompted. | |
| 6 | Quarantine | The word for pulling an invalid card out of circulation | **Default: keep** (precise — carries "never returns"), + first-use helper text near the action. | |
| 7 | Export / Export package | One form ("Create export" vs "Export package created") | "Export" alone likely suffices; "package" may earn its place if multi-file ZIP outputs (Amazon PDF/ZIP) arrive. | |
| 9 | Offering | The merchant + card type + denomination combination | **Default: keep.** Doug's own word (6/16: "active offerings"). Standardize casing. | |
| 10 | Empty values | One convention for absent data | Propose "Not provided" for missing data, "—" for empty cells; keep distinct meanings (e.g. "Never" for last-used) only where the distinction informs. | |

(#1 Merchant and #8 the activation boundary are already ruled above — numbering matches inventory §1.)

## How a ruling gets made

1. Proposer (Candace or Kaitlin) fills the Ruling cell: the chosen word + one sentence of why, naming
   the evidence — ideally which real person says it this way (email, call, walkthrough).
2. Hannah ratifies or amends, adds her name + date in the same cell.
3. Tim applies to the UI in the next batch; docs and design files update as touched.

Evidence beats preference. When client evidence is missing, put the term on the next client call's
list rather than guessing.
