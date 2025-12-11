#!/usr/bin/env python3
import json
import re

file_path = r'E:\project\Netflix-Content-Analysis-Personalized-Genre-Explorer-\Netflix_Genre.ipynb'

# Read with UTF-8-sig to skip BOM
with open(file_path, 'r', encoding='utf-8-sig') as f:
    content = f.read()

# Pattern: closing bracket/brace followed directly by opening bracket/brace without comma
# This is the most common JSON array/object delimiter error
content = re.sub(r'(\]|\})\s*\n\s*(\[|\{)', r'\1,\n\2', content)

# Try to parse
try:
    data = json.loads(content)
    print("✓ JSON is valid after fix!")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)
    
    print("✓ Notebook fixed and saved!")
    
except json.JSONDecodeError as e:
    print(f"✗ Still has JSON error at Line {e.lineno}, Column {e.colno}: {e.msg}")
    
    # Show context
    lines = content.split('\n')
    if 0 <= e.lineno - 1 < len(lines):
        line_num = e.lineno - 1
        start = max(0, line_num - 3)
        end = min(len(lines), line_num + 4)
        print("\nContext:")
        for i in range(start, end):
            marker = ">>> " if i == line_num else "    "
            print(f"{marker}Line {i+1}: {lines[i][:100]}")
