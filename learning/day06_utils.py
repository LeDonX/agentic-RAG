# Day 6 · Block A ①（配套模块）—— 一个 .py 文件就是一个模块
# 说明：本文件是「被导入方」；补全后既可直接运行，也可被同目录的 day06_modules.py 导入。
# 提醒：模块名 = 文件名（day06_utils）；不要给文件起关键字 / 标准库同名（如 json.py）。

# TODO ①-1（三项，各有独立观察目标）：
#   1) 写一个模块级常量 APP_NAME = "agentic-rag"
#   2) 写一个函数 describe(name: str) -> str
#      —— 输出格式：describe("检索") 的结果形如  agentic-rag :: 检索
#   3) 写一个 `if __name__ == "__main__":` 分支，里面打印一行任意中文短句
#
# ？？ 作答区（把三项写成可运行代码）

APP_NAME = "agentic-rag"


def describe(name: str) -> str:
    return f"{APP_NAME} :: {name}"


if __name__ == "__main__":
    print("执行main逻辑")
