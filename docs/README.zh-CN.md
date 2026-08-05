# Journal Cover Letter Skill｜投稿信撰写教程

[English](../README.md)

根据稿件材料撰写投稿信，也可以使用“稿件＋专家投稿信”继续训练这个 Skill。

## 从这里开始

| 我想做什么 | 使用哪个工具 | 它会做什么 |
|---|---|---|
| 根据稿件撰写投稿信 | **Journal Cover Letter Skill v3.2** | 读取稿件、核对期刊、撰写投稿信并检查结果 |
| 用专家投稿信改进 Skill | **Cover Letter Skill Trainer v0.2.0** | 比较盲生成的 AI 投稿信与已授权的专家投稿信，把有效思路写入新版 Skill |

### 撰写投稿信

- [下载 Codex Skill](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/v3.2/journal-cover-letter-skill-v3.2.skill)
- [下载 Codex Plugin](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/v3.2/journal-cover-letter-plugin-v3.2.zip)
- [下载供其他 AI 读取的 SKILL.md](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/v3.2/SKILL.md)

### 训练和改进 Skill

- [下载 Trainer Skill](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/trainer-v0.2.0/journal-cover-letter-skill-trainer-v0.2.0.skill)
- [下载 Trainer Plugin](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/trainer-v0.2.0/journal-cover-letter-skill-trainer-plugin-v0.2.0.zip)
- [下载便携版 Trainer SKILL.md](https://github.com/hujizhou35-cmd/journal-cover-letter-tutorial/releases/download/trainer-v0.2.0/SKILL.md)

### 我应该下载哪个文件？

| 文件 | 适合谁 |
|---|---|
| `.skill` | 想在 Codex 中安装一个 Skill |
| Plugin `.zip` | 想安装完整 Codex 插件包 |
| `SKILL.md` | 使用其他能够读取指令文件的 AI |

## 三步生成投稿信

1. 上传手稿，以及已有的 Title Page 或补充材料。
2. 告诉 Skill 目标期刊。如果有旧投稿信，说明允许它参考事实、格式、语气，还是只作为专家比较材料。
3. 确认缺失或冲突的事实。Skill 会查询期刊当前要求、撰写投稿信，并单独提供检查报告。

默认生成英文，也可以要求其他语言。

## 三类文章需要三种写法

| 路线 | 投稿信要回答什么？ |
|---|---|
| **Research** | 研究解决了什么科学问题、发现了什么、为什么值得关注？ |
| **Review** | 把已有证据综合起来以后，我们获得了什么新的理解？ |
| **Bibliometrics** | 文献地图揭示了领域怎样形成、发展、集中、分化、合作或转向？ |

## 为什么文献计量学需要单独一条路线？

文献计量学研究的是论文、引用、关键词、作者、机构和合作网络。它的主要结果是一张“研究领域地图”，不是治疗效果、作用机制，也不是普通的研究结果汇总。

一封有用的文献计量学投稿信要回答：

1. 分析覆盖了怎样的文献？
2. 这张地图揭示了什么以前看不清的结构或变化？
3. 哪些主题、合作关系或研究方向正在变化？
4. 这种变化为什么值得目标期刊的读者关注？
5. 哪些结论不能仅凭发文量、引用量或网络位置得出？

期刊投稿系统可能把文献计量学论文标为 `Review`，也可能标为 `Original Research`。Skill 会保留期刊的正式标签，同时使用 Bibliometrics 自己的写作逻辑。

## 使用专家案例训练 Skill

Trainer 会自动完成原来需要一遍遍手动操作的流程：

```text
当前 Skill
→ 稿件材料
→ 盲生成 AI 投稿信
→ 加入已授权的专家投稿信
→ 比较双方怎样选择和组织信息
→ 提炼可以迁移的思路
→ 修改 Skill
→ 在新的干净对话中重新测试
→ 人工确认后发布
```

Trainer 学习的是专家怎样选择事实、安排顺序和说服编辑，不是照抄专家的句子。专家信也可能使用早期标题、旧数字或不完整声明，因此事实始终以手稿和作者确认为准。

第一次生成时没有看专家信，并不代表整个训练循环都是盲测。专家信揭示后，每一轮候选投稿信都必须在没有接触专家材料的新对话中生成。具体操作见[傻瓜式 Trainer 教程](trainer-guide.zh-CN.md)。

## 我怎样持续改进这个项目

1. 先让当前 Skill 根据稿件生成投稿信。
2. AI 版本封存后，再加入已授权的专家投稿信。
3. 比较双方选择了什么、删除了什么、怎样排序、怎样突出价值。
4. 解释专家选择为什么更有效，而不是复制句子。
5. 把可以用于其他论文的思路写成通用规则。
6. 在新的干净对话中，用同一稿件重新生成。
7. 同时检查被修改的路线和没有修改的路线。
8. 确认改进不只适用于一个案例后再发布。

专家投稿信是用于学习和比较的 benchmark，不是不可质疑的标准。说服力不能覆盖事实准确性和证据边界。真实稿件和专家信不会上传到本仓库。

## 版本是怎样演进的

| 版本 | 比较时发现了什么 | Skill 怎样改变 |
|---|---|---|
| v1.0 | 投稿信首先不能写错题目、数字、作者、声明和期刊要求 | 增加稿件事实表、期刊查询、旧信使用权限和最终检查 |
| v2.0 | Research 和 Review 不能使用同一种写法 | Research 围绕科学发现讲故事；Review 说明证据综合产生的新理解 |
| v2.1 | Review 容易只告诉编辑“综述了什么” | 增加领域诊断、可记忆的新解释、适度宣传和具体读者价值 |
| v2.2 | Research 容易让复杂方法和大量结果遮住真正发现 | 先讲最值得编辑关注的科学发现，再说明方法增加了什么可信度 |
| v2.3 | Review 的结论仍可能宽泛，流程也可能重复询问已经明确的信息 | 使用“过去怎样理解→综合发现什么→判断应怎样改变”；加入资料完整时的快速路径；加强空泛宣传检查 |
| **v3.0** | **文献计量学既不是普通 Research，也不是传统 Review** | **革命性地增加 Bibliometrics 第三路线，并把期刊正式文章标签与投稿信写作逻辑分开** |
| v3.1 | 文献计量学投稿信可能过度抽象，丢掉论文自己的结果 | 强制保留论文特有的领域分类、前沿主题或方向转移，并加入盲法比较流程 |
| **v3.2** | 专家投稿信可能包含旧事实，文献计量学也容易只写排名和关键词 | 稿件事实优先；结合绩效分析与科学知识图谱；具体连接期刊读者；删除投稿系统专属信息 |

Trainer 的变化：

| 版本 | 改进 |
|---|---|
| Trainer v0.1.0 | 建立盲生成、专家比较、提炼规则、修改 Skill 和回归检查的基本循环 |
| Trainer v0.2.0 | 要求每一轮候选稿都使用没有接触专家信的新上下文，并记录实际隔离程度 |

详见[完整迭代记录](evolution.md)和[Trainer 更新记录](trainer-changelog.md)。

## 隐私和使用边界

- 不在本仓库公开真实稿件或真实专家投稿信。
- 所有公开示例均为虚构材料。
- 旧投稿信只能在得到允许后使用。
- 本项目不保证稿件录用。
- 作者仍需最终确认事实、声明和投稿要求。

详见[隐私说明](privacy.md)。

## 参与改进

欢迎使用已经发表的论文和相关投稿信帮助改进项目。请只分享你有权公开的材料，并先删除个人信息、保密内容和未公开投稿信息。详见[贡献指南](../.github/CONTRIBUTING.md)。

## 仓库目录

普通用户可以忽略下面的目录，直接从 Release 下载。

| 目录 | 用途 |
|---|---|
| `skills/` | 当前 Writer 和 Trainer 源码 |
| `docs/` | 中文主页、傻瓜教程、隐私和版本故事 |
| `development/` | 虚构示例、测试和打包工具 |
| `.codex-plugin/` | Writer Plugin 配置 |
| `.github/` | 自动检查和贡献入口 |

## 作者、引用与许可

作者：**Jizhou Hu，中国医科大学**。

项目使用 [MIT License](../LICENSE)，引用信息见 [CITATION.cff](../CITATION.cff)。
