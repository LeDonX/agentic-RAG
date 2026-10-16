# Day 5 · Block B（续）——@dataclass 与魔术方法（⑧⑨⑩）
# 产出物：Day 5 最终版 Document（@dataclass）
# 本文件与 day05_oop.py 相互独立：不 import 它的类，单独运行、输出干净

# ===== Block B · 知识点⑧：@dataclass（固化 Day 5 最终版 Document）=====
# 起跑点：@dataclass 只需「声明字段」，__init__ 由它自动生成。骨架如下，按下面三项补全即可 ——
#     from dataclasses import dataclass, field
#
#     @dataclass
#     class Document:
#         doc_id: str
#         ...（其余字段自己补）

# TODO ⑧（先手写预测 → 再跑验证）：

#   1) 用 @dataclass 定义最终版 Document：字段 doc_id: str、text: str、metadata: dict（默认空字典）
#      —— 上下文：默认空字典的正确写法是 `field(default_factory=dict)`（为什么不写 `= {}` 见 Q1/Q2）。
#      实例化一个实例并 print 它
#   2) 故意踩坑：先把 metadata 的默认值临时写成 `= {}` 跑一次，记录报错；跑完立刻改回 field(...)
#      —— 上下文：这一步就是看 Python 拦不拦得住这个手滑写法
#   3) 用 @dataclass 定义 PdfDocument(Document)，加字段 pages: int = 0，实例化并 print
#      —— 上下文：字段声明顺序 = 生成 __init__ 的参数顺序，且父类字段必须排在子类字段前面
#
#   口头作答（难度递增，前一条为后一条铺路；答案写在 # 后）：
#   # Q1（观察）：把 metadata 写成 `= {}` 时，报错发生在「定义这个类」的时候，还是「实例化」的时候？
#   # A1：
#   # Q2（根因）：为什么 Python 干脆禁止它？「默认值只求值一次」会带来什么后果？
#   # A2：
#   # Q3（关联）：它和 Day 4 ⑦ 的哪个坑是同一个根因？如果换到函数参数的默认值，正确写法是什么样？
#   # A3：
#   # Q4（Java 对比）：@dataclass 替你自动生成了哪些方法？Java 里对应的东西是什么？它和 Java 16 的 record 最关键的区别是什么？
#   # A4：
