# Marketing Mind · 营销思维训练场

[![GitHub Stars](https://img.shields.io/github/stars/OliverOuyang/Marketing-Mind?style=flat-square&color=DAA520)](https://github.com/OliverOuyang/Marketing-Mind/stargazers)
[![License: MIT](https://img.shields.io/badge/skill-MIT-green?style=flat-square)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey?style=flat-square)](LICENSE-CONTENT)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-blueviolet?style=flat-square)](https://agentskills.io)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-D97757?style=flat-square)](skills/marketing-mind/SKILL.md)

> **这也许是你用过最实用的营销 skill。**

一个给独立开发者、学生和创作者用的营销训练场：**一个 Claude skill + 10 个模块的课程 + 70 多份带出处的精读笔记 + 真实爆款拆解**。它能直接帮你写发布帖、复盘长文、小红书图卡和视频脚本，也能当导师带你把营销练成本能。

[English](README.en.md) · [作者心路](docs/origin-story.md) · [贡献指南](CONTRIBUTING.md)

---

## 它能做出什么

一句话需求，得到一份能直接改了发的稿子，缺的真实素材会用 `【待补】` 标出来，不编造。

| 你说 | 它给你（节选自 [drafts/01](drafts/01-launch-post-demo-video.md)） |
|---|---|
| "帮我给 demo-video 这个开源技能写一条发布帖，中英各一版" | 英文开头三选一：<br>A "The best way to record a demo video? Don't record it."<br>B "Still screen-recording your demo five times to get one clean take?"<br>C "A 54-second, 1080p demo video. Nobody touched a mouse."<br><br>小红书标题按平台重写，不是翻译：<br>"别再录屏了，让 AI 帮你把 demo 视频'拍'出来"<br><br>末尾附五个检验自检表、最弱一句的改写、待补素材清单 |

更多示范稿：[复盘长文](drafts/02-retro-research-crawler.md) · [短视频脚本](drafts/03-video-script-marketing-mind.md)

**拆过的爆款**（拆解即样品，也是 skill 的案例镜头）

| 案例 | 最关键的一招 |
|---|---|
| [BaiFu × Auday：七天卖了三十万（自述）的 Apple Watch 录音 App](cases/2026-10-20-baifu-auday.md) · [人物画像](cases/profiles/baifu.md) | 产品官号先替自己说话，创始人再用长文"认领" |
| [Sac《小王子：星辰之旅》：一个人、16 天（自述）的网页 3D 游戏](cases/2026-10-20-sac-little-prince.md) · [人物画像](cases/profiles/sac.md) | 预告定时首发，工具方和朋友首小时接力转发，第三天把做法当第二个产品发出去 |

## 一行安装

```bash
npx skills add OliverOuyang/Marketing-Mind
```

或在 Claude Code 里：

```
/plugin marketplace add OliverOuyang/Marketing-Mind
/plugin install marketing-mind@marketing-mind
```

**懒人版**：把下面这段话直接发给你的 agent。

> 帮我安装这个营销 skill：运行 `npx skills add OliverOuyang/Marketing-Mind`。装好后读 `skills/marketing-mind/SKILL.md`，然后问我想推广什么。

其他装法（手动复制、claude.ai 上传）见 [skills/README.md](skills/README.md)。

## 两个入口

### 入口一：给 agent 用（skill）

装好后直接说需求，skill 自己路由到对应模式：

| 你说 | 模式 |
|---|---|
| "写一条发布帖""写游戏首发帖""写篇复盘""做成小红书图卡""改 README 首屏" | 写作 |
| "帮我规划账号""出 15 个选题" | 运营 |
| "写个 45 秒的宣传视频脚本" | 视频 |
| "拆一下这次发布""这个人为什么火了" | 拆解 |
| "我有个想法" | 机会评估 |
| "用 BaiFu 的方法写""像小王子那样发布" | 写作/运营 + 案例镜头 |
| "开始今天的学习""点评""考考我" | 导师（只点评不代写） |

### 入口二：给人学（课程）

10 个模块分四阶段，每个模块有学习目标、核心框架、案例速读、推荐阅读、练习题（含加难度版本）和通关标准。把仓库 clone 下来，用 Claude Code 打开，说"开始今天的学习"，[CLAUDE.md](CLAUDE.md) 会让 Claude 进入导师模式。

```
阶段一：底层认知        00 营销思维底层 → 01 用户洞察
阶段二：把东西说清楚    02 定位与差异化 → 03 价值主张与报价 → 04 文案与说服
阶段三：让人看到并买单  05 渠道与增长 → 06 个人品牌 → 07 销售与谈判
阶段四：主动出击        08 机会捕捉 → 09 综合实战（真实项目，循环迭代）
```

| # | 模块 | 核心问题 |
|---|---|---|
| 00 | [营销思维底层](modules/00-foundations/README.md) | 营销到底是什么？为什么人会买？ |
| 01 | [用户洞察](modules/01-customer-insight/README.md) | 谁会买？他们真正要完成什么任务？ |
| 02 | [定位与差异化](modules/02-positioning/README.md) | 在对方脑子里，我占哪个位置？ |
| 03 | [价值主张与报价](modules/03-value-proposition/README.md) | 怎么让"选我"成为显而易见的好交易？ |
| 04 | [文案与说服](modules/04-copywriting/README.md) | 怎么写/说，才能让人看完就想行动？ |
| 05 | [渠道与增长](modules/05-channels-growth/README.md) | 去哪里找人？怎么低成本放大？ |
| 06 | [个人品牌](modules/06-personal-brand/README.md) | 怎么把"我"变成一个值得被记住的品牌？ |
| 07 | [销售与谈判](modules/07-sales-negotiation/README.md) | 怎么推进成交，怎么谈到好结果？ |
| 08 | [机会捕捉](modules/08-opportunity/README.md) | 怎么发现机会、判断机会、快速下注？ |
| 09 | [综合实战](modules/09-capstone/README.md) | 拿一个真实的东西，从 0 卖出去 |

fork 后用 [templates/progress.md](templates/progress.md) 覆盖根目录的 `PROGRESS.md`，从零记录自己的进度。现在的 `PROGRESS.md` 和 `practice/` 是作者 Oliver 的真实学习记录，留作样例。

## 资料库：每条结论都有出处

[library/](library/README.md) 收了营销、定位、文案、增长、个人品牌、销售、机会捕捉和独立开发者发布的经典资料，每份一篇精读笔记：

- **易懂**：每篇开头是"30 秒读懂"：一句话、一个例子、什么时候用、可信度。
- **权威**：优先用一手来源（原书、原论文、作者本人的文章和演讲），每篇标明 `source_level`（一手/二手）和 `verified`（是否读过原文）；查不实的数字标"（待核实）"。
- **合法**：版权书只放笔记和购买链接，不放原文；公版和 CC 授权的全文放在 `library/texts/`。

总索引：[library/INDEX.md](library/INDEX.md)。机器可读目录：[catalog.json](catalog.json)。

## 目录结构

```
Marketing-Mind/
├── skills/marketing-mind/   ← 唯一的 skill：SKILL.md + references/（各模式细则）+ lenses/（案例镜头）
├── modules/                 ← 10 个学习模块
├── library/                 ← 资料库：INDEX.md + notes/ 精读笔记 + texts/ 可再分发全文
├── cases/                   ← 案例拆解，profiles/ 是人物画像
├── drafts/                  ← skill 写的示范稿
├── launch/                  ← 本项目自己的发布物料
├── templates/               ← 案例、练习、周复盘、机会卡片、进度模板
├── practice/ · PROGRESS.md  ← 作者的真实学习记录（样例）
├── swipe-file/ · opportunities/
├── docs/                    ← 作者心路、Claude 项目设置
├── scripts/                 ← 生成索引和目录、检查链接
├── catalog.json             ← 机器可读目录
└── CLAUDE.md                ← 导师守则（在仓库里开 Claude Code 时自动读取）
```

## 三条底线

1. **每学必练**：没有练习记录的学习不算数。
2. **真实优先**：练习用真实对象（你的简历、你的项目、你想合作的人），不用假想题。
3. **结果说话**：判断好坏看对方的反应（回复率、点击、成交、拒绝理由），不看自己感觉。

## 作者

[Oliver Ouyang](https://github.com/OliverOuyang)。自己做小游戏，作品做出来了却没人看，于是开始系统学营销；两天后小王子刷屏，后来又看到 BaiFu 的发布，决定把营销吃透，把学到的东西做成了这个项目。完整心路见 [docs/origin-story.md](docs/origin-story.md)。

【待补：各平台入口（公众号、小红书、X、B 站）】

[![Star History](https://api.star-history.com/svg?repos=OliverOuyang/Marketing-Mind&type=Date)](https://star-history.com/#OliverOuyang/Marketing-Mind&Date)

## 授权

skill 与脚本 [MIT](LICENSE)；课程、笔记、案例等内容 [CC BY 4.0](LICENSE-CONTENT)，转载请署名。`library/texts/` 里的第三方全文保留各自的原协议。
