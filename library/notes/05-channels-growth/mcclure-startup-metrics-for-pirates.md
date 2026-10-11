---
title: "Startup Metrics for Pirates: AARRR!"
title_zh: 海盗指标：AARRR
author: Dave McClure
year: 2007（Seattle Ignite 演讲 2007-08；博文 2007-09-06）
type: talk
modules: ["05", "03"]
priority: 必读
access: 原文已下载（私有）
source_url: https://www.slideshare.net/slideshow/startup-metrics-for-pirates-long-version/89026
local_file: library-raw/mcclure-startup-metrics-for-pirates.md
---

# Startup Metrics for Pirates: AARRR!（海盗指标）

> 来源说明：本笔记依据两份材料，合并私有保存于 `library-raw/`：
> 1. SlideShare 上的演讲幻灯片（long version）的文字，共 20 页，下文用"幻灯片 N"标注。
> 2. 原博文。作者原来的博客 500hats.typepad.com 已随 Typepad 关闭而无法访问，这里通过 Wayback Machine 2010 年的快照读取。
>
> 作者在博文里写道："Please feel free to steal this talk & distribute to others"。

## 一句话

把用户的生命周期拆成 5 步：**A**cquisition → **A**ctivation → **R**etention → **R**eferral → **R**evenue（读起来像海盗的 "AARRR!"）。为每一步定义**可测量的转化事件**，找出转化最差的那一步，集中优化它。不要盯着总访问量这种虚荣指标。

## 核心论点

1. **5 步客户生命周期**（幻灯片 2）：
   - **Acquisition**：用户从各种渠道来到网站。
   - **Activation**：用户第一次访问时有"happy"的体验。
   - **Retention**：用户回来，多次访问。
   - **Referral**：用户喜欢到愿意推荐给别人。
   - **Revenue**：用户发生了某种变现行为。
2. **每一步都要定义成具体、可测量的事件，并标上估计价值**（幻灯片 4、13–17）。例如"3 次以上访问（首 30 天内）"，而不是"用户活跃"。McClure 特别注明，示例数据"*not* actuals; your mileage may vary"。
3. **激活的标准要"先瞎猜、快迭代"**（幻灯片 6）。他给的参考标准是：停留 10–30 秒以上，看 2–3 个以上页面，点击 3–5 次以上，用过 1 个关键功能。方法是做大量 landing page 测试和 A/B 测试："just make lots of dumb guesses & iterate QUICK"。
4. **留存靠简单的自动邮件**（幻灯片 7）：在第 +3、+7、+30 天发生命周期邮件，每周或每月发状态邮件，事件发生时发事件邮件。
5. **只在用户"开心"之后才请求推荐**（幻灯片 8）：平均满意度达到 8/10 以上再请人推荐。收入那一步，他直说"I don't know jack about your business"（幻灯片 9），要你自己去搞清楚。
6. **选渠道要看漏斗的深处，而不只是流量**（幻灯片 5、11–12、18）。按**量（#）、转化率（%）、成本（$）**三个维度比较渠道，并且在尽可能深的漏斗层级上比较，最好比到 $$$。不要只比到"访问了 landing page"。
7. **管理规则**（幻灯片 19–20）：
   - 产品投入 **80% 用在优化已有功能**，20% 用在新功能。
   - 只选 **5–10 个**转化步骤来盯，少比多好。
   - **每个指标都要有一个 owner**。

## 框架 / 模型

**示例转化指标表**（幻灯片 4，原文注明"*not* actuals"）：

| 阶段 | 用户状态 / 事件 | 转化率 | 估计价值 |
|---|---|---|---|
| Acquisition | 访问网站 | 100% | $0.01 |
| Acquisition | 没有立刻离开（2 页以上、10 秒以上、2 次以上点击） | 70% | $0.05 |
| Activation | 第一次访问体验"开心" | 30% | $0.25 |
| Activation | 订阅邮件、博客、RSS 或 widget | 5% | $1 |
| Activation | 注册账号（含资料） | 2% | $3 |
| Retention | 回访（首 30 天内 3 次以上） | 2% | $5 |
| Retention | 打开邮件或 RSS 后点击 | 3% | $2 |
| Referral | 推荐 1 个以上用户访问 | 2% | $3 |
| Referral | 推荐 1 个以上用户激活 | 1% | $10 |
| Revenue | 产生最低收入 | 2% | $5 |
| Revenue | 产生盈亏平衡的收入 | 1% | $25 |

**四类测量方法**（幻灯片 10）：
- **Qualitative**：可用性测试、观察少数用户。
- **Quantitative**：流量和使用量分析。
- **Comparative**：A/B 测试、多变量测试。
- **Competitive**：和竞品对比。

**渠道比较的维度**（幻灯片 12）：
- 受众细分（比如年轻女性、某个都市区）
- 渠道来源（社交、SEM、自然流量、PR）
- 主题或品牌承诺（比如"找工作"）
- 以上各项交叉后的转化结果

**Acquisition 渠道清单**（幻灯片 3）：SEO、SEM、Apps & Widgets、Affiliates、Email、PR、Biz Dev、Campaigns/Contests、Direct/Tel/TV、Social Networks、Blogs、Domains。

## 案例与数据

- 这个演讲本身就是案例：2007 年在 Seattle Ignite 的 5 分钟快讲，后来成为增长圈最常用的漏斗框架之一，"AARRR" 也成了通用语。作者说这个演讲 80% 的价值在两张图里，就是生命周期图和转化指标表（博文）。
- 示例表里的数字都是虚构的。真正值得学的是表格的**结构**：每一行是一个可测的事件，有转化率，有估计价值。

## 适用边界与常见误用

- **示例数字是虚构的，不能当基准**。很多二手资料把"30% 激活率"当作行业标准，这是误读。
- **顺序不是固定的**。AARRR 是 2007 年网站时代的线性漏斗。今天很多产品是 Referral 驱动 Acquisition 的循环（参考 Balfour 和 Andrew Chen），或者先 Revenue 后 Retention（订阅制）。也有人主张把 Retention 放在最前面看，因为留存不住，获客就是往漏桶里倒水。
- **"8/10 满意才请推荐"在今天常被 NPS 取代**，但原则不变：不要在用户还没获得价值时就要求分享。
- **不要过度量化**。对一个只有 30 个用户的学生项目，McClure 的"Qualitative"那一类方法（直接观察 5 个人用）比搭建数据看板更有用。
- **AARRR 诊断的是"哪一步漏"，不告诉你"为什么漏"**。找到漏点之后，要回到 01 模块（JTBD、访谈）找原因。

## 出题素材

1. **（Oliver 真实场景）给 research-crawler 定义 AARRR**：仿照幻灯片 4 的表格，为 research-crawler 写 8–11 行可测事件。例如 Activation 可以是"首次成功导出 CSV"，Referral 可以是"在 issue 或 README 里提到别人"。要求每一行都写清楚**用什么数据源**来测（GitHub traffic、PyPI 下载量、issue 等）。
2. **找最大漏点**（05 练习 5）：给 Oliver 一组 skills-library 的假数据，比如每周 500 次访问、40 个 star、8 次 clone、1 个 issue。请他按 AARRR 归类，找出最大的漏点，并说明为什么不能先加获客（加难度条件）。
3. **激活定义**：research-crawler 的"aha moment"是什么？请用 McClure 的方式先写出 3 个"dumb guesses"，再设计怎么验证哪个才是真正的激活点。
4. **深漏斗比较渠道**：Oliver 在 Hacker News 和 Berkeley Discord 各发了一次帖子。HN 带来 300 次访问、2 个 issue；Discord 带来 40 次访问、5 个人真正跑通。按幻灯片 18 的原则，哪个渠道更好？还需要什么数据？
5. **Owner 规则**：如果 Oliver 和一个同学一起维护项目，5 个指标怎么分配 owner？只选 5 个的话，选哪 5 个？

## 对应模块与练习

- **05 练习 5（漏斗诊断 AARRR）**：本文就是这道练习的出处。示例表可以当作漏斗模板。
- **05 练习 2、3（三个实验 / 跑一个）**：实验卡的成功指标应该设在漏斗的深处（幻灯片 18）。
- **05 通关标准**中的"在一个漏斗里找到最大漏点"。
- **03 练习 2（价值方程）、03 练习 5（真实报价）**：Revenue 那一步需要你自己想清楚（幻灯片 9）。
- **01 练习 4（真实访谈）**：找到漏点之后，用访谈找原因。

## 原文短引

- "just make lots of dumb guesses & iterate QUICK" —— 幻灯片 6（Activation）
- "Only encourage users to refer *after* they have 'happy' user experience" —— 幻灯片 8（Referral）
- "If you don't want to watch video, 80% of the value of the talk is in these 2 pix" —— 博文（2007-09-06）

## 获取方式

- 幻灯片：https://www.slideshare.net/slideshow/startup-metrics-for-pirates-long-version/89026
- 原博文（Wayback 快照）：http://web.archive.org/web/20100102220033/http://500hats.typepad.com/500blogs/2007/09/startup-metrics.html （原站 500hats.typepad.com 已关闭）
- 私有副本：`library-raw/mcclure-startup-metrics-for-pirates.md`
