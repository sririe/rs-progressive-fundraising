---
title: "RapidCents Payment Processor Diligence"
type: solution
category: vendor-evaluation
date: 2026-08-25
status: complete
tags: [rapidcents, elavon, benji-pays, payment-processing, vendor-evaluation, due-diligence, progressive]
key_insights:
  - RapidCents should not be rejected outright, but Progressive should not sign or cancel Elavon until the quoted savings, underwriting, Benji Pays compatibility, and operating workflow are proven in writing and through a controlled pilot
  - The quoted 2.00% Visa/Mastercard rate could be meaningful against Progressive's previously observed effective rate, but the annual savings estimate is not validated without a side-by-side analysis using Progressive's actual card mix and transaction volume
  - RapidCents' own merchant terms name Elavon as the acquirer, so this appears to be a Canadian service layer using Elavon rails rather than a clean move away from Elavon
  - Benji Pays does not publicly list RapidCents as a supported gateway; compatibility must be confirmed directly by Benji Pays and proven in a sandbox before any cutover
  - The strongest concern is not the marketing presentation but material contract and operating questions, including term length, contradictory cancellation language, reserves, underwriting for gift-card resale, and the complete fee schedule
  - At least one promoted award, the 2025 IDC CIO Award, is independently verifiable; the website testimonials remain weak evidence because they do not identify the customers' companies
key_decisions:
  - Treat RapidCents as a diligence and pilot opportunity, not an approved processor change
  - Keep Elavon live until Benji Pays compatibility, payment, refund, settlement, and reconciliation flows have been proven through at least one complete settlement cycle
  - Keep payment processing outside the Phase 1 card vault boundary
related:
  - projects/gift-cards/docs/plans/2026-03-31-discovery-synthesis.md
  - projects/gift-cards/docs/plans/2026-05-21-phase-1-mvp-boundary.html
participants:
  progressive:
    - Doug B.
  redstamp:
    - Spencer R.
blockers:
  - RapidCents has not supplied a complete signed fee schedule or contract package for review
  - Benji Pays has not independently confirmed the proposed RapidCents integration path, effort, or cost
  - RapidCents underwriting and reserve terms have not been confirmed for Progressive's gift-card-reseller business and actual transaction profile
---

# RapidCents Payment Processor Diligence

## Executive recommendation

Do not reject RapidCents, but do not sign an agreement or change the current Elavon setup yet.
The rate claim is financially important enough to investigate, but Progressive's current payment-link
workflow is working after substantial coordination and cannot be put at risk based on a headline rate
and vendor-managed references.

The correct next step is a gated diligence exercise. RapidCents must prove the full economics and its
ability to support Progressive's merchant category, Benji Pays must independently confirm the exact
integration path, and the complete workflow must pass a parallel pilot while Elavon remains live.

## Doug's inquiry

Doug forwarded the RapidCents proposal on August 22, 2026, and asked Redstamp for a general view and
help coordinating the setup if Progressive proceeds. He was attracted to RapidCents being a smaller
Canadian company and to its claim that it could lower processing costs while continuing to work with
Benji Pays.

RapidCents' salesperson offered:

- Visa and Mastercard at 2.00% plus $0.10, described as including premium and international cards
- American Express at 2.80% plus $0.15
- no monthly administration fee
- projected annual savings greater than $10,655
- a parallel setup while Elavon remains available, followed by a switch in one to two weeks
- no RapidCents setup or integration charge, while noting that Benji Pays might charge separately

Gmail source: thread `1a02bb25c1689fe5`, subject `FW: RapidCents Reference for Due Diligence`.

## What the historical record says

In April 2024, Avery Davidow at Benji Pays reviewed a Progressive Elavon statement. Based on that
statement, Avery calculated an effective Visa/Mastercard rate of approximately 2.384%. He described
the rate as not bad and advised that Progressive should probably remain with Elavon. He also said the
other processors he contacted would not board Progressive because gift-card resale was considered a
higher-risk merchant category.

The current Elavon and Benji Pays setup subsequently required meaningful coordination, including an
extended support call and configuration of the Elavon transaction and tokenization settings. That
history makes the migration risk material even if a new headline rate is lower.

Gmail sources: threads `18f112c1ae8c4dff` and `1912942a593f40fe`.

## Findings

### 1. The savings are plausible but unproven

A true all-in 2.00% Visa/Mastercard rate could be materially lower than the approximately 2.384%
effective rate Avery observed in 2024. However, the $10,655 annual savings claim cannot be validated
without applying both processors' complete fees to Progressive's last 12 months of actual card mix,
transaction sizes, refunds, disputes, international cards, and settlement activity.

RapidCents' public website shows different standard card-not-present pricing. A custom negotiated rate
may supersede that pricing, but the signed fee schedule must say so explicitly and identify every fee.

### 2. This is not necessarily a move away from Elavon

RapidCents' public merchant terms identify Elavon LLC and Elavon Canada as the acquirer. RapidCents
therefore appears to provide a Canadian payment-service layer while continuing to use Elavon
infrastructure. Doug's preference for a Canadian service partner can still be valid, but it should not
be presented as removing Elavon from the processing chain.

### 3. Benji Pays compatibility remains unverified

Benji Pays' public support material lists specific supported gateways and documents direct Elavon
Converge and Elavon EPG connections. RapidCents is not named in the public support list. This does not
prove incompatibility, but a salesperson's statement is not enough. Avery or another authorized Benji
Pays representative should confirm the exact gateway, credentials, token handling, refunds, and setup
effort in writing, followed by a sandbox test.

### 4. The contract deserves more scrutiny than the marketing

RapidCents' public terms include a four-year initial term, reserve and hold rights, and inconsistent
cancellation language: the summary says there is no early termination fee while another section
describes a CAD $500 fee during the initial term. The final agreement must reconcile those terms and
specify settlement timing, reserve exposure, dispute fees, currency-conversion charges, amendment
rights, and which quoted terms override the public agreement.

Underwriting approval must explicitly cover Progressive's gift-card-reseller business, actual annual
volume, and typical high-value transactions. This matters because Avery's prior processor search found
that several providers would not board the business category.

### 5. The public proof is mixed

The 2025 IDC CIO Award promoted by RapidCents is independently verifiable and should not be dismissed
as pay-to-play based on the available evidence. Spencer's skepticism about the testimonials is still
reasonable: the website quotes individuals without identifying their companies, making the examples
difficult to verify or compare with Progressive. Public third-party review volume is thin. Neither
point proves the company is illegitimate; it means the proof is not strong enough to replace direct
diligence.

## Required diligence gate

1. **Written Benji Pays confirmation.** Ask Avery to confirm the supported gateway route, required
   credentials, implementation effort and cost, token handling, refund flow, and whether Progressive's
   current secure payment-link workflow remains intact.
2. **Full contract and fee package.** Obtain the merchant agreement, information summary box, and
   complete fee schedule. Require written confirmation of the quoted rates by card type and every
   other fee, and resolve the term and cancellation contradiction.
3. **Category-specific underwriting.** Require written approval for gift-card resale at Progressive's
   actual annual volume and transaction size, including reserve, hold, settlement, and termination
   terms.
4. **Twelve-month cost comparison.** Reprice Progressive's actual last 12 months under both offers,
   including premium, corporate, international, Amex, per-transaction, dispute, refund, and any
   gateway fees.
5. **Security and regulatory evidence.** Request RapidCents' current PCI DSS Attestation of
   Compliance, SOC 2 report or bridge letter, and Bank of Canada payment service provider registration
   number or status explanation.
6. **Comparable reference.** Speak directly with a named Canadian merchant processing similar annual
   volume, average ticket size, card mix, and a higher-risk product category.
7. **Controlled parallel pilot.** Keep Elavon live. Test a normal high-value payment, premium or
   corporate card, international card, failed payment, refund, settlement, and reconciliation through
   a complete settlement cycle before deciding whether to cut over.

## Recommended ownership

- **Redstamp:** coordinate the diligence checklist and test plan; keep the card vault work separate.
- **Benji Pays/Avery:** confirm compatibility and own the payment-link integration details.
- **RapidCents:** provide underwriting approval, pricing, contract, compliance evidence, and test
  support.
- **Lloyd:** explain existing workflow details where needed, but should not be the primary owner of
  the processor evaluation.

## Recommended reply to Doug

**Subject: Re: RapidCents Reference for Due Diligence**

Hi Doug,

I spent some time digging into RapidCents. My short take: I wouldn't rule them out, but I also wouldn't
sign anything or start changing the Elavon setup yet.

The potential savings are worth testing. When Avery reviewed your Elavon statement in 2024, he calculated
the effective Visa/Mastercard rate at about 2.38%. If RapidCents can truly deliver an all-in 2.00% rate
across your actual mix of cards, that difference could be meaningful.

A few things stood out:

- RapidCents' own terms name Elavon as the underlying acquirer. This may be a Canadian service layer
  on top of Elavon rather than a complete move away.
- Benji Pays doesn't publicly list RapidCents as a supported connection. That doesn't mean it won't
  work, but I would want Avery to confirm the exact setup, cost, and effort.
- Their public agreement calls for a four-year initial term and has conflicting language about
  cancellation fees. We need the full agreement and fee schedule before relying on the savings estimate.
- I also spent some time on their website. The unnamed testimonials and generic customer photos didn't
  carry much weight for me. I had questions about the awards as well, but I was able to independently
  verify the IDC CIO Award. At least that one is legitimate.

None of that means RapidCents is a bad option. It just means I want them to prove the savings and the
setup before you take on the risk of changing something that currently works.

My recommendation is to treat this as a diligence exercise, not a switch. First, have RapidCents price
the last 12 months of actual transactions and confirm in writing that they will underwrite the gift-card
business at your volumes. Then have Avery review the proposed connection. If both check out, we can run
a parallel test while keeping Elavon live.

If that approach makes sense, I can coordinate it and pull Lloyd in only if we need details about the
current workflow. I wouldn't cancel Elavon until a full payment, refund, and reconciliation cycle has
worked end to end.

Best,

Spencer

## Public sources

- [RapidCents merchant terms](https://rapidcents.com/terms-of-services/)
- [RapidCents website](https://rapidcents.com/)
- [Benji Pays: connect Elavon Payment Gateway](https://support.benjipays.com/support/solutions/articles/150000222742-connect-elavon-payment-gateway-epg-to-benji-pays)
- [Benji Pays: connect Elavon Converge](https://support.benjipays.com/support/solutions/articles/150000019656-connect-to-elavon-converge)
- [IDC CIO Awards Canada 2025 winners](https://event.idc.com/wp-content/uploads/2025/11/CIO-Awards-Canada-Winning-Projects-2025.pdf?RefId=HorsaWebinarLP)
- [Bank of Canada retail payments oversight](https://www.bankofcanada.ca/regulatory-oversight/retail-payments/)
- [Bank of Canada payment service provider registry](https://www.bankofcanada.ca/regulatory-oversight/retail-payments/psp-registry/)
