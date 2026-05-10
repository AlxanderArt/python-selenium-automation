#!/usr/bin/env bash
# One-shot smoke runner: dry-run sanity check, smoke suite via Allure
# formatter, generate the static report, open it. Fails fast on any
# step so a broken discovery never wastes a live run.
set -euo pipefail

RESULT_DIR="test_results/$(date +%Y%m%d_%H%M%S)"
REPORT_DIR="reports/latest"

echo "→ Dry-run discovery"
behave --tags=@smoke --dry-run --no-summary

echo "→ Running smoke suite, results: $RESULT_DIR"
behave --tags=@smoke \
  -f allure_behave.formatter:AllureFormatter \
  -o "$RESULT_DIR"

echo "→ Generating report at $REPORT_DIR"
allure generate "$RESULT_DIR" -o "$REPORT_DIR" --clean

echo "→ Opening report"
allure open "$REPORT_DIR"
