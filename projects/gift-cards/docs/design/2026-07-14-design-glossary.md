# Card Vault — Design Glossary

**Status:** v0 — seeded 2026-07-14. Rulings land here as they're made (Candace/Kaitlin propose, Hannah
ratifies). Once a term is ruled, **every surface writes to it**: UI strings, docs, design specs, and any
AI-generated material. This file is the standing fix for machine-optimized naming.

## Ruled (inherited from Tim's style guide — ratified as glossary law)

| Term | Ruling | Why |
|------|--------|-----|
| **Request** | The internal fulfillment record is always a *request*. | Style guide, Content Style §Terminology. |
| **Cancel** (never "delete") | Requests are cancelled and retained, never deleted. | Records and audit history are preserved — the word carries the behavior. |
| **Downloaded internally** vs **Delivered to customer** | Two distinct events, never conflated. | Downloading an export ≠ the customer having the file; the security model depends on the distinction. |
| **Preparation** (never "activation") | The app *prepares* Walmart/Fiserv files. Progressive *activates* externally. | Contractual boundary — the app must never imply it activates cards. |
| **Official merchant capitalization** | Brand names render as the brand writes them (Loblaws, Walmart, Amazon). | Style guide. |

## Open rulings (from the string inventory, §1 — decide in order)

| # | Term | Question | Ruling | Ratified |
|---|------|----------|--------|----------|
| 1 | Vendor / Merchant / Supplier | The word for Amazon, Walmart, Loblaws… | | |
| 2 | Client / Customer | Account entity vs requesting party — one word or a ruled split | | |
| 3 | Fulfillment / Requests | One name for the area (nav, titles, eyebrows) | | |
| 4 | Denomination | Keep the industry word, or plainer? Confirm with operators | | |
| 5 | Allocate | Recommend keep — Lloyd's own word (7/14 email) | | |
| 6 | Quarantine | Recommend keep + first-use helper text | | |
| 7 | Export / Export package | One form | | |
| 9 | Offering | Recommend keep — Doug's own word (6/16 email) | | |
| 10 | Empty values | One convention ("Not provided" / "—") | | |

(Numbering matches `2026-07-14-ui-string-inventory.md` §1; #8 Preparation is already ruled above.)

## How a ruling gets made

1. Proposer writes the term, the choice, and one sentence of why (which real person says it this way).
2. Hannah ratifies or amends — one sentence of why, recorded in the table.
3. Tim applies to the UI in the next batch; docs and design files update as touched.

Evidence beats preference: the best argument is "Doug/Lloyd/Lisa says X" from an email, call, or
walkthrough. When client evidence is missing, put the term on the next client call's list rather than
guessing.
