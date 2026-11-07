# OpenAndy

**An open, machine-readable knowledge base of one person's experience, judgement, and the price paid for it.**

Built from a 2026-11-07 essay by AI 酋长 Andy (GitHub / X: [@AIPMAndy](https://github.com/AIPMAndy)): from a rural village in Hubei to AI product roles at Tencent and Baidu, to VP at a large-model company, to publishing the methods for free on GitHub.

## What this is

- A timeline where **every milestone states the cost**, not just the outcome: failed shops, cataract surgery, fatty liver, and "I have not succeeded; I just have more choices than I did as a child." → [STORY.md](STORY.md)
- **Nine axioms** the author actually uses to reason, plus a first-principles engineering method (question the requirement → delete → simplify → speed up → automate last). → [PRINCIPLES.md](PRINCIPLES.md)
- **Reusable checklists** that turn experience into decisions. → [DECISIONS.md](DECISIONS.md)
- **Five playbooks**: four layers of earning, the first paying client, AI for a small family business, what it cost, why open source. → [playbook/](playbook/)
- A **zero-dependency index** for humans and AI: [`data/index.json`](data/index.json), [`llms.txt`](llms.txt), [`llms-full.txt`](llms-full.txt), and [AGENTS.md](AGENTS.md), which tells an AI when it must answer "I don't know".

## What this is not

Not a success story, not a résumé, not a course, not a lead-gen funnel, not a chatbot. It calls no model, uploads nothing, requires no API key, and promises no income. All figures (¥300k monthly revenue at a student business, 1,000+ documented coaching clients, 60k followers, ¥400k annual revenue for a family farm business) are **the author's own public claims, not independently audited results**.

## Quick start

```bash
git clone https://github.com/AIPMAndy/OpenAndy.git
cd OpenAndy
python3 openandy.py list
python3 openandy.py ask 副业
python3 openandy.py show money-layers
python3 openandy.py check
```

Requires Python 3.9+, no third-party packages, no network access.

## Evidence and scope

Every claim is tagged `[公开自述]` (public self-account, unaudited), `[工作原则]` (the author's working rules), or `[本仓库整理]` (derived checklists, not facts). Where other materials give different employment years, this repository uses **only the 2026-11-07 essay's dating** and does not reconcile or infer. Customer names, employers, contract values, family identity details and private contact information are excluded by design. See [SOURCES.md](SOURCES.md).

## Author

AI 酋长 Andy — former AI product lead at Tencent and Baidu, former VP at a large-model company, now an AI entrepreneur. Publishes free Chinese handbooks and tools: [metaver.vip](https://metaver.vip/) · [all projects](https://aipmandy.github.io/) · WeChat `AIPMAndy`.

Vision: *let more people reach financial and mental freedom through AI* — starting with one person earning their first ¥400 on their own ability.

## License

Code: [MIT](LICENSE). Content: [CC BY-NC 4.0](LICENSE-CONTENT). Not career, investment, tax, medical or legal advice. Maintained 2026-11-07.
