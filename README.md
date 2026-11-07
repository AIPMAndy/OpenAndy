<div align="center">

# OpenAndy

**把我自己开源。**

经历、判断、错和代价，都在这里。人能看，AI 也能读。

[![License: MIT](https://img.shields.io/badge/代码-MIT-111827?style=flat-square)](LICENSE)
[![Content: CC BY-NC 4.0](https://img.shields.io/badge/内容-CC%20BY--NC%204.0-111827?style=flat-square)](LICENSE-CONTENT)
![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square)
![Dependencies](https://img.shields.io/badge/运行时依赖-0-2E7D32?style=flat-square)

</div>

---

2026 年 1 月 12 日，北京零下 15 度。早上 6 点多，我出门坐地铁去北医三院，做眼睛手术。

躺在手术台上，我以为自己不紧张。但眼睛不会骗人。换上人工晶体，手术结束，我需要别人扶着才能回去休息。

那天我想起自己这些年走过的路：湖北农村、辣椒拌饭、绿皮火车、腾讯、百度、副总裁。也想起手术前写在日记里的那句话——**"我燃烧自己努力工作，忙到忘记自己。"**

这个仓库，是我把自己开源的地方。

不是课程，不是简历，也不是"成功人士的十条建议"。我开倒过店，创业交过学费，2024 年身体出问题，2026 年上了手术台；我也确实从零做过亿级业务线、带过 50 人左右的团队、六年攒下 1000 多位有完整记录的咨询客户、帮父母把农产品做到一年 40 万产值。**两边都是真的，我都写进来。**

## 这里有什么

| 想看什么 | 直接看 | 里面是什么 |
|---|---|---|
| 我是谁、怎么跟我合作 | [ME.md](ME.md) | 一句话履历、我现在靠什么吃饭、我的偏好和偏见、我不做的事 |
| 我这一路怎么走的 | [STORY.md](STORY.md) | 11 个阶段，每段写清得到什么、付了什么 |
| 我怎么做判断 | [PRINCIPLES.md](PRINCIPLES.md) | 九条认知公理，加上质疑需求→删除→简化→加速→自动化的顺序 |
| 遇到具体问题怎么定 | [DECISIONS.md](DECISIONS.md) | 七组能直接打勾的清单：接不接这个活、要不要做副业、流水还是利润 |
| 赚钱这件事我怎么分层 | [playbook/01](playbook/01-money-layers.md) | 时间→经验→商业结果→内容获客，四层各自的代价 |
| 我怎么赚到第一笔自己的钱 | [playbook/02](playbook/02-first-client.md) | 六年、1000+ 客户，从一次改简历到长期信任 |
| 我怎么帮父母做生意 | [playbook/03](playbook/03-ai-for-small-business.md) | 免费工具、不到 1 万粉、一年 40 万产值 |
| 我付了什么代价 | [playbook/04](playbook/04-what-it-cost.md) | 眼睛、时间所有权，哪些钱不值得赚 |
| 我为什么免费 | [playbook/05](playbook/05-why-open.md) | 小时候没资源，所以少让人花几千块、少走几个月 |
| 这些事实从哪来、哪些对不上 | [SOURCES.md](SOURCES.md) | 来源分级、数字定语、口径冲突、隐私边界 |
| 让 AI 读、让 AI 引用 | [AGENTS.md](AGENTS.md) · [llms.txt](llms.txt) | 引用规则、索引、全量文本 |

## 为什么开源

我小时候没有多少资源，很多东西只能靠自己一点一点研究。如果今天一个普通人，能通过我公开的一份文档、一个工具，少花几千块钱、少走几个月弯路，这件事就值得做。

当然，我还要赚钱。我有家庭，有孩子，有公司要经营。免费的是这些文档和工具，收费的是要落到你业务里的服务。这两件事不冲突。

## 30 秒用起来

零依赖，不安装、不联网、不要 API Key。脚本只做检索和一致性检查，不生成建议。

```bash
git clone https://github.com/AIPMAndy/OpenAndy.git
cd OpenAndy

python3 openandy.py list                # 10 个条目
python3 openandy.py ask 副业            # 关键词检索
python3 openandy.py show what-it-cost   # 输出某篇全文
python3 openandy.py check               # 查索引、链接、来源、隐私、构建产物
python3 openandy.py build               # 重新生成 llms-full.txt
```

想让人读，打开 [`index.html`](index.html)；想让 AI 读，先给 [`llms.txt`](llms.txt) 和 [`AGENTS.md`](AGENTS.md)，再按需加载 [`llms-full.txt`](llms-full.txt)。

## 事实与边界

这段请务必看，因为它决定你该怎么用这里的东西。

- **数字都是我自己说的，没审计。** 40 万是**产值**不是利润；30 万是**月流水**不是利润；1000+ 是**有完整文档记录的咨询客户数**，不是 Offer 数；6 万多是全网粉丝合计，没分平台核验。
- **年份只按 2026-11-07 那篇文章算。** 另外一些履历材料的年份对不上，我不合并、不推断、不取中间值。对不上就说对不上。
- **客户、公司、金额、家人信息不写。** 能讲的是方法，不是别人的隐私。
- **不给收益承诺，不做医疗、投资、职业建议。** 我的路径只有一条，样本量是 1，照着做不保证任何结果。
- **相关不等于因果。** 我做了什么、后来发生了什么，不等于前者导致后者。文章里那些转折，我尽量写清哪些是我当时的判断，哪些是事后归因。

## 关于我

AI 酋长 Andy（GitHub / X / 微信：`AIPMAndy`）。前腾讯、百度 AI 产品负责人，做过大模型公司副总裁，现在自己干：面向企业做 AI + IP 获客，面向个人做高管 AI 陪跑、求职陪跑、副业陪跑。

个人官网 [metaver.vip](https://metaver.vip/)，全部开源项目在 [GitHub](https://github.com/AIPMAndy) 和[总目录](https://aipmandy.github.io/)。

我的愿景写出来很大：**让更多人类通过 AI 实现财富自由和精神自由。** 但它可以从一个人第一次靠自己的能力赚到 400 元开始。

## 许可

代码 [MIT](LICENSE)，内容 [CC BY-NC 4.0](LICENSE-CONTENT)。引用请附来源链接，保留事实分级标记；商用授权另谈。

<sub>2026-11-07 · v0.1.0 · 更新记录见 [CHANGELOG.md](CHANGELOG.md)</sub>
