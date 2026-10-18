students = [
    ("张三", 88),
    ("李四", 72),
    ("王五", 95),
]
# TODO 1：追加一个学生 ("赵六", 60)
students.append(("赵六", 60))
# TODO 2：用 for + tuple 解包，逐行打印 "姓名: 分数"（如 张三: 88）
total = 0
for name, score in students:
    print(f"{name}:{score}")
    total += score
# TODO 3：求平均分并打印（保留 2 位小数，用 Day 2 学的 f-string）
print(f"平均分:{total / len(students):.2f}")


# ===== Block B：dict / set =====

# TODO 4：把上面的 students（list，元素是 (姓名, 分数) 二元组）直接转成 dict，命名 score_map，并打印它
#         提示：dict() 能直接吃「二元组列表」
score_map = dict(students)
print(score_map)
# TODO 5：验证 [] 和 .get() 的差别（Java 工程师最大的惯性坑）
#         5a 用 score_map.get("赵七", 0) 取一个不存在的 key，打印结果
#         5b 再写 score_map["赵七"] 并运行一次，观察抛出的 KeyError（看完把这行注释掉或删掉）
print(score_map.get("赵七", 0))
# print(score_map["赵七"])
# TODO 6：用 for + .items() 遍历 score_map，逐行打印 "姓名 -> 分数"
for name, score in score_map.items():
    print(f"{name}->{score}")
# TODO 7：用 set 运算处理两个班次名单（Java 要调 addAll/retainAll/removeAll，Python 有独立运算符）
morning = {"张三", "李四", "王五", "赵六"}
evening = {"王五", "赵六", "孙七"}
#         7a 交集（两个班次都到的人）用 &
#         7b 并集（所有出现过的人）用 |
#         7c 差集（只在早班、没到晚班的人）用 -
#         三行都打印出来
print(morning & evening)
print(morning | evening)
print(morning - evening)


# ===== Block C：切片 / 推导式 / 解包 =====
scores = [88, 72, 95, 60, 100]

# TODO 8（切片）：用切片打印
#   8a 前 3 个元素
#   8b 后 2 个元素（用负索引）
#   8c 整个列表反转
#   8d 偶数下标元素（步长 2）
print(scores[0:3])
print(scores[-2:])
print(scores[::-1])
print(scores[::2])
# TODO 9（推导式）：
#   9a 用「列表推导式」从 students 中挑出分数 >= 80 的姓名 → 打印
#   9b 用「字典推导式」把 students 转成 {姓名: 分数} → 打印
names = [name for name, score in students if score >= 80]
print(names)

score_dict = {name: score for name, score in students}
print(score_dict)
# TODO 10（解包）：
#   10a first, *rest = scores → 打印 first 与 rest
#   10b a, b = 1, 2；再 a, b = b, a → 打印 a, b
first, *rest = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(first)
print(rest)

a, b = 1, 2
a, b = b, a
print(a, b)

nums = [3, 8, 1, 9, 4]
numbers = [num for num in nums if num > 4]
print(numbers)
