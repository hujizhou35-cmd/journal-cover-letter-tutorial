# Journal Cover Letter Skill｜投稿信撰写教程

[English](../README.md) · [下载最新版](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest) · [隐私说明](privacy.md)

上传手稿，告诉 AI 目标期刊，这个 Skill 会找出论文最值得编辑关注的内容，核对事实，并生成一封有针对性的投稿信。

**当前推荐版本：v2.2**

## 下载

- [Codex Skill（.skill）](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest/download/journal-cover-letter-skill-v2.2.skill)
- [Codex Plugin（.zip）](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest/download/journal-cover-letter-plugin-v2.2.zip)
- [供其他 AI 使用的完整 SKILL.md](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/latest/download/SKILL.md)

| 选择这个文件 | 适合什么情况 |
|---|---|
| `.skill` | 在 Codex 或支持 Agent Skills 的工具中安装独立 Skill |
| Plugin `.zip` | 安装完整的 Codex Plugin |
| `SKILL.md` | 把完整写作和判断流程交给其他 AI 阅读 |

单独的 `SKILL.md` 已包含完整写作逻辑；自动生成 DOCX 和脚本检查仍需要 Skill 或 Plugin 安装包。

## 三步开始

1. 从上面选择一个文件下载。
2. 上传手稿、Title Page 及希望 AI 使用的相关材料。
3. 告诉 AI 目标期刊，并让它撰写 Cover Letter。

示例：

> 请阅读这些手稿文件，帮我为［期刊名称］撰写 Cover Letter。先展示你提取的事实和主要亮点，得到我的确认后，再查询期刊并撰写最终版本。

如果提供旧版投稿信，请说明它可以用于事实核对、版式、语气、措辞，还是专家版本比较。Skill 不会自行假定权限。

## 它会做什么

1. 核对手稿事实，标出冲突和缺失信息。
2. 与你确认文章类型、主要亮点和旧投稿信的使用权限。
3. 查询目标期刊当前的官方要求。
4. 根据文章类型选择合适的写法。
5. 检查论断、声明、期刊信息和未删除的占位符。
6. 交付最终正文、可选 DOCX、简短检查结果和仍需确认的事项。

如果事实冲突、必要声明缺失或期刊要求无法核实，它不会把投稿信标记为可以直接提交。

## Research 和 Review 需要不同的写法

**Original Research** 通常需要讲清一条科学故事：问题为什么重要、现有研究不能解决什么、本研究发现了什么，以及这个发现改变了什么。

**Review 或 Synthesis** 使用另一套逻辑：说明把证据放在一起、重新组织或重新解释后，领域获得了什么新认识。描述性综述不会被强行包装成争议性发现。

## 我怎样持续改进这个 Skill

> 当前版本 Skill → 私下提供稿件材料 → 生成 AI 投稿信 → 加入专家撰写的投稿信 → 比较两种写法 → 提炼专家的思考方式 → 修改 Skill → 用同一材料重新测试 → 发布新版本

实际过程是：

1. 先让当前版本根据稿件生成一封投稿信。
2. 再提供一封有经验的学术专家实际撰写的投稿信。
3. 比较双方选择了什么、删掉了什么、强调了什么，以及怎样安排顺序。
4. 分析专家的选择为什么可能帮助编辑更快判断，但不直接照抄句子。
5. 把能够用于其他论文的经验写成通用规则。
6. 使用同一份材料重新生成，再次比较。
7. 重复“生成—比较—提炼—修改—验证”，改进稳定后再发布新版本。

专家投稿信是**比较基准，不是标准答案**。所有事实和论断仍然必须回到手稿核对。迭代中使用的私人手稿和真实投稿信不会上传到公开仓库。

## 版本是怎样演进的

| 版本 | 比较后发现的问题 | Skill 的改变 |
|---|---|---|
| v1.0 | 投稿信再有说服力，事实发生漂移仍然不安全 | 加入事实核对、期刊查询、旧信权限和最终检查 |
| v2.0 | Research 和 Review 不能使用同一种写法 | Research 围绕科学发现讲故事；Review 说明综合证据后获得了什么新理解 |
| v2.1 | Review 不能只说“我们综述了什么” | 加入领域诊断、新解释、适度推广和期刊学术对话 |
| v2.2 | Research 中的复杂方法可能遮住真正的科学发现 | 先写现象和发现，把方法转化为可信能力，删除不会改变编辑判断的细节 |

查看简短的[完整迭代说明](evolution.zh-CN.md)。

## 隐私和使用边界

- 真实手稿、投稿信、期刊、编辑和原始对话不会公开。
- 公开示例全部为虚构内容。
- 项目不能保证稿件被录用。
- 期刊政策可能变化，每次投稿都应重新核实。
- 作者仍需对事实、声明、伦理、利益冲突和最终投稿负责。

详见[隐私说明](privacy.md)。

## 参与改进

欢迎使用已经发表的文章和相关 Cover Letter 帮助改进本项目。请只分享你有权公开的材料，并提前移除个人信息、保密信息和未公开投稿信息。详见[贡献说明](../.github/CONTRIBUTING.md)。

## 仓库目录

普通使用者不需要理解技术目录，直接从 Release 下载即可。

| 目录 | 用途 |
|---|---|
| `skills/` | 当前 v2.2 Skill 源码 |
| `docs/` | 中文主页、迭代过程、隐私和更新记录 |
| `development/` | 虚构示例、测试、评估结果和打包工具 |
| `.codex-plugin/` | Codex Plugin 配置 |
| `.github/` | 自动检查和贡献入口 |

## 作者、引用与许可

作者：**Jizhou Hu（China Medical University）**。引用信息见 [CITATION.cff](../CITATION.cff)，项目采用 [MIT License](../LICENSE)。
