# Harness Engineer

<p align="center">
  <img src="./assets/banner.svg" alt="Harness Engineer banner" width="100%">
</p>

<p align="center">
  <a href="./README.md"><strong>English</strong></a>
</p>

<p align="center">
  <img alt="类型" src="https://img.shields.io/badge/类型-Codex%20Skill-0A7EA4">
  <img alt="主题" src="https://img.shields.io/badge/主题-Harness%20Engineering-1F9D55">
  <img alt="Ralph Loop" src="https://img.shields.io/badge/Ralph%20Loop-已内置%20Preset-7C3AED">
  <img alt="Built with Codex" src="https://img.shields.io/badge/Built%20with-Codex-10B981">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-EAB308">
</p>

<p align="center">
  <strong>把脆弱的 prompt 流程，升级成可恢复、可验证、可长期运行的 harness 工程。</strong>
</p>

<p align="center">
  <a href="#简介">简介</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="./CONTRIBUTING.md">贡献指南</a> ·
  <a href="./ROADMAP.md">路线图</a> ·
  <a href="./RELEASING.md">发布策略</a>
</p>

## 简介

`harness-engineer` 是一个用于设计并脚手架化 Agent Harness 工程的 Codex skill。

它面向的任务通常具备这些特征：

- 长时间运行
- 可重复执行
- 多步骤推进
- 风险较高
- 可能跨越多次 fresh-context 重启

这个 skill 不把 prompt 当成全部系统，而是帮助 Codex：

- 先澄清执行合同
- 选择最小安全拓扑
- 区分稳定知识与可变状态
- 生成真正的工程骨架
- 外置可恢复状态
- 在需要时直接生成 Ralph 风格循环骨架

## 项目状态

- 当前版本：[`v0.1.2`](https://github.com/3109406559-code/harness-engineer-skill/releases/tag/v0.1.2)
- 当前状态：loop preset、runner 分支和 project preset 都已通过回归
- 当前范围：一个正式 skill、一个回滚快照、一个脚手架脚本
- 演进方式：优先更新 doctrine，再更新脚手架脚本，最后才动 skill 触发逻辑

## 核心亮点

<table>
  <tr>
    <td width="33%">
      <strong>Harness Doctrine</strong><br>
      把 OpenAI、Anthropic、Ralph、OpenHarness 和本地实践笔记里的方法论蒸馏进一个可复用 skill。
    </td>
    <td width="33%">
      <strong>脚手架脚本</strong><br>
      内置 Python 生成器，可直接产出 baseline 或 Ralph Loop 风格项目骨架。
    </td>
    <td width="33%">
      <strong>Ralph Loop Preset</strong><br>
      直接生成 <code>PROMPT.md</code>、<code>tasks.json</code>、<code>progress.txt</code>、日志、归档和 Ralph runner。
    </td>
    <td width="33%">
      <strong>Project Presets</strong><br>
      为批处理、代码仓库、研究采集、UI 验证这几类任务提供默认结构偏置，不改变核心 loop 模型。
    </td>
  </tr>
</table>

## Ralph Loop 一眼看懂

<p align="center">
  <img src="./assets/ralph-loop-flow.svg" alt="Ralph Loop flow" width="100%">
</p>

## 仓库结构

```text
harness-engineer-skill/
├── assets/
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

## 包含版本

| 版本 | 路径 | 说明 |
|---|---|---|
| 当前正式版 | [`skills/harness-engineer/`](./skills/harness-engineer/) | 已包含 Ralph Loop preset |
| 历史快照 | [`snapshots/harness-engineer-backup-20260408-161519/`](./snapshots/harness-engineer-backup-20260408-161519/) | 加入 Ralph preset 前的备份版本 |

## 快速开始

### 1. 安装 skill

<details>
<summary><strong>Windows PowerShell</strong></summary>

```powershell
Copy-Item -LiteralPath .\skills\harness-engineer -Destination "$HOME\.codex\skills\harness-engineer" -Recurse -Force
```

</details>

<details>
<summary><strong>macOS / Linux</strong></summary>

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/harness-engineer ~/.codex/skills/harness-engineer
```

</details>

### 2. 显式调用

```text
Use $harness-engineer to clarify requirements and scaffold a robust harness project.
```

典型请求：

- `Use $harness-engineer to design a harness for a batch document-processing pipeline.`
- `Use $harness-engineer to refactor this prompt-only workflow into a recoverable harness.`
- `Use $harness-engineer to scaffold a Ralph Loop project for a multi-pass remediation task.`

## 脚手架脚本

内置辅助脚本：

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
- `--project-preset generic|batch-processing|repo-coding|research-collection|ui-validation`
- `--topology`
- `--runner`
- `--batch-size`
- `--with-features-file`
- `--with-failure-log`
- `--with-archives`

## Skill 会生成什么

### Baseline 模式

- `AGENTS.md`
- `config.yaml`
- `progress.txt`
- `docs/`
- `scripts/`
- validator 占位脚本
- summary 占位文件

### Ralph Loop 模式

- baseline 模式全部内容
- `PROMPT.md`
- `tasks.json`
- `docs/exec-plans/current-batch-plan.md`
- `logs/failure-log.jsonl`
- `archives/`
- Ralph 风格 runner 模板

### Project preset 叠加层

- `generic`
- `batch-processing`
- `repo-coding`
- `research-collection`
- `ui-validation`

可以把它理解成：loop preset 决定“怎么跑”，project preset 决定“这类任务默认长什么样”。

## 理念来源

这个 skill 是一个再蒸馏、再工程化的整合成果，主要来源于：

- OpenAI 的 Harness Engineering 理念
- Anthropic 关于长任务 harness 的文章
- `snarktank/ralph`
- `HKUDS/OpenHarness`
- 本地实践笔记与方法论抽象

它不是上述任一项目的官方下游发布，而是基于这些来源形成的独立 synthesis。

## 核心理念

> 更强的 prompt 有帮助，但更好的 harness 才能长期存活。

这个 skill 默认相信：

- 长任务必须把状态外置
- validator 比“感觉差不多了”更重要
- 拓扑应该尽量小
- 模型变强后，脚手架应该允许被削减，而不是无限膨胀

## Attribution

- 人类项目拥有者与维护者：仓库维护者
- AI 实现与打包协助：OpenAI Codex

当前采用 README 显式署名的方式标注 Codex 参与。如果你后面还想让提交历史也带上类似归属，可以在未来 commit 中加入 co-author trailer，或者使用专门的 bot / 账号身份。

## 已做验证

当前 skill 已通过：

- `quick_validate.py` 对 skill 的基础校验
- 脚手架脚本的 Python 编译检查
- 以下 smoke test：
  - baseline scaffold 生成
  - Ralph Loop scaffold 生成
  - 生成后的 validator 执行
  - 生成后的 runner 执行
  - 当前所有 project preset 的叠加路径

## 项目维护

- 贡献指南：[CONTRIBUTING.md](./CONTRIBUTING.md)
- 路线图：[ROADMAP.md](./ROADMAP.md)
- 发布策略：[RELEASING.md](./RELEASING.md)

## License

MIT，见 [LICENSE](./LICENSE)。
