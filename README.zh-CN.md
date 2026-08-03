# Journal Cover Letter Skill v2.0

[English](README.md)

一个根据手稿文件撰写学术期刊 Cover Letter 的开源 Skill 和 Codex Plugin。

v2.0 保留 v1.0 的事实核对和期刊检索，但改变了不同文章类型面向编辑时的表达方式。

> **状态：**旧版。新用户通常应选择 v2.1。

## v2.0 的关键想法

Original Research 和 Review 不应该使用同一套写作逻辑。

- **Original Research 往往需要讲故事。** Cover Letter 应从研究问题推进到设计上的不同、核心发现及其意义。
- **Review 不必模仿这条故事线。** 它的任务是说明已有证据被放在一起并重新组织后，出现了什么新的理解。

这个想法来自对 AI 版本和专家版本的比较。AI 版本通常谨慎但较平，专家版本更会取舍。v2.0 因此增强了语言的吸引力，同时继续检查因果、机制、亚组和临床意义是否越过证据边界。

## 它怎样工作

1. 阅读手稿文件和旧版 Cover Letter。
2. 向作者展示提取的事实和主要卖点。
3. 询问旧信可以怎样使用。
4. 得到作者确认后，查询目标期刊当前的官方要求。
5. 根据文章类型选择 Research 或 Review 的写法。
6. 在有限轮次内撰写、检查和修改信件。
7. 交付正文、可选 DOCX 和仍需作者确认的事项。

## 快速开始

> 请阅读这些手稿文件，帮我为 [期刊名称] 撰写 Cover Letter。先展示你提取的事实和主要卖点，再根据文章属于 Original Research 还是 Review 选择合适的写法。

## 安装

从对应 GitHub Release 下载 v2.0 的独立 Skill 包或 Plugin 包。不要与其他版本的文件混用。

## 隐私与使用边界

仓库示例全部为虚构内容。开发中使用过的真实手稿、Cover Letter、期刊信息和原始对话不会公开。

本项目不保证稿件被录用。作者仍需对事实、声明、伦理、利益冲突、期刊政策和最终投稿负责。

## 参与贡献

只分享你有权公开的已发表材料或虚构材料，并提前移除个人信息、保密信息和未公开投稿信息。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 作者与许可

作者：**Jizhou Hu（China Medical University）**。项目采用 [MIT License](LICENSE)，引用信息见 [CITATION.cff](CITATION.cff)。
