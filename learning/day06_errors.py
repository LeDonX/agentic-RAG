# Day 6 · Block D ⑧ —— 异常处理：try / except / else / finally + raise
# 前置：无（标准库自带）
# 运行：uv run python learning/day06_errors.py
#
# 【格式约定·必读】作答区内容必须是合法 Python：
#   (a) 长输出 / 片段 → 统一写进下面这个「答卷 docstring」里（含 Windows 路径 → 用 r"""）；
#   (b) 短答 / 口头答 → 写在对应 # 后。
#   严禁直接粘贴裸文本（否则 .py 立刻变成非法语法）。

r"""⑧ 作答区（命令输出贴这里）

—— ⑧-1 两种输入下的输出顺序
1 2.0
3 else
4 finally
-- 正常输入 -> 2.0
2 division by zero
4 finally
-- 除零输入 -> nan

—— ⑧-2 traceback 前 6 行
Traceback (most recent call last):
  File "C:\Users\LeDon\Desktop\Ai Space\python project\learning\day06_errors.py", line 86, in <module>
    load_setting("abc")
  File "C:\Users\LeDon\Desktop\Ai Space\python project\learning\day06_errors.py", line 81, in load_setting
    raise RuntimeError(f"配置项 {text!r} 非法") from e
RuntimeError: 配置项 'abc' 非法

—— ⑨-1 输出（导师代跑，修正 `except ParseError` → `except ValueError` 后）
ParseError ValueError
"""

# TODO ⑧-1（动手·执行顺序）：
#   下面 safe_div 已把四个块写全（try / except / else / finally），但一条 print 都没有。
#   请在四个块里各加一条 print 标上块名，然后跑
#     uv run python learning/day06_errors.py
#   —— 两种输入都要跑到：safe_div(6, 3) 与 safe_div(6, 0)
#   —— 输出格式：形如 `1 try` / `3 else`（编号 + 块名，按实际顺序逐行）
#   —— 观察目标：两种输入下各走哪几个块、先后顺序如何？`finally` 有没有被跳过过一次？
#
# ？？ 作答区（两次输出按顺序贴回上面答卷区）
class AppError(Exception):
    """本项目所有业务异常的基类（预期内的错误都从这里派生）。"""

class ParseError(AppError):
    """解析类错误：输入无法按预期格式解析为整数。"""

def safe_div(a: int, b: int) -> float:
    try:
        result = a / b
        print(f"1 {result}")
    except ZeroDivisionError as e:
        print(f"2 {e}")
        return float("nan")
    else:
        print('3 else')
        return result
    finally:
        print('4 finally')
        pass



#
# TODO ⑧-2（动手·raise 与异常链）：
#   起跑点：下面是两个只有签名、身体是占位 `...` 的函数。
#   1) 把 parse_int 补成：把 text 转成 int；转换失败时 **raise** 一个带说明的 ValueError
#      （信息里要含原始输入），并顺手写清 docstring。
#   2) 把 load_setting 补成：调用 parse_int；捕获它抛的 ValueError，再
#      用 `raise RuntimeError(...) from e` 重新抛出（保留原因）。
#   3) 在 __main__ 的最后加一行：load_setting("abc")
#   4) 跑脚本，把 traceback 的 **前 6 行** 贴回作答区
#   —— 观察目标：只用 `raise RuntimeError(...)` 与 `raise ... from e` 相比，traceback 里多了什么？
#
# ？？ 作答区（traceback 前 6 行贴回上面答卷区）


def parse_int(text: str) -> int:
    """把字符串转成整数；失败时 raise ParseError（信息里含原始输入）。"""
    try:
        i = int(text)
        return i
    except ValueError as exc:
        raise ParseError(f"无法把 {text!r} 解析成整数: {exc}") from exc


def load_setting(text: str) -> int:
    """读取一个整数设置；失败时带原因重新抛出。"""
    try:
        value = parse_int(text)
        return value
    except ValueError as e:
        raise RuntimeError(f"配置项 {text!r} 非法") from e

if __name__ == "__main__":
    print("-- 正常输入 ->", safe_div(6, 3))
    print("-- 除零输入 ->", safe_div(6, 0))
    try:
        load_setting("abc")
    except AppError as e:
        print(type(e).__name__, type(e.__cause__).__name__)
    load_setting("abc")  # ⑧-2 的裸调用：放最后，让 ⑨-1 的输出先打出来（此处仍会崩）

#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：Java 的 catch 变量只在 catch 块内可见。Python 的 `except ValueError as e` 里的 e，
#   #            出了 except 块之后再引用，会怎样？（先猜，再写两行验证）
#   # A1：引用不到
#   # Q2（根因）：Java 的方法必须声明 `throws IOException` 才能抛受检异常；Python 为什么完全不用声明？
#   #            运行期不检查异常，对「改一处、崩一片」意味着什么？
#   # A2：Java 的受检异常是编译期的契约提醒；Python 的"不声明"是把契约交给运行期和测试来兑现。
#   # Q3（Java 对比）：`finally` 块里写 `return` 会发生什么？裸 `except:` 与 `except Exception`
#   #            的边界差在哪（提示：`KeyboardInterrupt` 是 `Exception` 的子类吗）？
#   # A3：finally 里的 return 会覆盖 try 或 except 块里已经执行的 return。裸 except: 捕获的是 BaseException，也就是解释器里所有异常,except Exception: 只捕获 Exception 及其子类.不是。KeyboardInterrupt 直接继承自 BaseException，与 Exception 是兄弟关系。所以 except Exception: 不会捕获它，而裸 except: 会。


# ═══ ⑨ 自定义异常 与「异常层次」 ══════════════════════════════════
# TODO ⑨-1（动手·异常层次 + 基类捕获）：
#   起跑点：下面已给出项目异常基类 AppError。
#   1) 定义子类 ParseError(AppError)（只写 docstring 即可）
#   2) 把 parse_int 里那两处 raise 从 ValueError 改成 ParseError（保留 `from exc`）
#   3) 在 __main__ 最后再加一段：
#        try:
#            load_setting("abc")
#        except AppError as e:
#            print(type(e).__name__, type(e.__cause__).__name__)
#   —— 输出格式：形如 `ParseError ValueError`
#   —— 观察目标：except 写的是**父类**、抛的是**子类**，抓得住吗？
#      `e.__cause__` 里装的是什么、又是谁装进去的？
#
# ？？ 作答区（输出贴回上面答卷区）

#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：`except AppError` 能不能抓到 `ParseError`？为什么？（Java 对照：catch 父类抓子类）
#   # A1：能。Python 的 except 匹配遵循 isinstance 语义：except X 会捕获 X 及其所有子类的实例。ParseError 继承自 AppError，所以 ParseError 实例也是 AppError 实例，能被 except AppError 抓住。
#   # Q2（根因）：`e.__cause__` 里装的是哪个对象、由谁装进去？它 ≈ Java 的什么？
#   # A2：装的是最初由 int("abc") 抛出的 ValueError 实例,Throwable.getCause()
#   # Q3（设计·Java 对比）：项目里为什么常约定「一个异常基类 + 按域派生子类」？
#   #            Python 没有受检异常，调用方凭什么知道该捕哪个？
#   # A3：统一兜底：调用方可以 except AppError 一次捕获所有"预期内的业务错误"，同时又能按需捕获具体子类（如 ParseError）做差异化处理——粗细粒度兼顾。AppError 本身就是一个"可预期错误"的语义标记——捕它就够了；需要细化时再看具体子类。
