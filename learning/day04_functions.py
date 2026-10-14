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

# TODO ⑥-B：定义函数 describe(nums)，只 print 不 return（打印 "共 <n> 个分数"）
#   然后 r = describe(...) 把返回值接住，再 print(r)，观察是不是 None（体会 Python 没有 void）