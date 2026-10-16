# 学习进度追踪

> 本文件是学习进度的**唯一事实源**。每次会话开始时由导师（AI）读取，结束时由导师更新。
> 你在不同会话里学习时，只要让导师先读本文件，就能自动续接进度。
> 计划详情见 `LEARNING_PLAN.md`。
> 知识点速记 + 错题本见 `NOTES.txt`（每日收尾追加）。

## 协作约定（导师必读）

> 协作规则（先讲后练 / 分 Block / TODO 最后落盘 / 示例不落盘等）的**唯一事实源在 `PROMPT.md`「协作规则」一节**，本文件只管进度，不重复规则正文。改规则只改 `PROMPT.md`。

## 项目信息
- 项目：企业级知识库问答 Agentic RAG（产品形态对标 RAGFlow，生产化对标 bisheng，编排用 LangGraph）
- 学员：Java 工程师（6 年）转 Python AI 应用工程师
- 周期：6 周 / 42 天，每天 2-3 小时
- 里程碑：M1 = Week 1–4（可运行版）；M2 = Week 5–6（生产化版）
- 开始日期：2026-10-10

## 当前进度
- **当前 Day：5（进行中——Block A ①–⑤ 全部完成；Block B ⑥⑦ 完成；⑧⑨⑩ 待续）**
- **当前里程碑：M1（可运行版）**
- 上次会话（2026-10-14，Day 4）：**Day 4 全部完成并通过验收**——Block A 控制流 5 点 + Block B 函数 5 点（⑥`def`/return/多返回值、⑦可变默认参数陷阱★、⑧`*args/**kwargs`、⑨作用域 LEGB、⑩lambda）全部讲完、练习跑通
- 本次会话（2026-10-15，Day 5 进行中）：协作规则 1 改为「清单展示后不停顿、直接开始 Block A ①」；**Block A ①–⑤ 全部讲完、练习跑通、逐个验收通过**（①class 与实例化、②`self`/`__init__`、③实例属性 vs 类属性、④三种方法、⑤访问控制）；**Block B ⑥（继承与 `super()`）讲完并跑通**（子类 `PdfDocument(Document3)`、`super().__init__()`、父类属性遮蔽、`super().summary()` 叠加重写），`exit=0`
- **恢复点（新机器从这里起）**：Day 5 进行中 → 从 **Block B ⑧（`@dataclass`）的讲解开始**（题面已落在 `learning/day05_oop_b.py`）
- 下一步：⑧`@dataclass`（**固化 Day 5 最终版 `Document`**）→ ⑨`__repr__`/`__str__` → ⑩`__eq__`/`__len__`；⑧⑨⑩ 落在新文件 `learning/day05_oop_b.py`（按协作规则 7 拆分）；验收 = 能对比 Java 类与 Python 类
- ✅ `learning/day04_functions.py` 已全量跑通（`uv run python learning/day04_functions.py`）
- ✅ `learning/day05_oop.py` 全量可跑（`uv run python learning/day05_oop.py` → `exit=0`），含 Block A ①–⑤ 与 Block B ⑥⑦ 全部练习
- ✅ `learning/day05_oop_b.py` 已就位（Block B ⑧ 题面，待学员作答）

## 环境信息
- Python 版本：3.12.15（uv 托管，项目锁定 3.12）
- 包管理器：**uv 0.13.1**（本机为本次会话新装，位于 `C:\Users\10217\.local\bin`；新开终端若找不到 `uv`，先执行 `$env:Path = "$env:USERPROFILE\.local\bin;$env:Path"` 或重开终端）
- 虚拟环境：项目根目录 `.venv`（存在；本次会话由 `uv sync` 重建）
- 运行方式：统一用 `uv run python <脚本>`（裸 `python` 不在 PATH，直接调用会失败）
- Ollama 模型：未安装（Day 8 处理）
- 关键依赖：暂无（骨架 `src/agentic_rag/`，入口点 `agentic-rag`）

> ✅ **环境已复核（2026-10-14，本机）**：`uv --version` = 0.13.1；`uv run python --version` = 3.12.15；项目根 `.venv` 存在。
> 注意：裸 `python --version` 无输出（未加入 PATH），运行脚本请统一用 `uv run python <脚本>`。
> ⚠️ **`uv sync` 会有 warning**：`pyproject.toml` 里 `uv_build>=0.12.24,<0.13.0` 不含 0.13.1 —— 不影响使用，Day 6 学依赖管理时再一起修。
> ⚠️ **换机器续学**：新机器若没有 uv / `.venv`，先 `uv sync` 再继续；跨机器靠 **git** 同步（`git pull` 拉最新进度 → 学 → `git commit` + `git push`）。

## 配套文件
- `LEARNING_PLAN.md`：6 周 42 天计划、验收标准
- `WORKFLOW.md`：每日协作 SOP
- `NOTES.txt`：知识点速记 + 错题本（追加式，每日收尾更新；每周复盘日抽题复习）

## 进度总表

### M1 — 可运行版（Week 1–4）

**Week 1 — Python 快速上手**

| Day | 主题 | 状态 | 产出物 | 备注 |
|---|---|---|---|---|
| 1 | 环境搭建（uv）、REPL、`__main__`、Python vs Java | 已完成 | `learning/day01_indent.py`；骨架 `src/agentic_rag/` | 验收通过 |
| 2 | 基础语法（动态类型 / f-string / None） | 已完成 | `learning/day02_calculator.py` | 4 组用例通过；已纠正 `/` 与 `//` |
| 3 | 容器（list/dict/set、推导式、切片、解包） | 已完成 | `learning/day03_containers.py`（TODO 1–10 全部跑通） | 验收通过；已纠正 M-03-4/5/6 |
| 4 | 控制流与函数（默认参数、`*args/**kwargs`、lambda） | 已完成 | `learning/day04_functions.py` | Block A 5/5 + Block B 5/5（⑥⑦⑧⑨⑩）全部完成并跑通；Day 4 验收通过；错题 M-04-1/2/3/4 |
| 5 | 面向对象（class、`self`、`@dataclass`、魔术方法） | 进行中 | `learning/day05_oop.py` + `learning/day05_oop_b.py` | Block A ①–⑤ 全部验收通过；Block B ⑥⑦ 完成（⑦ = 多继承与 MRO）；⑧`@dataclass` / ⑨⑩魔术方法 待续（已拆到 `day05_oop_b.py`）；错题 M-05-1…9 |
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
- ✅ **Day 4 已完成**：Block A 5/5 + Block B 5/5（⑥⑦⑧⑨⑩）全部跑通；验收通过
- ✅ **环境已复核（2026-10-14 本机）**：uv 0.13.1 / `uv run python` 3.12.15 / `.venv` 存在（详见「环境信息」）
- **待复习错题**：M-04-1（`if` 过滤代替打印布尔结果）、M-04-2（空容器判假说成「空值为 0」）、M-04-3（只 print 的函数再套一层 print → 多打 `None`）、**M-04-4（`for...else` 条件漏掉「没被 break」）**；M-03-3/4/5；M-03-1/2/6 已掌握
- **Day 4 验收结论**：通过。核心考点 ⑦（可变默认参数陷阱）学员已能**解释**（默认值定义时求值一次 → 共享副作用）并**演示**（`log_bad` 第二次 `['a','b']`）。Q1（`for...else` 条件）、Q3（`args`=tuple / `kwargs`=dict 未答全）、Q4（规避说法不精确）为回忆偏差，已纠正／记错题
- ✅ **Day 5 进行中（2026-10-15）**：**Block A ①–⑤ 全部完成并逐个验收通过**（①class 与实例化、②`self`/`__init__`、③实例属性 vs 类属性、④三种方法 `@classmethod`/`@staticmethod`、⑤访问控制 `_x`/`__x`）；**Block B ⑥（继承与 `super()`）完成**——子类 `PdfDocument(Document3)`、`super().__init__()`、类属性遮蔽、`super().summary()` 叠加重写全部跑通，`uv run python learning/day05_oop.py` → `exit=0`；⑦⑧⑨⑩ 待续。会话到此暂停（学员要求提交推送）
- **Day 5 待复习错题**：M-05-1（默认打印 ≠ Java 地址）、M-05-2（没有 `new` / 类是一等对象）、M-05-3（实例属性存于 `__dict__`）、**M-05-4（抓错报错归属；⑥ Q1 又把崩点/缺失属性说错，计数 2）**、**M-05-5（漏 docstring / 照抄提示占位语，计数 3）**、M-05-6（「可变参数」vs「可变默认值」术语混用）、**M-05-7（注释漏 `#`，计数 2）**、**M-05-8（装饰器注入机制不透；⑥ Q2 无参 `super()` 机制同为照抄，计数 2）**
- **Day 5 恢复点**：从 **Block B ⑦（多继承与 MRO）的讲解**开始（`learning/day05_oop.py` §195 起为 Block B 区，⑥ 已跑通）
- ⚠️ **⑥ 验收留档**：代码与输出全对（`p1.summary()` → `[PDF·12页] [pdf] PDF 文档演示`；`p1.category` → `pdf`；`Document3.category` → `kb` 未被改）。Q1 崩点已按 M-05-4 纠正为「崩在 `p1.summary()` → `Document3.summary` 访问 `self.text`」；Q2 属照抄导师答案 → **下次开场需自测复述**「无参 `super()` = `__class__` + 方法首参，沿 MRO 往后找」
- 跨机器续接：已用 git 提交推送；新机器先 `git pull` → `uv sync` → 读 `PROGRESS.md` 的「恢复点」继续

## 会话日志
| 日期 | Day | 完成内容 | 笔记 | 下一步 |
|---|---|---|---|---|
| 2026-10-10 | 1 | uv 0.12.24 + Python 3.12.15 环境搭建；`src/agentic_rag/` 骨架；`__main__` 与 Java 心智模型验收通过 | `NOTES.txt` → Day 01 | Day 2 |
| 2026-10-12 | 2 | 基础语法（数值/字符串/f-string/None/IO）；完成 `day02_calculator.py`，4 组用例通过 | `NOTES.txt` → Day 02（含错题 M-02-1） | Day 3 |
| 2026-10-13 | 3 | Block A（list/tuple/for）由上一会话完成；本次补齐 **Block B（dict/set）+ Block C（推导式/切片/解包）**，`day03_containers.py` TODO 1–10 全部跑通，Day 3 验收通过 | `NOTES.txt` → Day 03（错题 M-03-1/2/3/4/5/6） | Day 4 |
| 2026-10-14 | 4 | 修复本机环境（装 uv 0.13.1 + `uv sync` 建 `.venv`）；Block A 控制流 5/5 讲完并验收；**Block B 函数 5/5（⑥`def`/return/多返回值、⑦可变默认参数陷阱、⑧`*args/**kwargs`、⑨作用域 LEGB、⑩lambda）全部讲完、练习跑通、Day 4 验收通过**；固化「先讲后练 + 分 Block + TODO 最后落盘」协作约定 | `NOTES.txt` → Day 04（速记 + 错题 M-04-1/2/3/4） | Day 5：面向对象 |
| 2026-10-15 | 5（进行中） | 协作规则 1 改为「清单展示后不停顿、直接开始 Block A ①」；**Block A ①–⑤ 全部讲完 + 练习 + 逐个验收通过**；**Block B ⑥ 继承与 `super()` 完成（`exit=0`）**；错题 M-05-4/5/7 各追加复发、M-05-8 追加复发；会话到此暂停（学员要求提交推送） | `NOTES.txt` → Day 05（速记 + 错题 M-05-1…8） | 续 Day 5：Block B ⑦ 多继承与 MRO → ⑧`@dataclass` → ⑨⑩ |
| 2026-10-16 | 5（进行中） | 四次流程反馈落地：① 新增协作规则 6（题面极简 / 题下空行 / 口头题预置 `#` / 合并凑数小题）→ ② 二次校准（追加「理解支架」：必要上下文 + 起跑点片段 + 口头题可多条、难度递增、带引导）→ ③ 新增协作规则 7（文件拆分）→ ④ 错题协议新增「手误不记、只记概念偏差」过滤标准；据此把 M-03-4/M-03-5/M-05-5/M-05-7 降级为 ⊘；**Block B ⑦ 多继承与 MRO 讲完、练习跑通、验收通过**；⑧ 题面按新规则重写并迁到新文件 `learning/day05_oop_b.py`（⑦ 及以前的 `day05_oop.py` 不迁移） | `NOTES.txt` → Day 05（错题 M-05-8 计数 3、新增 M-05-9；索引加 ⊘ 降级标注） | 续 Day 5：Block B ⑧`@dataclass` → ⑨⑩（在 `day05_oop_b.py`） |
