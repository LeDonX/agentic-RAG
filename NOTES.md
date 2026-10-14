# 学习笔记 & 错题本

> 与 `PROGRESS.md` 平级的学习侧记录：`PROGRESS.md` 管**进度**，本文件管**知识 + 错误**。
> 记录规则：
> - **追加式**：只增不改；勘误以「更正（日期）」条目追加。
> - **错题即时记**：导师一旦纠正我的错误，**当场**追加一条错题（不等收尾，避免细节丢失）。
> - **知识点收尾补**：每天收尾时统一追加当天「知识点速记」。
> - 标签：`#知识点` `#错题` `#易复发`（可用 Grep 检索）
> - 每天在**文件末尾**追加一个 `## Day XX` 小节；每周复盘日（Day 7/14/21/28）追加一节「复习记录」，并从「错题索引」抽 2–3 题考我。

---

## 错题索引

| 编号 | Day | 一句话 | 复发 | 状态 |
|---|---|---|---|---|
| M-02-1 | 2 | `/` 是浮点除，`//` 才是整除 | 0 | ✅ 已掌握 |
| M-03-1 | 3 | 格式说明符 `.2f` 不能脱离 f-string 使用 | 0 | ✅ 已掌握 |
| M-03-2 | 3 | 累加变量未初始化就 `+=` | 0 | ✅ 已掌握 |
| M-03-3 | 3 | 把 f-string 当类型转换用 | 0 | 🔁 复习中 |
| M-03-4 | 3 | 括号不配对（多打一个 `)`）→ SyntaxError | 0 | ☐ 待复习 |
| M-03-5 | 3 | 变量名拼写错误 → NameError | 0 | ☐ 待复习 |
| M-03-6 | 3 | 误解「list 不能当 key」的原因；实为不可哈希 | 0 | ✅ 已掌握 |
| M-04-1 | 4 | 用 `if` 过滤代替打印布尔结果 → 漏掉反例、两列无法对比 | 0 | 🔁 复习中 |
| M-04-2 | 4 | 把「空容器判假」的原因说成「空值为 0」（实为长度为 0） | 0 | 🔁 复习中 |

> 状态：☐ 待复习 / 🔁 复习中 / ✅ 已掌握
> 规则：同一根因**再次踩坑不新增条目**，只在原条目追加 `复发：Day XX` 并把计数 +1——用来暴露真正没掌握的点。

---

## Day 01 — 环境搭建 & Python 心智模型（2026-10-10）

**产出物**：`learning/day01_demo.py`、`learning/day01_indent.py`、骨架 `src/agentic_rag/`

### 一、知识点速记 `#知识点`

- **包管理（uv）**：uv 0.12.24 统一管 Python 版本（3.12.15）与依赖，虚拟环境落在项目根 `.venv`
  - Java 对照：`uv` ≈ Maven/Gradle + 版本管理器（nvm）的合体；`pyproject.toml` ≈ `pom.xml`
- **缩进即语法**：缩进决定代码块归属，没有 `{}`；同一个块必须缩进一致
  - Java 对照：Java 靠 `{}` 划分块，缩进纯属风格；Python 缩进是**语法的一部分**（见 `day01_indent.py`）
- **入口判断**：`if __name__ == "__main__":` 下的代码只在「直接运行」时执行
  - `__name__` 直接运行时是 `"__main__"`，被 import 时是模块名
  - Java 对照：角色上≈ `public static void main(String[] args)`，但更灵活——被 import 时不执行，不会像 Java 那样无法区分子模块入口
- **类型注解**：`def greet(name: str) -> str:` 只是**提示**，运行时不强制
  - Java 对照：Java 的类型是编译期强制的；Python 注解靠 mypy 这类工具在外部检查

### 二、错题 / 踩坑 `#错题`

（Day 1 无报错记录；环境搭建与 `__main__` 验收通过）

---

## Day 02 — 基础语法（2026-10-12）

**产出物**：`learning/day02_calculator.py`（4 组用例通过）

### 一、知识点速记 `#知识点`

- **动态类型**：变量没有类型，类型挂在**对象**上
  - Java 对照：`int a = 1;` 变量本身是 int 型容器；Python `a = 1` 只是把名字绑到 int 对象，之后可重新绑到 str
- **f-string**：`f"{aa/cc:.2f}"` 直接内嵌表达式 + 格式说明符
  - Java 对照：≈ `String.format("%.2f", v)`，但 f-string 更短且能内嵌任意表达式
- **None**：唯一空值，判断用 `is None`，不用 `== None`
  - Java 对照：≈ `null`，但 `None` 是一个真实存在的对象（有类型 `NoneType`）
- **输入输出**：`input()` **永远返回 `str`**，参与计算前必须 `float()` / `int()` 转换
  - Java 对照：≈ `Scanner.nextLine()` 返回 String，同样要 `Integer.parseInt`
- **真除法 vs 整除**：`/` 永远返回 float，`//` 才是整除
  - Java 对照：Java 两个 int 用 `/` 就是整除——**这是最容易踩的惯性坑**

### 二、错题 / 踩坑 `#错题`

#### M-02-1｜`/` 与 `//` 混淆 `#语法`

- **现象**：`7 / 2` 期望得到 `3`，实际得到 `3.5`
- **错误写法**：`result = 7 / 2`
- **根因**：把 Java「两个 int 相除即整除」的心智模型直接搬到了 Python
- **正解**：`7 // 2 == 3`（整除）、`7 / 2 == 3.5`（真除法）
- **Java 对照**：Java `7 / 2 == 3`（int 截断）、`7.0 / 2 == 3.5`；Python 的 `/` 与操作数类型无关，永远真除
- **复发**：—（已复述通过）

---

## Day 03 — 容器（2026-10-13）

**产出物**：`learning/day03_containers.py`（**已完成**：TODO 1–10 全部跑通；Day 3 验收通过）
**状态**：Block A（list/tuple/for）、Block B（dict/set）、Block C（推导式/切片/解包）**全部完成**；当日验收通过（3 题，Q3 经纠正后掌握）
> Block A 知识点由上一会话记录；Block B / Block C 为本次会话补齐。

### 一、知识点速记 `#知识点`

**Block A — list / tuple / for**

- **`list`**：有序、可变、可重复、可混装任意类型（无需泛型）
  - 负索引 `nums[-1]` = 最后一个；切片 `nums[1:3]` = 含头不含尾（Java 无此语法，要 `subList`）
  - Java 对照：`list` ≈ `ArrayList<Object>`，但 Python 没有「定长数组」概念
- **`tuple`**：不可变序列；`(5,)` 才是单元素元组，`(5)` 只是数字
  - 可变 vs 可哈希：**`list` 可变 → 不可哈希 → 不能当 dict key**；`tuple` 不可变 → 可哈希 → 可以
  - Java 对照：无直接对应，最近似 `List.of()` / 匿名 `record`
- **解包**：`x, y = point`；`return a, b` 本质是返回一个 tuple（Python 天然多返回值）
- **`for` 心智模型**：`for item in iterable` ≈ Java for-each（迭代机制相同），差异在两点
  1. Python **没有** C 风格 `for(int i=0;i<n;i++)`，要下标得用 `range(n)`
  2. **循环变量循环结束后仍然存活**（普通名字绑定）；Java 循环变量出作用域即失效
  - `for name, score in students:` = 遍历「元组列表」时**直接解包**（Java 只能先取对象再逐个 get）
- **执行模型（本次观感来源）**：Python **先整篇编译再执行** → 语法错误会挡住后面的运行期错误，所以只报第一个错

**Block B — dict / set（本次会话讲 + 练，验收通过）**

- **`dict`**：`d[k]` 取不到 **抛 `KeyError`**；`d.get(k, default)` 才安全；`"k" in d` 判 key；**保持插入顺序**
  - Java 对照：≈ `HashMap`，但 Java `get` 取不到返回 `null`（不报错）——**最大惯性坑**
  - `dict(二元组列表)` 可直接转换（如 `dict(students)`）；`for k, v in d.items()` 遍历（≈ `entrySet()`）
  - **key 必须可哈希**：`str/int/tuple` 可以，`list` **不行**
- **`set`**：自动去重、元素必须可哈希；`|` `&` `-` 有**独立运算符**（Java 只能调 `addAll/retainAll/removeAll`，且会原地改）
  - ⚠️ `{}` 是**空 dict**，空集合必须写 `set()`
  - **`set` 无序**：顺序由哈希决定、**跨进程还会变**（CPython 对 `str` 默认哈希随机化）→ 要顺序别用 `set`，用 `list`/`dict`

**Block C — 切片 / 推导式 / 解包**

- **切片 `seq[start:stop:step]`**：含头不含尾；`s[::-1]` 反转、`s[::2]` 隔一个取
  - Java 对照：Java 无切片语法，最接近 `subList`；但 **`subList` 是视图（改它会改原 list）**，Python 切片是**新对象（拷贝）**——关键差异
- **推导式**：`[表达式 for x in 可迭代 if 条件]`；字典推导式 `{k: v for ...}`；集合推导式 `{x for ...}`
  - Java 对照：≈ Stream API `filter/map/collect`，但 Python 一行搞定；列表推导式**立即求值**，要**惰性**用生成器表达式 `(x for ...)`
- **解包**：`first, *rest = seq`（`*` 把剩余收成一个 `list`）；`a, b = b, a` 交换无需临时变量
  - Java 对照：Java 无多重赋值 / 星号解包，交换必须用 `temp`

### 二、错题 / 踩坑 `#错题`

#### M-03-1｜格式说明符不能脱离 f-string 使用 `#语法`

- **现象**：`print(total/len(students):.2f)` 运行即报 `SyntaxError: invalid decimal literal`（Python 先整篇编译再执行，所以此错会挡住后面两个 bug）
- **错误写法**：`print(total/len(students):.2f)`
- **根因**：`.2f` 是 **f-string 内部**的格式说明符，只能写在 `{}` 的冒号之后，不是独立表达式语法
- **正解**：`print(f"{total/len(students):.2f}")`
- **Java 对照**：≈ `System.out.printf("%.2f%n", avg)`；Java 的格式串与参数是分开的两部分，Python 是「表达式 + 格式说明符」一起塞进 `{}`
- **复发**：—

#### M-03-2｜累加变量未初始化 `#语法`

- **现象**：`NameError: name 'total' is not defined`（循环内执行 `total += ...` 时）
- **错误写法**：循环里直接 `total += score`，循环前没有 `total = 0`
- **根因**：`+=` 会**先读取** `total` 再赋值；Python 没有「声明即可用」，读一个从未赋过值的名字就报 NameError
- **正解**：循环前先 `total = 0`
- **Java 对照**：Java 里 `int total;` 是声明，`total += score` 在**编译期**就报「可能未初始化」；Python 是**运行期**才报，且异常类型不同（NameError，不是编译错误）
- **复发**：—

#### M-03-3｜把 f-string 当类型转换用 `#语义` `#易复发`

- **现象**：`total += f"{score}"` → `TypeError: unsupported operand type(s) for +=: 'int' and 'str'`
- **错误写法**：`total += f"{score}"`
- **根因**：f-string 的作用是**排版出字符串**，不是做类型转换；`f"{88}"` 得到的是 `"88"`（str），`int + str` 直接报错
- **正解**：`total += score`；真要转类型用 `int()` / `float()` / `str()`
- **Java 对照**：Java 里 `s + 88` 会**隐式**把 88 转成字符串；Python **不做隐式转换**，`int + str` 一律 TypeError——动态类型语言要求你显式转换
- **复发**：—

#### M-03-4｜括号不配对 `#语法`

- **现象**：`print(score_map.get("赵七", 0)))` → `SyntaxError: unmatched ')'`；Python **先整篇编译再执行**，所以后面正确的 TODO 4/6/7 全都不执行
- **错误写法**：`print(score_map.get("赵七", 0)))`（多打一个右括号）
- **根因**：`print(` 一层、`get(` 一层，只需 **2** 个 `)`；多出的第 3 个无处配对
- **正解**：`print(score_map.get("赵七", 0))`
- **Java 对照**：Java 靠 `{}`、语法错误同样编译期报错，所以这不是 Python 特有；真正要点是**括号/引号必须成对**，且 SyntaxError 会**挡住整文件执行**（呼应 M-03-1）
- **复发**：—

#### M-03-5｜变量名拼写错误 `#语法`

- **现象**：`print(sccres[::-1])` → `NameError: name 'sccres' is not defined. Did you mean: 'score'?`；**前面几行正常打印后才崩**
- **错误写法**：`sccres`（把 `scores` 拼错）
- **根因**：Python 没有「声明」，名字必须先赋值存在；拼错的名字从未绑定过 → NameError
- **正解**：`print(scores[::-1])`
- **Java 对照**：Java 拼错变量名是**编译期**错误、整份代码不编译；Python 是**运行期**才报，且**前面已执行的输出保留**——这正是 **SyntaxError（全不跑）vs NameError（跑到那行才崩）** 的分水岭
- **复发**：—

#### M-03-6｜误解「list 不能当 key」的原因 `#概念`

- **现象（验收 Q3 答错）**：答成「list 可变→可能重复→违反 set 去重特性」，把「哈希」与「去重」混为一谈
- **根因**：真正原因是 **`list` 不可哈希（unhashable）**，与「是否会重复」无关。`dict`/`set` 靠 `hash()` 定位；Python 对**可变容器故意不提供 `__hash__`** → `hash([1,2])` 报 `TypeError: unhashable type: 'list'`
- **为什么可变就不能哈希**：list 当 key 后若内容变了 → 哈希也变 → 找不回该 key，整个哈希结构损坏
- **正解**：用 `tuple`（不可变→可哈希）：`d[("张三", 88)]` 合法；可变容器一律不行
- **Java 对照**：Java **不禁止**可变对象当 key（编译期不管），只有运行时 hashCode 变了才会 `get` 不到（经典坑）；Python 在语言层面直接把可变容器设为不可哈希
- **复述（2026-10-13，已掌握）**：答「list 可变 → 不可哈希；tuple 不可变 → 可哈希」✅
- **复发**：—

---

## Day 04 — 控制流与函数（2026-10-14，进行中）

**产出物**：`learning/day04_functions.py`、`learning/day04_demo.py`（导师示范）

### 一、知识点速记 `#知识点`

**Block A — 控制流（5 点，本日全部完成）**

- **`if / elif / else`**：条件**不加括号**，行尾 `:` + 缩进分层；`elif` 是一个词（不是 `else if`）
  - Java 对照：Java 要 `if (a > b) { }`（括号 + 花括号）；Python 靠「冒号 + 缩进」，多分支链用 `elif`
  - 命中第一个真分支后**其余分支全部跳过**（与 Java 一致，但更容易漏判边界：`>= 90` 在前、`>= 60` 在后）
- **真值判断 truthiness（本次验收考点）**：一句话记法 **「空 / 零 / 无」为假**
  - 数值看「是否为 0」：`0`、`0.0` 为假；**空容器看「长度是否为 0」**（调 `len()`，即容器的 `__len__`），`[]`、`{}`、`()`、`set()`、`""` 为假——`[]` 的**值不是数字 0**（M-04-2）
  - `None` / `False` 为假是语言特殊规定
  - ⚠️ **`if x:` ≠ `if x is not None:`**：前者连 `0`、空串、空容器一起判假；后者只判「是不是 None 这个对象」——业务上要区分「值为空」与「值未提供」时必须用 `is None` / `is not None`
- **`is` vs `==`（Java 工程师高危混淆点，与 Java 正好对调）**
  - Python：`is` 比较**身份**（是不是同一个对象，比 `id()`）；`==` 比较**值**（调 `__eq__`）
  - Java：`==` 比**引用**；`.equals()` 比**值**——**两者语义正好对调**
  - `None` 是**单例**，判定必须用 `is None`（官方 PEP8 规定），不要用 `== None`
- **三元表达式**：`X if 条件 else Y`——**结果在前、条件在后**（Java 是 `条件 ? X : Y`，顺序相反）
  - 它是**表达式**（有值、能直接赋给变量 / 塞进 `print`），不是语句
  - 风格：单变量拼接不必套 f-string；二元运算符两侧留空格（`a > b`，非 `a>b`）
- **`for...else`**：**循环没被 `break` 才执行 `else`**——是「没走 break 的收尾分支」，不是「循环结束的分支」
  - Java 对照：Java 要手写 flag（`boolean found=false; ...; if(!found) ...`）；Python 由 `for...else` 一步到位
  - 常见用途：查找 / 质数判断（遍历完都没命中 → else 报「没找到」）
- **`dict` 派发替代 `switch`**：`commands.get(name)` 查表 + `is not None` 判默认分支
  - 前提：**函数是一等对象**——`abs` 是函数对象本身，`abs(-5)` 才是调用（可存进 dict、当参数传、当返回值）
  - Java 对照：Java 没有一等函数（要 `interface` + 匿名类 / 方法引用）；Python 可直接把函数塞进 `dict` 当 `switch` 用
  - 项目关联：Day 18 的 `tools/` 工具注册表就是这个模式的放大版

**Block B — 函数（进行中：⑥ 已讲待练，⑦⑧⑨⑩ 未讲）**

- **`def` / `return`（知识点⑥）**
  - `def 名(参数):` 无括号条件、无返回类型声明；用 `return` 返回值
  - **不写 `return`（或只写 `return`）返回 `None`**——Python 没有 `void`，任何函数都**有**返回值
  - **多返回值**：`return 平均值, 最高分` 本质是返回一个 **tuple**，调用侧用解包接住 `avg, top = stats(nums)`
  - **无重载**：同名 `def` 后一个覆盖前一个（Java 靠参数列表重载，Python 没有）
  - **卫语句 early return**：边界（如空列表）先 `if not nums: return None, None` 提前返回，避免深层嵌套
  - Java 对照：≈ 方法，但「返回值可选、天然多返回值、无 void、无重载」是四点差异

### 二、错题 / 踩坑 `#错题`

#### M-04-1｜用 `if` 过滤代替打印布尔结果 `#思维` `#易复发`

- **现象**：TODO ②-B 要求「逐行打印每个值的 `is not None` 布尔结果」，学员写成 `if value is not None:` 再打印 `value` 本身 → `None` 那一行**没被打印**，7 行变 6 行，A/B 两列无法逐行对比；学员自己先察觉「似乎不太对」
- **错误写法**：

  ```python
  for label, value in cases:
      if value is not None:
          print(f"{label:10}is_not_None={value}")
  ```

- **根因**：把「**判断条件**」当成了「**输出结果**」。要观察一个条件的分布，就该**打印布尔表达式本身**（`{value is not None}`），而不是用 `if` 把它过滤掉——`if` 会把所有「假」的反例丢掉，而**反例恰恰是对比的关键**
- **正解**：

  ```python
  for label, value in cases:
      print(f"{label:10}is_not_None={value is not None}")   # 7 行全打印，True/False 直接可比
  ```

- **Java 对照**：Java `System.out.println(list != null)` 同样是把**布尔表达式**打出来；Python 的 f-string 也能把任意表达式渲染成字符串。注意区分：f-string **不是**类型转换（呼应 M-03-3），但「把布尔值渲染成 `True`/`False` 文本」正是它的本职
- **复发**：—
- **导师侧改进**：题面原写 `is_not_None=<值 is not None>` 易被读成「打印值」，已改为完整示例

#### M-04-2｜把「空容器判假」的原因说成「空值为 0」 `#概念`

- **现象**：②-B 验收回答「空列表、零、空字典、空字符串的 bool 是真值判断，**空值为 0 所以是 false**」——结论对，**机制说错**
- **根因**：判假的机制分两类，混成了一类：
  1. **数值 / 空串**：`0`、`0.0`、`""` —— 它**本身就是**「零 / 空」这个值
  2. **空容器**：`[]`、`{}`、`()`、`set()` —— 判假靠的是**长度**：Python 调 `len(obj)`，`len([]) == 0` → 假（即容器的 `__len__` 返回 0）；`[]` 的**值不是数字 0**
  3. `None` / `False` —— 语言特殊规定
- **正解**：一句话记法 **「空 / 零 / 无」为假**；容器看「长度是否为 0」，数值看「是否为 0」
- **Java 对照**：Java 没有这层统一机制（`bool` 只能来自 boolean 表达式）；最接近的是手写 `isEmpty()` / `size() == 0`
- **复发**：—