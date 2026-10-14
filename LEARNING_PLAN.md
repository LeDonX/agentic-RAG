# 企业级知识库问答 Agentic RAG — 学习计划与实施方案

> 本文件是「学什么、怎么做、照着谁做」的**唯一事实源**。
> 配套文件：`PROMPT.md`（导师提示词）、`PROGRESS.md`（进度追踪）。

---

## 0. 项目定位（一句话）

从零学 Python，**6 周**内亲手做出一个**企业级知识库问答的 Agentic RAG 应用**：
**产品形态对标 RAGFlow、生产化能力对标 bisheng、Agent 编排用 LangGraph 手写**。
它是转岗 **Python AI 应用工程师**的核心项目，也是面试的主要谈资。

---

## 1. 最终形态（项目做完后应具备的能力）

**A. 核心问答能力**
- 多格式文档入库（pdf / word / md / html）→ 切分 → 向量化 → 持久化
- 混合检索（向量 + BM25）→ cross-encoder 重排 → 带**引用来源**的回答
- 低分阈值兜底（召回不足时明确拒答，不编造）

**B. Agentic 编排（LangGraph）**
- 状态图：检索路由 → 查询改写 → 多跳检索 → 相关性评分 → 生成 → 反思/重试
- 多轮会话记忆（checkpointer 持久化）
- 多 Agent：supervisor 模式（一个 Agent 的工具是其他 Agent）

**C. 扩展机制（三大件，独立成层）**
- **Tools**：一工具一文件（知识库检索、NL2SQL、计算、代码沙箱）
- **MCP**：能接外部 MCP Server，也能把本项目能力**暴露为 MCP Server**
- **Skills**：按 `SKILL.md` 规范的可复用技能包（kb-qa / doc-summarize / report-gen）

**D. 生产化闭环（这是「企业级」和「玩具」的分界线）**
- **评测**：金标准评测集 + RAGAS/DeepEval 四指标 + 每次改动跑回归
- **可观测**：Phoenix/Opik 接入 trace，能看检索与生成全过程
- **数据飞轮**：反馈采集（👍/👎 + 标签）→ badcase 归因 → 回流进评测集

**E. 工程化**
- FastAPI 服务层 + Streamlit UI + Docker 化 + pytest/mypy/ruff + README/架构图

---

## 2. 技术栈（锁定）

| 层 | 选型 | 说明 |
|---|---|---|
| 语言 | Python 3.11+ | 目标岗位语言 |
| 包管理 | **uv**（astral-sh/uv） | 现代、快，替代 pip/venv 手工管理 |
| 本地模型 | **Ollama** + qwen2.5 | 免费、可离线、面试可演示 |
| LLM 编排 | **LangChain** + **LangGraph** | 岗位高频，Agent 编排核心 |
| 向量库 | **Chroma** | 轻量、本地持久化 |
| 检索 | 向量 + BM25（rank_bm25）+ cross-encoder 重排 | 混合检索 |
| 服务 | **FastAPI** + **Streamlit** | API + 演示 UI |
| 评测 | **DeepEval**（主力）+ RAGAS 指标参考 | DeepEval 活跃度更高 |
| 可观测 | **Arize Phoenix** 或 **Opik** | 纯 Python |
| MCP | **langchain-mcp-adapters** + MCP 官方 servers | MCP ↔ LangGraph 桥接 |
| 质量 | pytest / mypy / ruff | 工程规范 |

---

## 3. 两个里程碑

| 里程碑 | 时间 | 目标 | 完成标志（DoD） |
|---|---|---|---|
| **M1 可运行版** | Week 1–4 | 能对本地文档库提问，Agentic RAG 跑通并服务化 | 见 §8.1 |
| **M2 生产化版** | Week 5–6 | 有评测、可观测、数据飞轮、MCP、Skills、多 Agent | 见 §8.2 |

> **重要**：若时间只够 4 周，**M1 本身已是一个完整可讲的项目**；M2 是把它从「能跑」升级到「能上线」。

---

## 4. 定稿目录结构

```
python project/
├── PROMPT.md                      # 导师提示词
├── LEARNING_PLAN.md               # 本文件
├── PROGRESS.md                    # 进度追踪
├── NOTES.txt                       # 知识点速记 + 错题本（追加式）
├── README.md
├── pyproject.toml                 # uv 管理依赖
├── .env.example
├── .gitignore
├── Makefile                       # make ingest / chat / eval
├── Dockerfile
├── docker-compose.yml
│
├── configs/
│   ├── settings.yaml
│   ├── mcp_servers.yaml           # MCP Server 清单
│   └── prompts/                   # rewrite / grade / answer
│
├── skills/                        # Agent Skills（人写，SKILL.md 规范）
│   ├── kb-qa/SKILL.md
│   ├── doc-summarize/SKILL.md
│   └── report-gen/SKILL.md
│
├── data/
│   ├── raw/                       # 原始文档
│   ├── processed/                 # 切分后 chunk
│   ├── chroma/                    # 向量库
│   └── eval/
│       ├── golden_qa.jsonl        # 金标准评测集
│       └── feedback/badcases.jsonl
│
├── src/agentic_rag/
│   ├── config.py  logging.py
│   ├── ingestion/                 # loaders / splitter / embedder / pipeline
│   ├── retrieval/                 # vector_store / retriever / reranker
│   ├── llm/                       # chat_model / embeddings
│   ├── tools/                     # registry / schemas / retrieval_tool / sql_tool / code_exec
│   ├── mcp/                       # client / server / adapters
│   ├── skills/                    # loader / executor
│   ├── graph/                     # state / nodes / edges / builder / checkpointer
│   ├── evaluation/                # datasets / metrics / runner
│   ├── flywheel/                  # feedback / attribution / replay
│   ├── observability/             # tracing / callbacks
│   └── api/                       # routes/ + services/ + schemas.py + main.py
│
├── apps/ui/app.py                 # Streamlit（含 👍/👎 反馈按钮）
├── scripts/                       # ingest / chat / evaluate / export_badcases
├── tests/                         # unit/ + integration/
├── docs/                          # architecture.md（架构图）+ interview.md
└── learning/                      # 每日学习练习脚本（day0X_*.py，随学习进度新增）
```

**设计依据**（来自真实项目，非凭空）：
- `agent` / `mcp` / `tools` 独立成层 → RAGFlow `internal/agent`、`internal/mcp`、`internal/agentic_rag/tool_*.go`
- 「一工具一文件」→ RAGFlow `tool_search_chunks.go` / `tool_web_search.go` …
- 顶层 `skills/` → Dify 顶层 `skills/`、RAGFlow `.agents/skills/*/SKILL.md`
- `api/` 下 `controllers/services/repositories/models` 分层 → Dify `api/`
- 编排层极简（state/graph/prompts/config）→ open_deep_research `src/open_deep_research/`

---

## 5. 参考项目对照表（逐模块，星标为实测）

> ### 主要参考对象：**RAGFlow（infiniflow/ragflow）** —— 本项目整体对标它
>
> **选择理由**：① 定位完全一致（企业级知识库问答 + Agentic RAG，有独立的 `internal/agentic_rag/`）；② 星标最高（~90k），可信度与面试说服力最强；③ 模块划分与我们的目录一一对应（`agent` / `agentic_rag` / `mcp` / `deepdoc` / `ingestion`）；④ 三大扩展机制齐全（`tool_*.go` 一工具一文件、`internal/mcp` 一等模块、`.agents/skills/*/SKILL.md`）。
>
> **短板**：主仓库已重构为 **Go 主导** → **代码级只参考架构与模块划分，不抠实现**。
>
> **辅助参考分工**：
> | 补什么 | 用谁 |
> |---|---|
> | 编排层**代码级**参考（Python / LangGraph） | langchain-ai/langgraph + open_deep_research |
> | 同栈中文实现的**代码级**备选 | chatchat-space/Langchain-Chatchat |
> | 评测 / 可观测 / 数据飞轮 | bisheng、Dify、DeepEval、Phoenix/Opik |
> | 服务分层 | langgenius/dify `api/` |

| 模块 | 参考项目 | 星标 | 参考什么 |
|---|---|---|---|
| `graph/` | langchain-ai/langgraph、langchain-ai/open_deep_research | 42,963 / 12.7k | StateGraph、条件边、checkpointer、多 agent supervisor |
| `tools/` | infiniflow/ragflow `internal/agentic_rag/tool_*.go` | ~90k | 一工具一文件；工具清单 |
| `mcp/` | modelcontextprotocol/servers、langchain-ai/langchain-mcp-adapters | 91,095 / 3,655 | MCP server 清单；MCP↔LangChain 适配 |
| `skills/` | anthropics/skills | 180,136 | SKILL.md 规范（name/description frontmatter） |
| `retrieval/` | RAGFlow `internal/deepdoc`+`engine`、sentence-transformers | ~90k / 19,161 | 文档解析、混合检索、cross-encoder 重排 |
| `evaluation/` | confident-ai/deepeval、comet-ml/opik、ragas | 18,722 / 22,475 / 15,975 | RAGAS 四指标；断言式评测 |
| `observability/` | langfuse/langfuse、Arize-ai/phoenix、opik | 35,578 / 11,769 / 22,475 | trace、成本/延迟监控 |
| `ingestion/` | RAGFlow `internal/ingestion`+`deepdoc` | ~90k | 解析→切分→索引 pipeline |
| `llm/` | langchain-ollama | — | Ollama 集成 |
| `api/` | langgenius/dify `api/` | ~145k | 分层架构 |
| 企业治理 | dataelement/bisheng、1Panel-dev/MaxKB | ~11k / 20k | RBAC、多租户、SSO |
| `flywheel/` | ⚠️ **无单一权威项目** | — | 组合：Dify 标注 + Langfuse score + RAGAS「Evaluate and Improve」+ MAPE 飞轮论文 |

**已知风险提示**：
- `ragas` 仓库已改名为 `vibrantlabsai/ragas`，最近提交停在 2026-02，活跃度偏低 → 评测主力用 **DeepEval**。
- `langfuse` 主仓库是 TypeScript → 纯 Python 可观测优先 **Phoenix / Opik**。

---

## 6. 工作原则（贯穿全程）

1. **不凭空猜测**：任何技术选型、目录结构、模块设计，先找**真实高星项目**佐证；找不到权威项目时，明确说明「这是组合模式」，并给出可信来源（官方文档 / 论文 / 实践文章）。
2. **能参考就参考**：每个学习日都标注「今日参考项目」，先读源码再动手。
3. **不照抄**：参考的是**结构与思路**，代码由我亲手写（见 PROMPT.md 教学原则）。
4. **有产出**：每天必须留下可运行/可验证的产出物，不接受「只听课」。
5. **进度可续接**：每次会话开始先读 `PROGRESS.md`，结束必须回写。

---

## 7. 六周逐日计划（每天 2–3 小时）

### Week 1 — Python 快速上手（面向 Java 工程师）

| Day | 主题 | 参考 | 产出物 | 验收标准 |
|---|---|---|---|---|
| 1 | 环境搭建（uv / venv）、REPL、`__main__`、Python vs Java 心智模型 | uv 官方文档 | 可运行 hello 脚本 + 环境记录 | 能解释 `if __name__ == "__main__"` |
| 2 | 基础语法：动态类型、f-string、数值/字符串/None、输入输出 | Python 官方 Tutorial | 小型计算器脚本 | 能说出与 Java 类型的 3 点差异 |
| 3 | 容器：list/tuple/dict/set、推导式、切片、解包 | Python 官方 Tutorial | 数据处理练习 | 能写列表/字典推导式 |
| 4 | 控制流 + 函数：默认参数、`*args/**kwargs`、作用域、lambda | Python 官方 Tutorial | 一组工具函数 | 能解释可变默认参数陷阱 |
| 5 | 面向对象：class、`self`、继承、`@dataclass`、魔术方法 | Python 官方 Tutorial | 一个数据模型类 | 能对比 Java 类与 Python 类 |
| 6 | 模块/包/导入、依赖管理（pyproject + uv）、类型注解 + mypy、异常处理 | uv / mypy 文档 | 多文件小包 | `mypy` 通过 |
| 7 | **复盘**：CLI 小工具（文件批处理）+ pytest 入门 | pytest 文档 | 带测试的 CLI 工具 | `pytest` 全绿 |

### Week 2 — LLM & RAG 基础 + 最小可用 RAG

| Day | 主题 | 参考 | 产出物 | 验收标准 |
|---|---|---|---|---|
| 8 | LLM 应用基础（token/prompt/temperature/上下文）；Ollama 安装拉模型 | Ollama 文档 | 本地模型跑通 | `ollama run` 能对话 |
| 9 | Python 直连 Ollama API，理解 messages 结构 | Ollama API 文档 | 最简聊天脚本 | 能解释 role/content |
| 10 | LangChain 入门：ChatModel、PromptTemplate、LCEL、输出解析 | langchain 官方文档 | LCEL 链 Demo | 能用管道符串链 |
| 11 | 文档加载与切分：Document、Loader、RecursiveCharacterTextSplitter | langchain 文档、RAG_Techniques | 文档切分脚本 | 能解释 chunk_size/overlap |
| 12 | Embedding + Chroma：向量化、持久化、相似度检索 | langchain-chroma 文档 | 可检索的向量库 | 能检索出相关片段 |
| 13 | 最小 RAG 链：检索 → 拼上下文 → 生成 + 引用来源 | RAG_Techniques | 能问答的 RAG | 回答带来源 |
| 14 | **复盘**：多轮对话记忆 + 为检索/生成写 pytest | langchain 文档 | 带记忆的 RAG + 测试 | 测试全绿 |

### Week 3 — LangGraph 编排 + 工具 + Agentic RAG

| Day | 主题 | 参考 | 产出物 | 验收标准 |
|---|---|---|---|---|
| 15 | Agent 概念：ReAct、Function Calling；为什么 RAG 需要 Agent | langchain 文档 | 概念笔记 + 伪代码 | 能讲清 ReAct 循环 |
| 16 | LangGraph 基础：StateGraph、Node/Edge、State(TypedDict)、compile | langgraph 官方教程 | 最小状态图 | 能画出图结构 |
| 17 | 条件边与循环：检索路由、自反思 | langgraph 文档 | 带路由的图 | 能解释条件边 |
| 18 | 工具层 `tools/`：检索封装成 tool（一工具一文件）、ToolNode | langgraph 文档、RAGFlow | 多工具 Agent | 工具能被正确调用 |
| 19 | 进阶：查询改写、多跳检索、相关性评分（Corrective RAG） | langgraph agentic-rag 教程、open_deep_research | Corrective RAG 图 | 低质召回能触发改写 |
| 20 | 记忆与持久化：checkpointer、多轮会话状态 | langgraph 文档 | 有记忆的 Agent | 跨轮次记住上下文 |
| 21 | **复盘**：把 Week2 的 RAG 重构为完整 Agentic RAG 图 | — | 整合版 Agentic RAG | 端到端跑通 |

### Week 4 — 工程化 + 交付（M1 收尾）

| Day | 主题 | 参考 | 产出物 | 验收标准 |
|---|---|---|---|---|
| 22 | 工程化：目录分层、配置（pydantic-settings/.env）、日志 | Dify api/ | 规范项目结构 | 配置不硬编码 |
| 23 | 服务层：FastAPI（routes/ + services/ 分层） | Dify api/ | 可调用 API | `/chat` 能返回答案 |
| 24 | UI：Streamlit + **👍/👎 反馈按钮**（为飞轮埋点） | Streamlit 文档 | 可交互界面 | 反馈能落库 |
| 25 | 质量：pytest、mypy、ruff/black | — | 通过检查的代码库 | 三项全过 |
| 26 | 打包部署：Docker、README、Makefile/CLI | — | Dockerfile + 文档 | 一条命令起服务 |
| 27 | 检索增强：BM25 混合检索 + cross-encoder 重排 | RAGFlow、sentence-transformers | 混合检索版 | 重排后相关性提升 |
| 28 | **M1 复盘 + 演示**：画架构图，完整演示 | — | 架构图 + 演示 | 达 §8.1 DoD |

### Week 5 — 评测 + 可观测 + 数据飞轮（M2）

| Day | 主题 | 参考 | 产出物 | 验收标准 |
|---|---|---|---|---|
| 29 | 评测基础：构建金标准评测集 | RAGAS 官方指南 | `golden_qa.jsonl` | ≥30 条问答对 |
| 30 | RAGAS/DeepEval 四指标：faithfulness/answer relevancy/context precision/context recall | deepeval 文档 | 指标脚本 | 能算出 4 个指标 |
| 31 | 评测 runner + 回归：每次改动跑一遍 | — | `evaluate.py` | 一条命令出报告 |
| 32 | 可观测：Phoenix/Opik 接入 trace | Phoenix/Opik 文档 | trace 面板 | 能看到检索+生成链路 |
| 33 | 数据飞轮①：反馈采集（👍/👎 + 标签落库） | Dify 标注回复 | 反馈入库 | 反馈可查询 |
| 34 | 数据飞轮②：badcase 归因（检索/生成/切分）+ 回流评测集 | MAPE 飞轮论文 | 归因脚本 | 能定位错误环节 |
| 35 | **复盘**：跑完整闭环（badcase → 调优 → 回归） | — | 闭环记录 | 指标有提升 |

### Week 6 — MCP + Skills + 多 Agent + 求职收尾（M2）

| Day | 主题 | 参考 | 产出物 | 验收标准 |
|---|---|---|---|---|
| 36 | MCP 基础：协议 + `langchain-mcp-adapters` 接外部 MCP Server | modelcontextprotocol/servers | 接入 1 个外部 MCP | 外部工具可被调用 |
| 37 | 把本项目暴露为 MCP Server | MCP 文档、RAGFlow | 自建 MCP Server | 外部客户端能调本项目 |
| 38 | Skills：按 SKILL.md 规范做 2–3 个技能 | anthropics/skills | `skills/` 目录 | 技能可被加载执行 |
| 39 | 多 Agent：LangGraph supervisor 模式 | langgraph 文档 | 多 Agent 图 | 能分派到子 Agent |
| 40 | 端到端联调 + 权限/多租户最小实现（可选） | bisheng | 完整链路 | 全链路通 |
| 41 | 文档与架构图：architecture.md、README、面试问答整理 | — | 文档 | 面试可讲 |
| 42 | **M2 复盘 + 项目定稿**：简历项目描述 + 面试演练 | — | 项目定稿 | 达 §8.2 DoD |

---

## 8. 里程碑验收标准（DoD）

### 8.1 M1（Week 4 结束）
- [ ] 能对本地文档库提问，回答**带引用来源**
- [ ] 编排是 LangGraph 状态图（含检索路由 + 查询改写 + 生成）
- [ ] `tools/` 至少 2 个工具，且「一工具一文件」
- [ ] FastAPI 可调用 + Streamlit 可交互（含反馈按钮）
- [ ] Docker 一条命令起服务
- [ ] pytest / mypy / ruff 全过
- [ ] 有架构图

### 8.2 M2（Week 6 结束）
- [ ] 金标准评测集 + 评测脚本，能一键出四指标报告
- [ ] 有 trace 可观测
- [ ] 反馈采集 + badcase 归因 + 回流回归的闭环跑通
- [ ] 能接外部 MCP Server，且本项目可作为 MCP Server 被调用
- [ ] ≥2 个 Skill 可被加载
- [ ] 多 Agent（supervisor）可运行
- [ ] README + architecture.md + 面试问答整理完成

---

## 9. 可行性说明与风险

**为什么 6 周可行**
- 6 年 Java 功底：语言迁移成本低，Week 1 只补「Python 特有」而非通用编程。
- 每天 2–3 小时 ≈ 每周 14–18 小时，共约 **90–110 小时**，与上述范围匹配。
- 全程用**本地 Ollama**，零 API 成本、可离线，不阻塞学习。

**主要风险与对策**
| 风险 | 对策 |
|---|---|
| 时间不够（只能 4 周） | 停在 M1 即为完整项目；M2 可延后 |
| Python 生态工具多、易迷路 | 技术栈已锁定（§2），不引入额外框架 |
| RAG 效果不稳定 | Week 5 评测先行，用数据驱动调优而非拍脑袋 |
| MCP / 多 Agent 偏难 | 放在 Week 6，且以「能演示」为目标，不追求生产级 |
| 参考项目看不懂（RAGFlow 是 Go） | 只看**结构**不抠实现；代码级参考用 LangChain/LangGraph 生态 |

---

## 10. 现在开始

新会话开场：把 `PROMPT.md` 全文粘给导师 → 导师读 `PROGRESS.md` 汇报进度 → 开始当天任务。
