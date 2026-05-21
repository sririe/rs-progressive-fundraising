---
title: "Email to Lloyd — Fixture Package Request"
type: plan
category: client-email
date: 2026-04-27
status: ready-to-send
tags:
  - progressive
  - lloyd
  - email
  - fixture-request
  - reproduction
related:
  - projects/gift-cards/docs/plans/2026-04-23-lloyd-script-review-next-steps.md
  - projects/gift-cards/docs/plans/2026-04-27-pre-doug-return-punch-list.md
---

# Email to Lloyd — Fixture Package Request

**To:** Lloyd Scrubb (lscrubb@progressivefundraising.ca)
**Cc:** Danny Norton, Tim Lemke; optionally Doug Beers (Spencer's call)
**Subject:** Following up on the gift card scripts — a few more files to round things out
**Send when:** Monday April 27, 2026 (today)

---

Hi Lloyd,

Thanks again for sending the scripts and the Amazon workbook last week. Tim and I have spent some time with them and now have a clear picture of the general flow — invoice PDF into vendor-specific Excel files, then the Amazon Excel file into PDFs and ZIPs through the SVG template and Inkscape. That's exactly what we needed to confirm at the workflow level.

To finish the technical assessment and put a build estimate in front of Doug we can stand behind, we'd like to actually run the workflow end-to-end on one of our machines — using sanitized test data, no live card numbers needed. That requires a few more pieces beyond the two scripts you sent.

Could you put together a small reproducible package with the following?

- The folder context the scripts run from (the `prototype/` folder layout, or however you have it organized)
- `utilities.py` — the Amazon generator imports `zipFilesInDir` from it
- The Amazon SVG template under `templates/amazon-e-giftcard-template.svg`
- The vendor Excel templates under `orders/<vendor>/template/` — Amazon at minimum, plus whichever others you have handy
- One representative invoice PDF (sanitized is fine)
- One populated Amazon Excel input with fake/sanitized card data
- One known-good generated output folder, so we can compare what our reproduction produces against what yours produces today
- Any Walmart-side scripts (PowerShell or otherwise) and a quick note on how the activation step works
- A line or two on what SystemOne expects in the ZIP and the log file

If anything in there is easier to grab as a Drive folder share than as an attachment, that works too — whatever's easiest for you.

A few questions while I have you, none urgent:

1. The Amazon generator reads `SERIAL NUMBER` and requires it to be present, but it doesn't look like the serial gets written into the PDF or the log file. Is that just for inventory traceability in the input workbook, or am I missing where it ends up downstream?
2. For the vendor-provided merchants, is inventory population (claim codes, URLs, etc.) handled manually after the invoice-to-Excel step, or is there another script in the chain that we haven't seen?
3. Walmart activation — is that PowerShell, the Walmart Virtual GC portal, or some mix of both? Trying to confirm whether the activation step needs to live on a specific machine.
4. SystemOne — do you know if they have an API option, or is the ZIP upload + URL export always manual?

The goal of all this is not to take over your live process. It's to have everything we need to give Doug a credible answer on what the next system looks like, what it costs, and what it doesn't do. Reproducing the workflow once on our side makes our recommendation grounded in reality rather than in code reading.

Thanks Lloyd — really appreciate everything you've shared so far. Happy to jump on a quick call if any of this is easier to walk through than to write up.

Best,
Spencer

---

## Internal Notes (Not Part of the Email)

- Send Monday April 27. If we hit Wednesday April 29 without a reply, Danny nudges directly — Lloyd is responsive but easy to lose to email backlog.
- We should not cc Doug on this on send-day. He's on vacation and doesn't need to be looped into a routine technical request. Loop him in async if Lloyd surfaces any concern about sharing files.
- The four follow-up questions are low-pressure on purpose — they're not gating the fixture package, just rounding out the picture. If Lloyd answers them in the same reply, great; if not, we'll catch them at the reproduction stage.
- The Walmart question is the one we most want answered, since Tim digesting PowerShell is a Friday action item and his work is faster with a one-line orientation from Lloyd.
