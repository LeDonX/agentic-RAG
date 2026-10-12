# day01_demo.py

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(f"[模块级] __name__ = {__name__}")

if __name__ == "__main__":
    print("[入口] 我是被直接运行的")
    print(greet("LeDon"))