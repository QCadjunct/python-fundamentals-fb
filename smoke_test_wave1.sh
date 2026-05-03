#!/bin/bash

echo "=========================================="
echo "SMOKE TEST: Wave 1 Sections (22-32)"
echo "=========================================="
echo ""

sections=(
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

failed_files=()
passed_count=0
failed_count=0

for section in "${sections[@]}"; do
  echo "=== Testing: $section ==="
  
  if [ ! -d "notebooks/$section" ]; then
    echo "  ⚠️  Directory not found: notebooks/$section"
    echo ""
    continue
  fi
  
  py_files=(notebooks/$section/*.py)
  
  for file in "${py_files[@]}"; do
    if [ -f "$file" ]; then
      filename=$(basename "$file")
      echo -n "  Testing $filename ... "
      
      # Run the file and capture errors
      if timeout 5s python "$file" > /dev/null 2>&1; then
        echo "✅ PASS"
        ((passed_count++))
      else
        echo "❌ FAIL"
        failed_files+=("$file")
        ((failed_count++))
        
        # Show the error
        echo "    Error:"
        timeout 5s python "$file" 2>&1 | head -10 | sed 's/^/      /'
      fi
    fi
  done
  
  echo ""
done

echo "=========================================="
echo "SMOKE TEST RESULTS"
echo "=========================================="
echo "Passed: $passed_count"
echo "Failed: $failed_count"
echo ""

if [ ${#failed_files[@]} -gt 0 ]; then
  echo "Failed files:"
  for file in "${failed_files[@]}"; do
    echo "  - $file"
  done
  echo ""
  echo "Run individual files to see full errors:"
  echo "  python <filename>"
fi

echo ""
echo "Test complete: $(date)"
