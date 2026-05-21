---
title: "Security Decision Menu — Where Card Data Lives"
type: plan
category: client-input
date: 2026-04-27
status: draft
tags:
  - progressive
  - security
  - decision-menu
  - doug
  - card-vault
  - architecture
key_insights:
  - This is a decision Doug needs to make explicitly — not one we should bury inside an implementation plan.
  - Each option solves the Lloyd-and-Mario problem; they differ in where sensitive card data lives, who supports the system, and what the threat model looks like.
  - Doug's stated tolerance ("happy to invest to simplify") is not blanket authorization for any architecture — it is permission to weigh real trade-offs.
key_decisions:
  - Present three options with explicit trade-offs.
  - Recommend Option B (Secure Web Vault) but make the case for each option fairly so Doug can choose.
related:
  - projects/gift-cards/docs/plans/2026-03-11-internal-solution-comparison.md
  - projects/gift-cards/docs/plans/2026-04-23-team-brief-lloyd-scripts-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-27-updated-client-recommendation.md
---

# Security Decision Menu — Where Card Data Lives

**Audience:** Doug Beers
**Purpose:** Choose where Progressive's sensitive card data lives in the next-generation fulfillment system.

## Why This Is a Decision, Not a Detail

Progressive handles cash-equivalent assets — Amazon claim codes, Walmart card numbers and PINs, Loblaws card data. Today, that data lives on a small number of local machines on Lloyd's Google Drive folder structure, with no formal access controls, audit trail, or retention policy. The current model has worked because the people who handle the data are trusted insiders on a closed loop.

Any new system changes that loop. Even one that runs only on Progressive's office computers changes the threat model — because more people will touch it, more workflows will run through it, and more decisions about access need to be made deliberately rather than implicitly.

This document presents three architectures. Each one solves the Lloyd dependency, the Mario single-point-of-failure, and the "non-technical staff can run it" requirement. They differ in where card data lives, who can support the system remotely, and what kind of breach a hypothetical attacker would face.

---

## Option A — Local-Only Processing (Desktop Application)

A guided desktop tool installed on Progressive's office machines. Data never leaves the office network. Looks and feels like a modern application; under the hood, it replaces Lloyd's scripts with something Mario or any trained staff member can run.

| | |
|---|---|
| **Where card data lives** | On Progressive's office computers only. Never transits the public internet. |
| **Who supports it** | Redstamp can update the application but cannot remotely diagnose or fix issues without a screen-share or site visit. |
| **Threat model** | Office network compromise, lost laptop, malicious insider with physical access. Familiar to your team. |
| **Strongest argument** | This is the closest thing to "what you're doing today, but better." If you lose sleep over the idea of card numbers being accessible from outside the office, this is the option that doesn't ask you to lose that sleep. |
| **Weakest argument** | When something breaks, Redstamp can't see it without you on a video call. The Mario-replacement training burden is also higher — desktop apps are less self-explanatory than browser tools. |
| **Build investment (Redstamp)** | $8K–$15K |
| **Monthly support (steady state)** | 3–5 hrs (~$500–$750) |

---

## Option B — Secure Web Vault (Recommended)

A purpose-built, browser-accessible application hosted in a secure environment. Card data is encrypted at rest and in transit, scoped to a vault module that is structurally separate from the rest of the application, and only accessible to staff with an appropriate role. Redstamp can support, monitor, and patch the system remotely without ever touching raw card data.

| | |
|---|---|
| **Where card data lives** | In an encrypted vault on a managed cloud infrastructure provider (e.g., AWS, DigitalOcean, or Vercel + Neon). All access logged. Card data is not stored beyond the lifetime of the order it belongs to unless explicitly retained for reconciliation. |
| **Who supports it** | Redstamp full remote access. Issues can be diagnosed and fixed without a site visit. |
| **Threat model** | Internet-exposed surface, credential theft, web application vulnerabilities. Mature mitigations exist for all of these. |
| **Strongest argument** | This is the option that scales with the business. It is the foundation for everything else on the roadmap — direct-to-recipient delivery, customer self-service for trusted clients, white-label vendor portals — without rebuilding from scratch. It is also the option that lets Redstamp actually support you when something goes wrong. |
| **Weakest argument** | Card data does transit the public internet. The architecture must be solid, the access controls must be enforced, and the audit trail must be real. This is a real engineering responsibility — not a checkbox. We treat it that way. |
| **Build investment (Redstamp)** | $18K–$35K |
| **Monthly support (steady state)** | 5–10 hrs (~$750–$1,500) |
| **Hosting infrastructure** | $20–$50/mo, billed at cost |

---

## Option C — Hybrid (Web Workflow + Isolated Processing)

A web application for order management and workflow, with the actual card-data processing happening in a sandboxed environment that spins up, processes, and tears down. The web layer never touches raw card numbers.

| | |
|---|---|
| **Where card data lives** | Encrypted temporary storage during processing only. The web application has no persistent access to raw card data. |
| **Who supports it** | Redstamp full remote access — but with a layer of infrastructure that requires specialist knowledge to debug. |
| **Threat model** | Strongest separation of concerns. Easiest to pass a formal security audit. |
| **Strongest argument** | If Progressive ever needs to pass a formal security review for an enterprise client (a Save-on-Foods or Sequoia engagement might trigger this), this architecture is built to pass. |
| **Weakest argument** | Most expensive to build. Most expensive to maintain. Overkill for current volume. The team would need ongoing infrastructure expertise — Redstamp is effectively the ops team for the sandbox layer indefinitely. |
| **Build investment (Redstamp)** | $28K–$50K |
| **Monthly support (steady state)** | 8–14 hrs (~$1,200–$2,000) |

---

## Side-by-Side Trade-Offs

| | Option A (Desktop) | Option B (Web Vault) | Option C (Hybrid) |
|---|---|---|---|
| Solves the Lloyd / Mario problem | Yes | Yes | Yes |
| Card data on the public internet | No | Yes (encrypted, scoped) | Yes (transient, sandboxed) |
| Redstamp can support remotely | Limited | Yes | Yes |
| Foundation for direct-to-recipient delivery | Throwaway — needs rebuild | Natural extension | Natural extension |
| Foundation for white-label vendor portals | Throwaway — needs rebuild | Natural extension | Natural extension |
| Realistic time-to-V1 | Fastest | Middle | Slowest |
| Total cost over 24 months (build + support) | ~$20K–$33K | ~$36K–$71K | ~$57K–$98K |

---

## Our Recommendation

**Option B — Secure Web Vault.** It solves the immediate problem, gives Redstamp the ability to support you the way a partner should be able to, and is the only option that is also a foundation for what comes next. The security responsibility is real, and we will treat it as such — explicit threat modeling, access controls, audit trail, encryption at rest and in transit, and a retention policy you sign off on.

**Why we don't recommend Option A:** It solves today's problem and creates tomorrow's. When Progressive is ready to give a trusted client self-service for small orders, or stand up a Save-on-Foods instance, we'd be rebuilding the foundation we just built. The savings up front cost more in total over the life of the system.

**Why we don't recommend Option C:** It's the right answer for a company with a dedicated engineering team. Progressive isn't that. The security advantage is real, but the ongoing infrastructure burden is high enough that it changes Redstamp's role from "your partner" to "your ops team." That's not a relationship that scales for either of us at the current size of the business.

---

## What Choosing Option B Commits You To

- An explicit threat model and security architecture document, reviewed by you (and, optionally, an outside specialist) before the build starts.
- A written access policy: who can see what, for how long, and what gets logged.
- A retention policy: how long card data lives in the system after an order ships.
- A breach response plan: what we do if the worst happens.
- Annual review of all the above.

These are not procedural niceties. They are how a system handling cash-equivalent data is supposed to work. We will produce drafts for your sign-off — not bury this work inside the build.

---

## What We Need From You

A sentence or two of direction. The rest is ours to figure out.

- "Go with Option B — let's see the security architecture before kickoff."
- "Go with Option A — I want card data to stay on our machines."
- "Go with Option C — we're going to need an enterprise security review and I want to be ready."
- "Tell me more before I decide."

---

*Internal note for Spencer/Tim/Danny: this menu intentionally simplifies the technical pitch from the March 11 internal comparison. The pricing matches what we drafted internally; the framing leans on Doug's stated preference for being told what we recommend rather than choosing among technical options without context.*
