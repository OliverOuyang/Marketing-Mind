# 贡献指南

欢迎补案例、补资料、改课程、改 skill。所有贡献走 Pull Request，描述里说清改了什么、为什么改、依据是什么。

## 加一个案例拆解

1. 复制 [templates/case-study.md](templates/case-study.md) 到 `cases/YYYY-MM-DD-案例简称.md`。
2. 只用公开材料：原帖、原文、商店页、README、作者本人复盘。每个判断挂出处；数字区分"自述""媒体转述""第三方数据"。
3. 拆人用 `cases/profiles/<人名>.md`，结构见 [skills/marketing-mind/references/teardown.md](skills/marketing-mind/references/teardown.md)。不收集私人信息。
4. 在 [cases/README.md](cases/README.md) 索引登记一行。
5. 值得反复调用的打法，按 [lenses/README.md](skills/marketing-mind/lenses/README.md) 写一个案例镜头。

## 加一份资料笔记

1. 按 [library/README.md](library/README.md) 的模板写，放 `library/notes/<模块号>-<主题>/<slug>.md`。
2. 必须有：`30 秒读懂`、`source_level`、`verified`、官方 `source_url`、获取方式。
3. 版权：受版权保护的书和文章只写笔记和不超过三条的短引，**不要提交原文**。只有公版、CC 或作者明确允许转载的全文才能放 `library/texts/`，并在 frontmatter 写明协议。
4. 运行 `python3 scripts/build_index.py` 重新生成 `library/INDEX.md` 和 `catalog.json`。

## 改课程或 skill

- 模块改动要同步检查 `library/` 里对应笔记和模块末尾的"通关标准"。
- skill 只有一个：`skills/marketing-mind/`。新能力优先加进 `references/` 的已有模式，不另开 skill。
- 改完运行 `python3 scripts/check_links.py`，确认没有断链。

## 写作风格

- 中文为主，术语保留英文原词（Positioning、JTBD）。
- 先结论后理由，具体到例子和数字；不写空形容词。
- 不编造数据、案例和引文；查不实的标"（待核实）"。

## 授权

提交即表示你同意：skill 和脚本按 MIT、内容按 CC BY 4.0 发布（见 [LICENSE](LICENSE)、[LICENSE-CONTENT](LICENSE-CONTENT)）。
