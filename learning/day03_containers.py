students = [
    ( "张三" , 88 ),
    ( "李四" , 72 ),
    ( "王五" , 95 ),
]
# TODO 1：追加一个学生 ("赵六", 60)
students.append(("赵六", 60))
# TODO 2：用 for + tuple 解包，逐行打印 "姓名: 分数"（如 张三: 88）
total=0
for name,score in students:
    print(f"{name}:{score}")
    total+=score
# TODO 3：求平均分并打印（保留 2 位小数，用 Day 2 学的 f-string）
print(f"平均分:{total/len(students):.2f}")
