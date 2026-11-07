<div align="center">

# OpenAndy

**把一个人的经历、判断和代价，开源成人和 AI 都能读取的知识库。**

不是成功学，不是简历，不是又一本赚钱手册。

**从湖北农村到腾讯、百度、大模型公司副总裁，再到 2026 年把这些方法免费放到 GitHub——包括走错的路和付过的代价。**

[![License: MIT](https://img.shields.io/badge/代码-MIT-111827?style=flat-square)](LICENSE)
[![Content: CC BY-NC 4.0](https://img.shields.io/badge/内容-CC%20BY--NC%204.0-111827?style=flat-square)](LICENSE-CONTENT)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square)
![Dependencies](https://img.shields.io/badge/运行时依赖-0-2E7D32?style=flat-square)

</div>

---

**[📖 时间线与代价](STORY.md)** ｜ **[🧭 九条认知公理](PRINCIPLES.md)** ｜ **[✅ 可复用决策清单](DECISIONS.md)** ｜ **[📚 方法手册](playbook/)** ｜ **[🔍 事实来源与口径](SOURCES.md)** ｜ **[🤖 给 AI 的读取规则](AGENTS.md)** ｜ **[English](README_EN.md)**

## 这个仓库解决什么问题

2026 年 11 月，我写过一篇文章，讲自己从一个湖北农村孩子走到副总裁，花十几年才弄懂赚钱。文章发出去以后，最常被问的不是"怎么做到的"，而是"你说的那些坑，具体是怎么发生的"。

文章是叙事，不好检索，也不好复用。所以有了这个仓库：**把那篇文章和我长期使用的思考规则，拆成有出处、可检索、能被 AI 直接当上下文读取的结构化内容。**

它直接回答四个问题：

| 你的问题 | 直接看哪里 |
|---|---|
| 这个人到底经历了什么，哪些是事实、哪些是他的判断 | [时间线](STORY.md) · [事实口径](SOURCES.md) |
| 他做决定时实际用的是什么规则 | [九条认知公理](PRINCIPLES.md) · [决策清单](DECISIONS.md) |
| 赚钱这件事，他自己是怎么分层的 | [赚钱的四层](playbook/01-money-layers.md) |
| 我想让 AI 用这些经验，怎么接 | [给 AI 的规则](AGENTS.md) · [`llms.txt`](llms.txt) · [`llms-full.txt`](llms-full.txt) |

> **读完能拿走的东西**：一条带代价标注的时间线、9 条可复用的思考规则、5 份方法手册、一份决策自检清单，以及一套人和 AI 都能读的索引。所有数字均来自作者公开自述，未经独立审计；不提供收益、投资、医疗或法律建议。

## 这个仓库不是什么

按「先删非必需项」的原则，以下内容明确不做，避免它变成又一个内容农场：

1. **不是成功学。** [时间线](STORY.md) 里写进了开倒的店、白内障手术、脂肪肝，以及"我还没有成功"。
2. **不是课程或付费引流页。** 全部内容免费、无需登录、无需加微信，没有转化漏斗。
3. **不是个人简历。** 履历只保留已公开发表的自述，不补未公开的公司名、客户名、合同金额与联系方式。
4. **不是 AI 分身或聊天机器人。** 本仓库不调用任何模型、不上传数据。[AGENTS.md](AGENTS.md) 只规定 AI 该怎样引用这些材料、以及什么时候必须说"不知道"。
5. **不承诺收益。** 文中的 30 万月流水、1000+ 咨询客户、6 万粉丝、40 万年产值，都是作者自述的历史记录，不是可复制的结果，也不是预测。

## 30 秒上手

零依赖，只需 Python 3.9+。不需要安装、不需要 API Key、不联网。

```bash
git clone https://github.com/AIPMAndy/OpenAndy.git
cd OpenAndy

python3 openandy.py list              # 列出全部条目
python3 openandy.py ask 副业          # 按关键词检索
python3 openandy.py ask 身体 时间      # 多个词是"或"关系，按命中权重排序
python3 openandy.py show money-layers # 输出某一篇全文
python3 openandy.py check             # 校验索引、链接、口径与敏感信息
python3 openandy.py build             # 重新生成 llms-full.txt
```

想让人读，直接看 [`index.html`](index.html)（单文件静态页，无构建、无外部依赖）；想让 AI 读，把 [`llms-full.txt`](llms-full.txt) 塞进上下文即可。

## 事实与口径（重要）

这个仓库最容易被误用的地方，是把"一个人的经验"当成"普遍规律"。为此做三条硬约束：

- **分级标注。** `[公开自述]` = 作者本人公开发表、未经独立审计；`[工作原则]` = 作者长期使用的思考规则；`[本仓库整理]` = 由前两者推导的清单或方法，不是事实。完整定义见 [SOURCES.md](SOURCES.md)。
- **口径不合并。** 关于入职年份、任职区间，不同公开材料存在差异。本仓库**只采用 2026-11-07 那篇文章的自述口径**，不推断、不填平、不混入其他材料。
- **隐私不进仓库。** 不写客户姓名、具体雇主、家庭成员身份信息、电话与私人联系方式；贡献者也不得提交。这条由 `openandy.py check` 做基础扫描。

不同材料的时间口径差异、以及为什么这样处理，见 [SOURCES.md](SOURCES.md)。

## 仓库结构

```
OpenAndy/
├── README.md / README_EN.md     入口
├── STORY.md                     时间线：事实 / 当时判断 / 代价 / 可迁移的一条
├── PRINCIPLES.md                九条认知公理 + 第一性原理工程方法
├── DECISIONS.md                 可复用决策清单（把经历变成动作）
├── SOURCES.md                   事实来源、分级、口径冲突与隐私边界
├── AGENTS.md                    给 AI Agent 的读取与引用规则
├── playbook/                    5 份方法手册
├── data/index.json              唯一索引（只存元数据，不复制正文）
├── openandy.py                  零依赖 CLI：list / ask / show / check / build
├── tests/test_openandy.py       对行为做实质断言的测试
├── llms.txt / llms-full.txt     给 AI 的索引与全量文本
├── index.html                   单文件阅读页（不是独立 Web 项目）
└── CONTRIBUTING.md              贡献规则
```

**单一真源**：Markdown 是正文唯一来源，`data/index.json` 只存 id / 标题 / 路径 / 标签 / 摘要 / 来源，不复制内容。`check` 会验证两者是否漂移。

## 参与贡献

欢迎补充**有出处**的勘误、把某条方法用到自己场景后的复盘、以及翻译。不接受没有来源的成功案例、收益承诺和任何客户隐私。规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 关于作者

**AI 酋长 Andy**（GitHub / X / 微信：`AIPMAndy`），前腾讯、百度 AI 产品负责人，曾任大模型公司副总裁，现为 AI 创业者。把实战经验开源成免费的中文手册与工具，个人官网 [metaver.vip](https://metaver.vip/)，全部开源项目见 [GitHub](https://github.com/AIPMAndy) 与 [总目录](https://aipmandy.github.io/)。

愿景：**让更多人类通过 AI 实现财富自由和精神自由。** 这句话很大，但它可以从一个人第一次靠自己的能力赚到 400 元开始。

## 许可与边界

- 代码（CLI、测试、页面）：[MIT](LICENSE)
- 正文与文档：[CC BY-NC 4.0](LICENSE-CONTENT)（署名、非商业）
- 引用请标注来源与链接；转载原文、商用授权需另行联系。
- 内容基于作者截至 **2026-11-07** 的公开自述，不构成职业、投资、财税、医疗或法律建议。个人情况不同，重要决定请自行核验。

<sub>维护时间 2026-11-07 · v0.1.0 · 本仓库内容不承诺收益，所有数字均为历史自述而非业绩保证。</sub>
