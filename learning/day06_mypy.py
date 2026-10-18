# Day 6 · Block C ⑦ —— mypy：类型注解与静态类型检查
# 前置：mypy 已在 ⑤ 装好（dev 组）。命令都在项目根目录执行。
# 运行：uv run python learning/day06_mypy.py
#
# 【格式约定·必读】作答区内容必须是合法 Python：
#   (a) 长输出 / 片段 → 统一写进下面这个「答卷 docstring」里（含 Windows 路径 → 用 r"""）；
#   (b) 短答 / 口头答 → 写在对应 # 后。
#   严禁直接粘贴裸文本（否则 .py 立刻变成非法语法）。

r"""⑦ 作答区（命令输出贴这里）

—— ⑦-1 `uv run mypy learning/`
C:\Users\LeDon\Desktop\Ai Space\python project>uv run mypy learning/
learning\day05_oop.py:29: error: "Document" has no attribute "doc_id"  [attr-defined]
learning\day05_oop.py:30: error: "Document" has no attribute "text"  [attr-defined]
learning\day05_oop.py:34: error: "Document" has no attribute "doc_id"  [attr-defined]
learning\day05_oop.py:35: error: "Document" has no attribute "text"  [attr-defined]
learning\day05_oop.py:49: error: Name "Document" already defined on line 20  [no-redef]
learning\day05_oop.py:61: error: Too many arguments for "Document"  [call-arg]
learning\day05_oop.py:62: error: Too many arguments for "Document"  [call-arg]
learning\day05_oop.py:66: error: "Document" has no attribute "metadata"  [attr-defined]
learning\day05_oop.py:201: error: "Document3" has no attribute "_Document3__secret"  [attr-defined]
learning\day04_functions.py:96: error: Cannot call function of unknown type  [operator]
Found 10 errors in 2 files (checked 17 source files)
—— ⑦-2 三个错误 + `uv run python learning/day06_mypy.py` 的输出
learning\day06_mypy.py:73: error: Argument 1 to "ratio" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
learning\day06_mypy.py:62: error: Incompatible return value type (got "int", expected "str")  [return-value]
Found 1 error in 1 file (checked 1 source file)
learning\day06_mypy.py:77: error: "Chunk" has no attribute "age"  [attr-defined]
Found 2 errors in 1 file (checked 1 source file)
—— ⑦-3 加了 [tool.mypy] 之后
      Built agentic-rag @ file:///C:/Users/LeDon/Desktop/Ai%20Space/python%20project                                    Uninstalled 1 package in 32ms
Installed 1 package in 20ms
0.5 t hello
"""

# TODO ⑦-1（观察·基线）：
#   在项目根执行：uv run mypy learning/
#   —— 观察目标：汇总行说「几条 / 几个文件」？为什么剩下大部分文件一条都不报？
#   （提示：mypy 只看「被注解过」的名字；没注解的参数 / 变量 / 返回值它一律当 Any，
#     而 Any 不与任何类型冲突 —— 这就是「渐进类型」的入口）
#
# ？？ 作答区（汇总行 + 报错落在哪两个文件，贴回上面答卷区）

#
# TODO ⑦-2（动手·反向练习，造三种类型错）：
#   下面是三个**已注解**的函数 / 类的起跑点。请各造一个「故意犯规」，每造一个就单独跑一次
#   `uv run mypy learning/day06_mypy.py`，记下错误码：
#     a) 调用 ratio 时，故意传一个 str 当 total
#     b) 改 title_of 的函数体，让它 return 一个 int
#     c) 在 Chunk 实例上访问一个**不存在**的属性
#   —— 输出格式：形如 `<行号>: error: <描述>  [<错误码>]`
#   —— 三处**都别改回来**，最后直接 `uv run python learning/day06_mypy.py`
#   —— 观察目标：mypy 的报错和「脚本能不能跑」分别是哪一层的事？
#
# ？？ 作答区（三个错误码 + python 运行结果，贴回上面答卷区）


def ratio(total: int, part: int) -> float:
    return part / total


def title_of(doc: dict[str, str]) -> str:
    return doc["title"]


class Chunk:
    def __init__(self, text: str) -> None:
        self.text = text


if __name__ == "__main__":
    chunk = Chunk("hello")
    print(ratio(10, 5), title_of({"title": "t"}), chunk.text)

#
# TODO ⑦-3（动手·配置）：
#   在项目根 pyproject.toml 末尾加：
#     [tool.mypy]
#     python_version = "3.12"
#     warn_unused_ignores = true
#   再重跑 uv run mypy learning/，对比 ⑦-1 的条数。
#   —— 观察目标：条数变了吗？「写了配置文件」本身，能不能改变检查强度？
#
# ？？ 作答区（重跑后的汇总行贴回上面答卷区）

#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：同一批代码，mypy 只在那 2 个文件上报错、其余 14 个文件 0 条 —— 为什么？
#   # A1：
#   # Q2（根因）：Python 运行期根本不看类型，mypy 凭什么能抓出「参数类型不对」？它工作时你的脚本在跑吗？
#   # A2：
#   # Q3（Java 对比）：mypy ≈ Java 生态里的什么？「注解只是提示、运行期不强制」相比 Java「编译期强制」，好处与代价各是什么？
#   # A3：
