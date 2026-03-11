---
title: "Digital Gift Card Fulfillment Technology Landscape — 2025-2026"
type: solution
category: market-research
date: 2026-02-23
status: complete
tags: [digital-fulfillment, gift-card-technology, white-label, security, automation, market-research, competitive-landscape, API, SaaS]
key_insights:
  - The industry has moved to API-driven, inventory-free on-demand fulfillment — Progressive's manual PDF-generation model is a full generation behind
  - Canadian-specific platforms exist (Fundstream in Montreal) that could either be a partner, competitor, or template for what Progressive needs
  - White-label gift card platforms are commercially available SaaS products, not custom-build territory
  - Security best practices center on tokenization, MFA, role-based access, and never storing unencrypted card data at rest
  - Market consolidation strongly favors scale — small operators must either specialize in niche service or adopt platform infrastructure to survive
  - The build-vs-buy decision for Progressive likely tilts toward buy/integrate for fulfillment infrastructure and build for the customer-facing portal layer
related:
  - docs/discovery/2026-01-29-client-discovery-call.md
  - docs/discovery/2026-01-27-internal-pre-meeting.md
participants:
  redstamp:
    - Spencer R. (research lead)
---

# Digital Gift Card Fulfillment Technology Landscape — 2025-2026

Research conducted February 2026 to inform the Progressive Gift Cards engagement. This document covers the current state of digital gift card fulfillment technology, automation approaches, white-label platforms, security best practices, and industry trends relevant to a small Canadian bulk gift card reseller.

---

## 1. How Modern Gift Card Fulfillment Companies Handle Digital Delivery

### The Industry Standard: Self-Service Portals with API-Driven Fulfillment

The modern B2B digital gift card delivery model has moved decisively toward **self-service portals backed by API-driven fulfillment**. The manual process Progressive currently uses — generating PDFs from vendor data, encrypting, and emailing — is at least one technology generation behind the current standard.

**What best-in-class looks like today:**

- **Instant digital delivery** via email, SMS, or direct link — no file attachments, no encryption passwords
- **Self-service portals** where corporate buyers place orders, track status, and access reporting dashboards
- **Recipient choice models** where the buyer sends a reward link and the recipient picks their preferred brand from a catalog (rather than pre-selecting the brand)
- **Real-time tracking** of delivery, claim status, and redemption
- **Inventory-free on-demand fulfillment** — the platform sources cards at order time via API connections to brands, eliminating the need to hold inventory

### Major Platform Players

**Blackhawk Network (BHN) / CashStar**
- CashStar was acquired by BHN for $175M in 2017; its technology now powers BHN's digital gifting solutions
- Powers 400+ retailers' branded gift card programs
- Hawk Marketplace offers RESTful APIs for automated ordering plus bulk upload for large purchases
- Fulfills over $4 billion in rewards annually across 28 countries, issuing more than 1 billion gift cards per year
- Card catalog is configured per client/program — not a one-size-fits-all catalog
- Zero-fee model for partners who earn on each end-user purchase/claim
- Progressive already uses CashStar for Tim Hortons cards — this is their entry point into the broader BHN ecosystem

**Tremendous**
- Global B2B rewards and incentives platform
- ~2,000 brand catalog
- RESTful API for integration into existing workflows
- 4.6/5 rating on G2
- Focused on digital-only delivery

**Tango (now a division of Blackhawk Network)**
- Four product tiers: Reward Link (instant email delivery), Rewards Genius (self-serve dashboard), RaaS API (for embedding in apps/platforms), and integrations (Salesforce, Qualtrics, Zapier)
- ~3,100 brand catalog
- 4.5/5 rating on G2
- The Tango-BHN merger is a clear sign of industry consolidation

**Giftbit**
- RESTful API with 1,000+ global brand catalog
- Key differentiator: transparent breakage reclamation (unclaimed rewards revert to account)
- Real-time lifecycle tracking showing when rewards are claimed
- Zapier integration for no-code automation
- SOC 2 compliant
- Free signup with no minimums — low barrier to test
- Claims to save companies "up to 10 hours weekly" over manual processes
- Supports bulk sending via CSV upload

**Giftogram**
- 140,000+ brand catalog (largest in the space)
- Both digital and physical delivery (unusual — most platforms are digital-only)
- 4.8/5 on G2, rated #1 for Rewards & Incentives in 2025

**Fundstream (Montreal, Canada)**
- Canadian-headquartered, operating since 2003
- 40+ major Canadian retailer catalog including Canadian Tire, Walmart, Starbucks, WestJet, Sobeys
- Launched V3 of their fulfillment platform in May 2025
- Full API with order submission, real-time status tracking, bilingual asset database, address validation, and callback notifications
- SOC 2 Type 2 compliant
- Handles both digital and physical fulfillment
- White-label branding options
- **Highly relevant to Progressive** — this is a Canadian company doing exactly what Progressive does but with modern infrastructure. Could be a partner, a template, or a competitive threat.

### Implications for Progressive

Progressive's current model (Lloyd running scripts, generating PDFs, encrypting, emailing) maps to roughly 2010-era fulfillment practices. The industry has moved to:
1. API connections to brands for real-time card issuance
2. Web portals for customer self-service retrieval
3. Automated tracking and reporting
4. No local inventory management — on-demand sourcing

The gap is significant but also represents an opportunity: upgrading to modern practices would dramatically reduce operational burden and unlock the scalability Lloyd flagged as a concern.

---

## 2. Automation in Card Generation and Fulfillment

### The Core Question: Custom-Built vs. Off-the-Shelf

Progressive's current automation is entirely custom-built (Lloyd's scripts). The question is whether to continue down a custom path or adopt existing platforms.

### Off-the-Shelf Platforms

Several platforms exist specifically for automating gift card fulfillment:

**API-First Platforms (connect to brand APIs):**
- Giftbit, Tremendous, Tango/BHN, and Fundstream all provide APIs that handle the brand connection, card issuance, and delivery in one integration
- These platforms maintain their own relationships with brands and handle the card sourcing
- The operator focuses on the customer relationship, not the card generation mechanics

**Gift Card Management Software:**
- **Givex (Shift4)** — comprehensive programs covering transaction processing, card production, and fulfillment management
- **PassKit** — digital gift card management with Zapier and Make integrations, connecting to 8,000+ apps
- **SmartGifty** — digital gift card management system with PIN support
- **Enjovia** — create, fulfill, track, and redeem vouchers from one platform, with API support

### The Progressive-Specific Problem

Progressive's situation is unusual because they are a **reseller receiving raw card data from vendors** (card numbers + PINs) and generating the customer-facing deliverable themselves. This is different from most platform scenarios where the platform connects directly to the brand's API for real-time issuance.

Progressive's vendor types create three distinct fulfillment patterns:

| Pattern | Vendors | Current Process | Automation Path |
|---------|---------|-----------------|-----------------|
| **Pass-through URLs** | Best Buy, Starbucks | Forward URLs to customers | Trivial — just deliver the URL |
| **Generate from raw data** | Walmart, Amazon, Chapters, some Loblaws | Lloyd's scripts create PDFs from card numbers + PINs | Custom tooling needed OR shift to vendor APIs |
| **Integrated APIs** | Tim Hortons (CashStar), Amazon & Walmart (in progress) | API-based issuance | Already on the modern path |

**For the "generate from raw data" pattern, there is no off-the-shelf solution** that takes vendor-provided card numbers and PINs and generates branded deliverables. This is inherently custom work because each vendor provides data in different formats. However, Lloyd's scripts could be replaced with:

1. A lightweight web-based tool that any trained staff member could operate
2. Standardized data intake (CSV templates per vendor)
3. Automated PDF or URL generation
4. Direct upload to a customer portal

**For vendors with API integration paths** (Amazon, Walmart — noted as "in progress"), the long-term play is to eliminate the raw-data-generation step entirely and connect directly to vendor APIs for on-demand card issuance.

### Build vs. Buy Recommendation

| Aspect | Build Custom | Buy Platform |
|--------|-------------|--------------|
| **Timeline** | Months | Days to weeks |
| **Cost** | Higher upfront, lower ongoing | Lower upfront, ongoing subscription |
| **Customization** | Unlimited | Limited to platform capabilities |
| **Maintenance** | Progressive/Red Stamp owns it | Platform vendor handles updates |
| **Vendor coverage** | Only what you build | Platform's existing catalog |
| **Fit for Progressive's model** | Better for raw-data generation | Better for API-connected vendors |

**Likely answer: Hybrid approach.** Use a platform (potentially Fundstream, given the Canadian focus and existing retailer relationships) for vendors that support API-based issuance, while building a lightweight internal tool to replace Lloyd's scripts for the raw-data generation vendors. Over time, as more vendors offer direct API integration, the custom tool shrinks in scope.

---

## 3. White-Label Gift Card Platforms

### Market Overview

The white-label gift card platform market is active with multiple SaaS options available. This is not a space where Progressive would need to build from scratch.

### Key White-Label Platforms

**eGifter — White Label Gift Card Storefront**
- Turnkey, white-labeled storefront for digital and physical gift cards
- "Launch in days, not months" positioning
- Built-in card-not-present fraud indemnification
- Quick Start program requiring zero integration
- Also offers a B2B Sales Portal for corporate self-service bulk ordering
- Features: online registration, multiple payment methods, custom workflows, discount management, permissions, reporting

**eGiftify**
- 100% white-label platform (customer sees only the operator's branding)
- Covers digital, physical, and B2B/bulk gift cards
- Omnichannel management (eCommerce purchases redeemable in-store at POS)
- PCI-DSS compliant, encrypted transactions, GDPR compliant
- Integrates with major POS systems including Toast
- Marketing suite with automated birthday sends, BOGO promotions, SMS/email campaigns
- Positioning: "no expensive hardware or integrations required"

**BuyBox**
- SaaS solution for websites and gift card sales interfaces
- Full white-label with graphic customization
- Separate B2C and B2B modules

**Fundstream (again — notable for Progressive)**
- White-label branding options in their V3 platform
- Already Canadian, already covers Progressive's vendor mix
- Could potentially serve as the infrastructure for Progressive's white-label ambitions

**Global POS**
- Omnichannel SaaS gift card solution
- Dedicated back office for separate B2C and B2B management
- Partnerships with major industry resellers

### Implications for Progressive's White-Label Plans

Progressive's three-tier white-label vision (direct link, single-brand portal, fully branded white-label) maps well to existing SaaS offerings:

| Progressive Tier | Platform Equivalent | Complexity |
|-----------------|---------------------|------------|
| **Tier 1:** Direct link to Progressive site | Simple referral link — no platform needed | Low |
| **Tier 2:** Single-brand portal | eGifter Storefront or eGiftify with brand filtering | Medium |
| **Tier 3:** Fully branded white-label | eGiftify or Fundstream white-label | Medium-High |

**Key insight: Progressive should not build Tier 2 or Tier 3 white-label infrastructure from scratch.** The SaaS platforms listed above already solve this problem. The decision should be which platform to adopt, not whether to build custom. This directly addresses the concern from the discovery call about "creating technical debt that blocks white-label later" — adopting a platform that supports white-labeling from day one avoids this entirely.

**However, there is a tension:** These platforms assume the operator is either a brand issuing their own cards OR a rewards platform connecting to brand APIs. Progressive's hybrid model (reselling cards where they sometimes receive raw data and generate deliverables) may not map cleanly onto any single platform. This needs to be validated through direct conversations with platform vendors.

---

## 4. Security Considerations for Gift Card Portals

### Core Principle: Gift Card Numbers Are Cash

Tim flagged this in the discovery call and it is the single most important security consideration. An unsold gift card number sitting in a database or spreadsheet is equivalent to cash. If compromised, the loss is immediate and unrecoverable.

### Authentication Requirements

**Multi-Factor Authentication (MFA) — Now Mandatory Under PCI DSS 4.0**
- As of March 2025, MFA is required for all access to Cardholder Data Environments (not just admin accounts)
- 12-character minimum passwords with complexity requirements
- Lloyd was right to flag two-factor authentication as important for portal access

**Recommended authentication stack for Progressive's portal:**
1. Email/password login with enforced complexity
2. MFA via authenticator app or SMS (authenticator preferred)
3. Session timeout after inactivity
4. IP-based anomaly detection (flag logins from unexpected locations)
5. Rate limiting on login attempts

### Card Data Security

**Encryption at Rest**
- AES encryption for all stored gift card data
- Card numbers and PINs should never be stored in plaintext — not in databases, not in spreadsheets, not in email

**Tokenization**
- Replace actual card numbers with random tokens in the primary database
- Original card data stored in a separate secure token vault
- Even if the main database is breached, card data is useless without the vault
- PCI DSS-compliant token vault providers handle this infrastructure

**Display Security**
- Card numbers should be masked by default (show only last 4 digits)
- Full card number revealed only on explicit user action ("click to reveal")
- Time-limited display — full number visible for a fixed window (30-60 seconds), then re-masked
- One-time view option for high-security requirements
- No card data in URLs, browser history, or local storage
- Disable copy-paste restrictions are counterproductive (users will screenshot instead) — better to track access via audit logs

**Transmission Security**
- TLS 1.2+ for all connections
- Secure File Transfer Protocol (SFTP) for any bulk data exchange with vendors
- No card data transmitted via email (this is what Progressive's portal would eliminate)

### Fraud Prevention

**Velocity Controls**
- Cap gift card reveals per user/device/IP per hour and day
- Limit maximum denomination viewable per session
- Flag and hold high-value bulk reveals for manual review

**Activation Delays**
- For elevated-risk orders, delay card activation for 30-120 minutes while screening completes
- This creates a buffer to detect fraud before cards become active

**Audit Logging**
- Log every card number access: who, when, from where, which card
- Role-based access controls — not every staff member should see full card numbers
- Segregation of duties — the person uploading cards should not be the same person approving orders

### Regulatory Considerations (Canada)

- Gift card regulations in Canada continue to evolve at the provincial level
- PCMLTFA (Proceeds of Crime/Money Laundering) amendments expanding reporting entity definitions — unclear whether gift card resellers fall directly under FINTRAC reporting requirements, but worth validating
- New AML regulations being implemented in 2025-2026 with enhanced KYC requirements
- Provincial consumer protection rules vary (e.g., BC has specific gift card regulations)
- Progressive should consult with a compliance advisor on whether their specific operations trigger reporting obligations

### Practical Security Architecture for Progressive

```
[Customer] --HTTPS--> [Portal Frontend]
                          |
                    [Auth Layer: MFA]
                          |
                    [Application Server]
                          |
              +-----------+-----------+
              |                       |
    [Token Vault]           [Card Data Vault]
    (tokens only)           (encrypted, separate)
              |                       |
              +-------[Audit Log]-----+
```

**Key principle:** The web application never holds unencrypted card data in memory longer than necessary to display it. Card data is fetched from the vault on demand, displayed briefly, and discarded. All access is logged.

---

## 5. Industry Trends

### Consolidation Is Accelerating

The gift card industry is undergoing significant consolidation:

- **Blackhawk Network acquired CashStar** ($175M, 2017) — establishing dominance in first-party digital gift cards
- **Tango is now a division of Blackhawk Network** — further consolidation of the incentives/rewards space
- **InComm** remains a major competitor but faces pressure from the BHN conglomerate
- Regulatory compliance costs (fraud prevention, multi-state/multi-province reporting) favor scale
- The trend is toward "fewer niche cards and more consolidated balances tied to logged-in identities"

**What this means for Progressive:** The large platforms are getting larger. Small operators face increasing pressure to either specialize in service quality and niche relationships or adopt platform infrastructure that gives them enterprise-grade capabilities without enterprise-grade costs.

### Key Market Numbers

- Global gift card market projected at **$825.3 billion in 2026**
- US gift card market growing at **7% CAGR through 2029**, reaching $320+ billion by 2030
- Asia-Pacific market achieving 7.7% CAGR through 2030
- The B2B corporate rewards and incentive segment alone is valued at **$58 billion** in the US

### Four Technology Trends Shaping 2026 (via Fundstream)

1. **Digital, Mobile, and Physical Integration** — Gift cards synchronizing across loyalty programs, mobile wallets, eCommerce platforms, and POS systems. A single card transitions seamlessly between physical gifting, online redemption, and mobile wallet use.

2. **Data-Driven Personalization** — Using redemption trend data and customer preference analytics to optimize the entire gift card experience from issuance through redemption.

3. **API-Driven, Inventory-Free Fulfillment** — Real-time delivery, tracking, and reporting replacing manual processes. On-demand sourcing eliminating the need to hold inventory. This is the single most transformative trend for Progressive's operations.

4. **Aggregator and Brand Matchmaking** — Platforms expanding into use cases beyond traditional gifting: customer appeasement, employee retention, revenue generation. Better algorithms connecting distribution channels with brands.

### Emerging Patterns for Small Operators

**Platform adoption over custom building.** The era of custom scripts for card generation is ending. Even small operators are expected to adopt platform infrastructure — either as users of platforms like Fundstream/Giftbit or by building on top of APIs from BHN/InComm.

**Service differentiation over technology differentiation.** When everyone has access to the same platform infrastructure, competitive advantage shifts to relationships, speed of service, account management, and niche specialization (e.g., Canadian corporate gifting).

**Security as table stakes.** MFA, encryption at rest, tokenization, and audit logging are no longer enterprise-only requirements. PCI DSS 4.0 has made them mandatory for anyone handling card data. Small operators who cannot meet these standards face existential regulatory risk.

**URL-based delivery replacing PDF/email.** Doug's instinct to standardize on URL delivery is aligned with industry direction. PDFs-as-attachments are a legacy pattern. The modern approach is a secure URL that renders the card in-browser with time-limited display.

---

## Synthesis: What This Means for Progressive

### Progressive's Competitive Position

Progressive is a small Canadian operator in a market that increasingly favors scale. Their strengths are:
- Established relationships with major Canadian retailers
- Existing physical card fulfillment infrastructure
- Personal service to corporate clients
- Doug's willingness to invest in modernization

Their vulnerabilities are:
- Digital fulfillment entirely dependent on one contractor's custom scripts
- No API connections to vendors (except Tim Hortons via CashStar)
- No self-service portal for customers
- Security practices that pre-date PCI DSS 4.0 requirements
- Manual inventory management in spreadsheets

### Strategic Options

**Option 1: Platform Partnership**
Partner with an existing platform like Fundstream (Canadian, covers Progressive's vendor mix, has white-label capabilities). Progressive becomes a service/sales layer on top of Fundstream's infrastructure. This is the fastest path to modern capabilities but introduces dependency on a platform vendor and may compress margins.

**Option 2: Platform-Augmented Custom Build**
Use Red Stamp to build a customer portal and internal tooling, but integrate with platform APIs (Giftbit, BHN/Hawk Marketplace) for the vendor connections. Progressive maintains control of the customer experience while outsourcing the card sourcing and fulfillment infrastructure. This is the hybrid approach — more work than Option 1 but more control.

**Option 3: Full Custom Build**
Replace Lloyd's scripts with a complete custom fulfillment system including portal, internal tooling, vendor integrations, and white-label capabilities. Most expensive and slowest but gives Progressive full ownership. This only makes sense if Progressive's specific vendor relationships and processes cannot be served by existing platforms — which should be validated before committing to this path.

### Recommended Next Steps

1. **Validate platform fit.** Before designing a custom solution, have a discovery conversation with Fundstream and/or Giftbit to understand whether their platforms can accommodate Progressive's vendor mix and reseller model. This is the single highest-leverage research activity.

2. **Map vendor integration paths.** For each of Progressive's vendors, determine: (a) does the vendor offer a direct API for card issuance? (b) is the vendor available in any existing platform's catalog? (c) if neither, what is the vendor's data format and what custom tooling is needed?

3. **Prioritize security.** Regardless of platform choice, any solution that stores or displays gift card numbers must implement encryption at rest, tokenization, MFA, and audit logging. This is non-negotiable under PCI DSS 4.0.

4. **Phase the approach.** Phase 1 (customer portal for card retrieval) can proceed independently of the platform decision. Phase 2 (white-label) and Phase 3 (operational automation) should be informed by the platform validation.

---

## Sources

### Industry Platforms and Companies
- [Giftbit — Bulk Digital Gift Card Fulfillment](https://www.giftbit.com/blog/bulk-digital-gift-card-fulfillment-service)
- [Giftbit — Gift Card API](https://www.giftbit.com/gift-card-api)
- [eGifter — White Label Gift Card Storefront](https://corporate.egifter.com/gift-card-storefront/)
- [eGifter — B2B Sales Portal](https://corporate.egifter.com/b2b-sales-portal/)
- [eGiftify — White-Label Gift Card & Loyalty Platform](https://www.egiftify.com/)
- [Blackhawk Network — Incentive Resellers](https://blackhawknetwork.com/solutions/reward-incentives/product-overview/incentive-resellers)
- [Blackhawk Network — CashStar FAQ](https://blackhawknetwork.com/lets-talk/faq/cashstar)
- [Tango — Gift Card API & Rewards](https://www.tangocard.com/)
- [Tremendous — Gift Card & Rewards Platform](https://www.tremendous.com/)
- [Fundstream — Gift Card Fulfillment](https://www.fundstream.com/our-services/gift-card-fulfillment)
- [Fundstream — V3 Platform Launch](https://www.newswire.ca/news-releases/fundstream-launches-third-version-of-its-gift-card-fulfillment-service-863307139.html)
- [Fundstream — 4 Gift Card Technology Trends for 2026](https://www.fundstream.com/newsroom/future-gift-card-technology-4-trends-watch-2026)
- [GiftCard Partners — Program Management](https://www.giftcardpartners.com/gift-card-program-management-services)
- [Giftogram — Bulk Gift Cards at Scale](https://giftogram.com/blog/easily-send-digital-gift-cards-in-bulk-at-scale)
- [InComm — Bulk Gift Cards for Corporate Incentives](https://solutions.incommincentives.com/bulk-gift-cards-for-corporate-incentives-and-rewards/)

### Security and Compliance
- [Paytronix — Gift Card Security](https://www.paytronix.com/blog/gift-card-security)
- [Fosteron Tech — Gift Card Data Security Best Practices](https://fosterontech.com/gift-card-data-security-best-practices-for-retailers/)
- [Blackhawk Network — Gift Card Fraud Prevention](https://blackhawknetwork.com/resources/blog/gift-card-fraud-prevention-how-to-protect-your-gift-cards)
- [Incentivio — Restaurant Gift Card Security](https://www.incentivio.com/blog-news-restaurant-industry/advanced-security-measures-for-protecting-your-restaurants-gift-card-program)
- [PCI Security Standards Council](https://www.pcisecuritystandards.org/)
- [ClearlyPayments — PCI DSS 4.0 in 2025](https://www.clearlypayments.com/blog/pci-dss-4-0-facts-and-compliance-insights-in-2025/)
- [OWASP — Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

### Market Research and Trends
- [US Gift Card Market Report 2026 — GlobeNewsWire](https://www.globenewswire.com/news-release/2026/02/19/3240973/28124/en/United-States-Gift-Card-Business-and-Investment-Report-2026-A-320-Billion-Market-by-2030-Featuring-Walmart-Amazon-Costco-Home-Depot-Target-Apple-CVS-Sycamore-Partners-Kroger-Publix.html)
- [Asia-Pacific Gift Card Report 2026 — GlobeNewsWire](https://www.globenewswire.com/news-release/2026/02/20/3241878/28124/en/Asia-Pacific-Gift-Card-Business-Report-2026-A-371-Billion-Market-by-2030-Competitive-Advantage-Will-Move-from-More-Brands-to-Risk-Controls-Instant-Fulfillment-and-Enterprise-grade-.html)
- [Persistence Market Research — Gift Card Market Outlook 2033](https://www.persistencemarketresearch.com/market-research/gift-card-market.asp)
- [Motus CC — Gift Card Merchant Trends 2025](https://motuscc.com/payment-card-industry-news/gift-card-merchants-trends-should-watch-in-2025/)
- [BuyBox — How to Choose the Right Gift Card Solution](https://www.buybox.net/en/blog/choose-right-gift-card-solution)

### Canadian Regulatory
- [ClearlyPayments — Payment Compliance Canada 2025](https://www.clearlypayments.com/blog/payment-compliance-what-canada-merchants-need-to-know-in-2025/)
- [Cardivo — Gift Card Laws by Country](https://cardivo.com/gift-card-laws)
- [Lexology — Gift Card Regulation in Canada](https://www.lexology.com/library/detail.aspx?g=1c5df1a1-ba40-47ea-93e2-32ead194d0ae)
