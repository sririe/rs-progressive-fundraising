---
title: "Progressive Secure Card Vault and Fulfillment Tool SOW Draft"
type: plan
category: statement-of-work
date: 2026-05-27
status: draft
tags:
  - progressive
  - sow
  - secure-card-vault
  - fulfillment
  - digital-gift-cards
  - phase-1
key_decisions:
  - Phase 1 should focus on the Secure Card Vault and Fulfillment Tool rather than replacing the full customer-facing ordering experience.
  - QuickBooks integration, customer accounts, direct recipient delivery, and merchant-branded portals should remain outside Phase 1.
  - A lightweight handoff from the existing WordPress/Formidable order flow into the vault can be included if the current site supports it cleanly.
key_insights:
  - Discovery showed that digital gift card fulfillment is the highest-risk operational workflow because it relies on spreadsheets, scripts, manual file handling, and specific people knowing the process.
  - The first build should give Progressive one secure internal place to track pending orders, digital card inventory, allocation, export-ready files, and order activity.
  - Card data is cash-equivalent, so security, access rules, encrypted storage, production handling, and staff training need to be explicit in the scope.
participants:
  redstamp:
    - Spencer Ririe
    - Tim Lemke
  progressive:
    - Doug Beers
    - Mario
    - Lloyd
    - Elena
related:
  - projects/gift-cards/docs/plans/2026-05-27-progressive-client-presentation-draft.html
  - projects/gift-cards/docs/plans/2026-05-21-phase-1-mvp-boundary.html
  - projects/gift-cards/docs/plans/2026-05-21-current-state-workflow-map.html
  - projects/gift-cards/docs/plans/2026-05-21-merchant-fulfillment-matrix.html
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
source_documents:
  - /Users/spencer/Downloads/progressive-gift-cards-prd.md
  - https://docs.google.com/document/d/1Lnlpwk_4V9qLq7LM7CvPfgWWhhC3DBn7i2iG1IQ0ZGY/edit
  - https://docs.google.com/document/d/10QZWx-SKsru70UidZ1foT1AdRr-4KeC4SsetEP9mTNs/edit
blockers:
  - Confirm final project fee and agency rate before sending to Progressive.
  - Confirm the exact technical method for passing WordPress/Formidable orders into the vault.
  - Confirm the first set of merchant file formats and examples that must be supported in Phase 1.
---

# Progressive Fundraising - Secure Card Vault and Fulfillment Tool

## Internal Review Notes - Remove Before Sending

This section is not part of the client-facing SOW. It is included here so this file can act as the internal source of truth while the proposal is still being sharpened.

- **Project Fee:** This draft uses a recommended fixed Project Fee of **$32,000 CAD plus tax**, which sits inside the $25,000-$35,000 range discussed for Phase 1.
- **Agency Rate:** This draft uses **$160 CAD plus tax per hour**, matching the prior Progressive blog SOW. `CLIENT.md` currently lists `$150 CAD/hr`, so the final rate should be confirmed before sending.
- **Payment Schedule:** This draft uses a 40% / 40% / 20% milestone schedule to fit a 6-8 week software build. This can be simplified to 50% / 50% if preferred.
- **Physical Cards:** Tim's PRD includes physical card workflows as part of the prototype model. This SOW keeps the Phase 1 build focused on digital gift card fulfillment and excludes a full physical warehouse, pick-pack, or stickering workflow.
- **WordPress/Formidable Handoff:** This draft includes a lightweight handoff from the current public order flow into pending vault requests. The final scope should confirm whether this is handled through Formidable hooks, API/webhook, scheduled import, or another practical method.
- **Walmart:** This draft allows for supported data/file handling around Walmart only where it is based on existing scripts, templates, or sample outputs. It does not include automating Walmart's website, activation portal, login flow, or reconciliation process.
- **Initial Inventory Migration:** This draft assumes Progressive can provide current digital inventory in an agreed importable format or help normalize it. Large manual cleanup of historical files should be treated as additional scope if needed.
- **Support After Launch:** This SOW includes launch support and handoff, but not ongoing maintenance, monitoring, or help desk support. A separate support plan should likely follow once Progressive confirms how much operational support they want after launch.

---

## Statement of Work

**Delivered to:** Doug Beers  
**Client:** Progressive Fundraising  
**Date:** May 27, 2026

01. Project Overview  
02. Scope  
03. Tentative Timeline  
04. Assumptions  
05. Risks  
06. Out of Scope  
07. Project Terms  
08. Approvals

## 01. Project Overview

Redstamp and Progressive completed discovery into the current digital gift card order and fulfillment workflow. The discovery process showed that Progressive's current approach works because the team has built practical workarounds over time, but the workflow is difficult to operate, difficult to hand off, and increasingly risky as order volume and merchant complexity grow.

Today, digital gift card fulfillment depends on a mix of WordPress/Formidable order intake, email, spreadsheets, Google Drive folders, Lloyd's scripts, manual file preparation, encrypted file delivery, and team knowledge held by specific people. Digital card data is cash-equivalent, so the current reliance on spreadsheets, local scripts, and manual file handling creates operational and security risk.

This Statement of Work covers the recommended first build: a **Secure Card Vault and Fulfillment Tool**. The goal is to give Progressive one secure internal system for tracking pending digital gift card orders, digital card inventory, inventory allocation, customer-ready export files, fulfillment status, and order activity.

This first build is intended to make the internal fulfillment workflow more secure, visible, repeatable, and manageable for Progressive's team. It is not intended to replace the full customer-facing ordering experience, process payments, automate QuickBooks, or introduce direct recipient delivery in Phase 1.

## 02. Scope

### Project Setup and Production Planning

Redstamp will begin with a focused kickoff and production planning process to confirm the working details needed to turn the discovery recommendation and prototype requirements into a Phase 1 internal production application suitable for Progressive's digital gift card fulfillment workflow.

This includes:

- Confirming Progressive's Phase 1 admin users, permission levels, and who can view or manage card data.
- Confirming the order fields, payment-status values, fulfillment-status values, and closed-order rules needed for the first build.
- Reviewing representative order examples, merchant inventory files, Lloyd's scripts/templates, and known-good customer-ready files.
- Confirming the first set of merchant file formats and fulfillment patterns that must be supported.
- Confirming the preferred import format for adding digital gift card inventory to the vault.
- Confirming the preferred export format for customer-ready files.
- Confirming production hosting, access, backup, and launch requirements.

### Production Application Foundation

Redstamp will design and build a secure internal web application for Progressive's team to manage digital gift card fulfillment.

This includes:

- A Phase 1 internal production application suitable for Progressive's digital gift card fulfillment workflow.
- Authenticated access for Progressive staff.
- Role-based permissions for staff who need different levels of access.
- Separate staging and production environments.
- Managed production database setup.
- Field-level encrypted storage for sensitive card fields such as card numbers, PINs, URLs, or access codes.
- Secure environment configuration for credentials and secrets.
- Basic application logging and production backup configuration.
- Recorded activity for security-sensitive actions agreed during production planning.
- A simple visual interface aligned with Progressive's operational needs and brand familiarity.

### Fulfillment Request Workflow

Redstamp will build the core fulfillment request workflow so Progressive can see and manage the digital gift card orders that need fulfillment.

This includes:

- A dashboard view of open fulfillment work.
- A request list with search, filtering, and clear status indicators.
- Request detail pages showing customer, order, line-item, payment, allocation, export, and fulfillment information.
- Manual/admin request creation for ad hoc digital gift card orders that do not originate from the public website.
- A lightweight handoff from the existing WordPress/Formidable order flow into pending vault requests, or an agreed fallback intake method if the current website cannot support a clean handoff within Phase 1.
- Manual payment-status updates so Progressive can mark an order as paid and ready to fulfill.
- Open and closed request states.
- Void, archive, delete, or close actions with appropriate confirmation, recorded activity, and card return handling.

The Phase 1 workflow is expected to preserve Progressive's current payment and invoice process. The vault will track whether an order is ready to fulfill, but it will not process payments or create QuickBooks invoices.

### Digital Card Vault and Inventory Management

Redstamp will build the Digital Card Vault so Progressive can store and manage digital gift card inventory in one secure system.

This includes:

- Digital card inventory organized by merchant, denomination, source, status, and use.
- Inventory counts by merchant and denomination so staff can see what is available before fulfilling an order.
- Searchable merchant and denomination views.
- CSV-based import for adding digital card inventory to the vault.
- Validation rules for required import fields.
- Available, allocated, delivered/used, and unavailable status handling.
- Allocation of available cards to paid fulfillment requests.
- Prevention of accidental over-allocation.
- Return of allocated cards to available inventory when a request is voided, archived, deleted, or reversed before fulfillment.

### Merchant-Specific Fulfillment and Customer-Ready Files

Redstamp will support the agreed Phase 1 merchant fulfillment patterns needed to create customer-ready files from the vault. The Phase 1 build will be limited to the agreed initial merchant file formats, templates, and fulfillment rules confirmed during production planning; additional merchant formats or materially different file-creation rules would be handled through a change order or later phase.

This includes:

- Preparing customer-ready files for fulfilled digital gift card orders.
- Supporting the agreed Phase 1 merchant-specific file requirements where Progressive provides current examples, templates, or scripts.
- Replacing or standardizing existing manual file preparation where feasible within Phase 1.
- Generating agreed Phase 1 card files or PDFs where the required data, template, business rules, and acceptance examples are clearly supplied and approved.
- Tracking when a customer-ready file has been created for an order.

For Walmart or any merchant with a special activation process, Phase 1 may support the data and file preparation steps that are already understood from existing materials. Phase 1 does not include automating third-party merchant websites, activation portals, login-based merchant workflows, or monthly reconciliation unless those items are added through a change order.

Phase 1 does not assume Redstamp can validate whether every card is active, redeemable, or carrying the expected balance. If a merchant provides a reliable validation method, Redstamp can assess whether that should be added to the workflow through a separate scope decision.

### Order Activity History and Operational Visibility

Redstamp will add order activity records so Progressive can see what happened to each request over time.

This includes activity records for:

- Request creation.
- Payment-status changes.
- Digital card inventory imports.
- Card allocation.
- Customer-ready file creation.
- Request closeout.
- Request deletion or reversal.
- Cards returned to available inventory.
- Other security-sensitive actions agreed during production planning.

These records are intended to help Progressive understand fulfillment status, troubleshoot support questions, and reduce reliance on memory or informal notes.

### Migration, Training, and Launch

Redstamp will support Progressive through setup, training, and launch of the Phase 1 system.

This includes:

- Setting up staging and production environments.
- Loading agreed test data into staging.
- Supporting one agreed initial import batch of current digital card inventory into production after Progressive has normalized it to the approved format.
- Testing the fulfillment workflow with Progressive using realistic order examples.
- Hands-on training for the Progressive team members who will use the vault.
- Basic handoff documentation covering key workflows.
- Launch support during the agreed initial go-live period.

### Deliverables

Redstamp will deliver:

- Secure Card Vault and Fulfillment Tool production application.
- Fulfillment dashboard, request list, request detail, and closed request views.
- Manual/admin digital order creation.
- Lightweight WordPress/Formidable order handoff into pending vault requests, or an agreed fallback intake method if a clean handoff is not technically feasible within Phase 1.
- Digital Card Vault with merchant, denomination, quantity, source, status, and allocation tracking.
- CSV import workflow for digital card inventory.
- Inventory allocation workflow for paid digital gift card orders.
- Customer-ready file creation for the agreed Phase 1 merchant patterns.
- Order activity records for key fulfillment and security-sensitive actions.
- Staging and production setup.
- One agreed initial inventory import batch.
- Progressive team training and handoff documentation.

## 03. Tentative Timeline

Project begins upon signature of SOW. Resourcing is guaranteed by Redstamp for a period of 2 business days from the date the SOW is sent. After this period, Redstamp may need to reassess availability and the timeline may be impacted as a result.

The estimated timeline for this project is **6-8 weeks from kickoff**, assuming timely access, decisions, source materials, and feedback from Progressive.

| Phase | Estimated Timing | Focus |
| --- | --- | --- |
| Kickoff and production planning | Week 1 | Confirm users, permissions, fields, statuses, sample orders, inventory formats, merchant patterns, and production requirements. |
| Working V1 build | Weeks 2-4 | Build the core admin application, request workflow, card vault, inventory import, allocation, and customer-ready file workflow using test data. |
| Website handoff and merchant workflow setup | Weeks 3-5 | Connect or import website-created pending orders and configure agreed merchant-specific file patterns. |
| Security hardening and production setup | Weeks 5-6 | Configure authentication, permissions, encrypted sensitive fields, staging/production environments, backups, and production settings. |
| Migration, QA, training, and launch prep | Weeks 7-8 | Import initial inventory, test realistic workflows, train Progressive staff, prepare launch, and support go-live. |

Timeline estimates may shift if source materials are delayed, the current website cannot support the expected order handoff, merchant file formats require additional cleanup, or Progressive requests scope changes during the build.

## 04. Assumptions

1. Progressive will provide representative order examples, merchant inventory files, current scripts/templates, and known-good customer-ready outputs at the start of the project.
2. Progressive will provide safe test data for staging and testing. Real card data will not be used in preview or test environments unless both teams explicitly agree to the controls.
3. Progressive will identify the staff members who need access to the vault and approve their permission levels.
4. Progressive will designate a primary point of contact for consolidated feedback and project decisions.
5. Regular check-ins will be scheduled throughout the project.
6. The existing WordPress/Formidable order flow will remain in place during Phase 1.
7. Payment processing will remain external to the vault.
8. QuickBooks invoice creation and accounting workflows will remain manual in Phase 1.
9. Payment status in the vault will be updated manually by Progressive staff unless a future integration is approved.
10. The website order handoff assumes the current WordPress/Formidable setup can expose the needed order information through a practical technical path.
11. If the current website cannot support the expected handoff cleanly, Redstamp will recommend a simpler fallback such as scheduled import, manual import, or copy/paste-assisted intake.
12. Initial inventory migration is limited to one agreed import batch and assumes Progressive can provide current digital inventory in an approved importable format or assist with cleanup.
13. Merchant-specific file creation is limited to the agreed Phase 1 set where Progressive provides current examples, rules, templates, scripts, and acceptance examples.
14. Progressive will remain responsible for confirming merchant card validity, activation status, and balances unless a specific validation workflow is added to scope.
15. Progressive will continue to be responsible for secure handling of exported files after they leave the vault, including storage, transmission, access controls, and any customer delivery process outside the application.
16. Third-party hosting, software, plugins, licenses, or other pass-through costs are not included in the Project Fee unless specifically stated.
17. One consolidated round of feedback is included for each major workflow milestone.
18. Delays of more than five business days in required feedback, materials, or approvals may place the project on hold.

## 05. Risks

The following are identified as potential risks for this project.

| Risk | Mitigation Strategy |
| --- | --- |
| Sensitive card data: digital gift cards are cash-equivalent. | Redstamp will build security controls into the application, including authenticated access, role-based permissions, encrypted sensitive fields, restricted production access, and activity records for sensitive actions. Progressive will also need clear staff rules for who can access card data and how customer-ready files are handled after they leave the vault. |
| Source material variability: merchant files, spreadsheets, scripts, and templates may be inconsistent. | Redstamp will review representative examples during production planning and define the agreed Phase 1 merchant patterns before implementation. Significant cleanup or support for additional merchant formats may require a change order. |
| Website integration limits: the current WordPress/Formidable setup may not expose order data in the exact format needed. | Redstamp will recommend the most practical alternative, which may include scheduled import, manual import, or a simpler copy/paste-assisted intake step. |
| Card validity and balance checking may remain manual. | Phase 1 will track inventory and allocation inside the vault, but it will not guarantee card activation, balance validation, or merchant-side redemption state unless a reliable merchant-supported validation method is added to scope. |
| Special merchant workflows: merchants such as Walmart may require manual portal steps or third-party systems outside Progressive's control. | Phase 1 will not automate those external systems unless added later. Redstamp will keep the vault focused on supported data, file, and workflow steps. |
| Operational adoption: the value of the vault depends on Progressive moving digital card inventory and fulfillment tracking into the new system. | Redstamp will include training, handoff documentation, and realistic workflow testing with Progressive staff before launch. |
| Timeline pressure: a 6-8 week timeline assumes prompt access, decisions, materials, and feedback from Progressive. | Redstamp will schedule regular check-ins and flag any material delay or scope concern quickly so Progressive can make timely decisions. |

## 06. Out of Scope

The following items are not included in this Phase 1 Statement of Work:

- Full replacement of the public customer ordering experience.
- Customer accounts, customer order history, customer status views, or customer card retrieval.
- QuickBooks invoice creation, QuickBooks synchronization, or accounting automation.
- Payment processing, BenjaPay changes, or storage of credit card/payment information.
- Direct recipient delivery as a managed service.
- Secure customer delivery portal, expiring customer download links, or customer access logging.
- Automated delivery emails from the vault.
- Direct merchant integrations, merchant API certification, or automatic card issuing from merchant systems.
- Automation of third-party merchant websites, activation portals, or login-based merchant workflows.
- Walmart monthly reconciliation automation.
- Merchant-side card balance checking, activation verification, or redemption validation unless separately scoped.
- Redemption reporting where merchants do not provide the required data.
- Merchant-branded or white-label portals.
- Full physical card warehouse, pick-pack, stickering, or shipping workflow.
- SystemOne replacement.
- Inventory forecasting, reorder automation, or low-inventory alerts.
- Ongoing maintenance, monitoring, emergency support, operational help desk support, or support beyond the agreed launch support period, unless covered by a separate support agreement or approved T&M request.
- Large-scale manual cleanup of historical inventory files beyond the agreed import preparation.
- Additional merchant formats or file-creation rules beyond the agreed Phase 1 set.

## 07. Project Terms

1) **Project Fee.** The Client shall pay Redstamp for the performance of the Services. A total of **$32,000 CAD plus tax**.

The Client further agrees to provide any additional amounts for any disbursements or third-party costs incurred on the Client's behalf. Any additional work required to complete above the Project Fee, along with the time it will take and the additional cost of completion, will be calculated at Redstamp's hourly rate of **$160 CAD plus tax per hour** (the "Agency Rate"). Ongoing support after the agreed launch support period may be addressed through a separate Quarterly Maintenance and Support agreement or approved T&M request.

2) **Payment Schedule.** The Project Fee will be billed according to the following schedule:

| Milestone | Amount | Terms |
| --- | ---: | --- |
| Upon SOW approval and project kickoff | $12,800 CAD plus tax | NET 7 |
| Upon working V1 delivery for Progressive review | $12,800 CAD plus tax | NET 30 |
| Upon launch readiness, training, and project completion | $6,400 CAD plus tax | NET 30 |

Additional hours approved by Client will be billed at the Agency Rate at the end of the month that the hours were incurred, with payment terms NET 30.

3) **Change Orders.** Redstamp's fees are based on the time it will take to complete the Services under normal circumstances. If the Client expands or alters the project's scope, requires further alterations to the project after sign-off, or other factors arise such as multiple revision requests or delays on the Client's part in providing content, access, source materials, or instructions that require more hours from Redstamp than are currently anticipated to complete the project, Redstamp will:

a) advise you when Redstamp's estimate for the project has been exceeded;  
b) outline the additional work required to complete the project, along with the time it will take and the additional cost of completion calculated at the Agency Rate;  
c) provide a revised production schedule and estimated completion date; and  
d) ask you to confirm that you want Redstamp to complete the additional work.

4) **Master Services Agreement.** This Statement of Work is issued under the Services Agreement between Red Stamp Agency Inc. and Progressive Fundraising Inc. dated February 21, 2024.

5) **Validity.** This Statement of Work is valid for 30 days from the date above.

6) **Resourcing.** The resourcing proposed for this project can be guaranteed for two business days from the date this Statement of Work is sent. If Progressive approves the Statement of Work after that period, Redstamp will confirm the next available start date.

7) **Feedback and Approvals.** Progressive will provide consolidated feedback and approvals through the agreed project contact. Unless otherwise agreed, Progressive will provide feedback within two business days of receiving a review request.

8) **Project Holds.** If required feedback, access, source materials, approvals, or payment are delayed by more than five business days, Redstamp may place the project on hold. Restarting work after a hold may require rescheduling and may be billed at the Agency Rate if additional re-planning or rework is required.

## 08. Approvals

### RED STAMP AGENCY INC.

Per: _______________________________  
Spencer Ririe  
Co-Founder  
*Authorized Signature*  
Date: _______________________________

### PROGRESSIVE FUNDRAISING INC.

Per: _______________________________  
Doug Beers  
President  
*Authorized Signature*  
Date: _______________________________
