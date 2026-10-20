---
title: Steamworks Documentation — Wishlists / Coming Soon / Steam Next Fest / Visibility on Steam / Demos（附 Steam Platform Analysis: Wishlist Update, 2016）
title_zh: Steamworks 官方文档：愿望单、即将推出页、Steam 新品节、Steam 曝光机制、Demo（附 2016 年官方愿望单数据分析）
author: Valve（Steamworks 文档团队；数据分析帖署名 Steamworks Development）
year: 文档持续更新（2026-10-20 读取）；数据分析帖 2016-03-29
type: report
modules: ["09", "05", "07"]
priority: 必读
access: 仅笔记（免费原文在线，未存私有副本）
source_url: https://partner.steamgames.com/doc/marketing/wishlist
local_file:
source_level: 一手
verified: 已读原文
updated: 2026-10-20
---

# Steamworks 官方文档：Coming Soon、愿望单、Next Fest 与 Steam 曝光机制

> 资料说明：这是平台方 Valve 写给开发者的官方文档，公开可读（不用登录）。2026-10-20 读了以下原文，下文用【】标出处：
> 【愿望单】Wishlists（partner.steamgames.com/doc/marketing/wishlist）；
> 【即将推出】Coming Soon（/doc/store/coming_soon）；
> 【发售流程】Release Process（/doc/store/releasing）；
> 【新品节】Steam Next Fest（/doc/marketing/upcoming_events/nextfest）及【新品节建议】Steam Next Fest - Tips（/nextfest/tips）；
> 【曝光】Visibility on Steam（/doc/marketing/visibility）；
> 【Demo】Demos（/doc/store/application/demos）；
> 【上架费】Steam Direct Fee（/doc/gettingstarted/appfee）；
> 【2016 数据】Steamworks 开发者组公告 "Steam Platform Analysis: Wishlist Update"（2016-03-29，【愿望单】文档里链接的官方分析）。
>
> **为什么选官方文档做这一份**：Zukowski 等人的说法大多是"观察 + 推断"，平台规则本身应以 Valve 原文为准。两者冲突时，先信官方规则，再用第三方数据补"规则没说的部分"。Valve 文档会改，规则类内容（几天、几周、百分之几）要以最新原文为准。

## 30 秒读懂

- **一句话**：在 Steam 上，商店页越早挂出来越好；玩家点"加入愿望单"后，你的游戏发售或打折时 Steam 会替你发邮件提醒他们。但 Steam 决定把你推给谁，主要看真实的购买和游玩，不看你有多少愿望单、多少访问量。
- **举个例子**：你挂出即将推出页，攒了 1 万个愿望单。发售那天，这 1 万人会收到邮件。按 Valve 2016 年的全站统计，收到愿望单邮件的人一周内平均约 3.4% 会买，也就是三百来人（示例）。这三百来人买了、玩了，Steam 才会开始把你推给更多陌生人。
- **什么时候用**：只要打算在 Steam 上发游戏，就在定下方向、能公开谈论这款游戏时读。
- **可信度**：一手（平台官方文档，已读原文）。注意两点：2016 年那组转化数据已有十年，平台和用户行为都变了，只能当量级参考；文档里的规则也会更新。

## 核心论点

> 核心句：官方给出的三条最重要建议是：**尽早挂出即将推出页；发售后持续经营，不要发完就走；每次促销或活动后回看愿望单数据**【愿望单 Best Practices】。

1. **即将推出页 = 蓄水池 + 社区入口**【即将推出】。商店页公开后，玩家可以加愿望单，同时开启社区中心（Community Hub）。新产品发售前，商店页**至少要公开 2 周**；提交审核要预留**至少 7 个工作日**（店面审核通常 3–5 个工作日）【即将推出】【发售流程】。
2. **挂得早基本没有坏处**【即将推出 Timing】。官方原话的意思是：除非游戏在这期间变化很大，否则商店页提前很久挂出来没有明显坏处；两年前加愿望单的人，和两周前加的人，购买可能性差不多。官方唯一提醒：美术方向和核心玩法还没定时，可以先别公开。
3. **愿望单会触发自动邮件**【愿望单】：
   - 正式发售或进入抢先体验时，给所有愿望单用户发邮件或手机推送；从 EA 转正式版时再发一次。
   - 打折 ≥ 20%、持续 > 8 小时、并且覆盖最低价的那个包时，才会发邮件。
   - 同一款游戏对同一用户有约 2 周（FAQ 写 1–2 周）的邮件冷却期，大促期间会延长。
   - Demo 上线后，开发者可以手动给愿望单用户发**一次**通知，按钮要在 Demo 上线后 14 天内按【愿望单】【新品节 FAQ】。
4. **愿望单（基本）不影响算法曝光**【曝光】。官方列了"重要"与"不重要"：
   - 重要：**有人买、有人玩**；**支持的语言**；**标签**准确。
   - 不重要：除"热门即将推出"（Popular Upcoming）等少数例外，**愿望单数基本不是算法因素**；**商店页访问量不是因素**；**访问到购买的转化率不是因素**；**好评率在"褒贬不一"（40%）以上时不是因素**，跌破 40% 才会减少推荐。
   - 不能花钱买 Steam 曝光，Next Fest 也没有付费推广位【曝光 FAQ】【新品节 FAQ】。
5. **发售时的保底曝光是"新品队列"**【曝光 Baseline】。正式发售后，游戏进入新品池；系统优先给浏览量最少的新品排队，用户点进商店页就算一次浏览。在此基础上表现好，才可能上"新品与热门"、"热销"、首页大图等位置。同期发售的热门游戏多，你可能很快被挤下去。
6. **Next Fest 是给未发售游戏 + 可玩 Demo 的一周活动**【新品节】。每年 2 月、6 月、10 月各一次；每款游戏**只能参加一次**；必须已有公开商店页，开幕前 Demo 必须上线；不能在活动结束前发售；不能用序章、试玩版之类的"短版"代替本体参加。官方说早参加（收集反馈）和晚参加（临近发售攒热度）"都可以"。
7. **Demo 是买前试玩，要能代表成品质量**【Demo】。官方一般建议等发售时再放 Demo，但如果"玩家要上手摸一下才懂"，提前放高质量 Demo 是有用的。Demo 里要有回到本体商店页的入口，存档可以通过 Steam Cloud 带到正式版。

## 框架 / 模型

### A. 从 0 到发售的官方时间线（按文档规则拼接）

| 时点 | 动作 | 依据 |
|---|---|---|
| 任意时点 | 支付 100 美元 Steam Direct 上架费（每个新应用一份；该应用调整后总收入达 1,000 美元后可抵回） | 【上架费】 |
| 能公开谈论游戏时 | 完成店面清单 → 提交审核（预留 ≥ 7 个工作日）→ 点 "Post as Coming Soon" | 【即将推出】 |
| 发售前 ≥ 2 周（硬性） | 即将推出页必须已公开至少 2 周 | 【即将推出】【发售流程】 |
| Next Fest 前 5 周 | 开发者预览上线（看自己被分到哪个分区）；想赶上媒体预览，Demo 此时要提交审核 | 【新品节 Workback】 |
| Next Fest 前 3 周 | Demo 构建最晚提交审核的时间 | 【新品节】 |
| Next Fest 前 11 天（tips 页写 10 天） | 媒体预览开始，媒体能看到全部报名游戏 | 【新品节】【新品节建议】 |
| Next Fest 前 4 天 | 官方预告片发布 | 【新品节】 |
| 开幕当天 | 活动开始；官方建议至少提前 30 分钟让 Demo 上线 | 【新品节】 |
| 活动期间 | 前几天各分区随机排序，之后按用户行为个性化推荐 | 【新品节 Visibility】 |
| 结束后 | 官方发布"最多人玩的 Demo"回顾页；鼓励 Demo 继续保留 | 【新品节 After/FAQ】 |
| 发售 | 手动点 "Release App"；系统给全部愿望单用户发邮件 | 【发售流程】【愿望单】 |

### B. 曝光因素清单【曝光】

| 因素 | 官方结论 |
|---|---|
| 购买和游玩 | 强信号，是最重要的因素 |
| 支持语言 | 影响推给谁 |
| 标签 | 影响推给谁，要完整准确 |
| 愿望单数 | 基本不是因素（少数如热门即将推出除外），作用是发邮件 |
| 商店页流量 | 不是因素 |
| 访问→购买转化率 | 不是因素 |
| 好评率 | ≥ 40% 时不是因素；< 40% 推荐减少 |
| 付费 | 不能买曝光 |

### C. Next Fest 自查清单【新品节】【新品节建议】

1. 本体（不是 Demo）报名，确认出现绿色对勾。
2. 选 1–2 个主分类，检查标签，开发者预览里看分区对不对。
3. 想进官方预告片：报名截止前商店页至少有一个公开预告片，素材和标签是最新的。
4. Demo 主菜单放一个反馈入口（Steam 讨论区子版块、Discord 等），写明 Demo 会不会、什么时候下架。
5. 本体商店页勾选"在购买选项上方显示 Demo"。
6. 直播可选；要做就提前测试几次，默认打开聊天。
7. 活动期间不要同时开 Playtest，以免把玩家分流到两个版本。

## 案例与数据

**【2016 数据】Valve 官方愿望单分析（2016-03-29 发布）**，全站平均：

| 指标 | 数字 |
|---|---|
| 收到愿望单邮件后一周内购买（游戏） | 平均 3.4%，中位数 2.6% |
| 同上（DLC） | 平均 5.0%，中位数 3.0% |
| 游戏一生中愿望单最终转化为购买或激活的比例 | 平均 23% |
| 愿望单转化中发生在折扣期的比例 | 平均 63% |
| 从加愿望单到购买的时间 | 平均 116 天，中位数 36 天；31.4% 的购买者在加入后一周内购买 |
| 阶梯式折扣 vs 一直用同一折扣 | 阶梯式的转化提高 70% |
| 愿望单邮件退订率 | 不到 1% |

同一帖子的定性结论：发售一周后才加愿望单的人多是价格敏感型，会等打折、改价、内容更新等"触发事件"；一个人在 5 月没被 25% 折扣打动，6 月同样的 25% 折扣大概率也不行。

**说明**：这组数据发布于 2016 年，样本是当时的 Steam 全站。今天的用户量、游戏数量、推荐系统都不同，**只适合说明"愿望单要靠事件触发、多数购买发生在折扣期"这类方向，具体百分比不要直接套用**。Zukowski 给的"首周 1%–20%"是开发者自报的发售转化，口径不同，不能和 3.4% 直接比较（见同目录 Zukowski 笔记）。

## 适用边界与常见误用

- **只管 Steam**。itch.io、网页游戏、移动商店的规则完全不同。Oliver 的小游戏如果不上 Steam，这份笔记能迁移的是两条思路：**先建一个能"存住兴趣"的地方**（邮件列表、Discord、关注），以及**平台推荐看真实使用，不看你自己拉来的流量**。
- **误用 1："愿望单越多，Steam 越推我"**。官方说法正相反：愿望单的作用是发售和打折时的邮件，算法看的是之后的购买和游玩。Zukowski 也说"愿望单是引信，销售才是爆炸"。
- **误用 2："商店页刚挂出来没人加，就被算法判死刑"**。Zukowski 转述 Valve 在问答会上的说法：没有这种"永久记录"【见 Zukowski 笔记】。官方文档也写着访问量和转化率不是因素。
- **误用 3：把 Demo 留到 Next Fest 首发**。规则允许，但官方 FAQ 说任何时候放 Demo 都行，Zukowski 则明确建议别在 Next Fest 首发，以免带着 bug 用掉唯一一次机会。这是"规则允许"和"策略最优"的区别。
- **官方和第三方的分歧要讲清**：官方 Demo 文档说"一般建议等到发售"，而 Zukowski 和很多成功案例主张尽早放 Demo 找主播。两者针对的情况不同：官方说的是通用情况，Zukowski 说的是"玩了才懂"、需要主播带量的独立游戏。官方自己也承认"需要上手才懂"的游戏适合提前放。
- **文档内部也有小出入**：媒体预览在流程表里是"前 11 天"，在 tips 页是"前 10 天"；邮件冷却在正文是"2 周"，FAQ 是"1–2 周"。备课时引用更保守的那个，并注明以最新原文为准。

## 出题素材

1. **（Oliver 真实场景）存住兴趣**：你的小游戏现在如果有人看了一眼觉得不错，他能在哪里"存"下这份兴趣（相当于 Steam 愿望单）？如果没有，用一周时间搭一个，并写出它在发布当天会怎样把这些人叫回来。
2. **规则 vs 策略**：Next Fest 规则允许 Demo 开幕当天才上线。请列出"开幕首发 Demo"和"提前两个月放 Demo"各自的风险，并说明哪一种更适合"玩了才懂"的游戏。
3. **读懂曝光表**：一个开发者说"我把商店页访问量刷高了，Steam 就会推我"。用【曝光】的官方因素表反驳他，并告诉他该把力气花在哪。
4. **数字算一算**：假设发售时有 8,000 个愿望单。分别用 2016 年官方平均 3.4% 和 Zukowski 说的首周 10% 估算首周购买，解释两个数为什么差这么多、你会用哪个做计划（示例）。
5. **打折节奏**：根据"同一折扣对同一批人第二次基本无效"和"阶梯式折扣转化高 70%"，给一款 15 美元的游戏设计发售后第一年的折扣节奏，并说明每次折扣前要看哪项数据。

## 对应模块与练习

- **09 阶段 0 立项**：把时间线 A 抄进立项卡，倒推"商店页最晚哪天挂、Demo 最晚哪天交"。
- **09 阶段 5 触达**：Next Fest、Demo 通知、更新曝光轮次（Update Visibility Rounds）都可以写成 05 练习 2 的渠道实验卡；曝光因素表适合 05 练习 5（漏斗诊断），把"Steam 内部推荐"单列一层。
- **09 阶段 6 成交**：愿望单邮件、阶梯折扣是 03（报价）和 07（推进成交）在 Steam 上的落地形式。
- **09 阶段 7 复盘**：用 Steamworks 后台的愿望单增加/删除/购买和流量来源数据做复盘，对应最终复盘提纲第 1 条"目标 vs 结果"。
- 对照阅读：第三方经验和门槛数字见 [Zukowski 笔记](zukowski-how-to-market-a-game.md)。

## 原文短引

- "Players who wishlist your game two years ahead of release can be just as likely to purchase as someone who wishlisted two weeks ahead of release." ——【即将推出】Timing
- "With a few exceptions like the Popular Upcoming tab, wishlists are not a factor in your game's algorithmic visibility on Steam." ——【曝光】Key Visibility Elements
- "In almost all cases, users need some trigger or event to encourage conversion such as a change in the release state of the game, a discount, a major content update, or some other publicized event." ——【2016 数据】

## 获取方式

- 全部免费公开：
  - https://partner.steamgames.com/doc/marketing/wishlist
  - https://partner.steamgames.com/doc/store/coming_soon
  - https://partner.steamgames.com/doc/store/releasing
  - https://partner.steamgames.com/doc/marketing/upcoming_events/nextfest （及 /tips）
  - https://partner.steamgames.com/doc/marketing/visibility
  - https://partner.steamgames.com/doc/store/application/demos
  - https://partner.steamgames.com/doc/gettingstarted/appfee
  - https://steamcommunity.com/groups/steamworks/announcements/detail/950630846501680764 （2016 愿望单数据分析）
- Valve 每届 Next Fest 前开开发者问答会，录像在官方 YouTube 播放列表（链接见【新品节】页面）。
