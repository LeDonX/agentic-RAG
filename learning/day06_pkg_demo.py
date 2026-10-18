# Day 6 · Block A ②（包外导入方）—— 绝对导入 + import *
# 运行：uv run python learning/day06_pkg_demo.py
# 依赖：同目录的包 learning/day06_pkg/（先补全它：__init__.py / math_utils.py / text_utils.py）

# TODO ②-4（三项，各有独立观察目标；先写预测 → 再跑）：
#   1) 从包的子模块里取 add（绝对导入），打印 add(2, 3)
#      —— 观察目标：从包外引用时，导入路径怎么写（点号分层）
#
# ？？ 作答区（项1）
from day06_pkg.math_utils import add

print(add(2, 3))

#
#   2) 另起一行 import 整个包（import day06_pkg），看包的 __init__.py 那行 print 在何时出现
#      —— 观察目标：__init__.py 什么时候执行、总共执行几次
#
# ？？ 作答区（项2）
import day06_pkg

# 第一次被访问的时候就执行了，执行一次
#
#   3) 用 `from day06_pkg import *` 把 __all__ 里的名字全导进来，直接调用 shout("hi")
#      —— 观察目标：__all__ 没列到的名字会不会被 `*` 带进来
#
# ？？ 作答区（项3）
from day06_pkg import *

print(shout("hi"))
# 不会，all是白名单，只会导入白名单里的
#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：import day06_pkg 时，__init__.py 里那行 print 出现了吗？第二次 import 还会再出现吗？
#   # A1：没出现，不会出现。
#   # Q2（根因）：`from .math_utils import add` 里的 `.` 指什么？为什么「直接运行 __init__.py」会报 ImportError？
#   # A2：指的是当前包路径，也就是day06_pkg，因为直接运行它的父目录不存在
#   # Q3（Java 对比）：Python 的包 / `__all__` 与 Java 的包 / public 可见性，各自靠什么机制？
#   # A3：python靠all白名单，java靠public编译期决定
