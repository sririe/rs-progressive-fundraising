---
name: sow-drafting
description: "Draft production-ready Statements of Work for Redstamp client engagements. Supports fixed-fee, retainer, paid discovery, staff augmentation, and change order document types."
origin: built
companion_files:
  - "REDSTAMP-SOW-CONTEXT.md — Agency identity, document family, engagement types, pricing model, service verticals, client signals, operational workflow, template structures, tone guidelines, output format"
  - "REDSTAMP-SOW-EXAMPLES.md — 7 real executed SOWs across engagement types and budget ranges, with pattern summary"
argument-hint: "[engagement-type] [client-name] — plus upstream inputs (discovery notes, brief, prior SOWs)"
---

# <span data-proof="authored" data-by="ai:claude">SOW Drafting</span>

<span data-proof="authored" data-by="ai:claude">Use this skill to draft Statements of Work for Redstamp client engagements. The skill produces clean markdown that maps 1:1 to Redstamp's Google Doc template structure.</span>

## <span data-proof="authored" data-by="ai:claude">Before You Start</span>

<span data-proof="authored" data-by="ai:claude">Read both companion files before drafting:</span>

1. **<span data-proof="authored" data-by="ai:claude">REDSTAMP-SOW-CONTEXT.md</span>** <span data-proof="authored" data-by="ai:claude">— Institutional knowledge: agency identity, document family relationships, engagement taxonomy, pricing model, template structures, tone guidelines. This is the "what to know" file.</span>
2. **<span data-proof="authored" data-by="ai:claude">REDSTAMP-SOW-EXAMPLES.md</span>** <span data-proof="authored" data-by="ai:claude">— Real executed SOWs organized by type and budget. Match the closest example before drafting. This is the "what good looks like" file.</span>

<span data-proof="authored" data-by="ai:claude">Both files live at the repo root. If they've been promoted to aurora-skills, they'll be in the skill directory.</span>

## <span data-proof="authored" data-by="ai:claude">Inputs</span>

<span data-proof="authored" data-by="ai:claude">The skill expects the following upstream inputs. Gather these before invoking.</span>

### Client Context File

If the repo has a `CLIENT.md` at its root, read it first. It provides the legal entity name, rate, currency, SA reference, stakeholder details, and communication patterns — most of the "Required" and "Optional" inputs below can be pulled directly from it rather than requiring manual input.

### Required

* **Engagement type**: One of: `fixed-fee`, `retainer`, `discovery`, `staff-augmentation`, `change-order`
* **Client name**: Legal entity name for the approvals block (check `CLIENT.md` first)
* **Project name**: Short descriptive name for the SOW header
* **Project fee or monthly rate**: The number that goes in Project Terms
* **Agency rate for overages**: Per-hour rate in client's currency (check `CLIENT.md` for current rate)
* **Currency**: USD (US clients) or CAD (Canadian clients) (check `CLIENT.md`)
* **Scope description**: What Redstamp will deliver — from discovery notes, brief, or prior conversations

### <span data-proof="authored" data-by="ai:claude">Recommended</span>

* **<span data-proof="authored" data-by="ai:claude">Discovery notes or meeting transcripts</span>**<span data-proof="authored" data-by="ai:claude">: Client's own language for the Project Overview</span>

* **<span data-proof="authored" data-by="ai:claude">Prior SOWs for this client</span>**<span data-proof="authored" data-by="ai:claude">: For rate consistency and scope continuity</span>

* **<span data-proof="authored" data-by="ai:claude">Internal strategy brief or solution summary</span>**<span data-proof="authored" data-by="ai:claude">: Redstamp's recommended approach</span>

* **<span data-proof="authored" data-by="ai:claude">Timeline constraints</span>**<span data-proof="authored" data-by="ai:claude">: Hard dates, seasonal deadlines, client availability windows</span>

* **<span data-proof="authored" data-by="ai:claude">Client sophistication tier</span>**<span data-proof="authored" data-by="ai:claude">: High / Medium / Low (see CONTEXT.md section 6)</span>

### <span data-proof="authored" data-by="ai:claude">Optional</span>

* **Services Agreement reference**: Date and parties of the governing SA (check `CLIENT.md`)

* **<span data-proof="authored" data-by="ai:claude">Payment structure preference</span>**<span data-proof="authored" data-by="ai:claude">: If different from the default for this engagement type</span>

* **<span data-proof="authored" data-by="ai:claude">Travel or third-party cost considerations</span>**<span data-proof="authored" data-by="ai:claude">: If applicable</span>

* **<span data-proof="authored" data-by="ai:claude">Specific out-of-scope items</span>**<span data-proof="authored" data-by="ai:claude">: Client-requested exclusions or items to call out explicitly</span>

## <span data-proof="authored" data-by="ai:claude">Process</span>

### <span data-proof="authored" data-by="ai:claude">Step 1: Classify the engagement</span>

<span data-proof="authored" data-by="ai:claude">Determine which engagement type applies (see CONTEXT.md section 3). This drives template selection, section structure, payment defaults, and language patterns.</span>

| <span data-proof="authored" data-by="ai:claude">Type</span>               | <span data-proof="authored" data-by="ai:claude">Template</span>                    | <span data-proof="authored" data-by="ai:claude">Sections</span>                                                                                                               | <span data-proof="authored" data-by="ai:claude">Payment Default</span>            |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">Fixed-fee</span>          | <span data-proof="authored" data-by="ai:claude">Full fixed-fee (8 sections)</span> | <span data-proof="authored" data-by="ai:claude">Overview, Scope, Timeline, Assumptions, Risks, Out of Scope, Terms, Approvals</span>                                          | <span data-proof="authored" data-by="ai:claude">50/50 or milestone-based</span>   |
| <span data-proof="authored" data-by="ai:claude">Retainer</span>           | <span data-proof="authored" data-by="ai:claude">Full retainer (9 sections)</span>  | <span data-proof="authored" data-by="ai:claude">Overview, Scope, Identified Deliverables, Timeline (if applicable), Assumptions, Risks, Out of Scope, Terms, Approvals</span> | <span data-proof="authored" data-by="ai:claude">100% invoiced 1st of month</span> |
| <span data-proof="authored" data-by="ai:claude">Discovery</span>          | <span data-proof="authored" data-by="ai:claude">Simplified fixed-fee</span>        | <span data-proof="authored" data-by="ai:claude">Same as fixed-fee but lighter assumptions, shorter risks, frame as Phase 0</span>                                             | <span data-proof="authored" data-by="ai:claude">100% upfront or 50/50</span>      |
| <span data-proof="authored" data-by="ai:claude">Staff augmentation</span> | <span data-proof="authored" data-by="ai:claude">Adapted retainer</span>            | <span data-proof="authored" data-by="ai:claude">Scope describes embedded role, includes onboarding/reporting structure</span>                                                 | <span data-proof="authored" data-by="ai:claude">Monthly based on hours</span>     |
| <span data-proof="authored" data-by="ai:claude">Change order</span>       | <span data-proof="authored" data-by="ai:claude">Change order (6 sections)</span>   | <span data-proof="authored" data-by="ai:claude">Description, Summary of Changes, Impact, Revised Timeline, Revised Budget, Approvals</span>                                   | <span data-proof="authored" data-by="ai:claude">Per original SOW terms</span>     |

### <span data-proof="authored" data-by="ai:claude">Step 2: Select the closest example</span>

<span data-proof="authored" data-by="ai:claude">Find the example in EXAMPLES.md that best matches by engagement type and budget range. Use it as the structural and tonal reference — not a copy-paste source, but a calibration anchor.</span>

<span data-proof="authored" data-by="ai:claude">Key matching dimensions:</span>

* <span data-proof="authored" data-by="ai:claude">Engagement type (primary match)</span>

* <span data-proof="authored" data-by="ai:claude">Budget range (secondary match)</span>

* <span data-proof="authored" data-by="ai:claude">Client sophistication tier (tertiary match)</span>

### <span data-proof="authored" data-by="ai:claude">Step 3: Draft the Project Overview</span>

<span data-proof="authored" data-by="ai:claude">This is the section that makes the client feel heard. Requirements:</span>

* <span data-proof="authored" data-by="ai:claude">Reflect the client's own language and stated goals back to them</span>

* <span data-proof="authored" data-by="ai:claude">Reference the existing relationship and shared context</span>

* <span data-proof="authored" data-by="ai:claude">State the problem clearly without being adversarial</span>

* <span data-proof="authored" data-by="ai:claude">Frame what this engagement will accomplish</span>

* **<span data-proof="authored" data-by="ai:claude">Do not use generic agency-speak.</span>** <span data-proof="authored" data-by="ai:claude">If the client said "we can't keep up," say "the current process can't keep up" — don't say "operational inefficiencies have been identified."</span>

* <span data-proof="authored" data-by="ai:claude">Length should match budget: 1-2 paragraphs for discovery/small projects, 2-3 for medium, 3-4 for large</span>

### <span data-proof="authored" data-by="ai:claude">Step 4: Draft the Scope</span>

* <span data-proof="authored" data-by="ai:claude">Use bulleted lists organized by phase, category, or deliverable group</span>

* <span data-proof="authored" data-by="ai:claude">Each item should be</span> **<span data-proof="authored" data-by="ai:claude">specific enough to be verifiable</span>**<span data-proof="authored" data-by="ai:claude">: "Homepage design — desktop and mobile, 1 concept with 1 round of revisions" not "Website design services"</span>

* <span data-proof="authored" data-by="ai:claude">For discovery engagements: describe what will be investigated and what deliverables the investigation produces</span>

* <span data-proof="authored" data-by="ai:claude">For retainers: describe areas of work rather than specific deliverables; reference planning sessions for defining monthly work</span>

* <span data-proof="authored" data-by="ai:claude">End with a clear deliverables list if the scope section is long</span>

### <span data-proof="authored" data-by="ai:claude">Step 5: Draft the Timeline</span>

* <span data-proof="authored" data-by="ai:claude">Table format: Phase/Deliverable | Target Date/Window</span>

* <span data-proof="authored" data-by="ai:claude">Include the "contingent on timely feedback" disclaimer</span>

* <span data-proof="authored" data-by="ai:claude">For discovery: include session prep, the session itself, synthesis, and delivery</span>

* <span data-proof="authored" data-by="ai:claude">Add the 2 business day resourcing guarantee for medium+ engagements (see EXAMPLES.md pattern summary)</span>

* <span data-proof="authored" data-by="ai:claude">Note seasonal or hard deadline constraints where relevant</span>

### <span data-proof="authored" data-by="ai:claude">Step 6: Draft Assumptions</span>

<span data-proof="authored" data-by="ai:claude">Standard items to consider (include what's relevant, skip what isn't):</span>

* <span data-proof="authored" data-by="ai:claude">Client provides access/assets/content in a timely manner</span>

* <span data-proof="authored" data-by="ai:claude">Client designates single point of contact</span>

* <span data-proof="authored" data-by="ai:claude">Revision rounds included (typically 1; 2 for large projects)</span>

* <span data-proof="authored" data-by="ai:claude">Overage rate for additional rounds</span>

* <span data-proof="authored" data-by="ai:claude">Project fee excludes third-party costs (stock, fonts, plugins, hosting)</span>

* <span data-proof="authored" data-by="ai:claude">Hold/restart policy (fixed-fee only, not discovery)</span>

* <span data-proof="authored" data-by="ai:claude">Scheduled check-in cadence (bi-weekly or weekly for medium+ projects)</span>

* <span data-proof="authored" data-by="ai:claude">48-hour feedback turnaround expectation</span>

* <span data-proof="authored" data-by="ai:claude">Scope-specific assumptions that protect both parties</span>

<span data-proof="authored" data-by="ai:claude">For discovery engagements, add:</span>

* <span data-proof="authored" data-by="ai:claude">This is an assessment, not a build commitment</span>

* <span data-proof="authored" data-by="ai:claude">Findings inform a separate SOW for follow-on work</span>

* <span data-proof="authored" data-by="ai:claude">Specific staff availability requirements for the session</span>

### <span data-proof="authored" data-by="ai:claude">Step 7: Draft Risks</span>

<span data-proof="authored" data-by="ai:claude">The risks section is near-boilerplate (see EXAMPLES.md pattern summary). Use the standard 3-5 risk/mitigation pairs and customize only where the engagement has specific risks worth calling out.</span>

<span data-proof="authored" data-by="ai:claude">Standard risks:</span>

1. <span data-proof="authored" data-by="ai:claude">SOW based on current knowledge; deliverables may shift during discovery</span>
2. <span data-proof="authored" data-by="ai:claude">Client feedback delay causing project blockage</span>
3. <span data-proof="authored" data-by="ai:claude">Budget/timeline impact from scope changes</span>

<span data-proof="authored" data-by="ai:claude">Add engagement-specific risks only when they're real and non-obvious.</span>

### <span data-proof="authored" data-by="ai:claude">Step 8: Draft Out of Scope</span>

* <span data-proof="authored" data-by="ai:claude">Bulleted list of explicit exclusions</span>

* <span data-proof="authored" data-by="ai:claude">Include anything the client might reasonably expect but that isn't included</span>

* <span data-proof="authored" data-by="ai:claude">Include anything that came up in discovery conversations but was deferred</span>

* <span data-proof="authored" data-by="ai:claude">Common items: content creation, ongoing maintenance, additional pages/features, hosting, SEO</span>

* <span data-proof="authored" data-by="ai:claude">For discovery: explicitly exclude design, development, and implementation</span>

### <span data-proof="authored" data-by="ai:claude">Step 9: Draft Project Terms</span>

<span data-proof="authored" data-by="ai:claude">Include:</span>

* <span data-proof="authored" data-by="ai:claude">Project Fee (total in client currency) or Monthly Rate</span>

* <span data-proof="authored" data-by="ai:claude">Payment schedule (see CONTEXT.md section 4 for defaults by type and size)</span>

* <span data-proof="authored" data-by="ai:claude">Agency Rate for additional work</span>

* <span data-proof="authored" data-by="ai:claude">Change order language (standard block, references SA)</span>

* <span data-proof="authored" data-by="ai:claude">SOW validity (30 days)</span>

* <span data-proof="authored" data-by="ai:claude">SA reference</span>

* <span data-proof="authored" data-by="ai:claude">For retainers: hours included, termination clause, initial term</span>

### <span data-proof="authored" data-by="ai:claude">Step 10: Draft Approvals</span>

<span data-proof="authored" data-by="ai:claude">Standard format:</span>

* <span data-proof="authored" data-by="ai:claude">RED STAMP AGENCY INC. — Spencer Ririe, Co-Founder</span>

* <span data-proof="authored" data-by="ai:claude">[CLIENT ENTITY] — [Name], [Title]</span>

* <span data-proof="authored" data-by="ai:claude">Date lines for both</span>

* <span data-proof="authored" data-by="ai:claude">"per:___" prefix and "Authorized Signature" italic</span>

## <span data-proof="authored" data-by="ai:claude">Adaptation Signals</span>

<span data-proof="authored" data-by="ai:claude">The skill should flex output based on these signals:</span>

### <span data-proof="authored" data-by="ai:claude">Client Sophistication (from CONTEXT.md section 6)</span>

| <span data-proof="authored" data-by="ai:claude">Signal</span>                                                      | <span data-proof="authored" data-by="ai:claude">Adaptation</span>                                                                                 |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span data-proof="authored" data-by="ai:claude">High sophistication (large team, clear requirements, $50K+)</span> | <span data-proof="authored" data-by="ai:claude">Concise scope, less hand-holding in assumptions, reference conventions without explaining</span>  |
| <span data-proof="authored" data-by="ai:claude">Medium sophistication (growing company, $10-30K)</span>            | <span data-proof="authored" data-by="ai:claude">Balanced detail, explain key process steps, include revision cadence</span>                       |
| <span data-proof="authored" data-by="ai:claude">Low sophistication (limited resources, under $15K)</span>          | <span data-proof="authored" data-by="ai:claude">More detailed assumptions, explicit exclusions, simpler language, consider discovery first</span> |

### <span data-proof="authored" data-by="ai:claude">Budget-Scope Alignment</span>

<span data-proof="authored" data-by="ai:claude">If the requested scope clearly exceeds what the budget can deliver:</span>

1. <span data-proof="authored" data-by="ai:claude">Flag the gap — don't silently under-scope</span>
2. <span data-proof="authored" data-by="ai:claude">Suggest restructuring: reduced Redstamp scope + client self-serve</span>
3. <span data-proof="authored" data-by="ai:claude">Recommend discovery as an alternative entry point</span>
4. <span data-proof="authored" data-by="ai:claude">Consider multi-phase where Phase 1 fits the budget</span>

### <span data-proof="authored" data-by="ai:claude">Document Length</span>

<span data-proof="authored" data-by="ai:claude">Match budget to language density:</span>

* <span data-proof="authored" data-by="ai:claude">Discovery / sub-$10K: 2-3 pages</span>

* <span data-proof="authored" data-by="ai:claude">Medium ($10-30K): 3-4 pages</span>

* <span data-proof="authored" data-by="ai:claude">Large ($50K+): 4-6 pages</span>

## <span data-proof="authored" data-by="ai:claude">Scope Boundaries</span>

<span data-proof="authored" data-by="ai:claude">This skill</span> **<span data-proof="authored" data-by="ai:claude">does NOT</span>**<span data-proof="authored" data-by="ai:claude">:</span>

* <span data-proof="authored" data-by="ai:claude">Generate Services Agreements (SAs) — the SA is a separate document with its own legal review process</span>

* <span data-proof="authored" data-by="ai:claude">Generate proposals or pitch decks — those precede the SOW and have different structure/tone</span>

* <span data-proof="authored" data-by="ai:claude">Set or recommend pricing — rate and fee are inputs, not outputs</span>

* <span data-proof="authored" data-by="ai:claude">Generate GoodOps documents — GoodOps has its own templates and branding</span>

* <span data-proof="authored" data-by="ai:claude">Produce final formatted documents (Google Docs, PDF) — output is markdown ready for copy-paste or future automation</span>

* <span data-proof="authored" data-by="ai:claude">Send documents for signature — that's a separate workflow step</span>

## <span data-proof="authored" data-by="ai:claude">Output Format</span>

<span data-proof="authored" data-by="ai:claude">Clean markdown with:</span>

* <span data-proof="authored" data-by="ai:claude">H1 for document title ("STATEMENT OF WORK")</span>

* <span data-proof="authored" data-by="ai:claude">H2 for sections (Project Overview, Scope, etc.)</span>

* <span data-proof="authored" data-by="ai:claude">H3 for subsections within scope</span>

* <span data-proof="authored" data-by="ai:claude">Markdown tables for timeline, deliverables, and payment schedule</span>

* <span data-proof="authored" data-by="ai:claude">Numbered lists for Assumptions and Risks</span>

* <span data-proof="authored" data-by="ai:claude">Bulleted lists for Scope and Out of Scope</span>

* <span data-proof="authored" data-by="ai:claude">Placeholder tokens for unfilled variables:</span> <span data-proof="authored" data-by="ai:claude">`[Client Name]`,</span> <span data-proof="authored" data-by="ai:claude">`[Date]`,</span> <span data-proof="authored" data-by="ai:claude">`[RATE]`, etc.</span>

* <span data-proof="authored" data-by="ai:claude">No YAML frontmatter in the SOW output itself (add frontmatter only if saving as a repo document)</span>

<span data-proof="authored" data-by="ai:claude">The output should be directly paste-able into the Google Doc template with minimal reformatting.</span>

## <span data-proof="authored" data-by="ai:claude">Known Limitations (v1)</span>

* <span data-proof="authored" data-by="ai:claude">No automated rate lookup — rate must be provided as input (future: Harvest API integration)</span>

* <span data-proof="authored" data-by="ai:claude">No client data auto-population — client details must be provided (future: Airtable integration)</span>

* <span data-proof="authored" data-by="ai:claude">Change order template is the least tested — only one example exists</span>

* <span data-proof="authored" data-by="ai:claude">Staff augmentation has no real example in EXAMPLES.md yet — adapt from retainer template</span>

* <span data-proof="authored" data-by="ai:claude">The skill doesn't validate that scope matches budget — that judgment is on the operator</span>

## <span data-proof="authored" data-by="ai:claude">Integration Hooks (Future)</span>

* **<span data-proof="authored" data-by="ai:claude">Harvest API</span>** <span data-proof="authored" data-by="ai:claude">— Look up active client rate, project history, hours logged</span>

* **<span data-proof="authored" data-by="ai:claude">Airtable (Redstamp OS)</span>** <span data-proof="authored" data-by="ai:claude">— Auto-populate client details, project metadata</span>

* **<span data-proof="authored" data-by="ai:claude">Slack (#am-pm-review)</span>** <span data-proof="authored" data-by="ai:claude">— Generate output ready for the review workflow</span>

* **<span data-proof="authored" data-by="ai:claude">Docs Automator / SignWell</span>** <span data-proof="authored" data-by="ai:claude">— Structured data output for document generation pipeline</span>