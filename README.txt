Townlight Procurement
=============

Townlight Procurement is the Townlight module for procurement RFP drafting, proposal comparison, exception extraction, scoring summaries, board memo inputs, staff review queues, review-required Townlight Meetings/Contracts context packets, adversarial local integration mocks, and award-packet checklists.

Current state: v0.3.0 procurement support and staff review queue runtime. It ships a FastAPI package aligned to the Townlight Core 1.3.0.dev2, deterministic and database-backed RFP drafting, award-packet workpapers, staff-only review queue workflows, review-required context packets, adversarial local integration mocks, proposal comparison scaffolds, exception extraction, scoring summary helper, award-packet checklist, and accessible public sample UI at /townlight_procurement.

It does not evaluate vendors, award contracts, make award decisions, submit procurements, provide legal advice, call live LLMs, call live vendor portals, or replace a procurement system of record.

Staff routes require TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL plus TOWNLIGHT_PROCUREMENT_STAFF_API_KEY and trusted headers:

- X-Townlight-Procurement-Role: staff or service
- X-Townlight-Procurement-Staff-Key: configured staff key

Local development:

python -m pip install git+https://github.com/townlight/core.git@3021821bf9a92c790a399ad12aed821d65b09105
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
