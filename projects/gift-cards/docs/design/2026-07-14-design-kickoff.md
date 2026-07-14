# Card Vault — Design Kickoff (2026-07-14)

**In the room:** Spencer · Tim · Hannah · Candace · Kaitlin · Stephanie (PM)
**Context:** Card Vault SOW verbally approved by Progressive today; S&M agreement out for signature.
Tim's working prototype (GitLab) meets the project requirements; this phase makes it meet the users.

## Success — the one test

**A Progressive staff member logs in for the first time and completes their real workflow without
anyone helping them.** The users are named: Doug + Elena (admin); Lisa, Lloyd, and a new hire
(operations). No user interviews needed — every design question becomes "does this help Lisa's
first login?"

## The two gaps design closes

1. **Language** — labels, helper text, and terminology were written build-first; they need to be in
   Progressive's words. (Audit: `2026-07-14-ui-string-inventory.md`; rulings land in
   `2026-07-14-design-glossary.md`.)
2. **Workflow fit** — screens follow how the system was built, not how an operator's day runs.

Tim's groundwork is the foundation, not the problem: `docs/designer-user-flows.md` (all 15 flows) and
the style guide's Content Style section already carry designer-grade decisions. Read both first.

## Order of operations

| Phase | When | Deliverable |
|-------|------|-------------|
| 1 · Language pass | Week 1 | Approved glossary v1 + revised strings, applied by Tim in one batch. First ruling queued: Vendor vs Merchant. |
| 2 · Output & delivery flow | Weeks 2–4 | Redesigned export/delivery flow honoring 7/14 client requirements: legacy clients keep PDF-in-ZIP; new clients get the simpler path. |
| 3 · Screen-by-screen intuitiveness | Ongoing | Prioritized fix list from walking each flow as one of the five named users. |

## How we work

- **GitLab is truth; Figma is the mirror.** All current screens are imported to Figma for markup;
  the mirror refreshes after merges.
- **The loop:** Figma comment/redline → structured change request (prepared) → GitLab issue → Tim
  implements → screens re-imported.
- **Prepared materials** (string table, annotated screens, primer) arrive ready — the tedious parts
  are done before design sits down. The team Claude project answers "how does this flow work?"
  questions between syncs.
- **Nobody's workflow changes today.** Design happens in Figma with existing tools.

## Decisions needed in the room

1. **Tim:** preferred change-request format (GitLab issues / doc / tagged Figma comments) + mirror
   refresh cadence.
2. **Tim:** GitLab view access for Candace + Kaitlin.
3. **Hannah:** confirmed as tie-breaker on glossary/taste rulings.
4. **All:** phase order holds — words → output flow → ongoing polish.
5. **All:** standing sync — weekly 30-min design/dev, or async until phase 2.

## This week

| Who | By end of week |
|-----|----------------|
| Candace + Kaitlin | Read Tim's two docs; walk the prototype as "Lisa's first login"; start ruling on the string table |
| Tim | Access + change-request answer; flag screens about to change |
| Hannah | Skim the flow doc; first glossary ratifications (Vendor vs Merchant) |
| Stephanie | Track SOW signature (DropboxSign); put the standing sync on calendars |
| Spencer | Deliver string table + primer (done — this pack); confirm Figma mirror is complete |
