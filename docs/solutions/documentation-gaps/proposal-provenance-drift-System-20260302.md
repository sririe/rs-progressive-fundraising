---
module: System
date: 2026-03-02
problem_type: documentation_gap
component: documentation
symptoms:
  - "Proposal plan contained unsourced claims presented as client-confirmed decisions"
  - "Client requests reframed as exclusions without acknowledgment"
  - "Red Stamp interpretations blended with client statements without provenance tracking"
  - "No mechanism to distinguish confirmed decisions from assumptions or recommendations"
root_cause: inadequate_documentation
resolution_type: documentation_update
severity: high
tags: [provenance, decision-log, proposal, drift, cross-reference, source-fidelity, client-engagement]
---

# <span data-proof="authored" data-by="ai:claude">Troubleshooting: Proposal Document Drift from Source Materials</span>

## <span data-proof="authored" data-by="ai:claude">Problem</span>

<span data-proof="authored" data-by="ai:claude">A three-tier engagement proposal plan for Progressive Gift Cards drifted from its source materials (client meeting transcript, discovery call summary, internal pre-meeting notes) over iterative AI-assisted refinement. Each editing pass felt like improvement locally but introduced cumulative distortion: unsourced claims were added, client requests were reframed as exclusions, Red Stamp interpretations were presented as settled decisions, and there was no provenance tracking for where decisions came from.</span>

<span data-proof="authored" data-by="ai:claude">The drift was invisible during editing because the document remained structurally coherent — it read like a polished proposal. The divergence from source reality only surfaced during a deliberate cross-reference analysis against the original transcripts and notes.</span>

## <span data-proof="authored" data-by="ai:claude">Environment</span>

* <span data-proof="authored" data-by="ai:claude">Module: System (knowledge work / document governance)</span>

* <span data-proof="authored" data-by="ai:claude">Affected Component:</span> <span data-proof="authored" data-by="ai:claude">`docs/plans/2026-02-23-feat-three-tier-engagement-proposal-plan.md`</span>

* <span data-proof="authored" data-by="ai:claude">Source Documents: client meeting transcript (Jan 29, 2025), discovery call summary, internal pre-meeting notes, brainstorm document</span>

* <span data-proof="authored" data-by="ai:claude">Date: 2026-03-02</span>

## <span data-proof="authored" data-by="ai:claude">Symptoms</span>

* <span data-proof="authored" data-by="ai:claude">"Makes Progressive look unprofessional" appeared in the proposal — nobody in any source document used this language</span>

* <span data-proof="authored" data-by="ai:claude">"Incompatible software" listed as a delivery cause — not mentioned in any source</span>

* <span data-proof="authored" data-by="ai:claude">Magic link authentication presented as a decided approach — never discussed with Progressive; Lloyd raised 2FA concerns that pointed in a different direction</span>

* <span data-proof="authored" data-by="ai:claude">Individual recipient distribution listed as "explicitly excluded from all tiers" — but Doug explicitly asked for it: "I want to be able to deliver to the end user as well"</span>

* <span data-proof="authored" data-by="ai:claude">"Budget-conscious" framing used to reject assessment-only approach — but Doug said "I'm happy to invest in you guys"</span>

* <span data-proof="authored" data-by="ai:claude">Specific security parameters (8hr session timeout, 15min token expiry) stated as requirements — never discussed with anyone</span>

* <span data-proof="authored" data-by="ai:claude">Fundstream treated only as a rejected platform option — but Doug cited them as competitive pressure Progressive needs to match</span>

* <span data-proof="authored" data-by="ai:claude">"Two problems masquerading as one" framing presented as the client's view — but Doug's priorities were (1) portal, (2) white-label, (3) automation; operational fragility was Red Stamp's advisory observation</span>

## <span data-proof="authored" data-by="ai:claude">What Didn't Work</span>

**<span data-proof="authored" data-by="ai:claude">Editing without reference audit:</span>** <span data-proof="authored" data-by="ai:claude">Each refinement pass operated on the document's current state rather than checking claims against source materials. The document became self-referential — later edits built on earlier inferences, compounding drift.</span>

**<span data-proof="authored" data-by="ai:claude">Implicit decision tracking:</span>** <span data-proof="authored" data-by="ai:claude">Decisions lived in prose narrative without attribution. "We decided X" blended client statements, Red Stamp thinking, and things nobody had actually decided. There was no way to distinguish these without re-reading the original transcripts.</span>

## <span data-proof="authored" data-by="ai:claude">Solution</span>

### <span data-proof="authored" data-by="ai:claude">1. Cross-Reference Analysis</span>

<span data-proof="authored" data-by="ai:claude">Launched an analysis agent to read all source documents in parallel and compare them systematically against the proposal. The analysis produced:</span>

* **<span data-proof="authored" data-by="ai:claude">Alignment</span>**<span data-proof="authored" data-by="ai:claude">: 13 claims directly supported by source materials (with citations)</span>

* **<span data-proof="authored" data-by="ai:claude">Drift</span>**<span data-proof="authored" data-by="ai:claude">: 11 items that went beyond or reframed what sources actually said</span>

* **<span data-proof="authored" data-by="ai:claude">Gaps</span>**<span data-proof="authored" data-by="ai:claude">: 12 things from the sources that the proposal missed or under-represented</span>

* **<span data-proof="authored" data-by="ai:claude">Tone/framing</span>**<span data-proof="authored" data-by="ai:claude">: 6 observations about how the proposal's voice differed from the source conversations</span>

### <span data-proof="authored" data-by="ai:claude">2. Systematic Corrections</span>

<span data-proof="authored" data-by="ai:claude">Walked back each drifted claim:</span>

* <span data-proof="authored" data-by="ai:claude">Removed unsourced characterizations ("unprofessional", "incompatible software")</span>

* <span data-proof="authored" data-by="ai:claude">Changed magic link auth from "decided" to "recommended, needs validation" and surfaced Lloyd's 2FA concern</span>

* <span data-proof="authored" data-by="ai:claude">Changed individual recipient distribution from "excluded" to "deferred — Doug requested this"</span>

* <span data-proof="authored" data-by="ai:claude">Replaced "budget-conscious" framing with Doug's actual words about investment willingness</span>

* <span data-proof="authored" data-by="ai:claude">Removed specific security parameters, deferred to implementation</span>

* <span data-proof="authored" data-by="ai:claude">Added Fundstream as competitive pressure alongside platform rejection</span>

* <span data-proof="authored" data-by="ai:claude">Restructured problem statement to lead with Doug's stated priorities in his own words, then layer in Red Stamp's advisory observation</span>

### <span data-proof="authored" data-by="ai:claude">3. Decision Log (Structural Fix)</span>

<span data-proof="authored" data-by="ai:claude">Added a new "Decision Log" section with three provenance tiers:</span>

**<span data-proof="authored" data-by="ai:claude">Confirmed by client</span>** <span data-proof="authored" data-by="ai:claude">— Specific quotes with transcript timestamps and document sources. Example: "Doug on transcript ~36:10: 'The ordering will continue exactly how it is right now.'"</span>

**<span data-proof="authored" data-by="ai:claude">Red Stamp additions</span>** <span data-proof="authored" data-by="ai:claude">— Internal analysis and recommendations explicitly marked as such, with a column for whether client validation is needed. Example: "Magic link auth — recommended by Red Stamp; conflicts with Lloyd's 2FA concern; NEEDS VALIDATION."</span>

**<span data-proof="authored" data-by="ai:claude">Still needs resolution</span>** <span data-proof="authored" data-by="ai:claude">— Gaps, unknowns, and blocked decisions with what they block and how to resolve them. Example: "Card data storage (URLs vs raw data) — blocks portal security model — resolve via 30-min Lloyd conversation."</span>

### <span data-proof="authored" data-by="ai:claude">4. Additional Context Restored</span>

* <span data-proof="authored" data-by="ai:claude">Gord's "optional dashboard" framing (portal as fallback reference tool, not primary delivery channel)</span>

* <span data-proof="authored" data-by="ai:claude">Lloyd's existing process detail from the transcript (deep-dive doesn't start from zero)</span>

* <span data-proof="authored" data-by="ai:claude">Doug's physical automation roadmap (may intersect with Option 3 inventory management)</span>

* <span data-proof="authored" data-by="ai:claude">Red Stamp capacity concerns (Bronte flagged two-person dev team vs. Option 3 scope)</span>

* <span data-proof="authored" data-by="ai:claude">Shoppers/Loblaws generation status as uncertain</span>

* <span data-proof="authored" data-by="ai:claude">Corrected blocker date (January 2025, not 2026)</span>

## <span data-proof="authored" data-by="ai:claude">Why This Works</span>

**<span data-proof="authored" data-by="ai:claude">Makes drift visible in real-time, not discoverable in retrospect.</span>** <span data-proof="authored" data-by="ai:claude">The Decision Log separates "what the client said" from "what we think" from "what we don't know yet." Any reader — Spencer, Tim, or a future team member — can immediately see the provenance of every claim.</span>

**<span data-proof="authored" data-by="ai:claude">Closes the feedback loop.</span>** <span data-proof="authored" data-by="ai:claude">Specific attribution (date, speaker, source) makes it easy to re-verify claims and catch new drift on the next review.</span>

**<span data-proof="authored" data-by="ai:claude">Separates recommendation from decision.</span>** <span data-proof="authored" data-by="ai:claude">Red Stamp's job is to propose approaches; the client's job is to confirm. The Decision Log makes that boundary explicit.</span>

**<span data-proof="authored" data-by="ai:claude">Prevents "we thought you wanted X" conversations.</span>** <span data-proof="authored" data-by="ai:claude">Every exclusion now traces to either a client-confirmed deferral or a Red Stamp recommendation. Individual recipient distribution — the highest-risk item — is explicitly flagged as "Doug asked for this; present it as a phased deferral, not a cut."</span>

## <span data-proof="authored" data-by="ai:claude">Prevention</span>

**<span data-proof="authored" data-by="ai:claude">1. Provenance tagging from the start.</span>** <span data-proof="authored" data-by="ai:claude">When creating client-facing planning documents, tag every substantive claim as</span> <span data-proof="authored" data-by="ai:claude">`[CLIENT]`</span> <span data-proof="authored" data-by="ai:claude">(confirmed),</span> <span data-proof="authored" data-by="ai:claude">`[RED_STAMP]`</span> <span data-proof="authored" data-by="ai:claude">(recommendation), or</span> <span data-proof="authored" data-by="ai:claude">`[NEEDS_VALIDATION]`</span> <span data-proof="authored" data-by="ai:claude">(assumption). Do this during writing, not after.</span>

**<span data-proof="authored" data-by="ai:claude">2. Decision Log as a living source document.</span>** <span data-proof="authored" data-by="ai:claude">Create the decision log before writing the proposal. Update it during writing. Use it as a validation checklist before delivery. It's the evidence trail, not a retrospective summary.</span>

**<span data-proof="authored" data-by="ai:claude">3. Cross-reference validation before finalization.</span>** <span data-proof="authored" data-by="ai:claude">Before any proposal reaches the client, run a systematic check of key claims against source documents. This session's analysis took ~15 minutes of agent time and caught 11 drift items.</span>

**<span data-proof="authored" data-by="ai:claude">4. Exclusions as explicit phasing decisions.</span>** <span data-proof="authored" data-by="ai:claude">Never list something the client asked for under "exclusions" without acknowledging the request and explaining the phasing rationale. The framing should be "deferred to Phase X because Y," not "not included."</span>

**<span data-proof="authored" data-by="ai:claude">5. Oral validation gate.</span>** <span data-proof="authored" data-by="ai:claude">Before proposal delivery, confirm the top 3-5 risky assumptions verbally with the relevant people (Lloyd for technical, Doug for strategic). Log the confirmation in the decision tracker.</span>

**<span data-proof="authored" data-by="ai:claude">6. Freshness awareness.</span>** <span data-proof="authored" data-by="ai:claude">For long-running engagements (this proposal was built 13+ months after the source conversations), add a freshness notice flagging what may have changed and recommending a check-in before presenting.</span>

## <span data-proof="authored" data-by="ai:claude">Related Issues</span>

* [<span data-proof="authored" data-by="ai:claude">Proof Not Discoverable Across Projects</span>](../workflow-issues/proof-not-discoverable-across-projects-System-20260302.md) <span data-proof="authored" data-by="ai:claude">— Same session; the "Missed Signal" section in that doc addresses the same macro-vs-micro pattern: a brainstorm document about building systems wasn't connected to the immediate implementation work</span>