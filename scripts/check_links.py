#!/usr/bin/env python3
"""检查仓库内所有 Markdown 的相对链接是否指向存在的文件。用法：python3 scripts/check_links.py"""
import pathlib, re, sys, urllib.parse

root = pathlib.Path(__file__).resolve().parent.parent
bad = []
for md in root.rglob("*.md"):
    if ".git" in md.parts:
        continue
    text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        path = urllib.parse.unquote(target.split("#")[0])
        if path and not (md.parent / path).exists():
            bad.append(f"{md.relative_to(root)} -> {target}")
print("\n".join(bad) if bad else "所有相对链接都有效")
sys.exit(1 if bad else 0)
