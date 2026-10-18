a = input("数字")
aa = float(a)
b = input("运算符")
c = input("数字")
cc = float(c)

if b == "+":
    print(f"{aa + cc}")
elif b == "-":
    print(f"{aa - cc}")
elif b == "*":
    print(f"{aa * cc}")
elif b == "/":
    if cc == 0:
        print("除数不能为零")
    else:
        print(f"{aa / cc:.2f}")
else:
    print("输入有误")
