# Harness Engineer

<p align="center">
  <strong>一个用于设计并脚手架化 Agent Harness 工程的 Codex Skill。</strong>
</p>

<p align="center">
  <a href="./README.md">English</a>
</p>

<p align="center">
  <img alt="Skill" src="https://img.shields.io/badge/类型-Codex%20Skill-0A7EA4">
  <img alt="Focus" src="https://img.shields.io/badge/主题-Harness%20Engineering-1F9D55">
  <img alt="Loop" src="https://img.shields.io/badge/Ralph%20Preset-已内置-7C3AED">
  <img alt="Built with Codex" src="https://img.shields.io/badge/Built%20with-Codex-10B981">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-EAB308">
</p>

## 这个仓库是干什么的

`harness-engineer` 是一个可复用的 skill，用来把长任务、重复性任务、高风险任务或需要多人协作的 Agent 工作，变成真正可运行、可恢复、可验证的 harness 工程。

它的目标不是“堆更多提示词”，而是帮助 Codex：

- 先澄清执行合同
- 选择最小可行拓扑
- 搭出可恢复的工程骨架
- 区分稳定知识和可变状态
- 优先建立 validator 和机械约束
- 在需要时直接生成 Ralph 风格的循环骨架

这个仓库同时包含：

- 当前正式版 `harness-engineer`
- 一个升级 Ralph Loop preset 之前的备份快照

## 这个 Skill 能做什么

### 通用 Harness 工程设计

- 把 `AGENTS.md` 当目录地图，而不是百科全书
- 把 `docs/` 当系统知识库
- 把 `progress.txt` 当可恢复状态文件
- 用 `tasks.json` / `features.json` 保存可变的机器状态
- 用 validator 和结构规则替代“请遵守规范”式软提醒
- 保留后续升级空间，不把脚手架写死

### Ralph Loop 支持

当前版本已经内置显式的 `ralph-loop` preset，可直接脚手架出：

- `PROMPT.md`
- `progress.txt`
- `tasks.json`
- `docs/exec-plans/current-batch-plan.md`
- `logs/failure-log.jsonl`
- `archives/`
- Ralph 风格 runner 模板
- 对应 validator

## 仓库结构

```text
harness-engineer-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── versions.json
├── skills/
│   └── harness-engineer/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       └── scripts/init_harness_project.py
└── snapshots/
    └── harness-engineer-backup-20260408-161519/
```

## 包含的版本

| 版本 | 位置 | 说明 |
|---|---|---|
| 当前正式版 | [`skills/harness-engineer/`](./skills/harness-engineer/) | 已包含 Ralph Loop preset |
| 备份快照 | [`snapshots/harness-engineer-backup-20260408-161519/`](./snapshots/harness-engineer-backup-20260408-161519/) | 加入 Ralph preset 之前的备份版本 |

## 安装方式

把当前 skill 复制到你的 Codex skills 目录即可。

### Windows PowerShell

```powershell
Copy-Item -LiteralPath .\skills\harness-engineer -Destination "$HOME\.codex\skills\harness-engineer" -Recurse -Force
```

### macOS / Linux

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/harness-engineer ~/.codex/skills/harness-engineer
```

## 快速使用

安装后，可以显式调用这个 skill：

```text
Use $harness-engineer to clarify requirements and scaffold a robust harness project.
```

典型用法：

- “Use $harness-engineer to design a harness for a batch document-processing pipeline.”
- “Use $harness-engineer to refactor this prompt-only agent workflow into a recoverable harness.”
- “Use $harness-engineer to scaffold a Ralph Loop project for a multi-pass remediation task.”

## 脚手架脚本

Skill 自带一个辅助脚本：

[`skills/harness-engineer/scripts/init_harness_project.py`](./skills/harness-engineer/scripts/init_harness_project.py)

### 生成通用 harness 骨架

```powershell
python .\skills\harness-engineer\scripts\init_harness_project.py .\output --project-name "Example Harness"
```

### 生成 Ralph Loop 骨架

```powershell
python .\skills\harness-engineer\scripts\init_harness_project.py .\output --project-name "Example Ralph Harness" --preset ralph-loop
```

常用参数：

- `--preset baseline|ralph-loop`
- `--topology`
- `--runner`
- `--batch-size`
- `--with-features-file`
- `--with-failure-log`
- `--with-archives`

## 理念来源

这个 skill 是多方资料蒸馏后的结果，主要包括：

- OpenAI 的 Harness Engineering 文章
- Anthropic 关于长任务 harness 的两篇文章
- `snarktank/ralph`
- `HKUDS/OpenHarness`
- 以及额外的本地实践笔记与工程抽象

这个仓库不是上述任一项目的官方发布，而是基于它们进行的再提炼与工程化整合。

## 核心理念

> 更强的 prompt 有帮助，但更好的 harness 才能长期存活。

这个 skill 默认相信：

- 长任务必须把状态外置
- validator 比自我感觉“做完了”更重要
- 拓扑应该尽量小
- 模型变强后，脚手架应该允许被削减，而不是无限膨胀

## Attribution

- 人类项目拥有者与维护者：仓库维护者
- AI 实现与打包协助：OpenAI Codex

当前采用 README 显式署名的方式来标注 Codex 参与。如果你后面还想让提交历史也带上类似归属，可以在未来的 commit 中加入 co-author trailer，或者使用专门的 bot / 账号身份。

## 已做验证

当前 skill 已经过如下验证：

- `quick_validate.py` 校验 `SKILL.md`
- 脚手架脚本的 Python 编译检查
- 两种脚手架 smoke test：
  - baseline scaffold
  - Ralph Loop scaffold

## License

MIT，见 [LICENSE](./LICENSE)。
