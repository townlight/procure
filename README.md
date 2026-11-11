<a id="townlight_procurement"></a>

# Townlight Procurement

## Shared meeting imports · Windows 1.8.1.1

Windows 1.8.1.1 adds shared meeting imports for 31 source families, with 34 supported source/format pairs. Installed Windows Sandbox checks exercised preview, save and durable readback using public captures and fixtures, plus the documented Townlight handoffs. These checks do not establish automatic discovery on every live portal or a complete retest of every module.

[All 31 sources, formats and handoffs](https://townlight.github.io/manuals/meeting-imports.html) · [Installed acceptance](https://github.com/townlight/townlight/releases/download/townlight-windows-v1.8.1.1/ACCEPTANCE-Windows-1.8.1.1.md).

Windows 1.8.1.1 has fresh-install acceptance. An in-place upgrade to 1.8.1.1 was not exercised. The previous Windows 1.8.0.1 release tested upgrade from 1.7.2.1; that result applies to 1.8.0.1. Before an existing-city evaluation, back up city data and settings, close Townlight, keep the existing %LOCALAPPDATA%\CivicSuite profile, and use the same Windows account. Keep the prior installer and a restore path. Station continues to use its separately configured service.

The accepted MSI contains Townlight Runtime 0.3.1 and Meetings 1.0.6 distributions. Its health version strings still report Runtime 0.3.0 and Meetings 1.0.5. Default-branch source corrects those display strings; the signed MSI and its exact build source remain unchanged.


Townlight Procurement is the Townlight module for procurement RFP drafting, proposal comparison, exception extraction, scoring summaries, board memo inputs, staff review queues, review-required Townlight Meetings/Contracts context packets, adversarial local integration mocks, and award-packet checklists.

## In the Windows suite

Draft RFPs, compare proposals, and record an existing award decision with a linked contract draft. Install the [signed Townlight Windows beta 1.8.1.1](https://github.com/townlight/townlight/releases/tag/townlight-windows-v1.8.1.1) and select the full profile. See the [staff operating guide](https://townlight.github.io/manuals/windows-staff-workflows.html#procurement). The package examples below describe the standalone development interface.

Current state: **v0.3.0 procurement support and staff review queue runtime**. This repo ships a FastAPI package aligned to the Townlight Core 1.3.0.dev2, health/root endpoints, documentation gates, deterministic and database-backed RFP drafting, award-packet workpapers, staff-only review queue workflows, review-required Townlight Meetings/Contracts procurement context packets, adversarial local integration mocks, proposal comparison scaffolds, exception extraction, scoring summary helper, award-packet checklist, and accessible public sample UI at `/townlight_procurement`. It does **not** ship live vendor portals, official vendor evaluation decisions, legal advice, live LLM calls, e-procurement submission portals, award decisions, or procurement system-of-record integrations.

<a id="what-townlight_procurement-does"></a>

## What Townlight Procurement Does

- Draft sample RFP outlines and recommend a staff owner.
- Scaffold neutral proposal comparison rows for staff review.
- Flag common proposal exception language for staff/legal review.
- Build scoring summary scaffolds without ranking vendors.
- Produce award-packet checklists for procurement records.
- Persist RFP drafts and award-packet workpapers when `TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL` is configured.
- Route procurement review work through staff-only queue endpoints protected by `TOWNLIGHT_PROCUREMENT_STAFF_API_KEY`.
- Carry Townlight Meetings, Townlight Contracts, and solicitation context IDs into review-required packets without calling those systems live.
- Validate adversarial local integration mocks for spoofed roles, official evaluation attempts, award-decision attempts, submission attempts, legal-advice claims, stale context, and live vendor-portal claims.
- Demonstrate a public procurement-support UI at `/townlight_procurement`.

<a id="what-townlight_procurement-does-not-do"></a>

## What Townlight Procurement Does Not Do

- It does not evaluate vendors.
- It does not award contracts or make award decisions.
- It does not submit procurements.
- It does not provide legal advice.
- It does not call live LLMs or live vendor portals in this recovery release.
- It does not replace a procurement system of record.

<a id="civiccore-dependency"></a>

## Townlight Core Dependency

Townlight Procurement installs against the Townlight Core 1.3.0.dev2:

```bash
python -m pip install git+https://github.com/townlight/core.git@3021821bf9a92c790a399ad12aed821d65b09105
```

## API Surface

- `GET /` returns the shipped/planned boundary.
- `GET /health` returns package and Townlight Core versions.
- `GET /townlight_procurement` returns the accessible public sample UI.
- `POST /api/v1/townlight_procurement/rfps/draft` returns sample RFP drafting and a `staff_review_id` when persistence is configured.
- `GET /api/v1/townlight_procurement/rfps/draft/{draft_id}` retrieves a persisted RFP draft when workpaper persistence is configured.
- `POST /api/v1/townlight_procurement/proposals/compare` returns proposal comparison rows.
- `POST /api/v1/townlight_procurement/proposals/exceptions` returns exception flags.
- `POST /api/v1/townlight_procurement/scoring/summary` returns scoring-summary sections.
- `POST /api/v1/townlight_procurement/award-packet` returns an award-packet checklist and a `staff_review_id` when persistence is configured.
- `GET /api/v1/townlight_procurement/award-packet/{packet_id}` retrieves a persisted award-packet checklist when workpaper persistence is configured.
- `POST /api/v1/townlight_procurement/context/procurement-review` returns review-required procurement context with optional Townlight Meetings/Contracts IDs.
- `POST /api/v1/townlight_procurement/integrations/mock/procurement-context` validates local adversarial integration payloads.
- `POST /api/v1/townlight_procurement/staff/reviews` creates a staff-only review queue item.
- `GET /api/v1/townlight_procurement/staff/reviews` lists staff-only review queue items.
- `PATCH /api/v1/townlight_procurement/staff/reviews/{review_id}` updates staff-only queue status, assignment, and resolution.
- `GET /api/v1/townlight_procurement/staff/reviews/summary` returns staff queue counts.

## Optional Workpaper Persistence And Staff Queue

Set `TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL` to a SQLAlchemy database URL to store generated RFP drafts, award-packet checklists, and staff review queue records:

```bash
export TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL="sqlite+pysqlite:///./townlight_procurement.db"
```

Set `TOWNLIGHT_PROCUREMENT_STAFF_API_KEY` before using staff-only review routes:

```bash
export TOWNLIGHT_PROCUREMENT_STAFF_API_KEY="replace-with-city-secret"
```

Staff routes require `X-Townlight-Procurement-Role: staff` and `X-Townlight-Procurement-Staff-Key` matching the configured key. Townlight Procurement uses Townlight Core `staff_key_gate` for timing-safe key comparison. Without persistence, Townlight Procurement remains deterministic and stateless. Retrieval and staff-only endpoints return actionable `503` responses that name the required configuration.

## Local Development

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
bash scripts/verify-release.sh
```

## License

Code is Apache License 2.0. Documentation is CC BY 4.0.
