"""Day 4：控制流与函数（默认参数 / *args **kwargs / 作用域 / lambda）

运行：uv run python learning/day04_functions.py
产出物：一组可复用的工具函数（未来 tools/ 层的雏形）

说明：本文件按「一个知识点一段」推进，每讲完一点追加一段 TODO。
"""

# ===== Block A · 知识点①：if / elif / else =====

scores = [95, 72, 40]

# TODO ①：遍历 scores，按分数给 level 赋值并逐行打印，格式 "<分数> -> <等级>"
#   score >= 90 → "A"
#   score >= 60 → "B"
#   其余        → "C"
#   要求：条件不加括号；多分支用 elif；靠「冒号 + 缩进」分层
for score in scores:
    if score >= 90:
        level = "A"
    elif score >= 60:
        level = "B"
    else:
        level = "C"
    print(f"{score}->{level}")


# ===== Block A · 知识点②：真值判断（truthiness）=====

cases = [
    ("空列表", []),
    ("非空字符串", "张三"),
    ("零", 0),
    ("非空集合", {"py"}),
    ("None", None),
    ("空字典", {}),
    ("空字符串", ""),
]

# TODO ②-A：遍历 cases，逐行打印 "<标签> bool=<bool(值)>"（用 f-string 内嵌 bool(value)）
for label,value in cases:
    print(f"{label:10}bool={bool(value)}")
# TODO ②-B：再遍历一遍，这次判断「它不是 None」，逐行打印 "<标签> is_not_None=<值 is not None>"
#   跑完后对比 A、B 两列：哪些标签的结论不一样？业务上该用哪种写法？
for label,value in cases:
    print(f"{label:10}is_not_None={value is not None}")


# ===== Block A · 知识点③：三元表达式 =====

scores2 = [88, 45, 60, 59]

# TODO ③-A：遍历 scores2，用「一行三元表达式」算出 result（score >= 60 → "及格"，否则 → "不及格"），
#   打印 "<分数> <结果>"。要求写成 X if 条件 else Y 的顺序（结果在前、条件在后）
for score in scores2:
    label = '及格' if score >=60 else '不及格'
    print(f"{score}->{label}")
# TODO ③-B：给定两个数，用三元表达式把较大值赋给 bigger 并打印（不许用内置 max）
a, b = 3, 9
bigger = a if a>b else b
print(f"{bigger}")


# ===== Block A · 知识点④：for...else =====

candidates = [4, 9, 16, 25, 26]

# TODO ④：用 for...else 在 candidates 里查找 target
#   找到 → 打印 "找到了 <target>" 并 break
#   遍历完都没找到 → 由 else 分支打印 "没找到 <target>"
#   要求：else 与 for 对齐（同一缩进级）
#   跑两遍：target = 25（应只输出「找到了」），再把 target 改成 100（应只输出「没找到」）
target = 100
for num in candidates:
    if num == target:
        print('找到了')
        break
else:
    print(f"没找到{target}")


# ===== Block A · 知识点⑤：dict 派发（替代 switch）=====

commands = {"abs": abs, "bin": bin, "hex": hex}

# TODO ⑤：遍历 asked，用 commands.get(name) 查表并派发（不许用 commands[name]）
#   查到（fn 不是 None）→ 打印 f"{name}({value}) -> {fn(value)}"
#   查不到            → 打印 f"{name} -> 未知指令，走默认分支"
#   期望输出：bin(255) -> 0b11111111 / hex(255) -> 0xff / sqrt -> 未知指令，走默认分支
asked = ["bin", "hex", "sqrt"]
value = 255

for name in asked:
    fn = commands.get(name)
    if fn is not None:
        print(f"{name}({value}) -> {fn(value)}")
    else:
        print(f"{name} -> 未知指令，走默认分支")


# ===== Block B · 知识点⑥：函数 def / return / 多返回值 =====

scores_b = [88, 72, 95, 60]

# TODO ⑥-A：定义函数 stats(nums)，用 return 一次返回「平均值」和「最高分」两个值
#   nums 为空时返回 (None, None)（提示：if not nums: ...）
#   然后调用一次，用解包接住并打印，形如 "平均=78.75 最高=95"
#   提示：内置 sum()/len()/max() 直接可用，不用 import
#   期望：print(f"平均={avg} 最高={top}") → 平均=78.75 最高=95；print(stats([])) → (None, None)
def stats(nums):
    if not nums:
        print("数组为空")
        return None,None
    return sum(nums) / len(nums), max(nums)
avg , top = stats(scores_b)
print(f"平均={avg},最高={top}")
print(stats([]))
# TODO ⑥-B：定义函数 describe(nums)，只 print 不 return（打印 "共 <n> 个分数"）
#   然后 r = describe(...) 把返回值接住，再 print(r)，观察是不是 None（体会 Python 没有 void）
#   期望：共 4 个分数 / None
def describe(nums):
    print(f"共{len(nums)}个分数")
r = describe(scores_b)
print(r)


# ===== Block B · 知识点⑦：参数与默认值（可变默认参数陷阱）=====

# TODO ⑦-A（踩坑版）：定义 log_bad(msg, logs=[])，把 msg 追加进 logs 并 return logs
#   连续调用两次（第二次不传 logs）：print(log_bad("a")) / print(log_bad("b"))
#   观察：第二次为什么还带着第一次的内容？（期望 ['a'] 然后 ['a', 'b']）
def log_bad(msg, logs=[]):
    logs.append(msg)
    return logs
print(log_bad("a"))
print(log_bad("b"))
# TODO ⑦-B（修正版）：定义 log_safe(msg, logs=None)，logs is None 时新建 list 再 append
#   同样连续调用两次并打印：确认两次互不影响（期望 ['a'] 然后 ['b']）
def log_safe(msg, logs=None):
    logs = [] if logs is None else logs
    logs.append(msg)
    return logs
print(log_safe("a"))
print(log_safe("b"))
# TODO ⑦-C：打印 log_bad.__defaults__，看默认值是不是被共享的那个 list
#   体会：默认值只在「定义时」求值一次（期望 (['a', 'b'],)）
print(log_bad.__defaults__)


# ===== Block B · 知识点⑧：*args / **kwargs =====
# 同一个符号：定义侧是「收集」，调用侧是「展开」

# TODO ⑧-A（收集位置参数）：定义 total(*nums)，返回 sum(nums)（内置 sum 直接可用）
#   分别调用 print(total(1, 2, 3)) 与 print(total())（体会 total() 合法、返回 0）
#   期望：6 / 0
def total(*nums):
    return sum(nums)
print(total(1,2,3))
print(total())
# TODO ⑧-B（收集关键字参数）：定义 profile(name, **attrs)，打印 f"{name} -> {attrs}"（attrs 是 dict）
#   调用 profile("张三", age=18, city="北京")
#   期望：张三 -> {'age': 18, 'city': '北京'}
def profile(name, **attrs):
    print(f"{name} -> {attrs}")
profile("张三", age=18, city="北京")
# TODO ⑧-C（调用侧展开）：定义 echo(a, b, c) 只 print(a, b, c)
#   然后 pairs = [1, 2, 3] 用 echo(*pairs) 展开调用；info = {"a": 1, "b": 2, "c": 3} 用 echo(**info) 展开调用
#   期望：两次都打印 1 2 3
def echo(a, b, c):
    print(a, b, c)
pairs = [1, 2, 3]
echo(*pairs)
info = {"a": 1, "b": 2, "c": 3}
echo(**info)


# ===== Block B · 知识点⑨：作用域 LEGB =====
# L(局部) → E(外层) → G(全局) → B(内置)；函数里一旦「赋值」某名字，它就默认是局部名

counter = 0

# TODO ⑨-A（复现报错）：定义 try_bump()，函数体内写 `counter = counter + 1`（不声明 global）
#   用 try/except UnboundLocalError 包住调用，打印异常信息
#   期望：UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
def try_bump():
    counter = counter + 1
try:
    print(try_bump())
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
# TODO ⑨-B（改全局）：定义 bump_global()，用 `global counter` 声明后自增并 return
#   print(bump_global()) → 期望 1
def bump_global():
    global counter
    counter = counter + 1
    return counter
print(bump_global())
# TODO ⑨-C（闭包 / nonlocal）：定义 make_counter()，内部 n = 0，
#   再定义 inner() 用 `nonlocal n` 自增并 return n；make_counter 返回 inner
#   然后 c = make_counter()，print(c()) 两次 → 期望 1 然后 2（体会闭包记住了 n）
def make_counter():
    n = 0
    def inner():
        nonlocal n
        n = n + 1
        return n
    return inner
c = make_counter()
print(c())
print(c())


# ===== Block B · 知识点⑩：lambda =====
# lambda 参数: 表达式 —— 只能一个表达式，表达式的值就是返回值（≈ Java lambda，但不能写块）

# TODO ⑩-A（当排序 key）：words = ["banana", "apple", "kiwi"]
#   用 sorted(words, key=lambda w: len(w)) 按长度升序，打印
#   期望：['kiwi', 'apple', 'banana']
words = ["banana", "apple", "kiwi"]
sort = sorted(words,key=lambda x: len(x))
print(sort)
# TODO ⑩-B（配 map）：values = [3, 1, 4, 1, 5, 9, 2]
#   用 list(map(lambda x: x * x, values)) 求平方列表并打印
#   期望：[9, 1, 16, 1, 25, 81, 4]
values = [3, 1, 4, 1, 5, 9, 2]
value = list(map(lambda x:x*x, values))
print(value)
# TODO ⑩-C（当 max 的 key）：people = [("张三", 88), ("李四", 95), ("王五", 72)]
#   用 max(people, key=lambda p: p[1]) 找出分数最高的人并打印
#   期望：('李四', 95)
people = [("张三", 88), ("李四", 95), ("王五", 72)]
top=max(people,key=lambda p:p[1])
print(top)