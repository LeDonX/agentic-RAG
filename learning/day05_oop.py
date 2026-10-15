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

#q1 因为d2并没有在运行时挂doc_id
#q2 应该类似java中打印的是地址


# ===== Block A · 知识点②：self 与 __init__ =====

# TODO ②：
#   1) 给 Document 加 __init__(self, doc_id, text, metadata=None)：
#        · metadata 用 None 占位，函数体里 if metadata is None: metadata = {}（避开 Day4⑦）
#        · 三个属性都挂到 self 上；类补一行 docstring（① 漏了）
class Document:
    def __init__(self, doc_id, text, metadata=None):
        if metadata is None:
            metadata = {}
        self.doc_id = doc_id
        self.text = text
        self.metadata = metadata
#   2) 实例化两份：d1 不传 metadata；d2 传 {"source": "manual.pdf", "page": 3}
d1=Document("doc-001","RAG 是检索增强生成")
d2=Document("doc-001","RAG 是检索增强生成",{"source": "manual.pdf", "page": 3})
#   3) 逐行打印两份的 __dict__，并打印 d1.metadata is d2.metadata（应为 False）
print(d1.__dict__)
print(d2.__dict__) 
print(d1.metadata is d2.metadata)
#   4) 故意删掉一处 self. 前缀，跑一次，把报错原文抄成注释
class Document2:
#TypeError: Document2.__init__() missing 2 required positional arguments: 'doc_id' and 'text'
    def __init__(self, doc_id, text, metadata=None):
        if metadata is None:
            metadata = {}
        doc_id = doc_id
        self.text = text
        self.metadata = metadata
d=Document2("doc-002","RAG 是检索增强生成2",{"source": "manual.pdf", "page": 3})
print("实例化2成功，text =", d.text)
print(d.doc_id)
#   5) 注释回答：d.show() 等价于哪个函数调用？
#Document.show()


# ===== Block A · 知识点③：实例属性 vs 类属性 =====

# TODO ③（6 项，动手前先逐条看一遍）：
#   1) 给 Document 加类属性 category = "general"（写在类体里、__init__ 之外），
#      加注释说明它等价 Java 的什么
#   2) 实例化 d3、d4（不同 doc_id），打印 d3.category / d4.category / Document.category
#   3) 执行 d3.category = "faq"，再打印三者；并打印 d3.__dict__，观察 category 出现在哪里
#   4) 打印 "category" in Document.__dict__（应为 True）
#   5) 执行 Document.category = "kb"，再打印三者，用注释解释：为什么 d4 变了、d3 没变？
#   6) 注释回答：若 category 是 Java 的 static 字段，d3.category = "faq" 会发生什么？与 Python 有何相反之处？