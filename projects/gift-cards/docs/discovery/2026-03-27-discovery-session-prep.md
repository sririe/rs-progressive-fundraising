---
type: discovery
category: session-prep
tags:
  - lloyd
  - mario
  - workflow-mapping
  - technical-discovery
  - card-generation
key_insights:
  - Lloyd's March 26 email framed the current system as Python scripts, Java/Fiserv activation, local Windows dependencies, and vendor-specific card workflows.
  - The March 27 sessions needed to capture both technical architecture from Lloyd and operator workflow from Mario.
  - The discovery checklist centered on runbooks, technical specification inputs, security assessment, and strategic roadmap signals.
participants:
  red_stamp:
    - Spencer R.
    - Danny
  progressive:
    - Lloyd S.
    - Mario
    - Doug B.
related:
  - projects/gift-cards/docs/discovery/2026-03-27-lloyd-handoff-session1-notes.md
  - projects/gift-cards/docs/discovery/2026-03-27-mario-handoff-session2-notes.md
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
status: complete
blockers: []
---

# Progressive Discovery Session Prep — March 27, 2026

## Schedule

**Session 1: Technical Discovery with Lloyd (9:30-10:30am PDT, Remote)**
- Lloyd Scrubb (remote) walks through how the digital gift card system is built
- Danny in-person at Progressive office, Spencer remote via Google Meet
- Lloyd has ~1 hour — need to be efficient

**Session 2: Workflow Mapping with Mario (10:30am-1:30pm PDT, In-Office)**
- Danny in-person, Spencer remote
- Mario executes the workflow but has limited technical depth — read between the lines
- Doug available for framing and closeout

## What We Already Know (from Lloyd's email March 26)

### Architecture Overview
- All scripts in Python, stored on Progressive's Google Workspace: `G:\My Drive\progressive-fundraising\prototype`
- Main script: `e-giftcard-excelfile-generator-new-invoice-format.py` — generates Excel files for digital gift card generation/storage
- Run from PowerShell command line, prompts for PDF format invoice
- Windows environment: Python, Java, Windows libraries, Inkscape for PDF generation

### Vendor Categories
**"Generate" vendors** (Amazon, Indigo, Walmart): Progressive gets raw card data (numbers, PINs, claim codes) and generates PDF gift cards
- Generation process: obtain card info from inventory → update Excel → run generation program → produces PDFs in a ZIP file
- Customer delivery options: password-protected ZIP of PDFs, or URLs via password-protected Excel
- URL generation: upload ZIP to https://ecard.proegiftcards.ca/ → export Excel with URLs → add encryption password

**"Store/URL" vendors** (most others): Vendors provide URLs → pasted into Excel with encryption passwords

**Special cases:**
- Loblaws/Shoppers: previously had Progressive branding on gift cards, now generic URLs (treated like standard URL vendors)
- Petro-Canada: previously PDFs, now URLs
- Uber: discontinued

### Walmart/Fiserv Integration
- Only vendor with direct backend integration
- Java program: `walmart-giftcard-virtual-activation-production.jar`
- Executed from Desktop icon, prompts for Excel file
- Sends activation request to Fiserv

### Active API Work
- **Esso**: RESTful API, waiting on certification testing, Python
- **Blackhawk Network (Tim Hortons)**: RESTful API, waiting on certification, Python
  - Has async API calls requiring callback function
  - UAT: using ngrok for callbacks
  - Production: talking to SystemBind about hosting callback functionality (in progress)

### Scalability
- Good for large orders (many gift cards, few vendors)
- Not great for small orders with many vendors
- Lloyd's key insight: "if inventory were maintained in a well-known format it should be possible to eliminate any manual requirement for update of the final Excel file"

---

## Session 1: Questions for Lloyd (Technical Discovery)

### Architecture Deep Dive
1. Walk us through the folder structure in `G:\My Drive\progressive-fundraising\prototype` — what's in there beyond the main script?
2. How many separate scripts/programs exist in total? What does each one do?
3. What's the version history like? Is there any source control, or is it file-based versioning?
4. What happens when a script fails mid-execution? Is there error handling, logging, or does it just crash?
5. Are there any configuration files, or is everything hardcoded in the scripts?

### Vendor Integration Details
6. For the "generate" vendors — how is inventory currently maintained? What format is it in?
7. You mentioned "a well-known format" for inventory could eliminate manual Excel updates — what would that format look like in your mind?
8. How do you currently track which gift cards have been allocated vs. which are still in inventory?
9. When a new vendor is onboarded, what's the process for adding them to the system?
10. How many active vendors are there right now? Which ones have the highest volume?

### Walmart/Fiserv
11. What error handling exists in the Fiserv integration? What happens if an activation fails?
12. Is there retry logic, or does someone need to manually re-run?
13. What credentials are needed for the Fiserv connection? Where are they stored?
14. Has there ever been a production incident with the Walmart integration?

### Esso & Blackhawk API Work
15. What stage are the Esso and Blackhawk integrations actually at? Are we talking weeks or months from certification?
16. For Blackhawk's async callbacks — what data comes back in the callback? What needs to happen when it arrives?
17. What's the SystemBind conversation status? Is there a timeline or is it stalled?
18. If SystemBind can't host callbacks, what's the fallback?
19. Is there any documentation for either API integration?

### Security & Credentials
20. Where are API keys, passwords, and credentials stored? In the scripts? Environment variables? A separate file?
21. Who has access to the Google Workspace folder with the scripts?
22. How are encryption passwords for the customer-facing Excel files generated and managed?
23. Is there any audit trail for who generated what and when?

### Bus Factor & Knowledge Transfer
24. If you were unavailable tomorrow, could Mario execute every vendor workflow end-to-end?
25. What are the top 3 things that would be hardest to hand off?
26. Is there anything undocumented that lives only in your head?

---

## Session 2: Questions for Mario (Workflow Mapping)

*Note: Mario is the operator, not the builder. Ask about what he does, not how the system works. Watch his screen closely — the workflow reveals itself through his actions.*

### Opening the Day
1. When a new order comes in, how do you find out about it? Email? System notification?
2. What's the first thing you open on your computer when you're going to process an order?
3. Walk me through a typical order from the moment you receive it to the moment the customer gets their gift cards.

### Vendor-Specific Workflows
4. Which vendors do you process most often?
5. Which vendor is the easiest to process? What makes it easy?
6. Which vendor is the most annoying or difficult? What makes it hard?
7. Can you show us a real example of processing an order for [most common vendor]?
8. What changes between vendors? Is it just different websites, or does the whole process change?

### Pain Points (Operator Language)
9. What part of this takes the longest?
10. Where do you most often have to redo something or go back and fix a mistake?
11. Is there anything you have to look up or check with someone else before you can proceed?
12. What do you do when something doesn't work the way it's supposed to?
13. Have you ever accidentally sent the wrong gift cards or the wrong amounts? What happened?

### Tools & Screens
14. How many different tools/websites/programs do you have open while processing an order?
15. Can you show us your desktop? What are these icons? (Point to the Desktop icons Lloyd mentioned)
16. When you run the PowerShell script, what do you type? Can you show us?
17. What does the Excel file look like before and after you process it?

### Handoff & Edge Cases
18. What happens when a customer wants their cards in a specific format you don't usually do?
19. How do you handle partial orders — like if a vendor doesn't have enough inventory?
20. Who do you ask when you're not sure what to do?
21. What would you change about this process if you could change anything?

### Volume & Timing
22. How many orders do you typically process in a day? A week?
23. Are there peak periods where volume spikes?
24. How long does a typical order take from start to finish?

---

## Must-Capture Checklist

### For Vendor Runbooks
- [ ] Complete list of active digital vendors
- [ ] Step-by-step workflow for each vendor category (generate, URL, Walmart/Fiserv)
- [ ] Input format and source for each vendor
- [ ] Output format and delivery method for each vendor
- [ ] Edge cases and exceptions by vendor
- [ ] Which Desktop icons map to which programs
- [ ] Sample inputs and outputs captured/screenshotted

### For Technical Specification
- [ ] Complete inventory of scripts and programs (name, language, purpose)
- [ ] Dependencies and environment requirements
- [ ] Data flow diagram: order in → processing → customer delivery
- [ ] Integration points (Fiserv, Esso API, Blackhawk API, SystemBind, ecard.proegiftcards.ca)
- [ ] Where manual steps exist that could be automated
- [ ] Lloyd's "well-known format" vision documented

### For Security Assessment
- [ ] Where sensitive card data exists at each stage
- [ ] How credentials are stored and accessed
- [ ] Who has access to what
- [ ] How customer-facing files are encrypted
- [ ] Data retention — what happens to card data after delivery?
- [ ] Any compliance requirements mentioned

### For Strategic Roadmap
- [ ] Biggest risks identified
- [ ] Highest-impact automation opportunities
- [ ] What needs to happen before scaling digital volume
- [ ] Lloyd's priorities vs. operator pain points
- [ ] Multi-destination distribution demand signal (from Doug's client email)

---

## Live Process Map Template

Fill this in during the session for each vendor workflow:

```text
VENDOR: _______________
TYPE: [ ] Generate  [ ] URL  [ ] Fiserv

1. ORDER INTAKE
   - How received: _______________
   - Format: _______________
   - Who receives: _______________

2. INVENTORY CHECK
   - Where inventory lives: _______________
   - How checked: _______________
   - What if insufficient: _______________

3. PROCESSING
   - Script/program used: _______________
   - Inputs required: _______________
   - Manual steps: _______________
   - Automated steps: _______________
   - Time to complete: _______________

4. QUALITY CHECK
   - How verified: _______________
   - Common errors: _______________

5. CUSTOMER DELIVERY
   - Format: [ ] ZIP/PDF  [ ] URL Excel  [ ] Other: ___
   - How encrypted: _______________
   - How sent: _______________

6. POST-DELIVERY
   - Confirmation: _______________
   - Record keeping: _______________

PAIN POINTS: _______________
AUTOMATION OPPORTUNITIES: _______________
```

---

## Agentic Acceleration Watchlist

Flag these during the session — they're signals for the build phase:

1. **Manual data entry between systems** — anytime someone copies data from one place to another
2. **Format conversion steps** — Excel to PDF, ZIP to URL, any manual transformation
3. **Decision points that follow simple rules** — "if vendor X, then do Y" logic that a human is currently executing
4. **Waiting on vendor responses** — anywhere the process blocks on an external system
5. **Quality checks that could be automated** — validation that follows a pattern
6. **Credential/password management** — manual handling of encryption passwords
7. **Inventory management** — anything related to Lloyd's "well-known format" insight
8. **The callback problem** — Blackhawk's async pattern is a real architecture decision that will shape the build

### Red Flags to Watch For
- Workflows that exist only in Lloyd's head and haven't been passed to Mario
- Security practices that are "good enough for now" but won't survive scale
- Vendor relationships that are informal and undocumented
- Edge cases that Mario handles by "just knowing" rather than following a process

---

## Logistics

| | Session 1 | Session 2 |
|---|---|---|
| Time | 9:30-10:30am PDT | 10:30am-1:30pm PDT |
| Focus | Technical architecture | Workflow execution |
| Key person | Lloyd (remote) | Mario (in-person) |
| Location | Google Meet | Progressive office + Google Meet |
| Your role | Remote, probing questions | Remote, probing questions |
| Danny's role | In-person facilitator | In-person facilitator |
| Doug's role | — | Framing + closeout |

**OpenOats:** Running for live transcription. Consider feeding transcript into a Claude session with this checklist to identify gaps in real time.
