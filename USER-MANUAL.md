<a id="townlight_procurement-user-manual"></a>

# Townlight Procurement User Manual

## For Non-Technical Users

Townlight Procurement helps city staff keep solicitation drafts, proposal notes, exception flags, scoring summaries, staff review queues, board memo inputs, Townlight Meetings/Contracts context references, and award-packet records organized. It can draft an RFP outline, scaffold proposal comparison rows, flag common exception language, build a scoring summary, and assemble an award-packet checklist.

Current state: 0.3.0 procurement support and staff review queue runtime. Townlight Procurement can optionally save generated RFP drafts, award-packet checklists, and staff review queue records when IT configures a workpaper database. Staff-only review routes also require `TOWNLIGHT_PROCUREMENT_STAFF_API_KEY`. Townlight Procurement does not provide official vendor evaluation decisions, legal advice, live vendor portals, live LLM calls, e-procurement submission portals, award decisions, or procurement system-of-record updates. Staff own every decision.

## For IT and Technical Staff

Townlight Procurement is a FastAPI Python package pinned to the published `townlight-core==1.3.0.dev2` release wheel. The current runtime exposes:

- `GET /`
- `GET /health`
- `GET /townlight_procurement`
- `POST /api/v1/townlight_procurement/rfps/draft`
- `GET /api/v1/townlight_procurement/rfps/draft/{draft_id}`
- `POST /api/v1/townlight_procurement/proposals/compare`
- `POST /api/v1/townlight_procurement/proposals/exceptions`
- `POST /api/v1/townlight_procurement/scoring/summary`
- `POST /api/v1/townlight_procurement/award-packet`
- `GET /api/v1/townlight_procurement/award-packet/{packet_id}`
- `POST /api/v1/townlight_procurement/context/procurement-review`
- `POST /api/v1/townlight_procurement/integrations/mock/procurement-context`
- `POST /api/v1/townlight_procurement/staff/reviews`
- `GET /api/v1/townlight_procurement/staff/reviews`
- `PATCH /api/v1/townlight_procurement/staff/reviews/{review_id}`
- `GET /api/v1/townlight_procurement/staff/reviews/summary`

Optional persistence is controlled by `TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL`. Staff queue routes also require `TOWNLIGHT_PROCUREMENT_STAFF_API_KEY`, `X-Townlight-Procurement-Role: staff`, and `X-Townlight-Procurement-Staff-Key` matching the configured key. Townlight Procurement uses Townlight Core `staff_key_gate` for timing-safe key comparison.

Run:

```bash
python -m pip install git+https://github.com/townlight/core.git@3021821bf9a92c790a399ad12aed821d65b09105
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
```

## Architecture

```mermaid
flowchart LR
  Staff["Purchasing / finance / department leads"] --> Townlight Procurement["Townlight Procurement v0.3.0"]
  Townlight Procurement --> CivicCore["Townlight Core 1.3.0.dev2"]
  Townlight Procurement -. released context ID .-> CivicClerk["CivicClerk v1.0.0"]
  Townlight Procurement -. future context ID .-> CivicContracts["CivicContracts"]
  Townlight Procurement --> Queue["Staff review queue"]
  Townlight Procurement --> Workpapers["RFP / award workpaper database"]
  Townlight Procurement --> Export["Award packet checklist"]
```

Townlight Procurement depends on Townlight Core. Townlight Core does not depend on Townlight Procurement. Townlight Procurement v0.3.0 uses deterministic sample procurement data plus optional staff-gated persistence, review-required context packets for Townlight Meetings/Contracts references, staff review queue records, and adversarial local mocks for integration-depth validation.

## Upgrading standalone PostgreSQL data

Stop the old service and back up its PostgreSQL database. In the same database,
verify that the old schema exists and the new schema does not. As the schema
owner, run the following in a transaction, then start the upgraded service
and check that existing records are present. The operation keeps the tables
and data in the same database. SQLite files require no schema rename.

```sql
BEGIN;
ALTER SCHEMA civicprocure RENAME TO townlight_procurement;
COMMIT;
```
