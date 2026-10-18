# Day 6 · Block A ② —— 包自身的初始化模块（__init__.py）
# 说明：import 整个包（import day06_pkg）时会执行本文件。
# 提醒：本文件在包内，子模块之间用「相对导入」（from .xxx import ...）。

# TODO ②-1（三项，各有独立观察目标）：
#   1) 写一行 print，用来观察「import 这个包时它会不会执行」
#   2) 用相对导入把两个子模块的函数提升到包这一层：从 math_utils 取 add、从 text_utils 取 shout
#      —— 提示：`from .模块名 import 名字`
#   3) 写 __all__，只导出 add 与 shout（观察 `from day06_pkg import *` 会进来哪些名字）
#
# ？？ 作答区（把三项写成可运行代码）
print("导入包")

from .math_utils import add
from .text_utils import shout

__all__ = ["add", "shout"]
