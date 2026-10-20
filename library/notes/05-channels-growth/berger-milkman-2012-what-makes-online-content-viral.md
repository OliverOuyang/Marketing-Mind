---
title: What Makes Online Content Viral?
title_zh: 什么让网络内容疯传？
author: Jonah Berger & Katherine L. Milkman
year: 2012（Journal of Marketing Research, 49(2)；作者主页 PDF 为 2011 年 Ahead of Print 版）
type: paper
modules: ["05", "04"]
priority: 必读
access: 原文已下载（私有）
source_url: https://jonahberger.com/wp-content/uploads/2013/02/ViralityB.pdf
local_file: library-raw/berger-milkman-2012-what-makes-online-content-viral.pdf
source_level: 一手
verified: 已读原文
updated: 2026-10-20
---

# What Makes Online Content Viral?（什么让网络内容疯传？）

> 来源说明：本笔记依据作者主页提供的论文 PDF，私有保存于 `library-raw/`。这个版本是 JMR 的 "Ahead of Print" 版（页脚印有 © 2011 American Marketing Association），正式刊于 *Journal of Marketing Research* 2012 年 4 月刊，DOI 10.1509/jmr.10.0353。
>
> 下文按论文结构标注出处：Study 1（NYT 实地数据）、Study 2a / 2b / 3（实验）、General Discussion。另有 **Figure 2**（各特征 +1SD 的效果）。这篇论文是 Berger 后来那本书《Contagious》里 STEPPS 中 **E（Emotion）** 和 **P（Practical Value）** 两项的实证基础。

## 30 秒读懂

- **一句话**：内容会不会被转发，关键不在正面还是负面，而在于它能不能让人"激动起来"。敬畏、愤怒、焦虑让人更想转，悲伤让人更不想转。
- **举个例子**：作者分析了 2008 年三个月里约 7,000 篇《纽约时报》文章：愤怒程度高一个标准差，进入"最多转发榜"的概率提高 34%；悲伤程度高一个标准差，概率下降 16%（Study 1，Figure 2）。
- **什么时候用**：写标题、选内容角度时，判断这条内容属于高唤醒还是低唤醒情绪。
- **可信度**：一手。同行评审论文（Journal of Marketing Research, 2012），作者主页 PDF 已读（私有保存），文中数字已与 PDF 核对。

## 核心论点

1. **正面内容整体上比负面内容更容易被分享**（Study 1）。这推翻了"坏消息传得快"的简单说法。
2. **但情绪的"唤醒度"比正负更关键**（Study 1，Figure 2）。愤怒、焦虑虽然是负面情绪，却**增加**分享；悲伤同样是负面情绪，却**减少**分享。敬畏是高唤醒的正面情绪，显著增加分享。
3. **因果机制是生理唤醒**（Study 2a、2b、3）。实验中操纵情绪的强度，发现"唤醒感"中介了情绪对分享意愿的影响（Sobel 检验显著）。
4. **内容本身的特征和"被平台推荐"同样重要**（Study 1，Discussion）。愤怒增加 1 个标准差，对进入"最多转发榜"概率的提升，相当于在 NYT 首页头条多挂 **2.9 小时**，这差不多是文章平均头条时长的 4 倍。
5. **实用价值和有趣程度也会推动分享**（Study 1）。实用价值 +1SD，进入榜单的几率增加 30%；有趣程度 +1SD，增加 25%。但实用内容**在博客上反而略少被讨论**（General Discussion），因为博客本身就是评论，实用信息"已经说完了"。
6. **与其找 influencer，不如打造有传染力的内容**（General Discussion 结尾）。已有研究质疑 "influentials" 策略的成本效益，作者建议"focus on crafting contagious content"。

## 框架 / 模型

**情绪 × 唤醒度 二维表**（按论文结论整理）：

| | 高唤醒（activating） | 低唤醒（deactivating） |
|---|---|---|
| **正面** | 敬畏 awe、娱乐 amusement → **↑ 分享** | 满足 contentment、放松 → 论文推论：不如娱乐 |
| **负面** | 愤怒 anger、焦虑 anxiety → **↑ 分享** | 悲伤 sadness → **↓ 分享** |

**Figure 2：某特征增加 1 个标准差后，进入 NYT"最多转发榜"的拟合概率变化**：

| 特征 | 变化 |
|---|---|
| Anger 愤怒 | **+34%** |
| Awe 敬畏 | **+30%** |
| Practical value 实用价值 | **+30%** |
| Interest 有趣 | +25% |
| Anxiety 焦虑 | +21% |
| 首页头条时长（控制变量） | +20% |
| Emotionality 情绪浓度 | +18% |
| Surprise 惊奇 | +14% |
| Positivity 正面度 | +13% |
| Sadness 悲伤 | **−16%** |

## 案例与数据

- **Study 1 数据**：
  - 2008 年 8 月 30 日到 11 月 30 日，共 **6,956** 篇 NYT 文章。爬虫每 15 分钟抓一次首页和"最多转发榜"。约 20% 的文章上过榜。
  - 其中 2,566 篇由 3 名编码员人工评分，信度 α 均 > .70；情绪正负和浓度用 LIWC 做文本分析。
  - 回归模型是 logistic 回归，控制了日期固定效应、版面、作者、首页位置等变量。
  - NYT 读者的转发对象：朋友 42%，亲戚 40%，同事 10%。
- **示例标题**（论文表格）：
  - 敬畏："Rare Treatment Is Reported to Cure AIDS Patient"
  - 愤怒："What Red Ink? Wall Street Paid Hefty Bonuses"
  - 悲伤："Maimed on 9/11..."
- **Study 2a**（N=49）：广告故事。Jimmy Dean（一个做猪肉食品的品牌）请**拉比**当代言人，这是高娱乐版本；请农夫当代言人是低娱乐版本。分享意愿 3.97 vs 2.92，唤醒中介显著（Sobel z = 2.02）。
- **Study 2b**（N=45）：客服故事。"United Smashes Guitars"（高愤怒）对比"Dents"（低愤怒），分享意愿 5.71 vs 3.37。
- **Study 3**（N=47）：高悲伤版本的分享意愿反而**更低**，2.39 vs 3.80。
- **营销启示**（General Discussion）：
  - BMW 的系列短片 "The Hire"（"Ambush"、"Hostage"）制造焦虑，获得数百万观看。
  - 公共健康信息用愤怒或焦虑框架，比用悲伤框架更容易传开。
  - 企业应优先处理让顾客**焦虑或愤怒**的体验（比如 Motrin 广告引发妈妈群体的反弹），而不是让顾客"失望"的体验。

## 适用边界与常见误用

- **"愤怒传得快" ≠ "应该制造愤怒"**。愤怒内容会带来流量，也会带来品牌风险和社区毒性。对 Oliver 这样建立个人品牌的学生来说，靠愤怒涨粉的长期代价很高。更推荐用**敬畏**（"居然能这样"）、**有趣**、**实用**这三种。
- **数据来自 2008 年 NYT 的邮件转发**。论文自己也指出，**一对一的 narrowcasting**（发邮件给某个朋友）和**广播式分享**（发推、发朋友圈）的动机可能不同，广播式分享更多是为了自我呈现和身份信号（General Discussion）。在今天的算法推荐平台上，效果的大小需要重新检验。
- **相关 ≠ 你的内容也会这样**。Figure 2 是"概率提升的百分比"，不是"保证爆"。基数低的时候，提升 30% 仍然很小。
- **实验样本小**（每个实验 N 约 45–49），测的是"自报的分享意愿"而不是真实分享。但它和 Study 1 的实地数据结论一致，这增强了可信度。
- **不要只看情绪而忽略 Practical Value**：在小众技术圈（GitHub、Hacker News），实用价值往往才是主要驱动力。

## 出题素材

1. **（Oliver 真实场景）唤醒度改写**：给出 Oliver 发布 research-crawler 的一条推文初稿，请他判断初稿落在"情绪 × 唤醒度"表的哪一格，再分别改写成"敬畏版"和"实用版"。追问：哪一版更适合 Hacker News，哪一版更适合 Berkeley 的 Discord？为什么？
2. **读数据题（05 通关）**：Figure 2 中愤怒 +34%，敬畏 +30%。如果你是一个新账号，会选哪一种？请从风险、可持续性和个人品牌三个角度论证，不能只看数字。
3. **悲伤陷阱**：很多学生项目介绍会写"我花了无数个夜晚……"，这属于低唤醒的情绪。请把这个故事改写成"挑战被打破"的高唤醒版本，要求事实不变。
4. **Narrowcast vs Broadcast**：skills-library 的一条更新，Oliver 想让同学**私下转给**一个具体的朋友。这条内容应该怎么写？和"公开发帖"的写法有什么不同？（提示：一对一转发时，接收者会觉得对自己有用。）
5. **批判题**：论文建议"craft contagious content"而不是找 influencers。这和 Lenny 文中"影响者带来第一批用户"（Twitter / Om Malik）的案例冲突吗？请让 Oliver 说明两者分别在什么条件下成立。

## 对应模块与练习

- **05 练习 4（STEPPS 拆解）**：本文是 E（Emotion）和 P（Practical Value）的实证来源，拆解爆款时要标注**唤醒度**，而不只是标注"有情绪"。
- **05 练习 2（三个实验）**：可以设计一个"同一内容、不同情绪框架"的 A/B 实验。
- **04 练习 3（标题训练）**：用论文里的示例标题，给 20 个标题按"情绪 × 唤醒度"分类。
- **04 练习 6（真实发布）**：复盘时记录内容的情绪类型和转发数据。
- **07 模块**：Motrin 的案例说明，客户的愤怒比失望更需要优先处理（可用于异议和危机处理）。

## 原文短引

- "Content that evokes high-arousal positive (awe) or negative (anger or anxiety) emotions is more viral." —— Abstract
- "...this increase is equivalent to spending an additional 2.9 hours as the lead story on the New York Times website..." —— Study 1 Discussion
- "...it may be more beneficial to focus on crafting contagious content." —— General Discussion 结尾

## 获取方式

- 作者主页 PDF：https://jonahberger.com/wp-content/uploads/2013/02/ViralityB.pdf
- 正式出版：*Journal of Marketing Research*, 49(2), 2012, DOI: https://doi.org/10.1509/jmr.10.0353 （可以通过 UC Berkeley Library 的数据库访问）
- 私有副本：`library-raw/berger-milkman-2012-what-makes-online-content-viral.pdf`
