#!/usr/bin/env python3
"""从精读笔记的 frontmatter 生成 library/INDEX.md 和根目录 catalog.json。

用法：python3 scripts/build_index.py（只用标准库；frontmatter 按"每行 key: value"宽松解析）
"""
import json
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
LIB = ROOT / "library"

MODULES = {
    "00": ("营销底层", "00-foundations", "营销到底是什么？为什么人会买？"),
    "01": ("用户洞察", "01-customer-insight", "谁会买？他们真正要完成什么任务？"),
    "02": ("定位与差异化", "02-positioning", "在对方脑子里，我占哪个位置？"),
    "03": ("价值主张与报价", "03-value-proposition", "怎么让\"选我\"成为显而易见的好交易？"),
    "04": ("文案与说服", "04-copywriting", "怎么写/说，才能让人看完就想行动？"),
    "05": ("渠道与增长", "05-channels-growth", "去哪里找人？怎么低成本放大？"),
    "06": ("个人品牌", "06-personal-brand", "怎么把\"我\"变成一个值得被记住的品牌？"),
    "07": ("销售与谈判", "07-sales-negotiation", "怎么推进成交，怎么谈到好结果？"),
    "08": ("机会捕捉", "08-opportunity", "怎么发现机会、判断机会、快速下注？"),
    "09": ("综合实战", "09-capstone", "拿一个真实的东西，从 0 卖出去"),
}
PRIORITY = {"必读": 0, "推荐": 1, "选读": 2}


def parse_frontmatter(block):
    meta = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key] = [x.strip().strip("\"'") for x in value[1:-1].split(",") if x.strip()]
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1].replace('\\"', '"')
        meta[key] = value
    return meta


def load_note(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    meta = parse_frontmatter(m.group(1)) if m else {}
    one = re.search(r"\*\*一句话\*\*[：:]\s*(.+)", text)
    meta["summary"] = one.group(1).strip() if one else ""
    meta["path"] = path.relative_to(ROOT).as_posix()
    meta["folder"] = path.parent.name[:2]
    meta["modules"] = [str(x).zfill(2) for x in (meta.get("modules") or [meta["folder"]])]
    return meta


def cell(value):
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def build_index(notes):
    access = Counter(n.get("access", "") for n in notes)
    levels = Counter(n.get("source_level", "未标注") for n in notes)
    lines = [
        "# 资料库索引",
        "",
        "> 由 `scripts/build_index.py` 从各笔记的 frontmatter 自动生成，不要手改。约定与版权取舍见 [README.md](README.md)。",
        "",
        f"共 **{len(notes)}** 份资料。",
        "",
        "- 获取状态：" + "，".join(f"{k} {v}" for k, v in access.most_common()) + "。",
        "- 来源等级：" + "，".join(f"{k} {v}" for k, v in levels.most_common()) + "。",
        "",
        "**怎么读这张表**：每篇笔记开头都有\"30 秒读懂\"（一句话、一个例子、什么时候用、可信度）。"
        "\"来源\"一列写一手/二手和是否读过原文；标了\"细节以原书为准\"或\"（待核实）\"的内容不要当确证事实引用。",
        "",
    ]
    for code, (name, _, question) in MODULES.items():
        own = sorted(
            (n for n in notes if n["folder"] == code),
            key=lambda n: (PRIORITY.get(n.get("priority"), 9), str(n.get("title", ""))),
        )
        related = [n for n in notes if n["folder"] != code and code in n["modules"]]
        if not own and not related:
            continue
        lines += [f"## {code} {name}", "", f"> {question}", ""]
        if own:
            lines += [
                "| 资料 | 作者 | 类型 | 优先级 | 来源 | 一句话 | 笔记 |",
                "|---|---|---|---|---|---|---|",
            ]
            for n in own:
                title = cell(n.get("title"))
                if n.get("title_zh"):
                    title += f"（{cell(n['title_zh'])}）"
                link = f"[{title}]({n['source_url']})" if n.get("source_url") else title
                source = " · ".join(x for x in [cell(n.get("source_level")), cell(n.get("verified"))] if x)
                note = n["path"].removeprefix("library/")
                lines.append(
                    f"| {link} | {cell(n.get('author'))} | {cell(n.get('type'))} | {cell(n.get('priority'))} "
                    f"| {source or cell(n.get('access'))} | {cell(n['summary'])} | [笔记]({note}) |"
                )
            lines.append("")
        if related:
            refs = "、".join(f"[{cell(n.get('title'))}]({n['path'].removeprefix('library/')})" for n in related)
            lines += [f"也相关：{refs}", ""]
    (LIB / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


def build_catalog(notes):
    cases = []
    case_index = (ROOT / "cases" / "README.md").read_text(encoding="utf-8")
    for row in re.findall(r"^\| (\d{4}-\d{2}-\d{2}) \| \[([^\]]+)\]\(([^)]+)\)[^|]*\| ([^|]+) \| ([^|]+) \|", case_index, re.M):
        date, title, path, kind, key = row
        cases.append({"date": date, "title": title, "path": f"cases/{path}", "type": kind.strip(), "key_move": key.strip()})
    lenses = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "skills/marketing-mind/lenses").glob("*.md") if p.name != "README.md")
    catalog = {
        "name": "Marketing Mind",
        "repo": "https://github.com/OliverOuyang/Marketing-Mind",
        "skill": {
            "name": "marketing-mind",
            "path": "skills/marketing-mind/SKILL.md",
            "modes": {
                "mentor": "skills/marketing-mind/references/mentor.md",
                "teardown": "skills/marketing-mind/references/teardown.md",
                "writing": "skills/marketing-mind/references/writing.md",
                "operations": "skills/marketing-mind/references/operations.md",
                "video": "skills/marketing-mind/references/video.md",
                "opportunity": "skills/marketing-mind/references/opportunity.md",
            },
            "lenses": lenses,
        },
        "modules": [
            {"id": code, "title": name, "question": q, "path": f"modules/{folder}/README.md"}
            for code, (name, folder, q) in MODULES.items()
        ],
        "cases": cases,
        "notes": [
            {
                "path": n["path"],
                "title": n.get("title"),
                "title_zh": n.get("title_zh"),
                "author": n.get("author"),
                "year": n.get("year"),
                "type": n.get("type"),
                "modules": n["modules"],
                "keywords": [MODULES[m][0] for m in n["modules"] if m in MODULES],
                "priority": n.get("priority"),
                "access": n.get("access"),
                "source_level": n.get("source_level"),
                "verified": n.get("verified"),
                "source_url": n.get("source_url"),
                "summary": n["summary"],
            }
            for n in notes
        ],
    }
    (ROOT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")


if __name__ == "__main__":
    notes = [load_note(p) for p in sorted((LIB / "notes").glob("*/*.md"))]
    build_index(notes)
    build_catalog(notes)
    print(f"INDEX.md 与 catalog.json 已生成：{len(notes)} 份笔记")
