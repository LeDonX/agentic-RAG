# 学习进度追踪

> 本文件是学习进度的**唯一事实源**。每次会话开始时由导师（AI）读取，结束时由导师更新。
> 你在不同会话里学习时，只要让导师先读本文件，就能自动续接进度。
> 计划详情见 `LEARNING_PLAN.md`。
> 知识点速记 + 错题本见 `NOTES.md`（每日收尾追加）。

## 项目信息
- 项目：企业级知识库问答 Agentic RAG（产品形态对标 RAGFlow，生产化对标 bisheng，编排用 LangGraph）
- 学员：Java 工程师（6 年）转 Python AI 应用工程师
- 周期：6 周 / 42 天，每天 2-3 小时
- 里程碑：M1 = Week 1–4（可运行版）；M2 = Week 5–6（生产化版）
- 开始日期：2026-10-10

## 当前进度
- **当前 Day：3（进行中）**
- **当前里程碑：M1（可运行版）**
- 上次会话：Day 3 部分完成 —— Block A（list / tuple / for 语法）**验收通过**；Block B（dict / set）**已讲未练**；Block C（推导式 / 切片 / 解包）**未讲**
- **恢复点（新机器从这里起）**：Day 3 → Block B 动手任务 `TODO 4–7`（写进 `learning/day03_containers.py`）→ Block C → 当日验收
- 下一步：完成 Day 3 剩余部分并验收 → Day 4（控制流与函数）

## 环境信息
- Python 版本：3.12.15（uv 托管，项目锁定 3.12）— ⚠️ 见下方待确认项
- 包管理器：uv 0.12.24
- 虚拟环境：项目根目录 `.venv`
- Ollama 模型：未安装（Day 8 处理）
- 关键依赖：暂无（骨架 `src/agentic_rag/`，入口点 `agentic-rag`）

> ⚠️ **环境待确认（2026-10-13）**：当前机器上 `uv` 不在 PATH、项目根**没有** `.venv`，`python` 实际指向系统 **Python 3.11.5**——与上表记录（uv 0.12.24 / 3.12.15）不符。
> 换机器续学前请先跑 `uv --version` 与 `python --version` 确认，并把结果回写本节。

## 配套文件
- `LEARNING_PLAN.md`：6 周 42 天计划、验收标准
- `WORKFLOW.md`：每日协作 SOP
- `NOTES.md`：知识点速记 + 错题本（追加式，每日收尾更新；每周复盘日抽题复习）

## 进度总表

### M1 — 可运行版（Week 1–4）

**Week 1 — Python 快速上手**

| Day | 主题 | 状态 | 产出物 | 备注 |
|---|---|---|---|---|
| 1 | 环境搭建（uv）、REPL、`__main__`、Python vs Java | 已完成 | `learning/day01_demo.py`；骨架 `src/agentic_rag/` | 验收通过 |
| 2 | 基础语法（动态类型 / f-string / None） | 已完成 | `learning/day02_calculator.py` | 4 组用例通过；已纠正 `/` 与 `//` |
| 3 | 容器（list/dict/set、推导式、切片、解包） | 进行中 | `learning/day03_containers.py`（TODO 1–3 已通过，TODO 4–7 待做） | Block A 验收通过；Block B 已讲未练；Block C 未讲 |
| 4 | 控制流与函数（默认参数、`*args/**kwargs`、lambda） | 未开始 | | |
| 5 | 面向对象（class、`self`、`@dataclass`、魔术方法） | 未开始 | | |
| 6 | 模块/包/依赖管理/类型注解/异常 | 未开始 | | |
| 7 | 复盘：CLI 小工具 + pytest 入门 | 未开始 | | |

**Week 2 — LLM & RAG 基础 + 最小可用 RAG**

| Day | 主题 | 状态 | 产出物 | 备注 |
|---|---|---|---|---|
| 8 | LLM 基础 + Ollama 安装拉模型 | 未开始 | | |
| 9 | 直连 Ollama API（messages 结构） | 未开始 | | |
| 10 | LangChain 入门（ChatModel / PromptTemplate / LCEL） | 未开始 | | |
| 11 | 文档加载与切分（Splitter） | 未开始 | | |
| 12 | Embedding + Chroma（向量库） | 未开始 | | |
| 13 | 最小 RAG 链（检索 → 生成 + 引用） | 未开始 | | |
| 14 | 复盘：多轮记忆 + pytest | 未开始 | | |

**Week 3 — LangGraph 编排 + 工具 + Agentic RAG**

| Day | 主题 | 状态 | 产出物 | 备注 |
|---|---|---|---|---|
| 15 | Agent 概念（ReAct / Function Calling） | 未开始 | | |
| 16 | LangGraph 基础（StateGraph / Node / Edge） | 未开始 | | |
| 17 | 条件边与循环（路由 / 自反思） | 未开始 | | |
| 18 | 工具层 `tools/`（一工具一文件、ToolNode） | 未开始 | | |
| 19 | 进阶（查询改写 / 多跳 / Corrective RAG） | 未开始 | | |
| 20 | 记忆与持久化（checkpointer） | 未开始 | | |
| 21 | 复盘：重构为完整 Agentic RAG 图 | 未开始 | | |

**Week 4 — 工程化 + 交付（M1 收尾）**

| Day | 主题 | 状态 | 产出物 | 备注 |
|---|---|---|---|---|
| 22 | 工程化：目录分层 / 配置 / 日志 | 未开始 | | |
| 23 | 服务层：FastAPI（routes + services） | 未开始 | | |
| 24 | UI：Streamlit + 👍/👎 反馈埋点 | 未开始 | | |
| 25 | 质量：pytest / mypy / ruff | 未开始 | | |
| 26 | 打包部署：Docker / README / Makefile | 未开始 | | |
| 27 | 检索增强：BM25 + cross-encoder 重排 | 未开始 | | |
| 28 | **M1 复盘 + 演示**（架构图） | 未开始 | | |

### M2 — 生产化版（Week 5–6）

**Week 5 — 评测 + 可观测 + 数据飞轮**

| Day | 主题 | 状态 | 产出物 | 备注 |
|---|---|---|---|---|
| 29 | 评测基础：金标准评测集 | 未开始 | | |
| 30 | RAGAS/DeepEval 四指标 | 未开始 | | |
| 31 | 评测 runner + 回归 | 未开始 | | |
| 32 | 可观测：Phoenix/Opik 接入 trace | 未开始 | | |
| 33 | 数据飞轮①：反馈采集落库 | 未开始 | | |
| 34 | 数据飞轮②：badcase 归因 + 回流 | 未开始 | | |
| 35 | 复盘：跑完整闭环（badcase → 调优 → 回归） | 未开始 | | |

**Week 6 — MCP + Skills + 多 Agent + 求职收尾**

| Day | 主题 | 状态 | 产出物 | 备注 |
|---|---|---|---|---|
| 36 | MCP 基础：接入外部 MCP Server | 未开始 | | |
| 37 | 本项目暴露为 MCP Server | 未开始 | | |
| 38 | Skills：按 SKILL.md 做 2–3 个技能 | 未开始 | | |
| 39 | 多 Agent：supervisor 模式 | 未开始 | | |
| 40 | 端到端联调 + 权限最小实现（可选） | 未开始 | | |
| 41 | 文档与架构图 + 面试问答整理 | 未开始 | | |
| 42 | **M2 复盘 + 项目定稿**（简历描述 / 面试演练） | 未开始 | | |

## 里程碑检查（DoD）

### M1（Week 4 结束）
- [ ] 能对本地文档库提问，回答带引用来源
- [ ] LangGraph 状态图（检索路由 + 查询改写 + 生成）
- [ ] `tools/` ≥2 个工具，一工具一文件
- [ ] FastAPI 可调用 + Streamlit 可交互（含反馈按钮）
- [ ] Docker 一条命令起服务
- [ ] pytest / mypy / ruff 全过
- [ ] 有架构图

### M2（Week 6 结束）
- [ ] 金标准评测集 + 一键出四指标报告
- [ ] 有 trace 可观测
- [ ] 反馈采集 + badcase 归因 + 回流回归闭环跑通
- [ ] 能接外部 MCP Server，且本项目可作为 MCP Server 被调用
- [ ] ≥2 个 Skill 可被加载
- [ ] 多 Agent（supervisor）可运行
- [ ] README + architecture.md + 面试问答整理完成

## 遗留问题 / 待办
- **Day 3 未完成**：Block B（dict/set）动手任务 `TODO 4–7` 未做；Block C（推导式/切片/解包）未讲 —— **下次从 Block B 起**
- ⚠️ **环境待确认**：`uv` 不在 PATH、项目根无 `.venv`、`python` 指向系统 3.11.5（详见「环境信息」）
- 待复习错题：M-03-3（f-string 当类型转换用）标记 🔁；M-03-1 / M-03-2 已掌握
- 跨机器续接：换机器前把 `PROGRESS.md` / `NOTES.md` / `LEARNING_PLAN.md` / `learning/` 同步（或用 git 提交推送），否则新机器读不到进度

## 会话日志
| 日期 | Day | 完成内容 | 笔记 | 下一步 |
|---|---|---|---|---|
| 2026-10-10 | 1 | uv 0.12.24 + Python 3.12.15 环境搭建；`src/agentic_rag/` 骨架；`__main__` 与 Java 心智模型验收通过 | `NOTES.md` → Day 01 | Day 2 |
| 2026-10-12 | 2 | 基础语法（数值/字符串/f-string/None/IO）；完成 `day02_calculator.py`，4 组用例通过 | `NOTES.md` → Day 02（含错题 M-02-1） | Day 3 |
| 2026-10-13 | 3 | Block A（list/tuple/for 语法）讲解 + `day03_containers.py` TODO 1–3 跑通（平均分 78.75）；Block B（dict/set）已讲未练 | `NOTES.md` → Day 03（错题 M-03-1/2/3，均已修正） | Block B 动手 → Block C |
