#!/usr/bin/env bash
set -euo pipefail

required=(
  "README.md"
  "README.txt"
  "CHANGELOG.md"
  "CONTRIBUTING.md"
  "LICENSE"
  "LICENSE-CODE"
  "LICENSE-DOCS"
  ".gitignore"
  "AGENTS.md"
  "USER-MANUAL.md"
  "SECURITY.md"
  "SUPPORT.md"
  "CODE_OF_CONDUCT.md"
  ".github/PULL_REQUEST_TEMPLATE.md"
  ".github/ISSUE_TEMPLATE/bug_report.md"
  ".github/ISSUE_TEMPLATE/feature_request.md"
  ".github/ISSUE_TEMPLATE/config.yml"
  "docs/RECONCILIATION.md"
  "docs/MILESTONES.md"
  "docs/IMPLEMENTATION_PLAN.md"
  "docs/github-discussions-seed.md"
  "MILESTONE_0_7_DONE.md"
  "docs/index.html"
  "pyproject.toml"
  "townlight_procurement/__init__.py"
  "townlight_procurement/main.py"
  "townlight_procurement/rfp_draft.py"
  "townlight_procurement/proposal_compare.py"
  "townlight_procurement/exception_extract.py"
  "townlight_procurement/scoring_summary.py"
  "townlight_procurement/award_packet.py"
  "townlight_procurement/integration_mocks.py"
  "townlight_procurement/persistence.py"
  "townlight_procurement/public_ui.py"
)

echo "==> Required-artifact check"
for file in "${required[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "FAIL: missing required artifact: $file" >&2
    exit 1
  fi
done

echo "==> Current-facing shipped/planned truth check"
current_files=("README.md" "README.txt" "USER-MANUAL.md" "docs/index.html")
bad_markers=(
  "official vendor evaluation decisions are available"
  "legal advice is available"
  "live vendor portals are available"
  "live LLM calls are available"
  "e-procurement submission portals are available"
  "award decisions are available"
  "system-of-record integrations are available"
  "production staff-review queues are available"
)

for file in "${current_files[@]}"; do
  for marker in "${bad_markers[@]}"; do
    if grep -Fqi "$marker" "$file"; then
      echo "FAIL: stale/planned-as-shipped marker '$marker' found in $file" >&2
      exit 1
    fi
  done
done

echo "VERIFY-DOCS: PASSED"
