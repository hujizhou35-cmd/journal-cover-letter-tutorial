# Journal Cover Letter Skill

[English](README.md) · [迭代过程](docs/evolution.md) · [架构](docs/architecture.md) · [隐私](PRIVACY.md)

一个开源的 Codex Skill 与 Plugin：把手稿证据转化为面向编辑决策的学术期刊 Cover Letter。项目适用于通用学术投稿，并优先覆盖生物医学与生命科学场景。

> **当前推荐：**v2.1（清单版本 `2.1.0`）。v1.0 与 v2.0 作为 Legacy Releases 保留，用于复现和版本比较。

## 它与模板生成器有什么不同

模板只能排列段落，不能判断手稿事实是否可靠、结果能否支持因果或机制表述、编辑应该记住哪条故事，也不能判断稿件如何进入目标期刊正在进行的学术对话。

本项目把 Cover Letter 视为一份**编辑初筛决策简报**：

1. 识别手稿、Title Page、补充材料和既往 Cover Letter；
2. 建立带 `verified`、`conflict`、`missing` 状态的可追溯事实表；
3. 确认文章类型、投稿分支、目标期刊、声明和使用权限；
4. 检索目标期刊当前官方要求与近期相关学术对话；
5. 选择 Research 故事或 Review 的 editorial thesis；
6. 在证据边界内进行受控说服；
7. 执行有界审计与自适应长度循环；
8. 交付正文、可选 DOCX、审计、未解决事项和就绪状态。

默认输出英文，用户也可指定其他语言。

## 两条编辑路线

### Original Research

> 重要问题 → 知识缺口 → 设计优势 → 核心发现 → 可辩护意义 → 期刊对话

该路线围绕一条科学发现链讲故事。方法用于证明发现可信，而不是成为清单；同时检查因果、机制、亚组、代理指标和临床转化越界。

### Review 与 Synthesis

> 领域误读或未解决张力 → 综合干预 → editorial thesis → 改变的决策或研究议程 → 期刊对话 → 校准边界

该路线强调综述如何改变领域对既有证据的理解。对于描述性或范围综述，系统不会强行制造争议。

## 版本演进

| 公开版本 | 清单版本 | 状态 | 主要设计变化 |
|---|---:|---|---|
| v1.0 | `1.0.0` | Legacy | Fact Sheet、期刊检索、既往信权限、统一 `1-5-1-1` 迭代与审计 |
| v2.0 | `2.0.0` | Legacy | Research/Review 分流、科学故事、说服力校准、有界状态循环 |
| v2.1 | `2.1.0` | 推荐稳定版 | Review 领域诊断、`editorial_thesis`、受控营销、期刊对话、自适应长度 |

项目会学习人类撰写 Cover Letter 的选择、节奏和推广判断，但不会把它当成不可质疑的范本：**匿名专家信是 benchmark，而非 gold standard**。任何事实和论断仍需通过手稿级核查。详见[完整迭代说明](docs/evolution.md)。

## 安装

每个 Release 均提供：

- `journal-cover-letter-skill-vX.Y.skill`：独立 Skill 包；
- `journal-cover-letter-plugin-vX.Y.zip`：完整 Plugin 包；
- `SHA256SUMS.txt`：完整性校验值。

若按仓库方式安装独立 Skill，可将解压后的目录放在项目级：

```text
.agents/skills/journal-cover-letter-skill/
```

或放在用户级 Agent Skills 目录。Plugin 包可解压后，在支持本地 Plugin 的 Codex 环境中安装或导入。文件布局遵循当前 [OpenAI Skill](https://developers.openai.com/codex/build-skills) 与 [Plugin](https://developers.openai.com/plugins/build/plugins) 文档。

请选择同一 Release 的组件，不要将 v1.0 Skill 与 v2.1 Plugin 清单混用。

## 调用示例

上传相关文件后可以这样请求：

> 请分析这些文件，为 Original Research 投稿准备 Cover Letter。先停在 Fact Sheet 和故事候选项，得到我的确认后再检索期刊。

或者：

> 这是一篇范围综述。只有证据确实支持时才提出 editorial thesis；否则请诚实呈现描述性地图与研究议程，不要制造争议。

输出包括：

- 最终 Cover Letter 正文；
- 可选 DOCX；
- 事实、期刊、权限、故事/命题和论断强度审计；
- 仍需作者确认的事项；
- `SUBMISSION_READY`、`NEEDS_AUTHOR_CONFIRMATION`、`NEEDS_JOURNAL_VERIFICATION` 或 `BEST_SAFE_DRAFT_WITH_UNRESOLVED_ITEMS` 中的一种状态。

## 仓库结构

```text
.codex-plugin/plugin.json            Plugin 清单
skills/journal-cover-letter-skill/   可独立安装的 Skill
docs/specs/                           脱敏后的版本规格
examples/synthetic/                  仅包含虚构案例
evals/                               行为评测与人工复核材料
tests/                               确定性回归测试
scripts/                             结构、隐私和发布工具
```

## 合成示例与评测

公开测试覆盖：包含代理指标/中介/亚组风险的原始研究；可形成命题的系统综述；只支持描述性映射的范围综述；既往信权限；事实冲突或声明缺失；无法访问期刊官网；DOCX 生成。详见 [examples/synthetic](examples/synthetic/README.md)、[evals/evals.json](evals/evals.json) 与[静态人工复核页面](evals/review.html)。

仓库不包含任何真实手稿、真实 Cover Letter、活跃投稿期刊、编辑身份或未公开投稿细节。

## 局限

- 项目不保证录用。
- 期刊页面和政策会变化；必须核验当前官方信息才能标记就绪。
- 科学解释仍属于模型辅助判断，必须由作者复核。
- 作者对事实、声明、伦理、利益冲突和最终投稿合规负责。
- DOCX 可以继承版式，但不得携带隐藏文字、修订、元数据或旧期刊信息。

## 路线图

- 在不削弱共同证据门槛的前提下加入更多学科分支；
- 扩展多语言输出评测；
- 增加更多已获公开授权的 benchmark 配对；
- 完善可复现的人工版本比较；
- 稳定公开使用后再考虑通用插件目录提交；当前不提交到通用目录。

## 参与贡献

欢迎大家使用已发表的文章和相关 Cover Letter 一起对本项目进行升级。请仅提交你有权公开分享的材料，并在贡献前移除个人、保密和未公开投稿信息。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 作者、引用与许可

作者：**Jizhou Hu（China Medical University）**。引用信息见 [CITATION.cff](CITATION.cff)，项目采用 [MIT License](LICENSE)。
