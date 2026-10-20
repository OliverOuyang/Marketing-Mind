---
title: How Superhuman Built an Engine to Find Product/Market Fit
title_zh: Superhuman 如何搭建一台"寻找 PMF 的引擎"（Sean Ellis 40% 测试）
author: Rahul Vohra（First Round Review）
year: 2018（2018-11-12）
type: article
modules: ["01", "05", "03"]
priority: 推荐
access: 原文已下载（私有）
source_url: https://www.firstround.com/review/how-superhuman-built-an-engine-to-find-product-market-fit
local_file: library-raw/vohra-superhuman-product-market-fit.md
source_level: 一手
verified: 已读原文
updated: 2026-10-20
---

# How Superhuman Built an Engine to Find Product/Market Fit

## 30 秒读懂

- **一句话**：判断产品有没有找到市场，可以直接问用户："如果以后再也不能用了，你会有多失望？"选"非常失望"的人达到 40%，通常说明产品站住了；没到就围绕最爱它的那群人继续改。
- **举个例子**：Superhuman 第一次测只有 22%。只看最爱它的那几类用户后升到 33%；之后一半精力强化用户最看重的"速度"，一半精力补移动端等短板，三个季度后升到 58%（First Round Review，2018）。
- **什么时候用**：已经有一批真实用户，想决定下一步是加倍投入长处还是先补短板时。
- **可信度**：一手。作者本人在 First Round Review 发表的原文，全文已读（存私有目录）。40% 门槛是 Sean Ellis 的经验基准，不是定律。

## 核心论点

1. **经典 PMF 定义都是滞后指标。** Graham（做出人们想要的东西）、Altman（用户自发推荐）、Andreessen（"Investment bankers are staking out your house"）描述的都是"有了 PMF 之后的样子"，对上线前的团队"so post hoc, so unactionable"（第 1 节）。
2. **Sean Ellis 的领先指标**：问"How would you feel if you could no longer use the product?"，看回答"very disappointed"的比例。Ellis 对近百家创业公司做过基准：增长困难的公司几乎都低于 40%，有强劲牵引力的几乎都高于 40%（"Anchoring around a metric"）。
3. **样本门槛很低**：只调查"最近体验过核心功能的人"（过去两周至少用过两次）；约 **40 份回答**就能得到方向上正确的结果。每个用户只调查一次，以免干扰基准。
4. **用"非常失望"的人来收窄市场，而不是用先入为主的画像收窄。** 让数据说话，甚至可能发现你没想到的细分市场。
5. **不是所有反馈都该听。** "Not disappointed"的人："politely disregard"——他们会要求分散注意力的功能、然后流失，留下"a mangled, muddled roadmap"。"Somewhat disappointed"的人再按"主要好处是否与核心卖点一致"切一刀：一致的才认真听。
6. **路线图一半加倍投入用户最爱的，一半解决阻碍别人爱上的。** "If you only double down on what users love, your product-market fit score won't increase. If you only address what holds users back, your competition will likely overtake you."

## 框架 / 模型

### A. 四问调查（直接可用）

1. How would you feel if you could no longer use [X]? — A) Very disappointed B) Somewhat disappointed C) Not disappointed
2. What type of people do you think would most benefit from [X]?
3. What is the main benefit you receive from [X]?
4. How can we improve [X] for you?

第 2 题最巧：满意用户"will almost always describe themselves"，而且用的是对他们最重要的词——直接可当文案素材。

### B. PMF 引擎四步

| 步骤 | 做法 | Superhuman 的结果 |
|---|---|---|
| 1. 细分，画出 HXC | 按第 1 题分组 → 给每人打 persona 标签 → 只保留"非常失望"组里出现的 persona（创始人、经理、高管、BD）；用第 2 题答案 + Julie Supan 的 HXC（high-expectation customer，目标人群中最挑剔、会为核心好处买单并传播的人）框架写画像 | 只看这些 persona，分数从 22% → 33%（文中说"jumped by 10%"，实际是 11 个百分点） |
| 2. 分析反馈 | 第 3 题（非常失望组）→ 找核心好处：**速度、专注、快捷键**；忽略不失望组；有点失望组中"主要好处=速度"的人看第 4 题 | 阻碍：**没有移动端**；长尾：集成、附件、日历、统一收件箱、搜索、已读回执 |
| 3. 排路线图 | 50% 加倍投入（更快：UI 100ms → <50ms；更多快捷键；Snippets 自动化；设计小细节如 "-->" 自动变 →）；50% 解决阻碍（移动端、日历等）；用"成本×影响"低/中/高打分，先做低成本高影响 | — |
| 4. 重复 | 持续调查新用户，PMF 分数成为最重要指标（每周/月/季度），产品团队 OKR 的唯一 KR | 三个季度内 33% → **58%** |

### C. 用户分层决策表

| 群体 | 怎么对待 |
|---|---|
| Very disappointed | 定义 HXC、找核心好处、学他们的用词 |
| Somewhat disappointed + 核心好处一致 | 重点倾听"什么在阻碍你"——通常是一个小东西 |
| Somewhat disappointed + 核心好处不一致 | 礼貌忽略 |
| Not disappointed | 礼貌忽略，不要据此改路线图 |

## 案例与数据

- **Superhuman 背景**：2015 开始写代码；2016 年 7 人；2017 夏 14 人仍未发布；Vohra 前一家公司 Rapportive 被 LinkedIn 收购，所以融资和媒体都不是问题——这恰恰让传统 PMF 信号失灵（他们主动不扩大用户）。
- **首测**：当时可调查用户 100–200 人；"very disappointed" 仅 **22%**。
- **Slack 基准**：Hiten Shah 2015 年向 731 名 Slack 用户提问，**51%** 回答非常失望（当时约 50 万付费用户）——说明 40% 很难超过。
- **HXC 画像"Nicole"**：与很多人打交道的忙碌职业人（高管、创始人、经理、BD）；每天读 100–200 封、发 15–40 封邮件（忙时 80 封）；以回复及时为荣；一周最多 2–3 次 Inbox Zero，大约一年一次"邮件破产"；对新产品开放，但对"有工具能让我处理邮件更快"持怀疑。
- **用户原话**（第 3 题）："Speed! The app is crazy fast, and the UX + keyboard shortcuts make me an actual superhuman."
- **日历**：团队内部不常用日历，凭直觉不会优先做；反馈把它"massively moved up"。
- **结果**：22% → 33%（细分后）→ 58%（三个季度后）；团队增至 22 人；NPS 同步上升；投资人主动要求追加。
- **警示**：随着超出早期用户，用户要求与现有产品功能对等，PMF 分数可能下降；SaaS 要持续改进，路线图每季度按此流程重建。

## 适用边界与常见误用

1. **40% 是经验基准，不是定律。** 来源是 Ellis 对"近百家"创业公司的观察，主要是互联网/SaaS 产品；对低频产品（比如找房、婚礼服务）、B2B 少数大客户、或刚上线不久的工具不一定适用。
2. **调查对象选错会让数字失真**：必须是"体验过核心价值"的活跃用户；把只注册没用过的人纳入会严重压低分数；反复调查同一人会抬高或扰乱分数。
3. **小样本 + 自选择偏差**：愿意回问卷的人本来就偏爱产品。40 份是"方向正确"，不是统计显著。
4. **"忽略不失望的人"有前提**：前提是你已经决定了核心好处和目标人群。在完全探索期，不失望的人的流失原因可能告诉你"选错了市场"。与 Mom Test 互补：问卷告诉你"多少人爱"，访谈告诉你"为什么"。
5. **这是"人们说的"数据**：仍是态度题，不是行为。应与留存、付费、推荐等行为数据对照（01 模块"永远更相信行为"）。
6. **"jumped by 10%"的表述**：原文说 22% 细分后到 33%，实际涨了 11 个百分点（相对涨幅 50%）——可作为"看清数字口径"的小练习。

## 出题素材

1. **（Oliver 真实场景）给 research-crawler 跑一次 Ellis 测试**：找出最近两周真正用过它（至少跑过两次抓取）的人——哪怕只有 5–10 个。改写四问（中文/英文各一版），写出你的预测："非常失望"比例会是多少？为什么？跑完后对比。追问：如果用户少于 40 人，你还能得出什么结论、不能得出什么结论？
2. **（Oliver 真实场景）为你自己写 HXC**：如果"产品"是你本人（找实习/合作），谁是你的"Nicole"——最挑剔、但一旦认可你就会主动推荐你的那个人？用 Nicole 的格式写 120 字画像（要有数字、要有怀疑点）。
3. **分层决策**：给你 20 条反馈（导师可现场编：5 条非常失望、8 条有点失望、7 条不失望），让你按决策表分类，并说明哪 3 条会进入下季度路线图。
4. **路线图 50/50**：Vohra 说只做用户爱的分数不涨，只补短板会被竞争对手超过。用你的个人作品集网站举例，各写 2 条"加倍投入"和"解决阻碍"的改动。
5. **批判题**：为什么"你会推荐给朋友吗"（NPS）和"不能用了你会多失望"问的是不同的东西？哪一个更接近"需要"、哪一个更接近"喜欢"？

## 对应模块与练习

- `modules/01-customer-insight`：核心概念 3（说/做/想——问卷是"说"，需与行为互证）；练习 4（真实访谈——用问卷第 2、3 题收集用户原话）；练习 6（数据版用户原话收集的分层思路）；学习目标 4（有证据支撑的用户画像——HXC 就是一个模板）。
- `modules/05-channels-growth`：PMF 前不要追增长（Vohra 最后的建议）。
- `modules/03-value-proposition`：用"核心好处"（speed）收敛价值主张。

## 原文短引

1. "Ask your users how they'd feel if they could no longer use your product. The group that answers 'very disappointed' will unlock product-market fit."（Anchoring around a metric 节）
2. "Politely disregard those who would not be disappointed without your product. They are so far from loving you that they are essentially a lost cause."（第 2 步）
3. "happy users will almost always describe themselves, not other people, using the words that matter most to them."（第 1 步）

## 获取方式

- First Round Review 免费原文：https://www.firstround.com/review/how-superhuman-built-an-engine-to-find-product-market-fit
- 相关：Sean Ellis《Hacking Growth》（与 Morgan Brown 合著，版权书）；Julie Supan 的 HXC 框架（Supan 个人网站文章）；文中提及的 Paul Graham、Marc Andreessen 原文（Andreessen "The only thing that matters" 由其他模块收录）。
