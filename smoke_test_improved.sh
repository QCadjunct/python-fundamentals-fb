#!/bin/bash

echo "=========================================="
echo "IMPROVED SMOKE TEST: Sections 20-32"
echo "=========================================="
echo ""

sections=(
  "20-modules-imports"
  "21-dates-times"
  "22-csv-module"
  "23-random-module"
  "25-decimal-module"
  "26-custom-classes"
  "27-practice-test-2"
  "28-3rd-party-libraries"
  "29-numpy"
  "30-pandas"
  "31-matplotlib"
  "32-practice-test-3"
)

passed_count=0
failed_count=0
syntax_errors=()
runtime_errors=()

for section in "${sections[@]}"; do
  echo "=== Testing: $section ==="
  
  for file in notebooks/$section/*.py; do
    if [ -f "$file" ]; then
      filename=$(basename "$file")
      
      # First: Check syntax
      if ! python -m py_compile "$file" 2>/dev/null; then
        echo "  ❌ $filename (SYNTAX ERROR)"
        syntax_errors+=("$file")
        ((failed_count++))
        continue
      fi
      
      # Second: Try to run (allow output, just check for crashes)
      if timeout 10s python "$file" >/dev/null 2>&1; then
        echo "  ✅ $filename"
        ((passed_count++))
      else
        exit_code=$?
        if [ $exit_code -eq 124 ]; then
          echo "  ⏱️  $filename (TIMEOUT - might be interactive)"
        else
          echo "  ⚠️  $filename (exit code: $exit_code)"
          runtime_errors+=("$file")
        fi
        ((failed_count++))
      fi
    fi
  done
  
  echo ""
done

echo "=========================================="
echo "RESULTS"
echo "=========================================="
echo "Passed: $passed_count"
echo "Failed: $failed_count"
echo ""

if [ ${#syntax_errors[@]} -gt 0 ]; then
  echo "Syntax Errors:"
  for file in "${syntax_errors[@]}"; do
    echo "  - $file"
  done
  echo ""
fi

if [ ${#runtime_errors[@]} -gt 0 ]; then
  echo "Runtime Errors:"
  for file in "${runtime_errors[@]}"; do
    echo "  - $file"
  done
fi
