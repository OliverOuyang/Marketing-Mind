# Marketing Mind

[![GitHub Stars](https://img.shields.io/github/stars/OliverOuyang/Marketing-Mind?style=flat-square&color=DAA520)](https://github.com/OliverOuyang/Marketing-Mind/stargazers)
[![License: MIT](https://img.shields.io/badge/skill-MIT-green?style=flat-square)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey?style=flat-square)](LICENSE-CONTENT)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-blueviolet?style=flat-square)](https://agentskills.io)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-D97757?style=flat-square)](skills/marketing-mind/SKILL.md)

> **Maybe the most practical marketing skill you'll ever use.**

A marketing training ground for indie developers, students and creators: **one Claude skill + a 10-module course + 70+ sourced reading notes + teardowns of real viral launches**. The skill writes launch posts, retrospective long-form articles, Xiaohongshu (RedNote) card posts and video scripts for your own work, and can act as a Socratic mentor that only critiques when you want to practice. Content is in Chinese; the skill can write in English.

[中文](README.md)

## Install

```bash
npx skills add OliverOuyang/Marketing-Mind
```

Or in Claude Code:

```
/plugin marketplace add OliverOuyang/Marketing-Mind
/plugin install marketing-mind@marketing-mind
```

Or just tell your agent:

> Install this marketing skill: run `npx skills add OliverOuyang/Marketing-Mind`, read `skills/marketing-mind/SKILL.md`, then ask me what I want to promote.

## What the skill does

| You say | Mode |
|---|---|
| "Write a launch post / a retro article / a README hero section" | Writing |
| "Plan my account / give me 15 topics" | Operations |
| "Write a 45-second promo video script" | Video |
| "Break down this launch / why did this person go viral" | Teardown |
| "I have an idea" | Opportunity check |
| "Critique this / quiz me" | Mentor (critique only, no ghostwriting) |

Every output ends with a five-check self-review, a rewrite of the weakest line, and a list of real material you still need to supply. It never invents data, screenshots, testimonials or experiences.

## What's inside

- `skills/marketing-mind/`: the only skill (router + per-mode references + creator "lenses")
- `modules/`: 10 modules from marketing fundamentals to a real-world capstone
- `library/`: reading notes on classic sources (Dunford, Christensen, Cialdini, Ries & Trout, Moore, Berger, Graham and more), each with a 30-second summary, source level and verification status. Copyrighted books are summarized, never redistributed.
- `cases/`: teardowns of viral launches, starting with indie developer BaiFu
- `drafts/`: sample outputs written with the skill

## License

Skill and scripts: [MIT](LICENSE). Course, notes and cases: [CC BY 4.0](LICENSE-CONTENT). Third-party texts in `library/texts/` keep their own licenses.
