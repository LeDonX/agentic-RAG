# Day 6 · Block A ③ —— 导入的执行模型（sys.modules 缓存 / sys.path 搜索 / __main__）
# 运行：uv run python learning/day06_cache.py
# 依赖：同目录的 day06_utils.py（Block A ① 已写好）

# TODO ③-1（三项，各有独立观察目标；先写预测 → 再跑）：
#   1) 打印 sys.path[0]
#      —— 观察目标：直接运行脚本时，「第一搜索路径」是不是脚本所在目录
#
# ？？ 作答区（项1）
import sys

print(sys.path[0])
# 是的
#
#   2) 对 day06_utils 连续 import 两次（第二次用别名），打印两次绑定的名字是否同一个对象，
#      再打印它是否就是 sys.modules["day06_utils"]
#      —— 观察目标：第二次 import 到底有没有重新执行这个模块
#
# ？？ 作答区（项2）
import day06_utils
import day06_utils as d6

print(day06_utils is d6)
print(day06_utils is sys.modules["day06_utils"])
#
#   3) 打印当前脚本自己的 __name__，再打印 sys.modules["__main__"] 的 __name__
#      —— 观察目标：直接运行的脚本，是以什么名字进 sys.modules 的
#
# ？？ 作答区（项3）
print(__name__)
print(sys.modules["__main__"].__name__)
# 以main
#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：第二次 import day06_utils（别名那次）会重新执行它的顶层代码吗？你用什么证据判断？
#   # A1：不会，因为是同一个对象
#   # Q2（根因）：sys.modules 在 import 流程里起什么作用？sys.path 又是用来干什么的？
#   # A2：sys.modules 是「模块名 → 已加载 module 对象」的缓存字典；sys.path 是「去哪里找模块文件」的搜索路径列表
#   # Q3（Java 对比）：sys.modules / sys.path 分别对应 Java 里的什么？
#   # A3：类加载器的缓存，类的全限定名
