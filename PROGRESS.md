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
- **当前 Day：7（✅ 已完成，2026-10-19）**
- **当前里程碑：M1（可运行版）**
- 上次会话（2026-10-18，Day 6 收尾）：**Day 6 全部完成并通过验收**——Block A ①②③ + Block B ④⑤ + Block C ⑥⑦ + Block D ⑧⑨ 全部讲完、跑通、逐个验收通过；`ruff` 通过、`mypy` 通过
- 本次会话（2026-10-19，Day 7 收尾）：**Day 7 全部完成并通过验收**——Block A 复盘抽题 ①②（M-06-4/5/6/7 逐条复盘，M-06-5 复发 Day 07）；**Block B ③ argparse、④ `iter_files`、⑤ 结构拆分（纯函数 `count_words` + `main(argv)` + `__main__` 薄壳）** 讲完、跑通、逐个验收通过；**Block C ⑥⑦ pytest 入门**（发现规则 / 裸 assert / `@pytest.mark.parametrize` / `pytest.raises`）验收通过；`pytest` 已加入 `[dependency-groups].dev` 并 `uv sync`；**验收 = `uv run pytest learning/ -v` → 6 passed**；day07 两文件 `ruff` All checks passed / `mypy` Success；错题 M-07-1（`rglob` 实参应为 glob 模式）、M-07-2（隐式返回 None → mypy）均由学员自修
- **恢复点（新机器从这里起）**：Day 8 未开始 → 读本文件「下一步」，从 **Day 8 LLM 基础 + Ollama 安装** 继续
- 下一步：**Day 8 —— LLM 基础 + Ollama 安装拉模型**（装 Ollama、`ollama pull` 拉模型、跑通一次本地对话；为 Day 9 直连 Ollama API 做准备）
- ✅ `learning/day04_functions.py` 已全量跑通（`uv run python learning/day04_functions.py`）
- ✅ `learning/day05_oop.py` 全量可跑（`uv run python learning/day05_oop.py` → `exit=0`），含 Block A ①–⑤ 与 Block B ⑥⑦ 全部练习
- ✅ `learning/day05_oop_b.py` 全量可跑（Block B ⑧⑨⑩ 练习 + 作答全在册）
- ✅ `learning/day06_errors.py` 已修正并可跑（`uv run python learning/day06_errors.py` → 打印 `ParseError ValueError` 后按预期在末尾裸调用处崩，用于演示 ⑧-2 因果链）；`ruff check` → All checks passed；`mypy` → Success
- ✅ `learning/day06_ruff.py` / `day06_mypy.py` 均 `ruff check` 通过

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
| 5 | 面向对象（class、`self`、`@dataclass`、魔术方法） | 已完成 | `learning/day05_oop.py` + `learning/day05_oop_b.py` | Block A ①–⑤ + Block B ⑥–⑩ 全部讲完、跑通、逐个验收通过；Day 5 最终版 `Document` 固化；错题 M-05-1…12；验收 = 能对比 Java 类与 Python 类 |
| 6 | 模块/包/依赖管理/类型注解/异常 | 已完成 | `learning/day06_utils.py`、`day06_modules.py`、`day06_pkg/` + `day06_pkg_demo.py`、`day06_cache.py`、`day06_deps.py`、`day06_uv.py`、`day06_ruff.py`、`day06_mypy.py`、`day06_errors.py`；`pyproject.toml`（dev 组 + `[tool.ruff]` + `[tool.mypy]`） | Block A ①②③ + Block B ④⑤ + Block C ⑥⑦ + Block D ⑧⑨ 全部完成并验收；ruff All checks passed / mypy Success；错题 M-06-1…7（M-06-3 ⊘） |
| 7 | 复盘：CLI 小工具 + pytest 入门 | ✅ 已完成 | `learning/day07_cli.py` + `learning/test_day07_cli.py` | Block A ①② 复盘 + Block B ③④⑤ + Block C ⑥⑦ 全部完成并验收；`uv run pytest learning/ -v` → 6 passed；day07 两文件 ruff All checks passed / mypy Success；错题 M-07-1/2（均由学员自修） |

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
- ✅ **Day 7 已完成（2026-10-19）**：Block A 复盘 ①② + Block B ③④⑤ + Block C ⑥⑦ 全部讲完、跑通、逐个验收通过；验收 = `uv run pytest learning/ -v` → 6 passed；`pytest` 已加入 dev 组。`learning/demo.py` / `learning/demo2.py` 是讲解示例（`sys.argv` / argparse）的临时复刻 —— 按 PROMPT 规则 5「示例不落盘」**未纳入 git**，可自行删除
- **Day 7 遗留（不修，留 Day 25）**：`uv run ruff check learning/`（全目录）仍 5 条（`F841/F823` @`day04_functions.py`、`F401/F403/F405` @`day06_pkg_demo.py`，老文件教学噪声）——**非 day07 改动文件**，Day 7 交卷自检只针对改动文件，故不阻塞验收
- ✅ **Day 4 已完成**：Block A 5/5 + Block B 5/5（⑥⑦⑧⑨⑩）全部跑通；验收通过
- ✅ **环境已复核（2026-10-14 本机）**：uv 0.13.1 / `uv run python` 3.12.15 / `.venv` 存在（详见「环境信息」）
- **待复习错题**：M-04-1（`if` 过滤代替打印布尔结果）、M-04-2（空容器判假说成「空值为 0」）、M-04-3（只 print 的函数再套一层 print → 多打 `None`）、**M-04-4（`for...else` 条件漏掉「没被 break」）**；M-03-3/4/5；M-03-1/2/6 已掌握
- **Day 4 验收结论**：通过。核心考点 ⑦（可变默认参数陷阱）学员已能**解释**（默认值定义时求值一次 → 共享副作用）并**演示**（`log_bad` 第二次 `['a','b']`）。Q1（`for...else` 条件）、Q3（`args`=tuple / `kwargs`=dict 未答全）、Q4（规避说法不精确）为回忆偏差，已纠正／记错题
- ✅ **Day 5 已完成（2026-10-16）**：Block A ①–⑤ + Block B ⑥⑦（`learning/day05_oop.py`）+ ⑧⑨⑩（`learning/day05_oop_b.py`）全部讲完、练习跑通、逐个验收通过；两文件均可 `uv run python` 跑通；Day 5 最终版 `Document`（`doc_id`/`text`/`metadata` + 子类 `PdfDocument`）固化
- **待复习错题（Day 5）**：M-05-1（默认打印 ≠ Java 地址）、M-05-2（没有 `new` / 类是一等对象）、M-05-3（实例属性存于 `__dict__`）、M-05-4（抓错报错归属，计数 2）、M-05-5（漏 docstring / 未逐条对题，计数 3，已降级 ⊘）、M-05-6（「可变参数」vs「可变默认值」）、M-05-7（漏 `#`，计数 2，已降级 ⊘ + 流程修复）、M-05-8（装饰器注入机制不透，计数 3 → 已由开场自测消化）、M-05-9（以为 `self.__class__` 能标识「声明类」）、**M-05-10（把 `field(default_factory)` 当函数参数默认值的正解）**、**M-05-11（dataclasses 拦可变默认值的时机 + 判据说错）**、**M-05-12（`@dataclass` 误用在无字段注解的类上）**
- **⑨ 题面格式未对齐复发 3 次** → 已转导师侧流程修复（题面目标输出单列一行强调 + 验收直接给可复制替换代码）
- **Day 6 开场自测（M-05-9 遗留）**：不看笔记回答「继承来的方法里，`self.__class__` 是哪个类？」
- ⚠️ **⑥ 验收留档**：代码与输出全对（`p1.summary()` → `[PDF·12页] [pdf] PDF 文档演示`；`p1.category` → `pdf`；`Document3.category` → `kb` 未被改）。Q1 崩点已按 M-05-4 纠正；Q2 属照抄导师答案 → **该自测已于 2026-10-16 开场独立复述通过**
- 跨机器续接：已用 git 提交推送；新机器先 `git pull` → `uv sync` → 读 `PROGRESS.md` 的「恢复点」继续
- ✅ **Day 6 已完成（2026-10-18）**：Block A ①②③（模块/包/导入：执行模型、`sys.modules`/`sys.path`/`__main__`、`__package__` 与相对导入）、Block B ④⑤（`pyproject.toml` + uv 工作流）、**Block C ⑥⑦（ruff / mypy）**、**Block D ⑧⑨（异常处理 / 自定义异常层次）** 全部讲完、练习跑通、逐个验收通过；`ruff check learning/` 从 59 → 5 条（我代加的 `per-file-ignores` 生效）；`mypy learning/` 基线 10 条（`--strict` 92 条）
- **待复习错题（Day 6，Day 7 复盘日抽题）**：M-06-4（`select` 是替换默认集、不是叠加 → 实测 20→59）、M-06-5（Java 工具对照：Checkstyle/PMD ↔ `check`、Spotless ↔ `format`）、M-06-6（捕获范围过宽，把 TypeError 并进「输入非法」掩盖了自造 bug）、**M-06-7（`except` 捕了永不抛出的类型 → 死分支 + 异常静默穿透；改 raise 类型却忘改 `except`）**；M-06-1/2 为回忆偏差、M-06-3 已降级 ⊘
- **Day 6 验收结论**：**通过**。⑦ mypy 三题由导师作答并讲解（渐进类型 / 静态分析不跑脚本 / ≈ javac 的取舍）；⑧ 执行顺序与异常链全对（`raise ... from e` → `__cause__`）；⑨ 口头三题全对（isinstance 语义抓父类、`__cause__` 装的是 `int()` 抛的 ValueError、基类约定的价值）；⑨-1 动手项**未通过**（`except ParseError` 死分支 + `__main__` 裸调用先崩 → 期待输出从未打印）→ 已由导师代改并实测通过，记错题 M-06-7
- **⑥ ruff 遗留 5 条**（不修，留 Day 25）：`F823/F841` @`learning/day04_functions.py`、`F401/F403/F405` @`learning/day06_pkg_demo.py`（导入未用 / 星号导入相关，属老文件教学噪声）
- ✅ **（已解决）Day 6 遗留**：`pyproject.toml` 的 `[build-system] requires` 已改为 `["uv_build>=0.12.24,<0.14.0"]`（含本机 uv 0.13.1），`uv sync` 上限 warning 消失
- **Docstring 勘误**：`learning/day06_errors.py` 的 `parse_int` docstring 已随 ⑨-1 代改同步为「失败时 raise ParseError」

## 会话日志
| 日期 | Day | 完成内容 | 笔记 | 下一步 |
|---|---|---|---|---|
| 2026-10-10 | 1 | uv 0.12.24 + Python 3.12.15 环境搭建；`src/agentic_rag/` 骨架；`__main__` 与 Java 心智模型验收通过 | `NOTES.txt` → Day 01 | Day 2 |
| 2026-10-12 | 2 | 基础语法（数值/字符串/f-string/None/IO）；完成 `day02_calculator.py`，4 组用例通过 | `NOTES.txt` → Day 02（含错题 M-02-1） | Day 3 |
| 2026-10-13 | 3 | Block A（list/tuple/for）由上一会话完成；本次补齐 **Block B（dict/set）+ Block C（推导式/切片/解包）**，`day03_containers.py` TODO 1–10 全部跑通，Day 3 验收通过 | `NOTES.txt` → Day 03（错题 M-03-1/2/3/4/5/6） | Day 4 |
| 2026-10-14 | 4 | 修复本机环境（装 uv 0.13.1 + `uv sync` 建 `.venv`）；Block A 控制流 5/5 讲完并验收；**Block B 函数 5/5（⑥`def`/return/多返回值、⑦可变默认参数陷阱、⑧`*args/**kwargs`、⑨作用域 LEGB、⑩lambda）全部讲完、练习跑通、Day 4 验收通过**；固化「先讲后练 + 分 Block + TODO 最后落盘」协作约定 | `NOTES.txt` → Day 04（速记 + 错题 M-04-1/2/3/4） | Day 5：面向对象 |
| 2026-10-15 | 5（进行中） | 协作规则 1 改为「清单展示后不停顿、直接开始 Block A ①」；**Block A ①–⑤ 全部讲完 + 练习 + 逐个验收通过**；**Block B ⑥ 继承与 `super()` 完成（`exit=0`）**；错题 M-05-4/5/7 各追加复发、M-05-8 追加复发；会话到此暂停（学员要求提交推送） | `NOTES.txt` → Day 05（速记 + 错题 M-05-1…8） | 续 Day 5：Block B ⑦ 多继承与 MRO → ⑧`@dataclass` → ⑨⑩ |
| 2026-10-16 | 5（进行中） | 四次流程反馈落地：① 新增协作规则 6（题面极简 / 题下空行 / 口头题预置 `#` / 合并凑数小题）→ ② 二次校准（追加「理解支架」：必要上下文 + 起跑点片段 + 口头题可多条、难度递增、带引导）→ ③ 新增协作规则 7（文件拆分）→ ④ 错题协议新增「手误不记、只记概念偏差」过滤标准；据此把 M-03-4/M-03-5/M-05-5/M-05-7 降级为 ⊘；**Block B ⑦ 多继承与 MRO 讲完、练习跑通、验收通过**；⑧ 题面按新规则重写并迁到新文件 `learning/day05_oop_b.py`（⑦ 及以前的 `day05_oop.py` 不迁移） | `NOTES.txt` → Day 05（错题 M-05-8 计数 3、新增 M-05-9；索引加 ⊘ 降级标注） | 续 Day 5：Block B ⑧`@dataclass` → ⑨⑩（在 `day05_oop_b.py`） |
| 2026-10-16 | 5（✅ 完成） | 开场自测「无参 `super()` 沿 MRO」独立复述通过（M-05-8 消化）；**Block B ⑧`@dataclass`、⑨`__repr__`/`__str__`、⑩`__eq__`/`__len__` 讲完、练习跑通、逐个验收通过**（全在 `learning/day05_oop_b.py`）；Day 5 收尾：速记补齐 ⑦–⑩、状态行更新 | `NOTES.txt` → Day 05（速记 ⑦–⑩ + 错题 M-05-10/11/12；索引加 M-05-12） | Day 6：模块/包/依赖管理/类型注解/异常 |
| 2026-10-18 | 6（✅ 完成） | **Day 6 全部完成**：Block A ①②③（模块/包/导入：执行模型、`sys.modules`/`sys.path`/`__main__`、`__package__` 与相对导入）+ Block B ④⑤（`pyproject.toml` 解剖 + uv 工作流）+ Block C ⑥⑦（ruff / mypy）+ Block D ⑧⑨（异常处理 / 自定义异常层次）全部讲完、练习跑通、逐个验收通过；⑥ 两个遗留项（`r"""` 裸串 + `per-file-ignores`）由导师代改后 `ruff check learning/` 59 → 5 条；⑦ mypy 三题由导师作答讲解；⑨-1 因 `except ParseError` 死分支未通过 → 导师代改并实测 `ParseError ValueError`；错题 M-06-4/5/6/7（M-06-3 降级 ⊘） | `NOTES.txt` → Day 06（知识点速记 Block A–D + 错题 M-06-1…7 + Day 6 会话小结） | Day 7：复盘日（抽题复习 + CLI 小工具 + pytest 入门） |
| 2026-10-19 | 7（✅ 完成） | **Day 7 全部完成**：Block A 复盘抽题 ①②（M-06-4/5/6/7，M-06-5 复发）× Block B ③ argparse / ④ `iter_files` / ⑤ 结构拆分（纯函数 + `main` + 薄壳）× Block C ⑥⑦ pytest 入门（发现规则 / `parametrize` / `raises`）；`pytest` 加入 dev 组 + `uv sync`；验收 `uv run pytest learning/ -v` → 6 passed；错题 M-07-1/2 由学员自修；⑦a 因学员倦怠降为**填空级**（导师给骨架、学员填 3 行数据） | `NOTES.txt` → Day 07（速记 ④/⑤/⑥/⑦ + 错题 M-07-1/2 + 会话小结） | Day 8：LLM 基础 + Ollama 安装拉模型 |
