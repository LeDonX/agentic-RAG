# learning/day04_demo.py — Day 4 · Block A 最小可运行示例（导师示范，先跑通再自己写 TODO）
# 运行：uv run python learning/day04_demo.py

print("===== ① if / elif / else：没有括号，靠冒号 + 缩进 =====")
scores = [95, 72, 40]
for score in scores:
    if score >= 90:
        level = "A"
    elif score >= 60:      # Java 里写 else if
        level = "B"
    else:
        level = "C"
    print(f"{score} -> {level}")

print()
print("===== ② truthiness：哪些值会被 if 当成 False =====")
cases = [
    ("空列表", []),
    ("非空字符串", "张三"),
    ("零", 0),
    ("非空集合", {"py"}),
    ("None", None),
    ("空字典", {}),
    ("空字符串", ""),
]
for label, value in cases:            # 这里复用了 Day 3 的元组解包
    print(f"{label:8} repr={str(value):12} bool={bool(value)}")

print()
print("===== ③ 三元表达式：结果在前、条件在后 =====")
for score in [88, 45, 60, 59]:
    result = "及格" if score >= 60 else "不及格"     # Java: score>=60 ? "及格" : "不及格"
    print(f"{score} -> {result}")

print()
print("===== ④ for...else：循环没被 break 才走 else =====")
for n in (97, 91):
    for i in range(2, n):             # 含头不含尾，等价 Java for (int i = 2; i < n; i++)
        if n % i == 0:
            print(f"{n} 不是质数（被 {i} 整除 → break，else 不执行）")
            break
    else:
        print(f"{n} 是质数（循环完整跑完 → 走 else）")

print()
print("===== ⑤ 没有 switch：工程里用 dict 派发 =====")
handlers = {"+": "加法", "-": "减法", "*": "乘法"}
for op in ("*", "%"):
    print(f"指令 {op} -> {handlers.get(op, '未知指令（走默认分支）')}")
