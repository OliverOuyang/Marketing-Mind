# 发布帖：demo-video 技能（中英各一版）

- 用的方法：baifu-lens 模式一 · 发布帖 7 个零件 + 按平台改说法
- 推的对象：Oliver-Skills 里的 [demo-video](https://github.com/OliverOuyang/Oliver-Skills/blob/main/skills/demo-video/SKILL.md)
- 读者：接外包、投标、做开源的独立开发者；他们的顾虑是"录演示视频太费时间，录出来还糊"
- 目标：Star 仓库，或者直接装上试一次
- 素材来源：仓库 README 与 SKILL.md 里写明的事实（Playwright 驱动真实网页、2 倍像素截帧、镜头推拉、AI 英文配音、试跑与字数上限、一个酒店图片搜索 demo 跑出 54 秒 14MB 的成片）。没有的数据一律标【待补】。

---

## 英文版（X / Product Hunt，约 110 词）

**开头备选（三选一）**

- A（反转）：The best way to record a demo video? Don't record it.
- B（反问）：Still screen-recording your demo five times to get one clean take?
- C（结果先行）：A 54-second, 1080p demo video. Nobody touched a mouse.

**正文（用开头 A）**

> The best way to record a demo video? Don't record it.
>
> demo-video is a Claude Code skill that turns a live URL into a 1080p walkthrough.
>
> A real browser clicks through your site, the camera zooms in on what matters, captions and an AI voiceover are added in post.
>
> No fake UI: every frame is your real page, and the script only describes what's on screen.
>
> Free and open source. Dry-run first, so you see the voiceover cost before you pay a cent.
>
> What would you demo first: your side project, or that client pitch due Friday?
>
> 👉 【待补：仓库链接】
> 🎬 Sample: 【待补：酒店图片搜索 demo 的成片或 GIF】

## 中文版（小红书，约 190 字）

中文版不是翻译，按小红书改说法：少讲技术栈，多讲"你也可以"和看得见的成果。

**笔记标题备选**

- 别再录屏了，让 AI 帮你把 demo 视频"拍"出来
- 投标前一晚，我用一个技能做完了演示视频
- 54 秒成片，全程没碰鼠标

**封面**：成片里镜头推近按钮的一帧 + 大字"全程没碰鼠标"

**正文**

> 做完一个项目，最烦的一步是录演示视频：录五遍才有一遍不卡，录出来还糊。
>
> 我把这一步交给了 AI：给它一个网址，它自己打开真实网页去点、去输入，镜头会推近你想让人看的地方，最后配上字幕和英文旁白，导出 1080p 视频。
>
> 画面全是真实页面，旁白只说屏幕上正在发生的事，不吹不存在的功能。
>
> 开源免费，配音先试跑，先告诉你要花多少字数再生成。
>
> 你最想先给哪个项目做一支演示视频？评论区告诉我 👇
>
> 链接：【待补】
>
> #个人开发者 #独立开发 #ClaudeCode #AI工具 #效率神器

---

## 五镜头自检

| 镜头 | 结果 | 理由 |
|---|---|---|
| 故事是热的 | 半 | 中文版有"录五遍才有一遍不卡"的痛点，但这句是推测的通用痛点，需要 Oliver 换成他自己真实录崩的一次 |
| 作品先说话 | ✗（待补） | 帖子成败全看那段样片；现在只有文字描述，没有可直接看的成果 |
| 可转述的素材 | 半 | "全程没碰鼠标""54 秒 1080p"能被转述，但缺一个能被转发的 GIF |
| 窄切口、大口号 | 半 | 窄切口清楚（URL 变演示视频），没有大口号；发布帖可以不要，但个人号认领时要补 |
| 先拆最大顾虑 | ✓ | "No fake UI / 画面全是真实页面"拆掉"AI 视频是假的"；"Dry-run first"拆掉"会不会偷偷烧钱" |

**最弱的一句**：英文版零件 3（替代方案没有的东西）不够锋利。"the camera zooms in on what matters" 是 Loom、Screen Studio 也能做到的事。真正独有的是"不用人录"，开头已经说了，中间应该换成一个具体对比：

- 原句：A real browser clicks through your site, the camera zooms in on what matters…
- 改写：Screen recorders still need you to perform. This one performs for you: a real browser clicks, types and scrolls, and the camera follows.

## 发出去之前要补

1. 样片：酒店图片搜索 demo 的 54 秒成片，或者剪一个 10 秒 GIF（帖子的核心，没有它不要发）。
2. 仓库链接，以及是否单独给这个技能一个落地页。
3. 一次你自己"录崩"的真实经历，替换中文版第一句。
4. 确认一个说法：README 写着酒店 demo 是投标 demo；如果涉及客户，样片里不能出现客户信息。
5. 生成一支视频大约花多少钱（MiniMax 按字数计费），有了这个数，"Dry-run first"后面可以接一句具体报价。

## 下一步

先补第 1 项：用 demo-video 给 Oliver-Skills 自己的仓库页做一支 30 秒样片，它既是帖子的素材，也是这个技能最好的证明。
