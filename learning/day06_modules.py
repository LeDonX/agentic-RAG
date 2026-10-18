# Day 6 · Block A ①（导入方）—— import 的三种写法
# 运行：uv run python learning/day06_modules.py
# 依赖：同目录的 day06_utils.py（先补全它，再跑本文件）

# TODO ①-2（三项，各有独立观察目标；先写预测 → 再跑）：
#   1) 用 `import day06_utils` 这种写法导入，打印「被导入模块自己的 __name__」与常量 APP_NAME
#
# ？？ 作答区（项1）
import day06_utils

print(day06_utils.__name__)
print(day06_utils.APP_NAME)
#
#   2) 换成 `from day06_utils import describe` 这种写法，调用 describe("hello") 并打印
#      —— 输出格式：describe("hello") 结果形如  agentic-rag :: hello
#      —— 观察目标：这种写法之后，APP_NAME 这个名字还能直接写吗
#
# ？？ 作答区（项2）
from day06_utils import describe

print(describe("hello"))
#
#   3) 换成 `import day06_utils as u`，改用别名再访问一次 APP_NAME
#      —— 观察目标：别名与原模块名是否指向同一个对象
#
# ？？ 作答区（项3）
import day06_utils as d6

print(d6.APP_NAME)
#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：直接运行 day06_utils.py，与 被 day06_modules.py 导入，两种情况 __name__ 各是什么？第 3 项那句短句在哪种情况下打印？
#   # A1：前者是__main__，后者是模块名。直接运行而不是被调用时才打印。
#   # Q2（根因）：为什么一行 import 就能让另一个文件的代码「跑起来」？第二次 import 同一个模块还会重新执行吗？
#   # A2：import的时候会编译运行，第二次直接读缓存。
#   # Q3（Java 对比）：Java 的 import 与 Python 的 import，在「何时执行代码」上的差别是什么？
#   # A3：java是编译期执行，python是运行期才执行
