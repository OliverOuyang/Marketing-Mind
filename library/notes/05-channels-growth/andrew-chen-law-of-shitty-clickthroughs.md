---
title: "The Law of Shitty Clickthroughs（附 The Cold Start Problem 书目笔记）"
title_zh: 点击率必烂定律（附：冷启动）
author: Andrew Chen
year: 2012（博文）；2021（The Cold Start Problem，Harper Business）
type: essay
modules: ["05", "08"]
priority: 推荐
access: 原文已下载（私有）
source_url: https://andrewchen.com/the-law-of-shitty-clickthroughs/
local_file: library-raw/andrew-chen-law-of-shitty-clickthroughs.md
source_level: 一手
verified: 已读原文
updated: 2026-10-20
---

# The Law of Shitty Clickthroughs（点击率必烂定律）

> 来源说明：主文是 Andrew Chen 博客上的免费文章，私有保存于 `library-raw/`。文章按小标题分节：First it works, and then it doesn't / Novelty / First-to-market never lasts / More scale means less qualified customers / How to fight / The real solution。文中没有标注日期，从引用的数据（Facebook 2011）和提到的"当前未被占领的渠道"（Open Graph、移动推送）推断，大约写于 2012 年。
>
> 附录部分是他的书《The Cold Start Problem》（2021），受版权保护，只做书目笔记。作者在自己博客上公开的书的 Introduction 预览，也私有保存为 `library-raw/andrew-chen-cold-start-intro-preview.md`。
>
> 搜索时发现作者网站上挂着一份整本书的 PDF，但书内明确写着版权保留，不能确认是有意公开，所以**没有保存**。

## 30 秒读懂

- **一句话**：任何营销渠道，刚开始效果都好，用的人一多就会变差，这是规律不是你做错了。与其把旧渠道再优化一点，不如早点找到别人还没用的新渠道。
- **举个例子**：1994 年 HotWired 上第一个横幅广告的点击率是 78%，到 2011 年 Facebook 横幅广告只有 0.05%（First it works... 一节）。同样，你在 50 人的同学群里发小游戏链接，第一次很多人点，第五次就没人理了（示例）。
- **什么时候用**：复盘一个渠道"突然不灵了"、或者在决定下一步该把精力投到哪个新渠道时。
- **可信度**：一手。博文原文已读（私有保存）；附录的《The Cold Start Problem》是版权书，只读了作者公开的 Introduction 预览，书目部分细节以原书为准。

## 核心论点

1. **衰减是规律，不是你做错了**（First it works...）。
   - 1994 年 HotWired 上第一个横幅广告的点击率是 **78%**，2011 年 Facebook 横幅广告的平均点击率是 **0.05%**，相差约 **1,500 倍**。
   - 邮件打开率也在逐年下降，同时每天发出的邮件数量涨到了 300 亿封以上。
2. **驱动一：新奇感消退**（Novelty）。人们第一次看到横幅广告时，会出于好奇去点。之后大脑会学会过滤，这就是 banner blindness。同一套广告素材用久了，点击率也会持续下滑，所以需要轮换素材。
3. **驱动二：先发优势不持久**（First-to-market never lasts）。一个手法一旦奏效，竞争对手很快就会跟进，各种竞品监测工具让抄袭变得极其容易。
   - 文中的例子：用一个免费工具就能查到 Airbnb 的搜索广告投放情况，每天预算 **$10,638**，购买 **62,729** 个关键词。
4. **驱动三：规模越大，客户质量越低**（More scale...）。早期采用者对任何营销都反应更好（参照 Technology Adoption Lifecycle），所以**小规模测出的漂亮数字天然偏乐观**。
   - CAC 上升 30%，同时 LTV 下降 30%，回本时间就可能**翻倍**。对一家公司来说，这可能就是生与死的差别。
5. **两种对抗方法**（How to fight / The real solution）：
   - **Nomad strategy（游牧策略）**：不断换新素材、测试新的投放渠道，把衰减从"几个月"拖到"几年"。但这只能维持基本水平。
   - **有用的信息不衰减**："When you are marketing with useful information, then CTRs stay high."这句话是区分"广告"和"信息"的试金石。
   - **10× 解法：找到下一个未被开发的渠道**。别人问"你见过有人用 XYZ 获客吗？"时，他能给出的最高信任票是："No I haven't, and that's good – that means there's a higher chance of it working. You should try it."

## 框架 / 模型

**渠道生命周期曲线**（根据文章整理）：

```
效果
 ▲   新渠道（无竞争、新奇）
 │  ╭─╮
 │ ╱   ╲___  竞争者跟进 + 新奇消退
 │╱        ╲____  扩张到主流人群（质量下降）
 │               ╲______________  "shitty clickthroughs"
 └──────────────────────────────▶ 时间
     ↑ 最佳进入点：别人还没做
```

**三种驱动力 × 对策**：

| 驱动力 | 表现 | 对策 |
|---|---|---|
| Novelty fades | 同一素材的点击率下滑，banner blindness | 轮换素材；把广告做成**有用的信息** |
| First-to-market never lasts | 竞争者复制你的关键词和文案 | 进入下一个未被占领的渠道 |
| Less qualified at scale | 早期数据偏乐观，CAC↑ LTV↓ | 不要按小规模数据线性外推，按人群分层看 |

## 案例与数据

| 数据 / 案例 | 出处 | 说明 |
|---|---|---|
| 横幅广告点击率：HotWired 1994 年 78%，Facebook 2011 年 0.05%，约 1,500 倍 | First it works... | 作者称数据来自他人转述，只能当作量级参考 |
| 邮件打开率逐年下降，而每天发出的邮件超过 300 亿封 | 同上（引用 eMarketer） | 供给越多，注意力越稀缺 |
| 同一广告素材不轮换，点击率随时间下滑 | Novelty（引用 Retargeter 的分析） | 素材疲劳 |
| Banner blindness 眼动研究 | Novelty（引用 Jakob Nielsen） | 用户的视线会"滑过"广告区域 |
| Airbnb 搜索广告：每天 $10,638，62,729 个关键词 | First-to-market never lasts | 竞品的投放用免费工具就能查到 |
| CAC +30%、LTV −30%，回本时间可能翻倍 | More scale... | 小规模测试的数据偏乐观 |
| 文中当时"未被占领"的渠道：Open Graph、移动推送 | The real solution | 今天看，这两个渠道都已经饱和，这恰好印证了定律本身 |

## 附：The Cold Start Problem（书目笔记，按章节概念整理，不写页码）

- **核心问题**（Introduction，见私有预览）：网络型产品（社交、市场、协作工具）**用户越多越有价值**，但正因为如此，起步时极难，因为没人愿意用一个朋友或同事都不在的产品。Chen 借用"寒冷天气里汽车难以发动"来比喻这个问题。这和 Paul Graham 的"摇柄"比喻相映成趣。
  - 预览中的 Uber 案例：Uber 把每个城市当作一个独立的网络来经营，周会逐个城市看供需（surge 比例）。Lyft 推出 $250/$250 的司机推荐奖励后，Uber 讨论把奖励提高到 **$750/$750**。总量数字在 Uber 内部被视为"mostly meaningless"的虚荣指标。
- **生命周期五阶段**（全书结构）：The Cold Start Problem → Tipping Point → Escape Velocity → Hitting the Ceiling → The Moat。
- **关键概念**：
  - **Atomic network**：能够自我维持的最小网络，先在一个很小的范围内把它做成。
  - **Hard side**：网络里更稀缺、更难获取的一边，比如司机、创作者、卖家。
  - **"Come for the tool, stay for the network"**：先用单人也有用的工具吸引人，再逐步长出网络。
- 和 Andrew Chen 本文的关系：这本书讲的是**怎样让产品本身成为渠道**（网络效应、病毒传播），也就是 Balfour 所说的 product-channel fit 里的 virality 一类。

## 适用边界与常见误用

- **"定律"是经验规律，不是物理定律**。少数渠道衰减很慢，尤其是建立在有用信息之上的渠道，比如 SEO 长尾内容、真正有用的 newsletter。
- **不要把"找新渠道"变成"追热点"**。新渠道必须和产品匹配（参考 Balfour 的 product-channel fit），否则只是早早浪费时间。
- **对小项目的含义**：Oliver 的项目处于"早期采用者"阶段，现在看到的高回应率（同学捧场、HN 首页）**一定会下降**。复盘时不要用第一周的数据外推。
- **文中的数据来源比较随意**（Airbnb 的数据来自第三方免费工具，HotWired 78% 来自转述），只能当作量级参考。
- **The Cold Start Problem 主要适用于网络型产品**。research-crawler 是单人工具，网络效应弱；skills-library 如果允许社区贡献技能，就有"贡献者是 hard side"的网络属性。

## 出题素材

1. **（Oliver 真实场景）找未开发的渠道**：列出 5 个"你从没见过有人用来推广开源工具"的渠道，比如课程 office hour、某个学科的 Discord、arXiv 论文致谢、研究生院系的 newsletter、和图书馆员合作的工作坊。挑一个写成渠道实验卡（05 练习 2）。追问：它和产品匹配吗？
2. **小数据陷阱**：Oliver 在一个 50 人的群里发帖，有 10 人 star，转化率 20%。如果把这个比例外推到 5,000 人的大群，为什么不会还是 20%？请用文中的三个驱动力逐条分析。
3. **广告 vs 信息**：把 research-crawler 的一条"广告式"推文，改写成"即使不用这个工具也有价值的信息"，例如"抓取 Berkeley 课程数据时的 3 个反爬坑"，再在结尾带出工具。对应 04 练习 6。
4. **Atomic network**：如果 skills-library 想变成一个社区，它最小的自我维持网络是什么？多少个贡献者、多少个使用者、在哪个圈子？哪一边是 hard side？
5. **加难度**：预算为零、只有 2 周时间，请设计一个"nomad"计划，在同一个渠道里保持新鲜感（换素材、换角度），并写出每一轮要换掉什么。

## 对应模块与练习

- **05 练习 1（牛眼外环 19 渠道）**：本文是"为什么要在外环里大胆找冷门渠道"的理论依据。
- **05 练习 2、3（三个实验 / 跑一个）**：复盘时区分"渠道本身无效"和"渠道在衰减"。
- **05 练习 5（漏斗诊断 AARRR）**：More scale 一节提醒要按人群分层看漏斗。
- **08 练习 1（信号日记）**：记录"还没人用的新平台、新功能"作为机会信号。
- 对照阅读：Balfour《Four Fits》（新渠道的生命周期与平台周期）、Weinberg《Traction》（牛眼）。

## 原文短引

- "Over time, all marketing strategies result in shitty clickthrough rates." —— First it works, and then it doesn't
- "When you are marketing with useful information, then CTRs stay high." —— How to fight
- "No I haven't, and that's good – that means there's a higher chance of it working. You should try it." —— The real solution

## 获取方式

- 免费原文：https://andrewchen.com/the-law-of-shitty-clickthroughs/
- 书：*The Cold Start Problem*（Harper Business，2021）。官方网站：https://www.coldstart.com/ ；作者公开的 Introduction 预览：https://andrewchen.com/chapter-one-cold-start
- 借阅：Open Library 检索 https://openlibrary.org/search?q=cold+start+problem+andrew+chen
- 私有副本：`library-raw/andrew-chen-law-of-shitty-clickthroughs.md`；`library-raw/andrew-chen-cold-start-intro-preview.md`
