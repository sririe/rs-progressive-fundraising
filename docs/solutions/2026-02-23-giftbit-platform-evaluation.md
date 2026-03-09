---
title: "Giftbit Platform Evaluation for Progressive Gift Cards"
type: solution
category: vendor-evaluation
date: 2026-02-23
status: complete
tags: [giftbit, vendor-evaluation, digital-fulfillment, API, gift-card-platform, Canadian, reseller, white-label, pricing, security]
key_insights:
  - Giftbit is a B2B digital rewards distribution platform, not a direct-to-consumer gift card company — it is designed for companies like Progressive to use as infrastructure
  - The platform explicitly supports white-label/partner arrangements with API-driven branded delivery and revenue sharing
  - Canadian brand coverage is strong but has notable gaps — Walmart, Loblaws/Shoppers Drug Mart, and Save-on-Foods are NOT confirmed in the catalog
  - Pricing is face-value with no subscription fees — Giftbit makes money on brand spreads (negotiated discounts from brands) and breakage on promotional rewards
  - SOC 2 compliant since November 2023, but no confirmed PCI DSS certification
  - The platform is designed for the use case where the platform sources cards on-demand via API — it does NOT support Progressive's current model of receiving raw card data from vendors and generating deliverables
  - Small company (24 employees, $4.45M funding, Victoria BC) — not a startup risk but not enterprise-scale either
key_decisions: []
related:
  - docs/solutions/2026-02-23-gift-card-fulfillment-technology-landscape.md
  - docs/discovery/2025-01-29-client-discovery-call.md
participants:
  redstamp:
    - Spencer R. (research lead)
blockers:
  - Need to confirm exact Canadian brand catalog by creating a free account or contacting Giftbit sales
  - Need to validate whether Giftbit's model is compatible with Progressive's existing vendor relationships (where Progressive buys cards at wholesale and resells)
  - Need to understand if Progressive would be buying cards at face value through Giftbit or if reseller/wholesale pricing is available
---

# Giftbit Platform Evaluation for Progressive Gift Cards

Deep-dive evaluation of Giftbit (giftbit.com) as potential fulfillment infrastructure for Progressive Gift Cards. Research conducted February 2026.

---

## 1. Business Model

### What Giftbit Is

Giftbit is a **B2B digital rewards distribution platform** headquartered in Victoria, BC, Canada. Founded in 2011 by Leif Baradoy and Peter Locke, the company provides a web application and API that enables businesses to buy, send, and track digital gift cards and prepaid cards globally.

**Company profile:**
- Headquarters: 2031 Store Street, Victoria, BC V8T 5L9, Canada
- Founded: 2011
- Employees: ~24
- Total funding: $4.45M (21 investors including Acequia Capital, Conconi Growth Partners, Freestyle Capital)
- CEO: Leif Baradoy (co-founder, still leading)
- Notable clients: Netflix, Red Bull, Shopify, Gusto
- Customer satisfaction: 95.7% CSAT; 99% CSAT for customer success team in 2024
- Review ratings: 4.6/5 on G2 (82 reviews), 4.6/5 on Capterra

### How It Works

Giftbit is an **intermediary between brands and businesses**. They maintain relationships with gift card issuers (brands), negotiate bulk purchasing discounts, and provide a platform for businesses to order and distribute those cards to recipients. The flow is:

```
Brand (e.g., Tim Hortons) --> Giftbit (platform/API) --> Business (e.g., Progressive) --> Recipient
```

When a business sends a reward through Giftbit:
1. The business funds their Giftbit account (via wire transfer, EFT, or credit card)
2. They create a reward (single or bulk) specifying brand, amount, and delivery method
3. Giftbit sources the card from the brand in real-time (no pre-purchased inventory needed)
4. The recipient receives the card via email, SMS, direct link, or embedded in an app
5. Giftbit tracks whether the reward is claimed, unclaimed, or expired

### Is It a SaaS Platform or a Gift Card Company?

It is a **SaaS platform** — specifically, a rewards distribution platform. Giftbit does not issue gift cards itself. It aggregates access to 1,000+ brands and provides the ordering, delivery, and tracking infrastructure. Think of it as a "gift card marketplace with an API" rather than a gift card issuer.

### Can a Reseller Like Progressive Use It?

**Yes, but with a critical caveat.** Giftbit is designed for companies that want to **send gift cards as rewards, incentives, or gifts to end recipients**. It explicitly supports partner/reseller arrangements through its partnerships program. However:

**The fundamental model difference:** Giftbit assumes the platform operator buys cards through Giftbit at the time of distribution. Progressive's current model involves buying cards directly from vendors at wholesale prices, receiving raw card data, and generating deliverables themselves. These are different supply chains.

If Progressive were to use Giftbit, they would be **replacing their vendor relationships with Giftbit's vendor relationships** for the brands in Giftbit's catalog. This could be advantageous (automation, no manual generation) or disadvantageous (loss of direct wholesale pricing, margin compression) depending on the economics.

---

## 2. Reseller/Partner Capabilities

### Partnership Program

Giftbit explicitly offers a [partnership program](https://www.giftbit.com/partnerships) for companies that want to embed rewards into their own products or services. The program includes:

- **White-label API integration**: Fully customize and integrate a digital rewards function in your own environment
- **Branded delivery**: Landing pages include your logo and custom messaging
- **Revenue sharing**: Custom financial arrangements where partners earn on reward volume
- **Volume discounts**: Pricing improves with scale
- **No integration costs**: Free to integrate and access all products and services
- **No minimums or exclusivity contracts**: Low-commitment entry

### White-Label Capabilities

Giftbit supports several levels of branding control:

| Delivery Method | Branding Level | Use Case |
|----------------|---------------|----------|
| **Email delivery** | Custom email templates with your branding | Standard reward distribution |
| **Shortlink** | Branded landing page with your logo and messaging | Share via any channel (Slack, SMS, etc.) |
| **Direct link** | Minimal Giftbit branding | Quick distribution |
| **Embedded** | In-app reward URLs, fully integrated | Custom portal or app |
| **API-driven** | Complete control — you build the UI | Maximum customization |

For Progressive's white-label ambitions (Tier 2/3 portals for Save-on-Foods, Sequoia Group, White Spot), the **API-driven approach** would give Progressive full control over the customer experience while using Giftbit for backend card sourcing and delivery.

### Fit for Progressive's Reseller Model

**What works:**
- Progressive could maintain its own customer relationships and branding
- The API allows Progressive to build its own portal/ordering experience
- Revenue sharing and volume discounts could offset the loss of direct wholesale pricing
- Breakage recapture (getting back value on unclaimed promotional rewards) adds a revenue stream Progressive does not currently have

**What does not work (or needs validation):**
- Progressive currently buys cards at wholesale directly from vendors. Giftbit would insert itself as an intermediary, potentially compressing Progressive's margin
- For vendors where Progressive receives raw card data (Walmart, Amazon, Chapters, Loblaws), Giftbit's model is fundamentally different — Giftbit sources cards on-demand rather than accepting pre-purchased inventory
- Progressive's physical card business is not served by Giftbit (digital only, except for physical prepaid Visa)
- The "faux commerce" model (order on site, pay via BenjaPay) does not map to Giftbit's "fund account, then distribute" model

---

## 3. Canadian Brand Coverage

### Confirmed Canadian Brands in Giftbit's Catalog

Based on blog posts and catalog pages, the following Canadian brands are confirmed available:

**Food & Beverage:**
- Tim Hortons ($5-$100 denominations)
- Harvey's
- Swiss Chalet
- Montana's BBQ & Bar
- Earls
- Davids Tea

**Grocery:**
- Sobeys
- Foodland
- FreshCo
- Thrifty Foods
- Safeway
- IGA

**Retail:**
- Indigo (this covers Chapters)
- Best Buy
- HomeSense
- Home Hardware
- Lush
- Ardene
- Penningtons
- Kent

**Gas & Travel:**
- Petro-Canada
- Esso and Mobil
- Air Canada (up to $2,500 — notable for executive rewards)

**Digital/Global (available in Canada):**
- Amazon.ca
- Starbucks

**Prepaid Cards:**
- Visa (prepaid, digital and physical)
- Mastercard (prepaid)

### Progressive's Target Brands — Coverage Assessment

| Brand | In Giftbit Catalog? | Notes |
|-------|---------------------|-------|
| **Walmart Canada** | UNCONFIRMED | Mentioned in one blog post as a grocery option alongside Instacart/DoorDash, but NOT listed in Canadian catalog posts. Requires verification. |
| **Amazon Canada** | YES | Amazon.ca confirmed available |
| **Loblaws/Shoppers Drug Mart** | NOT FOUND | No mention in any catalog listing or blog post. Major gap. |
| **Tim Hortons** | YES | Featured brand, $5-$100 |
| **Best Buy** | YES | Confirmed in Canadian catalog |
| **Starbucks** | YES | Available globally |
| **Chapters/Indigo** | YES | Listed as "Indigo" |
| **Save-on-Foods** | NOT FOUND | No mention anywhere. Significant gap for Progressive's white-label plans. |
| **White Spot** | NOT FOUND | No mention. Not surprising — smaller regional chain. |
| **Sobeys** | YES | Confirmed, plus sub-brands (Foodland, FreshCo, Safeway, IGA, Thrifty Foods) |

### Coverage Gaps

The gaps are significant for Progressive's specific needs:

1. **Loblaws/Shoppers Drug Mart** — This is a major Canadian retailer and one of Progressive's key vendors for manual card generation. Its absence from Giftbit's catalog means Progressive could not use Giftbit to replace Lloyd's Loblaws card generation workflow.

2. **Walmart Canada** — Ambiguous. May be available (mentioned in one context) but not prominently listed. Needs verification.

3. **Save-on-Foods** — Absence is directly relevant to Progressive's white-label plans (Save-on-Foods is one of the three target white-label clients).

4. **White Spot** — Another target white-label client. Not available.

**Important caveat:** Giftbit states they "constantly refresh the catalog" and new brands are added regularly. The catalog as researched online may not reflect the current live catalog. A free account signup or sales conversation would provide definitive answers.

---

## 4. API Capabilities

### Overview

Giftbit provides a RESTful JSON API with comprehensive documentation available at [giftbit.com/api-documentation](https://www.giftbit.com/api-documentation). The API is ungated — developers can access docs and a sandbox environment without prior registration.

### Core Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/ping` | GET | Validate authentication and API availability |
| `/brands` | GET | Retrieve available brands with filtering (price, currency, region, search) |
| `/brands/{brand_code}` | GET | Brand detail including pricing and availability |
| `/regions` | GET | List geographical regions |
| `/campaign` | POST | Create rewards (email delivery or shortlink) |
| `/campaign/{id}` | GET | Retrieve order status and details |
| `/direct_links` | POST | Create direct link rewards (immediate URL in response) |
| `/embedded` | POST | Create embedded reward URLs for in-app delivery |
| `/gifts` | GET | List rewards with filtering (status, delivery, recipient, price, date) |
| `/gifts/{uuid}` | GET | Individual reward details |
| `/gifts/{uuid}` | PUT | Resend unclaimed rewards |
| `/gifts/{uuid}` | DELETE | Cancel unclaimed rewards |
| `/links/{id}` | GET | Retrieve shortlink/direct link URLs |
| `/funds` | GET | View account balance (USD, CAD) |
| `/funds` | POST | Add funds via credit card |

### Authentication

Bearer token authentication via HTTP `Authorization` header. API keys generated through the account dashboard. Separate sandbox (Testbed) and production environments available.

**Production access requires manual approval:** Developers must email `sales@giftbit.com` to request production activation, typically granted within 24 hours.

### Key Technical Features

- **Idempotency**: Client-supplied request IDs prevent duplicate reward issuance on retries. If the same ID is submitted twice, only one reward is created.
- **Sandbox environment**: Full testing at `testbedapp.giftbit.com` with demo credits
- **Rate limiting**: Adaptive system allowing bursts; returns 429 with exponential backoff expected
- **Multiple delivery types**: Email, shortlink (with branded landing page), direct link (minimal branding), embedded (in-app)
- **Full catalog option**: Omit brand codes to let recipients choose from all available brands at a given price point
- **Custom metadata**: Attach tracking data to orders
- **Pagination and sorting**: On list endpoints

### What the API Does NOT Have

- **No webhooks or callbacks**: Integration relies on polling for status updates. This is a meaningful limitation for real-time workflow integration.
- **No SDK libraries**: Pure REST API — no official client libraries for Ruby, Python, Node, etc.
- **No batch/bulk endpoint**: Bulk operations are achieved by iterating through individual API calls (or using CSV upload through the web UI). There is no single "send 600 cards" API call.
- **No inventory management**: You cannot upload your own card data (numbers + PINs) to Giftbit. The platform sources cards on-demand.

### Integration Speed

Giftbit claims developers typically integrate in 48 hours or less. The Prime46 case study is cited as achieving full automation in 48 hours of development time.

### Zapier Integration (No-Code)

For non-technical users, Giftbit integrates with Zapier (8,000+ apps). Available triggers include CRM events, payment platform transactions, form submissions, and Slack messages. This could be relevant for Progressive's non-technical team.

### API Fit for Progressive

The API is well-suited for building a customer portal that distributes cards sourced through Giftbit. However, it is **not designed for Progressive's current workflow** of receiving raw card data and generating deliverables. Progressive would need to shift to Giftbit's supply chain model (on-demand sourcing) rather than importing existing inventory.

---

## 5. Pricing

### Core Model: Face Value, No Fees

Giftbit's pricing is remarkably simple on the surface:

- **No subscription fees**
- **No account setup costs**
- **No minimums**
- **No exclusivity contracts**
- **You pay face value for rewards**: A $25 card costs $25

### How Giftbit Actually Makes Money

Giftbit's revenue comes from two streams that are not directly charged to the customer:

1. **Brand spreads**: Giftbit negotiates bulk purchasing discounts with brands. If Giftbit buys a $25 Starbucks card for $23 and sells it for $25, the $2 spread is their revenue. Some of this spread is shared back with high-volume customers as "revenue sharing."

2. **Breakage recapture**: When promotional rewards (those with an expiration date) go unclaimed, Giftbit retains a portion of the unclaimed value. The split is 75% Giftbit / 25% customer. Standard rewards (no expiration) do not generate breakage.

### Additional Fees

| Fee Type | Amount | When It Applies |
|----------|--------|-----------------|
| Credit card funding | 3.5% | When funding account via credit card |
| Currency conversion | 2% | When funding currency differs from reward currency |
| Physical Visa (USD) | $4.95/card | Physical prepaid Visa mailing |
| Physical Mastercard (GBP) | 1 GBP/card | Physical prepaid Mastercard mailing |
| Physical Visa (AUD) | $2 AUD/card | Physical prepaid Visa mailing |
| Wire/EFT funding | Free | Bank transfer funding |

### Volume/Partner Pricing

For high-volume customers and partners, Giftbit offers:
- Volume discounts (specifics not published — contact sales)
- Revenue sharing from brand spreads
- Custom financial arrangements

Giftbit claims "the most transparent pricing in the industry" and invites customers to "ask about spreads, discounts, and revenue sharing."

### Critical Pricing Question for Progressive

**Progressive currently buys cards at wholesale prices directly from vendors.** If Progressive switches to Giftbit, the economics change fundamentally:

- **Current model**: Progressive buys a $25 Walmart card at (hypothetical) $23.50 wholesale, sells for $25.00, earns $1.50 margin.
- **Giftbit model**: Progressive pays $25.00 face value through Giftbit. Margin comes from: (a) whatever markup Progressive charges the corporate client above face value, and (b) any revenue sharing Giftbit offers back.

The question is whether Giftbit's revenue sharing and volume discounts would match or exceed the margins Progressive currently achieves through direct wholesale purchasing. **This is the single most important question to answer in a sales conversation with Giftbit.**

### Breakage Controversy

User reviews flag a significant complaint about breakage handling: when promotional rewards with expiration dates go unclaimed, Giftbit retains 75% of the value (returning only 25% to the customer). Some users describe this as "deceptive." For Progressive's use case (delivering cards that corporate clients have already paid for), this is less relevant because cards would typically be sent as standard rewards (no expiration), not promotional rewards. However, it is worth understanding the distinction clearly before committing.

---

## 6. Security and Compliance

### SOC 2 Compliance

Giftbit achieved SOC 2 compliance as of **November 9, 2023**. Per CEO Leif Baradoy: "We've always been champions of security."

The SOC 2 certification covers:
- Confidentiality
- Availability
- Processing integrity

**Not confirmed:** Whether this is SOC 2 Type 1 (point-in-time) or Type 2 (sustained over a monitoring period). Type 2 is significantly more rigorous. The audit firm is also not disclosed publicly.

### Infrastructure Security

Based on available information:
- Data encryption in transit (HTTPS/TLS)
- Data encrypted at rest
- AWS infrastructure controls
- Secure identifiers (tokenization)
- Access controls and authentication

### PCI DSS Compliance

**Not confirmed.** Giftbit does not publicly claim PCI DSS certification. Given that they handle gift card data (cash-equivalent), this is a notable absence. However, since Giftbit does not process credit card payments directly (they use payment processors for account funding) and gift cards themselves are not covered under PCI DSS in the same way credit cards are, SOC 2 may be the more relevant certification for their business model.

### What This Means for Progressive

Giftbit's SOC 2 compliance is a positive signal — it means they have been independently audited on security controls. For Progressive's concern about gift card numbers being "like cash":

**If Progressive uses Giftbit's delivery mechanism**, card numbers are generated and delivered through Giftbit's infrastructure, meaning Progressive never needs to handle, store, or encrypt card numbers themselves. This actually eliminates Tim's concern about storing unsold inventory on web infrastructure — the cards exist only in Giftbit's SOC 2-compliant environment until the recipient claims them.

**If Progressive uses the embedded/API approach** to build their own portal, card data still flows through Giftbit's backend. Progressive's portal would display a Giftbit-generated link or embed, not raw card numbers.

---

## 7. Bulk/Corporate Features

### Bulk Sending Capabilities

Giftbit supports bulk operations through multiple channels:

**Web UI (CSV Upload):**
- Upload a CSV with recipient names and emails
- Send to multiple recipients in a single operation
- Customize the email template, brand selection, and amounts
- Schedule delivery for a future date/time

**API (Programmatic):**
- Create rewards individually via API calls in a loop
- No dedicated "batch" endpoint — each reward is a separate API call
- Idempotency keys prevent duplicates if operations need retrying
- Rate limiting is adaptive (allows bursts)

**Zapier (No-Code Automation):**
- Trigger bulk sends based on events in other systems
- Connect to CRM, HRIS, or payment platforms

### Can It Handle 600 Cards at Once?

For the specific scenario of a 600-card Loblaws order (the benchmark from the discovery call):

- **Via CSV upload**: Yes, 600 recipients can be uploaded and sent in a single operation
- **Via API**: Yes, but requires 600 individual API calls. With rate limiting, this would still complete in minutes rather than the 3+ hours Lloyd's current scripts take
- **Caveat**: Loblaws is not confirmed in the catalog, so this specific scenario may not be possible through Giftbit regardless

### Corporate Features

| Feature | Available? | Details |
|---------|-----------|---------|
| Bulk CSV upload | Yes | Upload contacts and send in one operation |
| Scheduled delivery | Yes | Set future delivery dates |
| Recipient choice (pick-a-card) | Yes | Recipients choose from catalog or curated list |
| Custom email templates | Yes | Branded emails with your messaging |
| Team accounts | Yes | Multiple administrators per account |
| Spending limits/controls | Yes | Budget caps and approval workflows |
| Real-time tracking | Yes | Claimed vs. unclaimed status |
| Delivery issue detection | Yes | Bounced emails, spam filter alerts |
| Reporting/analytics | Yes | CSV exports, lifecycle data |
| Physical card mailing | Limited | Prepaid Visa only, not branded retailer cards |
| Custom denomination | Yes | Set any amount within brand's range |
| Multi-currency (CAD/USD) | Yes | Fund in CAD, send in CAD |
| French language support | Partial | Depends on brand's assets |
| Order history/audit trail | Yes | Full order and redemption history |

### What Is Missing for Progressive's Corporate Use Case

1. **No "order on behalf of" workflow**: Giftbit assumes the account holder is sending rewards directly to end recipients. Progressive's model involves a corporate client ordering cards, Progressive fulfilling them, and the corporate client distributing to their own employees/recipients. Giftbit does not have a "client account" or "sub-account" structure for this.

2. **No invoice/PO workflow**: Progressive's corporate clients likely expect invoicing and purchase orders. Giftbit requires pre-funding the account. Progressive would need to manage the financial layer themselves.

3. **No physical branded cards**: Only digital delivery (plus physical prepaid Visa). Progressive's physical card business is not served.

4. **No raw data import**: Progressive cannot upload card numbers and PINs they have already purchased from vendors. Giftbit only distributes cards it sources through its own brand relationships.

---

## Synthesis: Giftbit as Fulfillment Infrastructure for Progressive

### What Giftbit Solves

1. **Eliminates manual card generation** for brands in Giftbit's catalog — no more Lloyd running scripts
2. **Provides a modern delivery mechanism** — email, links, embeds instead of encrypted PDF attachments
3. **Adds tracking and reporting** that Progressive currently lacks
4. **SOC 2 compliance** offloads security burden from Progressive's infrastructure
5. **Canadian company** with CAD support and a growing Canadian catalog
6. **No upfront cost** — free to test with a sandbox account
7. **API enables custom portal** — Progressive could build their own customer-facing experience

### What Giftbit Does NOT Solve

1. **Does not replace the raw-data generation workflow** — for vendors where Progressive receives card numbers and PINs (the most labor-intensive part of Lloyd's work), Giftbit offers no solution because it cannot ingest externally-sourced card data
2. **Canadian catalog gaps** — Loblaws, Shoppers Drug Mart, Save-on-Foods, and White Spot are not confirmed available. These are core to Progressive's business and white-label plans.
3. **Margin model conflict** — Progressive currently earns margin on the spread between wholesale purchase price and face value. Giftbit charges face value and may or may not offer comparable spreads through revenue sharing. This needs direct negotiation.
4. **No physical cards** — Progressive's physical card business (which is their current bread and butter) is untouched by Giftbit
5. **No batch API** — sending 600 individual API calls is possible but less elegant than a single batch operation
6. **No webhooks** — status updates require polling, which complicates real-time portal integration
7. **Small company risk** — 24 employees, $4.45M in funding. Not at imminent risk, but not a deeply capitalized enterprise vendor either

### Comparison: Giftbit vs. Fundstream

For Progressive's specific needs, it is worth comparing Giftbit against Fundstream (the Montreal-based platform identified in the landscape research):

| Dimension | Giftbit | Fundstream |
|-----------|---------|------------|
| Headquarters | Victoria, BC | Montreal, QC |
| Canadian focus | Canadian company, growing Canadian catalog | Canadian company, deep Canadian catalog (40+ retailers) |
| Walmart Canada | Unconfirmed | Confirmed |
| Loblaws | Not found | Need to verify |
| Physical + digital | Digital only (+ prepaid Visa) | Both physical and digital |
| White-label | API-based, partner program | White-label branding options |
| SOC 2 | Type not specified, achieved Nov 2023 | SOC 2 Type 2 |
| API | Well-documented REST API | Full API with callbacks |
| Pricing model | Face value, no fees, revenue sharing | Not publicly detailed |
| Company maturity | Founded 2011, ~24 employees | Founded 2003, V3 platform launched 2025 |

Fundstream appears to be a stronger fit for Progressive's Canadian-focused, hybrid physical/digital model, but both warrant direct conversations.

### Recommended Next Steps

1. **Create a free Giftbit account** to browse the actual live catalog and verify which of Progressive's target brands are available. This takes minutes and costs nothing.

2. **Request a sales conversation with Giftbit's partnerships team** to understand:
   - What volume discounts and revenue sharing look like for Progressive's expected order volume
   - Whether Loblaws, Walmart Canada, and Save-on-Foods are available or on the roadmap
   - Whether Giftbit can support a "reseller" workflow where Progressive orders on behalf of corporate clients
   - What "partner" pricing actually means in dollar terms

3. **Do the same with Fundstream** for direct comparison.

4. **Map the coverage gap**: For each of Progressive's vendors, document whether the cards are available through Giftbit, Fundstream, or only through direct vendor relationships. This gap analysis will determine whether a platform can fully replace Lloyd's workflow or only partially.

5. **Do not assume Giftbit replaces the raw-data workflow.** For vendors where Progressive receives card numbers and PINs, a separate internal tool is still needed regardless of whether Giftbit is adopted for other vendors.

---

## Sources

### Giftbit Official
- [Giftbit Homepage](https://www.giftbit.com/)
- [Giftbit Pricing](https://www.giftbit.com/pricing)
- [Giftbit Gift Card API](https://www.giftbit.com/gift-card-api)
- [Giftbit Partnerships](https://www.giftbit.com/partnerships)
- [Giftbit API Basics](https://www.giftbit.com/resources/gift-card-api-basics)
- [Giftbit API Documentation (GitHub)](https://github.com/Giftbit/Giftbit-API-Docs/blob/master/apiary.apib)
- [Giftbit Popular Brands Catalog](https://www.giftbit.com/catalog-popular)
- [Giftbit About Us](https://www.giftbit.com/about-us)
- [Giftbit SOC 2 Announcement](https://info.giftbit.com/giftbit-soc-2-compliant)
- [Giftbit Gift Card Integration](https://www.giftbit.com/resources/gift-card-integration)
- [Giftbit Pricing Help Article](https://intercom.help/giftbit/en/articles/5777183-what-does-giftbit-cost)
- [Giftbit Blog: Canadian Brands (Tim Hortons)](https://www.giftbit.com/blog/send-tim-hortons-gift-cards)
- [Giftbit Blog: Gift Card Distribution in Canada](https://www.giftbit.com/blog/gift-card-distribution-canada)
- [Giftbit Blog: Bulk Digital Gift Card Fulfillment](https://www.giftbit.com/blog/bulk-digital-gift-card-fulfillment-service)
- [Giftbit Blog: Gift Card Distributor Pricing](https://www.giftbit.com/blog/gift-card-distributor-pricing)
- [Giftbit Blog: Practical Rewards (Grocery Cards)](https://www.giftbit.com/blog/practical-rewards)

### Press & News
- [Giftbit Makes Global Incentive Programs Easy (Oct 2024 Press Release)](https://www.globenewswire.com/news-release/2024/10/22/2967084/0/en/Giftbit-Makes-Global-Incentive-Programs-Easy-Automated-and-Transparent.html)
- [Rewards Are Working for Businesses Using Giftbit (Oct 2025 Press Release)](https://www.globenewswire.com/news-release/2025/10/21/3170449/0/en/Rewards-Are-Working-for-Businesses-Using-Giftbit.html)

### Reviews & Comparisons
- [Giftbit Reviews on Capterra](https://www.capterra.com/p/173343/Giftbit/reviews/)
- [Giftbit Reviews on G2](https://www.g2.com/products/giftbit/reviews)
- [Giftbit Reviews on GetApp](https://www.getapp.com/customer-management-software/a/giftbit/)
- [PerkUp: Giftbit Review](https://perkupapp.com/post/giftbit-review-everything-you-need-to-know)

### Company Data
- [Giftbit on Tracxn](https://tracxn.com/d/companies/giftbit/__5P--SimCkvblDNs-QKM91bjCiBM29UJxWSarax4Zq10)
- [Giftbit on CBInsights](https://www.cbinsights.com/company/giftbit)
- [Giftbit on PitchBook](https://pitchbook.com/profiles/company/58643-29)

### Industry Context
- [Blackhawk Network Acquires Tango Card (Payments Dive)](https://www.paymentsdive.com/news/blackhawk-network-acquires-tango-card-gift-cards-digital-rewards/706268/)
