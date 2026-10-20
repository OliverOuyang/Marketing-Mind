# skills/

本仓库只有一个 skill：**[marketing-mind](marketing-mind/SKILL.md)**，覆盖学、拆、做三类事。

| 模式 | 什么时候触发 | 细则 |
|---|---|---|
| 导师 | "开始今天的学习""出题""考考我""点评""我先写" | [mentor.md](marketing-mind/references/mentor.md) |
| 拆解 | "拆这个案例""这个人为什么火了" | [teardown.md](marketing-mind/references/teardown.md) |
| 写作 | 发布帖、长文、复盘、小红书图卡、README 首屏、自我介绍 | [writing.md](marketing-mind/references/writing.md) |
| 运营 | 账号定位、选题库、发布节奏 | [operations.md](marketing-mind/references/operations.md) |
| 视频 | 宣传片、演示视频、短视频脚本 | [video.md](marketing-mind/references/video.md) |
| 机会评估 | "我有个想法" | [opportunity.md](marketing-mind/references/opportunity.md) |
| 案例镜头 | "用 BaiFu 的方法写""像小王子（Sac）那样发布" | [lenses/](marketing-mind/lenses/README.md) |

## 安装

**Claude Code（推荐）**

```
/plugin marketplace add OliverOuyang/Marketing-Mind
/plugin install marketing-mind@marketing-mind
```

更新：`/plugin marketplace update marketing-mind`。

**手动**：把 `skills/marketing-mind/` 整个文件夹复制到 `~/.claude/skills/`（个人）或项目的 `.claude/skills/`。

**claude.ai**：在 Settings → Capabilities → Skills 上传 `skills/marketing-mind/` 文件夹打包成的 zip。只上传 `SKILL.md` 也能用，读不到的细则会去 GitHub 读。

## 历史

2026-10-20 之前这里是 `baifu-lens`（只按 BaiFu 一个人的方法写发布内容）。为了开源，把导师、拆案例、写作、运营、视频、机会评估合成一个通用 skill，BaiFu 降级为其中一个[案例镜头](marketing-mind/lenses/baifu.md)，同时加入 [Sac 镜头](marketing-mind/lenses/sac.md)（作品/游戏发布）。原 baifu-lens 的写作、运营、视频规则全部保留在 `references/` 里。
