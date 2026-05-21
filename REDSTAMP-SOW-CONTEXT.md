# Redstamp SOW Skill — Agency Context

> **Purpose:** Companion context file for the Redstamp SOW drafting skill. Provides the institutional knowledge, pricing model, engagement taxonomy, operational workflow, document family relationships, and template structures needed to generate accurate, production-ready Statements of Work and related documents.
>
> **Maintained by:** Spencer Ririe, Co-Founder & Creative Director
>
> **Last updated:** 2026-03-25

---

## 1. Agency Identity

- **Brand name:** Redstamp (one word, always — never "Red Stamp" in body copy)
- **Legal entity:** RED STAMP AGENCY INC. (used in legal sections, approvals blocks, and formal headers only)
- **Positioning:** B2B AI-native digital marketing and creative agency
- **Headquarters:** British Columbia, Canada
- **Legal address for notices:** 1200-900 West Hastings Street, Vancouver, BC V6C 1E5
- **Legal email:** legal@redstamp.com
- **Note:** GoodOps is a separate service line with its own operating model, templates, and branding. This skill covers Redstamp engagements only.

### Key People (Document-Relevant)

| Name | Role | Signing Title (varies by doc) | Document Relevance |
|------|------|------|------|
| Spencer Ririe | Co-Founder & Creative Director | "Co-Founder and CCO" (SA), "Co-Founder" (SOWs), "Co-Founder and Creative Director" (COs) | Signs all documents, sets pricing, leads strategy and scoping |
| Danny Norton | Director of Operations | "Director of Operations" | Operational co-reviewer, manages SOW review workflow, handles client onboarding |
| Stephanie Lamon | Senior Project Manager | — | Manages SOW review workflow in #am-pm-review, coordinates reviewer assignments, handles Dropbox Sign send, tracks client follow-ups |
| Kelso | Co-Founder | — | Stakeholder on major engagements |
| Bronte | Dev Lead | — | Technical scoping input on dev-heavy SOWs |

> **Note on signing titles:** Spencer's signing title is inconsistent across the document family. The skill should default to "Co-Founder" on SOWs and Change Orders unless instructed otherwise. The SA uses "Co-Founder and CCO."

---

## 2. Document Family & Relationships

Redstamp uses four interconnected document types. The skill should understand how they relate:

```
Services Agreement (SA)
  └── governs all downstream documents
  └── SOW references: "issued under a Services Agreement"
  └── SA terms prevail over SOW terms in any conflict
  │
  ├── Statement of Work (SOW) — Fixed-Fee
  │     └── scopes a discrete project with defined deliverables
  │     └── references SA for legal terms (IP, confidentiality, liability)
  │
  ├── Statement of Work (SOW) — Retainer
  │     └── scopes an ongoing monthly engagement
  │     └── references SA for legal terms
  │     └── includes termination/renewal terms specific to retainers
  │
  └── Change Order (CO)
        └── modifies scope/budget/timeline of an existing SOW
        └── references both the SA and the specific SOW being amended
        └── requires signatures from both parties
```

### What the SA Already Covers (SOW Should NOT Duplicate)

The Services Agreement handles these terms — SOWs should reference the SA rather than restating them:

- **IP ownership:** Client owns all deliverables upon payment of all invoices. Redstamp retains rejected work and portfolio rights. Background IP remains Redstamp's with a perpetual license to client.
- **Confidentiality:** Mutual NDA built into SA.
- **Change order process:** SA Section 1.2 defines the formal change order procedure (advise → outline → revised schedule → client approval).
- **Client timeliness:** 5 business day delay = project on hold, rescheduled per Redstamp's availability.
- **Payment terms:** NET 30 default. 2% monthly interest (compounded daily, 27.11% annually) on overdue invoices. Redstamp may suspend work and withhold deliverables if past due.
- **Warranty:** 15 business days post-delivery for functional deficiencies only. After warranty, billed at project rate.
- **Indemnification:** Mutual, with $500K cap on Redstamp's liability.
- **Limitation of liability:** Capped at value of services in the SOW or total fees payable, whichever is greater.
- **Termination:** Material breach with 10-day cure period. Redstamp can terminate for convenience with 30 days written notice.
- **Non-solicitation:** 6 months post-termination.
- **Governing law:** British Columbia.

### What the SOW MUST Specify (Not Covered by SA)

- Project-specific scope and deliverables
- Timeline and milestones
- Pricing (project fee or monthly retainer rate)
- Payment schedule (deposit/milestone splits)
- Hours allocation and hourly rate for overages
- Project-specific assumptions and risks
- Out-of-scope exclusions
- Number of included revision rounds
- Hold/restart policy with specific rates (fixed-fee only)
- Retainer termination notice period (retainer only)

---

## 3. Engagement Types

The skill must generate documents for all of the following engagement shapes. Each has distinct structural, pricing, and language patterns.

### 3a. Fixed-Fee Project

- **Template sections (8):** Project Overview → Scope → Tentative Timeline → Assumptions → Risks → Out of Scope → Project Terms → Approvals
- **Typical range:** $3,000–$100,000+ depending on complexity
- **Payment structure:** Usually 50/50 split (50% upon execution NET 7, balance at midpoint or completion NET 30). Larger projects may use 3-milestone splits.
- **Examples:** Website redesigns/builds (WordPress, Webflow), brand identity projects, animation/video production, landing page builds, technical audits, campaign creative packages
- **Key language patterns:**
  - "Project Fee" (not "cost" or "price")
  - Change order process referencing SA
  - Hold/restart policy: if project is placed on hold by Client, work will be rescheduled and a restart fee applies at [rate] per hour
  - Scheduled check-in cadence (typically bi-weekly or weekly)
  - Third-party costs (plugins, stock, fonts) explicitly excluded from project fee

### 3b. Retainer Agreement

- **Template sections (9):** Project Overview → Scope → Identified Retainer Deliverables → Tentative Timeline (if applicable) → Assumptions → Risks → Out of Scope → Project Terms → Approvals
- **Typical range:** $1,500–$15,000+/month depending on hours and complexity
- **Payment structure:** 100% invoiced on the 1st of each month. Overage hours billed the following month at the agreed hourly rate.
- **Examples:** Ongoing design support, website maintenance, marketing creative production, on-demand dev hours, content creation
- **Key language patterns:**
  - "Retainer" and "Monthly Rate"
  - Hours cap with overage billing clause
  - Deliverables defined through "planning sessions and project-specific creative briefs" rather than upfront
  - Termination clause: either party may terminate with written notice, effective no earlier than the last day of the month following the notice month
  - Unused hours do NOT roll over (unless explicitly stated otherwise)

### 3c. Paid Discovery / Diagnostic

- **Template:** Use fixed-fee template, simplified (fewer assumptions, shorter timeline, lighter risk section)
- **Typical range:** $2,500–$5,000
- **Purpose:** De-risk larger engagements by scoping unknowns first. Delivers a concrete audit, assessment, or recommendation document with a go/no-go decision point for both parties.
- **Payment structure:** 100% upfront or 50/50
- **Examples:** Technical audit of inherited dev work, content inventory, competitive analysis, platform migration assessment, website framework diagnostic
- **Key language:** Frame as "Phase 0" or "Discovery Engagement." Explicitly state that findings will inform a subsequent SOW for the full project, but do not commit to a specific follow-on scope or price.

### 3d. Staff Augmentation

- **Template:** Retainer template adapted — scope describes the embedded role rather than deliverables
- **Typical range:** Based on weekly hours × rate (e.g., 20 hrs/week × $150/hr × 12 weeks)
- **Examples:** Senior designer embedded in client team, dev resource for a defined sprint
- **Key language:** Define weekly hour commitment, reporting structure (who the resource reports to on the client side), communication channels, and onboarding requirements. Include a mutual action plan or onboarding checklist as an appendix when appropriate.

### 3e. Change Order

- **Template sections (6):** Change Order Description → Summary of Changes → Impact → Revised Timeline → Revised Budget → Approvals
- **Purpose:** Amend scope, timeline, or budget of an existing SOW
- **Key fields:** References the original SOW number/title, original project fee, adjustment amount, and revised total
- **Approvals:** Both Redstamp and Client must sign

---

## 4. Pricing Model

### Hourly Rates

Redstamp's hourly rate is **not fixed** — it flexes per client and engagement:

- **Minimum:** $150/hour (used for relationship-building, smaller clients, or reduced-scope engagements)
- **Standard:** $175–$180/hour
- **Premium:** Up to $195/hour (complex strategy work, tight timelines, specialized expertise)
- **Currency:** USD for US-based clients, CAD for Canadian clients. SOW template uses dual notation: "$X,XXX.XX USD" or "$X,XXX.XX CAD"

> **Rate determination is per-client.** The skill should treat rate as an input variable, not a default. If generating a SOW for an existing client, check for prior rate history (future integration: Harvest API for active project rates).

### Project Estimation

- Projects are estimated in hours internally, then converted to a project fee
- Typical project estimates range from 20–600+ hours depending on complexity
- The SOW presents the **project fee** — not the hourly breakdown (hours are internal)
- Hourly rate appears in the SOW only in the context of: (a) overage/additional work billing, and (b) hold/restart fees

### Multi-Option Proposals

Redstamp frequently presents **tiered proposals** with 2–3 options (e.g., Basic / Recommended / Premium). Each tier varies scope and deliverables, not just price. The SOW itself covers one selected option — but the skill should be capable of generating option-comparison language for proposal documents that precede the SOW.

### Payment Structures by Engagement Type

| Type | Typical Structure |
|------|------------------|
| Fixed-fee (small, under $10K) | 50% on execution NET 7, 50% at completion NET 30 |
| Fixed-fee (medium, $10–50K) | 50% on execution NET 7, 50% at midpoint NET 30 |
| Fixed-fee (large, $50K+) | 3 milestones: 40/30/30 or 33/33/34 |
| Retainer | 100% invoiced 1st of each month |
| Discovery | 100% upfront or 50/50 |
| Staff augmentation | Monthly invoicing based on hours worked |

---

## 5. Service Verticals

The skill should recognize these service categories and adjust scope language, deliverable naming, and assumptions accordingly:

- **Website Design & Development** — WordPress, Webflow; includes architecture, UX, visual design, front-end/back-end development, CMS configuration, QA, launch support
- **Brand Identity & Activation** — Logo, visual identity systems, brand guidelines, brand activation across digital touchpoints
- **Digital Marketing** — ABM campaigns, paid media creative (display, social, LinkedIn), SEO strategy, content marketing
- **Marketing Technology** — HubSpot integration, analytics setup (GA4/GTM), form/CRM configuration, marketing automation
- **Ongoing Maintenance & Support** — Security updates, WordPress/Webflow maintenance, on-demand bug fixes, performance monitoring
- **Creative Production** — Animation, video, illustration, tradeshow materials, print collateral
- **Strategy & Consulting** — Paid discovery, competitive analysis, content audits, migration assessments, digital transformation roadmaps

---

## 6. Client Context Signals

The skill should adapt language, detail level, and assumptions based on client signals:

### Client Sophistication Tiers

| Tier | Signals | SOW Adaptation |
|------|---------|----------------|
| **High** (e.g., Nitro, Forethought) | Large marketing team, established brand, clear requirements, $50K+ budgets | Concise scope, less hand-holding in assumptions, can reference industry conventions without explaining them |
| **Medium** (e.g., Terminal, Onward Robotics) | Growing company, some marketing maturity, $10–30K budgets | Balanced detail, explain key process steps, include revision cadence |
| **Low** (e.g., MOHR Retail, smaller orgs) | Limited internal resources, may need education on process, under $15K budgets | More detailed assumptions, explicit out-of-scope items, consider paid discovery first, simpler deliverable descriptions |

### Budget-Scope Alignment

When client budget expectations are significantly below what their requirements demand, the skill should:
1. Flag the gap rather than silently scoping to a number that can't deliver
2. Suggest creative restructuring: reduced Redstamp scope + client self-serve on lower-value tasks
3. Recommend paid discovery as an alternative entry point
4. Consider multi-phase approaches where Phase 1 fits the budget and Phase 2 is scoped separately

---

## 7. Operational Workflow

### Current SOW Creation Flow

```
1. Client discovery (call notes, intake workbook, or brief)
     ↓
2. Internal artifacts: Solution Summary and/or Reverse Brief
     ↓
3. SOW drafted (currently in Google Docs template)
     ↓
4. Posted to #am-pm-review channel in Slack
   - 🔴 red circle emoji = urgent/critical review
   - 👀 eyes emoji = triggers review form workflow
   - Reviewer opens doc, answers questions in form, comments inline
   - ✅ green check = approved for sending
     ↓
5. Manual send via Dropbox Sign
     ↓
6. Client signs → engagement begins
```

### Future-State Automation (In Progress)

- Evaluating **Docs Automator** for Airtable → document generation (good MCP/API support, agent-friendly)
- Evaluating **SignWell** as potential Dropbox Sign replacement (better variable population from structured data)
- Near-term skill goal: generate **clean markdown** that maps 1:1 to the Google Doc template structure, ready for copy-paste or future automation pipeline
- Long-term: Airtable as structured data source → Docs Automator (or equivalent) → e-sign tool, with the skill generating the structured data payload rather than a formatted document

### Upstream Inputs the Skill Should Expect

- **Client discovery notes** — call transcripts, meeting summaries, or intake form responses
- **Solution Summary** — internal Redstamp document outlining recommended approach and options
- **Reverse Brief** — structured analysis of client inputs with gap identification and strategic direction
- **Previous SOWs for the same client** — for rate consistency and scope continuity
- **Harvest data** (future) — active projects, billing rates, hours logged

---

## 8. Template Structures (Canonical)

### 8a. Fixed-Fee SOW Template

**Header block:**
- Redstamp logo
- "STATEMENT OF WORK" title
- Issued under SA reference
- Date, SOW validity (30 days)
- Client name and project name fields

**Sections:**

1. **Project Overview** — 1-2 paragraph summary of the engagement. Should make the client feel heard — reflect their stated challenges and goals back to them.

2. **Scope** — Bulleted list of deliverables organized by phase or category. Each item should be specific enough to be verifiable ("Homepage design — 1 concept, 1 round of revisions" not "Design the website").

3. **Tentative Timeline** — Table format: Phase | Deliverable | Target Date. Include kickoff, key milestones, and estimated completion. Note that dates are estimates subject to timely client feedback.

4. **Assumptions** — Numbered list. Standard items include:
   - Client provides all content/assets in a timely manner
   - One round of revisions per deliverable included
   - Scheduled check-ins (frequency specified)
   - Project fee does not include third-party costs (stock photography, fonts, plugins, hosting)
   - Hold policy: if placed on hold by Client for more than [X] business days, a restart fee of [rate]/hr applies
   - Client designates a single point of contact for approvals

5. **Risks** — Numbered list with risk + mitigation pairs. Common risks: scope creep, delayed client feedback, third-party dependencies, content readiness.

6. **Out of Scope** — Bulleted list of explicit exclusions. Critical for preventing scope creep. Common items: copywriting (unless scoped), SEO, ongoing maintenance, hosting, additional pages/features beyond what's listed.

7. **Project Terms** — Includes:
   - Project Fee (total amount in client's currency)
   - Payment schedule (deposit + milestone splits)
   - Hourly rate for additional work
   - Change order reference to SA
   - SOW validity period (30 days)

8. **Approvals** — Signature block for both parties:
   - RED STAMP AGENCY INC. — Spencer Ririe, Co-Founder
   - [CLIENT COMPANY] — [Name], [Title]
   - Date lines for both

### 8b. Retainer SOW Template

Same header block as fixed-fee, plus sections:

1. **Project Overview** — Describes the ongoing relationship and Redstamp's role. Emphasizes flexibility and the planning-session model for defining monthly deliverables.

2. **Scope** — Broader than fixed-fee. Lists areas of work rather than specific deliverables. References that specific deliverables will be defined through planning sessions and creative briefs.

3. **Identified Retainer Deliverables** — Table format: Deliverable | Description | Monthly Allocation. Lists the known/expected monthly outputs with hour allocations. This section may be marked "if applicable" for flexible retainers.

4. **Tentative Timeline** *(if applicable)* — Used when the retainer has a defined start phase or ramp-up period. Otherwise omitted.

5. **Assumptions** — Similar to fixed-fee but lighter. No hold policy, no restart fee, no scheduled check-in clause (inherent to retainer cadence).

6. **Risks** — Similar to fixed-fee.

7. **Out of Scope** — Similar to fixed-fee.

8. **Project Terms** — Includes:
   - Monthly Retainer Rate
   - Hours included per month
   - Overage rate (hourly)
   - Payment schedule (invoiced 1st of each month)
   - Initial term length
   - Termination clause: either party may terminate with written notice, effective no earlier than the last day of the month following the notice month
   - Change order reference to SA

9. **Approvals** — Same format as fixed-fee.

### 8c. Change Order Template

**Header block:**
- "CHANGE ORDER" title
- References: SA and specific SOW being amended
- Date, CO number

**Sections:**

1. **Change Order Description** — What is changing and why.
2. **Summary of Changes** — Table: Original Scope Item | Revised Scope Item.
3. **Impact** — How changes affect timeline, budget, and/or deliverables.
4. **Revised Timeline** — Updated milestone table.
5. **Revised Budget** — Original fee, adjustment, new total.
6. **Approvals** — Both parties sign.

---

## 9. Tone & Voice Guidelines

- **Professional but not stiff.** Redstamp's SOWs should read as confident and clear, not legalistic. Save the legal language for the SA.
- **Collaborative framing.** Use "we" and "our" when describing the partnership. The SOW should feel like a shared plan, not a vendor dictating terms.
- **Make the client feel heard.** The Project Overview should reflect the client's own language and stated goals back to them. If they said "we need to look more professional," the overview should reference evolving their digital presence — not use generic agency-speak.
- **Specificity over abstraction.** "Homepage design — desktop and mobile, 1 concept with 1 round of revisions" beats "Website design services."
- **Protect both parties.** Assumptions and Out of Scope sections exist to prevent misunderstandings. Be explicit without being adversarial.
- **Match budget to language density.** A $5K diagnostic gets a 2-page SOW. A $100K website redesign gets 4-6 pages. Don't over-document small engagements or under-document large ones.

---

## 10. Output Format

### Current Target: Markdown

The skill should output clean markdown that maps 1:1 to the Google Doc template structure:

- Use heading levels that match the template hierarchy (H1 for document title, H2 for sections, H3 for subsections)
- Use markdown tables for timeline, deliverables, and payment schedule sections
- Use numbered lists for Assumptions and Risks
- Use bulleted lists for Scope and Out of Scope
- Include placeholder tokens for variable fields: `[Client Name]`, `[Project Name]`, `[Client Rate]`, `[Project Fee]`, `[Date]`, etc.
- Output should be directly paste-able into the Google Doc template with minimal reformatting

### Future Target: Structured Data

When the automation pipeline matures (Airtable → Docs Automator → e-sign), the skill should be capable of outputting structured JSON with field-value pairs that map to document template merge fields. This is not required for v1 but the markdown structure should be clean enough that a future parsing step can extract the fields programmatically.

---

## 11. Integration Hooks (Future)

These are not required for v1 of the skill but should be designed-for:

- **Harvest API** — Check existing client projects for current billing rate, active/archived status, and hours history. Use to ensure rate consistency across engagements.
- **Airtable** — Redstamp OS contains structured client and project data. Future source for auto-populating client details, project metadata, and rate history.
- **Slack (#am-pm-review)** — SOW review workflow. The skill doesn't need to post to Slack, but should generate output that's ready for the review process.
- **Docs Automator / SignWell** — Future document generation and e-sign pipeline. Skill output should be structured enough to feed these tools.

---

## Appendix: Known Template Issues to Clean Up

1. **Signing title inconsistency:** Spencer's title varies across documents (CCO, Co-Founder, Co-Founder and Creative Director). Standardize.
2. **Change Order template has hardcoded numbers:** The Payment Terms section references "145 hours/month" and "870 hours" — these are from a specific client CO, not generic placeholders. Replace with `[Hours]` tokens.
3. **Fixed-fee template has a hardcoded restart rate:** Assumptions section references "$160 USD per hour" instead of using `[Client Rate]`. Should this be a flat restart rate or flex with the client rate? Needs a decision.
4. **SA email typo:** An earlier version of the SA had "legal@redsstamp.com" (double s). Current version shows "legal@redstamp.com" — verify the live version is correct.
