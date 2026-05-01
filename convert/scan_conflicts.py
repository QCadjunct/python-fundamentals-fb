import json, pathlib, sys

SOURCE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 \
         else pathlib.Path('source_notebooks/python-fundamentals-main')
clean, conflicts = [], []

for nb in sorted(SOURCE.rglob('*.ipynb')):
    var_cells = {}
    try:
        cells = json.loads(nb.read_text())['cells']
    except Exception:
        continue
    code_cells = [c for c in cells if c['cell_type'] == 'code']
    for i, cell in enumerate(code_cells):
        for line in ''.join(cell['source']).splitlines():
            line = line.strip()
            if '=' in line and not line.startswith(('#','==','!=','<=','>=')):
                lhs = line.split('=')[0].strip()
                if lhs.isidentifier() and not lhs.startswith('_'):
                    var_cells.setdefault(lhs, []).append(i)
    redef = {v: c for v, c in var_cells.items() if len(c) > 1}
    rel = str(nb.relative_to(SOURCE))
    if redef:
        conflicts.append((rel, redef))
    else:
        clean.append(rel)

print(f'Total : {len(clean) + len(conflicts)}')
print(f'Clean : {len(clean)}')
print(f'Conflicts : {len(conflicts)}')
print()
print('--- CLEAN ---')
for r in clean:
    print(f'  {r}')
print()
print('--- CONFLICTS ---')
for r, redef in conflicts:
    print(f'  {r}')
    for v, c in list(redef.items())[:3]:
        print(f'    {v!r} → cells {c}')
