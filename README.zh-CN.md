# Journal Cover Letter Skill

[English](README.md)

一个开源的 Codex Skill 与 Plugin：把手稿证据转化为面向编辑决策的学术期刊 Cover Letter。项目优先覆盖生物医学与生命科学场景，同时保持跨学科通用性。

它并不是套模板生成器。项目会先建立可追溯的事实表，确认既往 Cover Letter 的使用权限，查询目标期刊最新官方要求，选择贡献主线，并在生成正文或 DOCX 前审计事实与论断强度。

## 工作流程

1. 识别手稿、Title Page、补充材料和既往 Cover Letter。
2. 建立带 `verified/conflict/missing` 状态的事实表。
3. 确认文章类型、投稿分支、目标期刊、声明及既往信使用权限。
4. 经作者确认后，查询目标期刊当前官方要求与读者定位。
5. 将手稿转换为一个中心问题和分层贡献。
6. 执行有界的写作、审计与压缩循环。
7. 交付正文、可选 DOCX、审计报告、未解决事项与就绪状态。

## v1.0

本版本建立以事实为基础的 `1-5-1-1` 流程：一个中心问题、最多五项分层贡献、一项带边界的意义，以及一项面向期刊读者的契合主张。

## 安装

可从对应 GitHub Release 安装独立 Skill 包或 Plugin 包。仓库根目录本身也符合 Plugin 结构，Skill 位于 `skills/journal-cover-letter-skill/`。

调用示例：

> 请分析这些手稿文件，并协助我为学术期刊投稿准备 Cover Letter。

默认输出英文；用户可明确要求其他语言。

## 隐私

请勿提交保密手稿、未公开投稿材料、可识别通信或真实的期刊检索记录。仓库示例均为合成材料。详见 [PRIVACY.md](PRIVACY.md)。

## 局限

本项目不保证稿件录用，也不能替代作者对事实、声明、伦理、利益冲突、期刊政策和投稿合规性的最终核查。

## 参与贡献

欢迎大家使用已发表的文章和相关 Cover Letter 一起对本项目进行升级。请仅提交你有权公开分享的材料，并在贡献前移除个人、保密和未公开投稿信息。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 作者与许可

作者：**Jizhou Hu（China Medical University）**。项目采用 [MIT License](LICENSE)，引用信息见 [CITATION.cff](CITATION.cff)。
