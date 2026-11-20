Windows 1.8.2.1 maintenance release

Windows 1.8.2.1 packages the staff authorization, explicit database configuration and component metadata corrections. Its exact signed installed checks cover setup, the 1.8.1.1 upgrade, saved staff records, procurement/Contracts handoffs, backup/restore and uninstall retention. Unchanged module and 31-source/34-format import evidence remains attributed to the earlier build that produced it; this is not a new exhaustive test of every module or live provider.

Windows 1.8.2.1 has signed installed acceptance for fresh setup and an in-place upgrade from Windows 1.8.1.1. Before upgrading, back up city data and settings, close Townlight, run the signed MSI, and reopen it under the same Windows account with the existing %LOCALAPPDATA%\CivicSuite profile. Keep the prior installer and a restore path. Other upgrade paths are unverified. Station uses its separately configured service. The acceptance summary distinguishes new maintenance checks from reused workflow evidence.

Release and downloads · Acceptance and limits.

Townlight Procurement

Shared meeting imports · Windows 1.8.1.1

Windows 1.8.1.1 adds shared meeting imports for 31 source families, with 34 supported source/format pairs. Installed Windows Sandbox checks exercised preview, save and durable readback using public captures and fixtures, plus the documented Townlight handoffs. These checks do not establish automatic discovery on every live portal or a complete retest of every module.

All 31 sources, formats and handoffs · Installed acceptance.

Windows 1.8.2.1 has signed installed acceptance for fresh setup and an in-place upgrade from Windows 1.8.1.1. Before upgrading, back up city data and settings, close Townlight, run the signed MSI, and reopen it under the same Windows account with the existing %LOCALAPPDATA%\CivicSuite profile. Keep the prior installer and a restore path. Other upgrade paths are unverified. Station uses its separately configured service. The acceptance summary distinguishes new maintenance checks from reused workflow evidence.

Windows 1.8.2.1 contains Townlight Runtime 0.3.2 and Meetings 1.0.6. Its current component sources and installed evidence are identified in the maintenance acceptance summary.

Townlight Procurement is the Townlight module for procurement RFP drafting, proposal comparison, exception extraction, scoring summaries, board memo inputs, staff review queues, review-required Townlight Meetings/Contracts context packets, adversarial local integration mocks, and award-packet checklists.

In the Windows suite

Draft RFPs, compare proposals, and record an existing award decision with a linked contract draft. Install the signed Townlight Windows beta 1.8.1.1 and select the full profile. See the staff operating guide. The package examples below describe the standalone development interface.

Current state: v0.3.1 procurement support and staff review queue runtime. This repo ships a FastAPI package aligned to the Townlight Core 1.3.0.dev2, health/root endpoints, documentation gates, deterministic and database-backed RFP drafting, award-packet workpapers, staff-only review queue workflows, review-required Townlight Meetings/Contracts procurement context packets, adversarial local integration mocks, proposal comparison scaffolds, exception extraction, scoring summary helper, award-packet checklist, and accessible public sample UI at /townlight_procurement. It does not ship live vendor portals, official vendor evaluation decisions, legal advice, live LLM calls, e-procurement submission portals, award decisions, or procurement system-of-record integrations.

What Townlight Procurement Does

- Draft sample RFP outlines and recommend a staff owner.
- Scaffold neutral proposal comparison rows for staff review.
- Flag common proposal exception language for staff/legal review.
- Build scoring summary scaffolds without ranking vendors.
- Produce award-packet checklists for procurement records.
- Persist RFP drafts and award-packet workpapers when TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL is configured.
- Route procurement review work through staff-only queue endpoints protected by TOWNLIGHT_PROCUREMENT_STAFF_API_KEY.
- Carry Townlight Meetings, Townlight Contracts, and solicitation context IDs into review-required packets without calling those systems live.
- Validate adversarial local integration mocks for spoofed roles, official evaluation attempts, award-decision attempts, submission attempts, legal-advice claims, stale context, and live vendor-portal claims.
- Demonstrate a public procurement-support UI at /townlight_procurement.

What Townlight Procurement Does Not Do

- It does not evaluate vendors.
- It does not award contracts or make award decisions.
- It does not submit procurements.
- It does not provide legal advice.
- It does not call live LLMs or live vendor portals in this recovery release.
- It does not replace a procurement system of record.

Townlight Core Dependency

Townlight Procurement installs against the Townlight Core 1.3.0.dev2:

    python -m pip install git+https://github.com/townlight/core.git@3021821bf9a92c790a399ad12aed821d65b09105

API Surface

- GET / returns the shipped/planned boundary.
- GET /health returns package and Townlight Core versions.
- GET /townlight_procurement returns the accessible public sample UI.
- POST /api/v1/townlight_procurement/rfps/draft returns sample RFP drafting and a staff_review_id when persistence is configured.
- GET /api/v1/townlight_procurement/rfps/draft/{draft_id} retrieves a persisted RFP draft when workpaper persistence is configured.
- POST /api/v1/townlight_procurement/proposals/compare returns proposal comparison rows.
- POST /api/v1/townlight_procurement/proposals/exceptions returns exception flags.
- POST /api/v1/townlight_procurement/scoring/summary returns scoring-summary sections.
- POST /api/v1/townlight_procurement/award-packet returns an award-packet checklist and a staff_review_id when persistence is configured.
- GET /api/v1/townlight_procurement/award-packet/{packet_id} retrieves a persisted award-packet checklist when workpaper persistence is configured.
- POST /api/v1/townlight_procurement/context/procurement-review returns review-required procurement context with optional Townlight Meetings/Contracts IDs.
- POST /api/v1/townlight_procurement/integrations/mock/procurement-context validates local adversarial integration payloads.
- POST /api/v1/townlight_procurement/staff/reviews creates a staff-only review queue item.
- GET /api/v1/townlight_procurement/staff/reviews lists staff-only review queue items.
- PATCH /api/v1/townlight_procurement/staff/reviews/{review_id} updates staff-only queue status, assignment, and resolution.
- GET /api/v1/townlight_procurement/staff/reviews/summary returns staff queue counts.

Optional Workpaper Persistence And Staff Queue

Set TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL to a SQLAlchemy database URL to store generated RFP drafts, award-packet checklists, and staff review queue records:

    export TOWNLIGHT_PROCUREMENT_WORKPAPER_DB_URL="sqlite+pysqlite:///./townlight_procurement.db"

Set TOWNLIGHT_PROCUREMENT_STAFF_API_KEY before using staff-only review routes:

    export TOWNLIGHT_PROCUREMENT_STAFF_API_KEY="replace-with-city-secret"

Staff routes require X-Townlight-Procurement-Role: staff and X-Townlight-Procurement-Staff-Key matching the configured key. Townlight Procurement uses Townlight Core staff_key_gate for timing-safe key comparison. Without persistence, Townlight Procurement remains deterministic and stateless. Retrieval and staff-only endpoints return actionable 503 responses that name the required configuration.

Local Development

    python -m pip install -e ".[dev]"
    python -m pytest -q
    bash scripts/verify-release.sh

License

Current Townlight-owned code is AGPL-3.0-only. Documentation is CC BY 4.0.

Current source licensing

Current Townlight-owned Procurement source is AGPL-3.0-only, aligned with its Townlight Core dependency. A standalone installation includes that dependency and must retain its applicable notices and source obligations; it is not an Apache-only combination. Historical Apache grants and original releases retain their terms; the prior notice is preserved in docs/history/licensing/Apache-2.0-original.txt. This source correction does not relicense third-party code or replace the released Windows 1.8.1.1 artifacts.

Historical version tags

The retained v1.0.0 tag is a superseded pre-recovery source identity, not the current Procurement package or a current Windows release. Its numeric ordering must not be used to choose the installed version. The current Windows bundle contains townlight-procurement 0.3.1; use the published Suite version and exact component source pins. The historical tag and original release artifacts remain unchanged. GitHub has no separate v1.0.0 release page for this repository.
