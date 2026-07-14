---
title: "Card Vault — Design Primer"
type: reference
category: internal-design
date: 2026-07-14
status: current
audience: internal (design team) — also feeds the team Claude project
---

# Card Vault — Design Primer

**For:** Candace, Kaitlin, Hannah · **Date:** 2026-07-14
**Read next:** `docs/designer-user-flows.md` and `docs/application-style-guide.md` in the prototype repo
(`gitlab.com/rs-dev/progressive-gift-cards-card-vault`) — Tim wrote both for designers, and they're the
deepest sources. This primer is the fast orientation before those.

## What this is

Progressive Fundraising sells gift cards to schools, teams, and community groups, who resell them to
raise money. Today, turning an incoming order into delivered digital gift cards is a pile of manual
steps and scripts. The **Card Vault** is the internal web app that replaces that pile: orders come in
(from the Pro Gift Cards website or entered by hand), cards live encrypted in a vault, staff allocate
cards to orders, generate the delivery file, and record that the customer got it — with every sensitive
action audited.

It is an internal operational tool for a five-person team, used daily. It is not a marketing site and
has no customer login.

## The people (real, named — these are the personas)

| Who | Role | What they do in the app |
|-----|------|------------------------|
| Doug, Elena | Admin | Everything below, plus user accounts, integrations, cancelling mistakes |
| Lisa, Lloyd, new hire | Operations | The daily work: review requests, import card inventory, allocate, export, record delivery, fix invalid cards |
| (role exists) | Finance | Payment status only — no access to card data |
| (role exists) | Viewer | Read-only |

**The success test for every design decision: one of these five people logs in for the first time and
completes their workflow without help.**

## The life of a request (the spine of the whole app)

1. **A request arrives** — from the website form, or staff create one manually.
2. **Payment is tracked** — manually marked Draft → Invoiced → Payment pending → Paid.
3. **Cards are allocated** — once paid, available cards in the vault are reserved for the request.
   (Some merchants — Walmart — need an external *preparation* step first; the app prepares a file,
   Progressive activates it outside the app, and the results are imported back.)
4. **An export is created and downloaded** — the delivery file, in whatever format that merchant's
   cards require. Downloading is a sensitive, audited act.
5. **Delivery is recorded** — staff confirm the customer actually received the file (separate from
   downloading it).
6. **The request is closed** — and lives on, read-only, in Closed Requests.

Things that go wrong have named paths: not enough cards = *Needs inventory*; a bad card gets
*quarantined* (never returns to inventory) and replaced; a mistaken request is *cancelled* (never
deleted — history is kept).

## Vocabulary that matters (see the glossary doc for rulings)

- **Request** — the fulfillment record. **Client** — the organization ordering.
- **Offering** — a card someone can order: merchant + card type + denomination.
- **Allocate** — reserve specific cards from the vault for a request.
- **Quarantine** — permanently pull an invalid card out of circulation.
- **The activation boundary** — the app prepares merchant work files and imports activated
  results; only Progressive activates, always outside the app. Copy may say "activated result
  import" but must never imply the app performs activation.
- **Downloaded internally ≠ delivered to customer** — two events, tracked separately.

## What's live design territory vs. not

**Yours now:** the language pass (see `2026-07-14-ui-string-inventory.md`), then the export/delivery
flow (fresh client requirements 7/14: legacy clients keep the PDF-in-ZIP option; new clients get a
simpler path), then screen-by-screen intuitiveness against the first-login test.

**Being redesigned anyway (don't polish):** the Card Preparation screen (`/card-vault/generation`) is
placeholder UI awaiting the Walmart preparation/result-import redesign.

**Locked (not design-changeable):** the client-consumed and process-bound output CSV headers
(Loblaws/Shoppers, Amazon workbook, Walmart work file — see inventory §3.15 for the per-profile
status), and anything implying the app activates cards, processes payments, or hosts customer
downloads — all out of scope by agreement.

## Where things live

- **Truth:** the GitLab repo — what's merged is what exists.
- **Mirror:** the Figma file of imported screens — refreshed after merges; comment and redline there.
- **This docs set:** primer, glossary, string inventory — in the Redstamp project repo, and mirrored
  into the Progressive Fundraising project in the Redstamp Claude workspace (internal team workspace;
  client-confidential material stays within Redstamp-controlled surfaces).
