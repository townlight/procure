<a id="civicprocure-agent-contract"></a>

# Townlight Procurement Agent Contract

## Source of Truth

- Upstream suite spec: `townlight/townlight/docs/CivicSuiteUnifiedSpec.md`, especially the Townlight Procurement catalog entry and suite-wide non-negotiables.
- Townlight Procurement supports RFP drafting, proposal comparison, exception extraction, scoring summaries, board memo inputs, and award-packet checklists.
- Staff own every decision.

## Hard Boundaries

- Townlight Procurement never evaluates vendors, awards contracts, submits procurements, provides legal advice, or updates a procurement system of record.
- Townlight Procurement v0.2.0 must not call live LLMs or live vendor portals.
- Proposal comparisons, exception flags, scoring summaries, and award packets must be marked staff-review-required where applicable.
- Townlight Procurement depends on Townlight Core; Townlight Core must never depend on Townlight Procurement.
- Townlight Procurement may reference Townlight Meetings, Townlight Contracts, and Townlight Records concepts only through released contracts, context IDs, or deterministic sample data in this recovery release.

## Verification

Run `bash scripts/verify-release.sh` before every push or release.
