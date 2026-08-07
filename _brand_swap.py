# -*- coding: utf-8 -*-
import pathlib, glob

old = '<div class="brand">Cyan<span>Cast</span></div>'
new = '<div class="brand"><span class="cyan">Cyan</span>Cast</div>'

files = glob.glob("E:/cyancast-project/deploy/**/*.html", recursive=True)
n_files = 0
n_total = 0
for f in files:
    p = pathlib.Path(f)
    t = p.read_text(encoding='utf-8')
    c = t.count(old)
    if c:
        t = t.replace(old, new)
        p.write_text(t, encoding='utf-8')
        n_files += 1
        n_total += c
print(f"files changed: {n_files}, replacements: {n_total}")

# verify no old pattern remains
remaining = sum(1 for f in files if old in pathlib.Path(f).read_text(encoding='utf-8'))
print("old pattern remaining:", remaining)