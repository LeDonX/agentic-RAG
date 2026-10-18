"""Day 5：面向对象（class / self / 继承 / @dataclass / 魔术方法）

运行：uv run python learning/day05_oop.py
产出物：一个数据模型类（Document），未来 Day 11 文档入库可直接复用

说明：本文件按「一个知识点一段」推进，每讲完一点追加一段 TODO。
"""

# ===== Block A · 知识点①：class 与实例化（没有 new）=====


# TODO ①：
#   1) 定义一个 Document 类，空类体用 pass，带一行 docstring（今天不写 __init__）
#   2) 用「类名加括号」实例化 d1、d2（不许出现 new）
#   3) 给 d1 动态挂 doc_id = "doc-001"、text = "RAG 是检索增强生成"
#   4) 逐行打印：type(d1)、d1 is d2、d1.doc_id、d1.text、d1 本身
#   5) 用两行注释回答：
#        Q1 为什么 d2.doc_id 会报 AttributeError？（对比 Java 字段）
#        Q2 为什么 print(d1) 打印的不是内容，而是一串地址？
class Document:
    """知识库文档数据模型。"""

    pass


d1 = Document()
d2 = Document()

d1.doc_id = "doc-001"
d1.text = "RAG 是检索增强生成"

print(type(d1))
print(d1 is d2)
print(d1.doc_id)
print(d1.text)
print(d1)

# q1 因为d2并没有在运行时挂doc_id
# q2 应该类似java中打印的是地址


# ===== Block A · 知识点②：self 与 __init__ =====


# TODO ②：
#   1) 给 Document 加 __init__(self, doc_id, text, metadata=None)：
#        · metadata 用 None 占位，函数体里 if metadata is None: metadata = {}（避开 Day4⑦）
#        · 三个属性都挂到 self 上；类补一行 docstring（① 漏了）
class Document:
    """知识库文档数据模型。"""

    def __init__(self, doc_id, text, metadata=None):
        if metadata is None:
            metadata = {}
        self.doc_id = doc_id
        self.text = text
        self.metadata = metadata


#   2) 实例化两份：d1 不传 metadata；d2 传 {"source": "manual.pdf", "page": 3}
d1 = Document("doc-001", "RAG 是检索增强生成")
d2 = Document("doc-001", "RAG 是检索增强生成", {"source": "manual.pdf", "page": 3})
#   3) 逐行打印两份的 __dict__，并打印 d1.metadata is d2.metadata（应为 False）
print(d1.__dict__)
print(d2.__dict__)
print(d1.metadata is d2.metadata)


#   4) 故意删掉一处 self. 前缀，跑一次，把报错原文抄成注释
class Document2:
    """知识库文档数据模型。"""

    # TypeError: Document2.__init__() missing 2 required positional arguments: 'doc_id' and 'text'
    def __init__(self, doc_id, text, metadata=None):
        if metadata is None:
            metadata = {}
        doc_id = doc_id
        self.text = text
        self.metadata = metadata


d = Document2("doc-002", "RAG 是检索增强生成2", {"source": "manual.pdf", "page": 3})
print("实例化2成功，text =", d.text)
# print(d.doc_id)
#   5) 注释回答：d.show() 等价于哪个函数调用？
# Document.show()


# ===== Block A · 知识点③：实例属性 vs 类属性 =====


# TODO ③（6 项，动手前先逐条看一遍）：
#   1) 给 Document 加类属性 category = "general"（写在类体里、__init__ 之外），
#      加注释说明它等价 Java 的什么
class Document3:
    """知识库文档数据模型。"""

    category = "general"

    def __init__(self, doc_id, text, metadata=None):
        self.doc_id = doc_id
        self.text = text
        self.metadata = metadata
        self._cache = {}
        self.__secret = "hidden"

    def summary(self):
        # self收到的是实例对象
        return f"[{self.category}] {self.text}"

    def reveal(self):
        return self.__secret

    @classmethod
    def from_text(cls, doc_id, text):
        print("  cls.__name__ =", cls.__name__)
        return cls(doc_id, text)

    @staticmethod
    def is_supported_format(name):
        return name.lower().endswith((".pdf", ".md", ".txt"))


# 相当于java中的静态变量
#   2) 实例化 d3、d4（不同 doc_id），打印 d3.category / d4.category / Document.category
d3 = Document3(1, "d3")
d4 = Document3(2, "d4")
print(d3.category)
print(d4.category)
print(Document3.category)
#   3) 执行 d3.category = "faq"，再打印三者；并打印 d3.__dict__，观察 category 出现在哪里
d3.category = "faq"
print(d3.__dict__)
print(d3.category)
print(d4.category)
print(Document3.category)
#   4) 打印 "category" in Document.__dict__（应为 True）
print("category" in Document3.__dict__)
#   5) 执行 Document.category = "kb"，再打印三者，用注释解释：为什么 d4 变了、d3 没变？
Document3.category = "kb"
print(d3.category)
print(d4.category)
print(Document3.category)
# 因为上面有赋值操作，给d3挂上了实例字典，而d4依旧用的是类字典
#   6) 注释回答：若 category 是 Java 的 static 字段，d3.category = "faq" 会发生什么？与 Python 有何相反之处？
# 所有实例都会共享faq，python只会给d3实例挂上实例字典


# ===== Block A · 知识点④：三种方法（实例方法 / @classmethod / @staticmethod）=====
# 说明：本节全部在 Document3 上做（Document / Document2 作脚手架保留，不合并）

# TODO ④（6 项，动手前先逐条看一遍）：
#   1) 补 docstring：给 Document3 加 """..."""；顺手给上面的 Document（②版）、Document2 也各补一行
#      （① ② 遗留的 M-05-5，本次一并了结）
#   2) 给 Document3 加【实例方法】summary(self)：返回 f"[{self.category}] {self.text}"
#      加注释说明 self 收到的是什么
#   3) 给 Document3 加【类方法】from_text(cls, doc_id, text)：
#        · 用 @classmethod 装饰；函数体先 print("  cls.__name__ =", cls.__name__)
#        · 再 return cls(doc_id, text) 造实例（工厂方法）
#   4) 给 Document3 加【静态方法】is_supported_format(name)：
#        · 用 @staticmethod 装饰；返回 name.lower().endswith((".pdf", ".md", ".txt"))
#   5) 逐行调用并打印，观察输出：
#        · Document3.from_text("doc-100", "hello").summary()   —— 类调类方法
#        · d3.summary()                                        —— 实例调实例方法
#        · d3.from_text("doc-101", "world").summary()          —— 实例也能调类方法，注意 cls 是谁
#        · Document3.is_supported_format("a.PDF")  /  Document3.is_supported_format("a.png")
#        · d3.is_supported_format("x.md")                      —— 实例也能调静态方法

print(Document3.from_text("doc-100", "hello").summary())
print(d3.summary())
print(d3.from_text("doc-101", "world").summary())
print(Document3.is_supported_format("a.PDF"))
print(Document3.is_supported_format("a.png"))
print(d3.is_supported_format("x.md"))
#   6) 注释回答：
#        Q1 @classmethod 与 @staticmethod 分别等价 Java 的什么？classmethod 为什么必须收 cls？
#        Q2 若把 @classmethod 的装饰器删掉（只留 def from_text(cls, ...)），调用会怎样？
# q1 `@classmethod` ≈ Java 的 静态工厂方法 、`@staticmethod` ≈ Java 的 static 方法 ✅。 为什么必须收`cls` ：`@classmethod` 在 调用时 （无论`类.f()` 还是`实例.f()` ）Python 会 自动把「调用所用的那个类」塞作第一个实参 ，所以第一个形参必须接得住它（`cls` 只是约定名）。它有两点用处：①`cls` 是 实际调用的类 → 子类调用时工厂返回 子类 实例（多态）；② 借`cls` 才能`cls(...)` 造实例、或访问/改类属性。
# q2 删掉装饰器后，`Document3.from_text("doc-100","hello")` ： 不再注入类 → 第一个实参`"doc-100"` 落进`cls` （是 字符串 、不是类），同时少一个实参 → 先报`TypeError: from_text() missing 1 required positional argument: 'text'` ；即便参数凑够，`cls(doc_id, text)` 也会因`cls` 是`str` 报`TypeError: 'str' object is not callable` 。→ 关键不是「 没得到 cls」，而是 cls 收到了错误的东西 ——装饰器是语义开关，不是风格。


# ===== Block A · 知识点⑤：访问控制（_x / __x / __x__）=====
# 说明：本节仍在 Document3 上继续

# TODO ⑤（5 项，动手前先逐条看一遍）：
#   1) 给 Document3.__init__ 加两个属性：
#        · self._cache = {}           单下划线（注释：约定内部用）
#        · self.__secret = "hidden"   双下划线（类内会被改写成 _Document3__secret）
#   2) 给 Document3 加方法 reveal(self)：return self.__secret（体会类体内自动改写）
#   3) d5 = Document3("doc-200", "secret demo")，逐行打印：
#        · d5.text
#        · d5._cache                   ← 单下划线只是约定，照样读得到
#        · d5.reveal()                 ← 类内用 __secret 正常
#        · [k for k in d5.__dict__]    ← 看 __secret 被改写成了什么名字
#        · d5._Document3__secret       ← 绕开改写也能读到 → 不是真私有
d5 = Document3("doc-200", "secret demo")
print(d5.text)
print(d5._cache)
print(d5.reveal())
print([k for k in d5.__dict__])
print(d5._Document3__secret)
#   4) 故意报错演示：把 print(d5.__secret) 放在【文件最后一行】（隔离，参照 M-05-4），
#      跑一次把报错原文抄成注释（应为 AttributeError: 'Document3' object has no attribute '__secret'）；
#      抄完【把该行注释掉】，保持文件后续可跑（Day 6 起还要用）
# AttributeError: 'Document3' object has no attribute '__secret'
# print(d5.__secret)
#   5) 注释回答：
#        Q1 _x 与 __x 各自想表达什么？谁能真正挡住外部访问？
#        Q2 与 Java 的 private 相比，最本质的区别是什么？
# q1 前者是类内部使用，后者会触发名称改写，会在前面追加_类名。后者会挡住外部访问，但是也可以通过增加_类名绕过。
# q2 java中的private是编译期硬性规则，python大多算约定，最终还是可以被绕过。


# ===== Block B · 知识点⑥：继承 与 super() =====
# 说明：本节在 Document3 之下新增一个子类；Document / Document2 / Document3 一律不动


# TODO ⑥（6 项，动手前先逐条看一遍）：
#   1) 定义 class PdfDocument(Document3)，docstring 一行「PDF 文档子类。」
#        __init__(self, doc_id, text, pages)：
#          · 第一行先 super().__init__(doc_id, text)   ← 父类属性（含 _cache / __secret）靠这行才挂上
#          · 再 self.pages = pages
class PdfDocument(Document3):
    """「PDF 文档子类。」"""

    category = "pdf"

    def __init__(self, doc_id, text, pages):
        super().__init__(doc_id, text)
        self.pages = pages

    def summary(self):
        return f"[PDF·{self.pages}页] " + super().summary()


#   2) 在 PdfDocument 的【类体里】加类属性 category = "pdf"（不要写在 __init__ 里）
#   3) 重写 summary(self)：返回 f"[PDF·{self.pages}页] " + super().summary()
#        · 体会 super().summary()：先跑父类的输出，再在子类前面拼前缀
#   4) 实例化 p1 = PdfDocument("doc-300", "PDF 文档演示", 12)，逐行 print 并观察：
#        · p1.summary()                  ← 子类重写版（前半段子是子类拼的、后半段是父类给的）
#        · p1.pages                      ← 1) 里自己挂的
#        · p1.category                   ← 谁赢？类属性查找从【子类】开始
#        · Document3.category            ← 父类那份有没有被改？
#        · p1.__dict__                   ← 看父类 __init__ 到底挂了哪些键（_Document3__secret 在不在）
#        · isinstance(p1, Document3)          ← 应为 True
#        · issubclass(PdfDocument, Document3) ← 应为 True
p1 = PdfDocument("doc-300", "PDF 文档演示", 12)
print(p1.summary())
print(p1.pages)
print(p1.category)
print(Document3.category)
print(p1.__dict__)
print(isinstance(p1, Document3))
print(issubclass(PdfDocument, Document3))
#   5) 故意报错演示（隔离，参照 M-05-4）：
#        · 临时把 1) 里那行 super().__init__(doc_id, text) 【注释掉】，重跑
#        · 把报错原文【完整】抄成本行下方注释（要含最后那行 AttributeError 原文，一个字都别省）
#        · 抄完把 super().__init__(doc_id, text) 【取消注释】，恢复文件可跑
# AttributeError: 'PdfDocument' object has no attribute 'text'
#   6) 注释回答：
#        Q1 不调 super().__init__() 为什么会崩？崩在哪个方法里、报的是哪个属性缺失？
#        Q2 Python 3 的 super() 为什么可以不写参数？与 Java 的 super(...) 最本质的区别是什么？
# Q1 崩在`p1.summary()` 里 →`super().summary()` →`Document3.summary` 访问`self.text` 那一下
# q2 Python 3 在 编译期 给类体注入一个隐式变量`__class__` ，无参`super()` 就用「当前方法的第一个参数（`self` /`cls` ）+ 这个`__class__` 」推出「从哪个类往后找」——参数能省是编译器替你填了。Java 的`super` 是 关键字 、编译期静态绑定、只能指直接父类。补一句复述即可（这层是 ⑦ MRO 的地基：`super()` 不是「找父类」，是「 沿 MRO 往后找 」）。


# ===== Block B · 知识点⑦：多继承与 MRO =====
# 说明：本节在下面新建一组小类做演示，不改动上面的 Document / Document2 / Document3 / PdfDocument

# TODO ⑦（先手写预测 → 再跑验证）：


#   1) 定义 A、B（各带 mark() 返回自己类名）与 C(A, B)；先打印 C.__mro__，再打印 C().mark()
class A:
    def __init__(self):
        super().__init__()

    def mark(self):
        return "A"


class B:
    def __init__(self):
        super().__init__()

    def mark(self):
        return "B"


class C(A, B):
    def __init__(self):
        super().__init__()


print(C.__mro__)
# C A B
print(C().mark())


# A
#   2) 定义 D(B, A)；打印 D.__mro__ 与 D().mark()
class D(B, A):
    def __init__(self):
        super().__init__()


print(D.__mro__)
# D B A
print(D().mark())


# B
#   3) 菱形验证：定义 Base / L(Base) / R(Base) / Leaf(L, R)，每层 __init__ 先调 super().__init__()，
#      再把本类名追加进 self.log；实例化 Leaf 后打印 .log
class Base:
    def __init__(self):
        self.log = ["Base"]


class L(Base):
    def __init__(self):
        super().__init__()
        self.log.append("L")


class R(Base):
    def __init__(self):
        super().__init__()
        self.log.append("R")


class Leaf(L, R):
    def __init__(self):
        super().__init__()
        self.log.append("Leaf")


print(Leaf.__mro__)
print(Leaf().log)
#   口头作答（答案写在 # 后）：
#   # Q1：MRO 为什么必须是一条线性表，而不是保留继承树？
#   # A1：C3 线性化把树压成一条 有序线性表 ，并保证两条：① 子类永远排在自己父类 之前 （否则子类方法被父类盖掉，违反继承语义）；② 同一类 只出现一次 （菱形里 Base 只算一次，这正是「协作式`super()` 」能成立的前提）。
#   # Q2：C 与 D 只是父类顺序不同，mark() 结果为何会变？
#   # A2：因为往父类找时是根据MRO的顺序去找，父类顺序不同找到的也就不同，而且找到第一个mark()就执行了，不会再往后找了。
