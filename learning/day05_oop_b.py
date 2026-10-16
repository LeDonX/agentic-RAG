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
from dataclasses import dataclass, field

@dataclass
class Document():
    doc_id: str
    text: str
    metadata: dict = field(default_factory=dict)
    #metadata: dict = {}
    def __repr__(self):
        return f"Document(doc_id={self.doc_id!r}, text={self.text!r})"
        
    def __str__(self):
        return f"[文档 {self.doc_id}] {self.text}"
d = Document("a","text",{'name':'test'})
print(d)
#   2) 故意踩坑：先把 metadata 的默认值临时写成 `= {}` 跑一次，记录报错；跑完立刻改回 field(...)
#      —— 上下文：这一步就是看 Python 拦不拦得住这个手滑写法
#ValueError: mutable default <class 'dict'> for field metadata is not allowed: use default_factory
#   3) 用 @dataclass 定义 PdfDocument(Document)，加字段 pages: int = 0，实例化并 print
#      —— 上下文：字段声明顺序 = 生成 __init__ 的参数顺序，且父类字段必须排在子类字段前面
from dataclasses import dataclass, field

@dataclass
class PdfDocument(Document):
    pages: int = 0
    
p = PdfDocument("a","text",{'name':'test'},12)
print(p)
#   口头作答（难度递增，前一条为后一条铺路；答案写在 # 后）：
#   # Q1（观察）：把 metadata 写成 `= {}` 时，报错发生在「定义这个类」的时候，还是「实例化」的时候？
#   # A1：定义这个类
#   # Q2（根因）：为什么 Python 干脆禁止它？「默认值只求值一次」会带来什么后果？
#   # A2：不是python禁止的，是dataclasses禁止的，拦截发生在`@dataclass` 装饰器处理字段时，检测到了是不可哈希值。默认求一次会让之后没传这个参数的实例都共享同一个值。
#   # Q3（关联）：它和 Day 4 ⑦ 的哪个坑是同一个根因？如果换到函数参数的默认值，正确写法是什么样？
#   # A3：使用了可变类型。
def f(metadata=None):
    if metadata is None:
        metadata = {}
#   # Q4（Java 对比）：@dataclass 替你自动生成了哪些方法？Java 里对应的东西是什么？它和 Java 16 的 record 最关键的区别是什么？
#   # A4：__init__/__repr__/__eq__，构造函数、toString()、equals()，dataclass默认可变、可继承、访问通过属性


# ===== Block B · 知识点⑨：魔术方法 __repr__ / __str__ =====
# 上下文：@dataclass 已自动生成 __repr__（⑧ 你见过它的输出）；本节要你手动重写 __repr__、再加 __str__，看两者分工

# TODO ⑨（先手写预测 → 再跑验证）：

#   1) 在 Document 类体里重写 __repr__，让它对 d2 的输出形如 `Document(doc_id='doc-002', text='向量检索')`（字符串带引号）
#      —— 上下文：重写会覆盖 @dataclass 自动生成的那份。实例化 d2 = Document("doc-002", "向量检索")，依次 print(d2)、print([d2])
#
d2 = Document("doc-002", "向量检索")
print(d2)
print([d2])
#   2) 在 Document 里再加 __str__，让它对 d2 的输出形如 `[文档 doc-002] 向量检索`（人类视角、不带引号）
#      再依次 print(d2)、print(str(d2))、print(repr(d2))、print([d2])
#
print(d2)
print(str(d2))
print(repr(d2))
print([d2])
#   3) 故意踩坑：把 __repr__ 临时【注释掉】（只留 __str__），再 print([d2]) 一次，看列表里变成什么；
#      跑完恢复 __repr__，保持文件可跑
#多了属性打印：[Document(doc_id='doc-002', text='向量检索', metadata={})]
# 口头作答（难度递增，前一条为后一条铺路；答案写在 # 后）：
#   # Q1（观察）：项2 的四行里，print(d2) 走的是 __str__ 还是 __repr__？print([d2]) 走的又是哪个？
#   # A1：__str__，__repr__
#   # Q2（根因）：为什么「容器里展示元素」用的是 __repr__，而不是 __str__？只写 __str__、不写 __repr__，print([d2]) 会怎样？
#   # A2：容器的字符串表示要“无歧义”且“尽量能重建对象”，str 是给最终用户看的、可读优先的表示。str走自己写的，repr走dataclasses的。
#   # Q3（Java 对比）：Java 只有 toString()；List.toString() 里元素走的是谁？Python 的 list 里元素走的是谁？差别在哪？
#   # A3：元素的toString。repr，可以区分字符串类型
#   # Q4（约定）：一个类若只想 print 好看、不关心调试，只写 __str__ 够不够？只写 __repr__ 够不够？为什么？
#   # A4：写了str就会走，没写就走repr


# ===== Block B · 知识点⑩：魔术方法 __eq__ / __len__ =====
# 上下文：⑧ 演示过 @dataclass 自动生成的 __eq__（Document("a","b") == Document("a","b") → True）。本节在下文新建小类，观察 == 与 len() 的底层钩子

# TODO ⑩（先手写预测 → 再跑验证）：

#   1) 定义普通类 Pair（字段 a、b），先【不写】__eq__。实例化 p1 = Pair(1, 2)、p2 = Pair(1, 2)，
#      逐行打印 p1 == p2、p1 is p2、p1 == p1
#      —— 上下文：先看「不写 __eq__」时 == 的默认行为
#
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # def __eq__(self, other):
        # return isinstance(other, Pair) and (self.a, self.b) == (other.a, other.b)
p1 = Pair(1, 2)
p2 = Pair(1, 2)
print(p1 == p2)
print(p1 is p2)
print(p1 == p1)
#   2) 给 Pair 加 __eq__：用 isinstance 判类型 + 把 (a, b) 组成元组比较
#      再打印 p1 == p2；然后打印 Pair.__hash__ 与 hash(p1)，看重写 __eq__ 的副作用
#      —— 上下文：Java 重写 equals 通常还要重写 hashCode；这里看 Python「自动」做了什么
#
print(p1 == p2)
print(Pair.__hash__)
# print(hash(p1))
#   3) 定义类 Bag，__init__(self, items) + __len__ 返回 len(self.items)：
#      打印 len(Bag([1,2,3]))、bool(Bag([]))、bool(Bag([1]))
#      —— 上下文：Day4 学过「空容器判假看长度」，这里看对象版
#
class Bag:
    def __init__(self, items):
        self.items = items
        
    def __len__(self):
        return len(self.items)

print(len(Bag([1,2,3])))
print(bool(Bag([])))
print(bool(Bag([1])))
# 口头作答（难度递增，前一条为后一条铺路；答案写在 # 后）：
#   # Q1（观察）：项1 里 p1 == p2 是 True 还是 False？不写 __eq__ 为什么是这个结果？
#   # A1：false,默认比较的是身份
#   # Q2（根因）：项2 里 hash(p1) 为什么报错？重写 __eq__ 后 Python 顺手对 __hash__ 做了什么？
#   # A2：__eq__会废掉__hash__，把__hash__置为none
#   # Q3（Java 对比）：Java「重写 equals 应重写 hashCode」是约定、编译器不强制；Python 这边是什么性质的行为？
#   # A3：强制的，重写eq会自动把hash置为none
#   # Q4（回到项目）：@dataclass 默认 eq=True，让 ⑧ 的 Document("a","b")==Document("a","b") 得到什么结果？这样的 Document 可哈希吗（能进 set / 当 dict key 吗）？
#   # A4：true，值相等。不可哈希，因为hash是none
