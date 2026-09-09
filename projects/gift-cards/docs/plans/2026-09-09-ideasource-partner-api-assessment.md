# IdeaSource partner API inquiry — assessment (2026-09-09)

> Session artifact, AUR2 Prime seat. Source inbound: Gmail thread `1a0877cf7180a4f7` (Doug fwd,
> 2026-09-09). Spencer's reply sent same day ~13:09 PT. Internal ticket: Asana task
> `1218337331514879` (`[Progressive] IdeaSource Partner API Inquiry`, assigned Tim, Stephanie
> following). Technical findings from a read-only survey of the vault app @ `main`
> (`~/projects-work/progressive-card-vault/app`).

## The inquiry

Calvin Tang (`calvin@ideasource.ca`), IdeaSource — Canadian employee recognition/rewards company
supplying physical awards, wants to add digital gift cards. Ask: "an API style solution where our
system can connect to yours to submit orders." Doug frames it as Progressive's first move into the
loyalty/rewards segment (Fundstream's stronghold — RBC Rewards fulfillment). Doug + Gord are
setting up a meeting with IdeaSource.

Precision note: IdeaSource is employee recognition, not loyalty per se — adjacent to the RBC
segment but likely trickle-cadence, one-card-at-a-time volume.

## Strategic read

- **This inbound is the demand evidence the roadmap deferred expansion for.** The 2026-05-21
  roadmap review put "order submission" in Phase 2 and merchant-branded portals in Phase 3,
  gated on partnerships justifying the investment.
- **The white-label thread converges here.** A partner order-capture layer on the vault serves
  both: the API is the headless (cheaper) entry; white-label portals are the same layer with a
  hosted UI. Build once, both channels ride it.
- **Also converges with the Redeem Gift button** (Ottawa Catholic retiree flow) and Doug's prior
  automated-email-delivery asks: all three point at the same Phase 2 muscle — automated
  single-card digital fulfillment.

## Technical read (vault survey, 2026-09-09)

The intake pattern already exists: `src/app/api/integrations/wordpress/formidable/orders/route.ts`
is a signed external order-intake API — HMAC-SHA256 per-connection auth (encrypted secrets in
`WordpressConnection`), Zod-validated payloads, idempotency on `(sourceSystem, sourceEntryId)`,
audit logging, all creation funneled through `src/lib/fulfillment-request-service.ts`.

Gaps between today and partner-ready:

1. Generalize `WordpressConnection` into a partner/credential entity (no tenant linkage, scopes,
   per-partner pricing/catalog today).
2. Stable vendor/SKU contract (current matching is fuzzy name lookup + hardcoded aliases).
3. Read/status endpoints and likely webhooks (no programmatic order state or card delivery).
4. Hardening: no rate limiting on intake, 5-min HMAC replay window with no nonce cache, API
   orders attributed to oldest user row, racy request-number generator.
5. **The decision fork (not code):** everything downstream of intake is human-gated (operator
   allocates/exports/confirms). Trickle-cadence partner orders need automated allocation +
   delivery of cash-equivalent inventory — a security-posture change, and Gord's territory.
   Second fork: deliver to recipient email vs. hand card payloads to the partner's system
   (custody transfer, bigger liability conversation).

## Discovery questions given to Doug for the IdeaSource meeting

Monthly volume + order shape (single vs batch); merchants/denominations; delivery model
(recipient email vs card data to their system); payment model (prepaid float vs invoicing —
prepaid safer); timeline; prior supplier-integration experience.

## Positioning sent

Confident on capability, priced to verification state ("would require some technical work" —
sent before Tim's review), risk language kept internal, roadmap tie named to client ("align with
the automated email delivery we moved to Phase 2 as well as the white label portal idea").
Tim's input requested via the Asana ticket before scoping expectations firm up.
