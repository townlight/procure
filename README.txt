
## Shared meeting imports · Windows 1.8.1.1

Windows 1.8.1.1 adds shared meeting imports for 31 source families, with 34 supported source/format pairs. Installed Windows Sandbox checks exercised preview, save and durable readback using public captures and fixtures, plus the documented Townlight handoffs. These checks do not establish automatic discovery on every live portal or a complete retest of every module.

[All 31 sources, formats and handoffs](https://townlight.github.io/manuals/meeting-imports.html) · [Installed acceptance](https://github.com/townlight/townlight/releases/download/townlight-windows-v1.8.1.1/ACCEPTANCE-Windows-1.8.1.1.md).

Windows 1.8.1.1 has fresh-install acceptance. An in-place upgrade to 1.8.1.1 was not exercised. The previous Windows 1.8.0.1 release tested upgrade from 1.7.2.1; that result applies to 1.8.0.1. Before an existing-city evaluation, back up city data and settings, close Townlight, keep the existing %LOCALAPPDATA%\CivicSuite profile, and use the same Windows account. Keep the prior installer and a restore path. Station continues to use its separately configured service.

The accepted MSI contains Townlight Runtime 0.3.1 and Meetings 1.0.6 distributions. Its health version strings still report Runtime 0.3.0 and Meetings 1.0.5. Default-branch source corrects those display strings; the signed MSI and its exact build source remain unchanged.

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
