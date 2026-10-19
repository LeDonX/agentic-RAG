"""Day 07 —— Block C ⑥：pytest 入门 —— 为 day07_cli 的纯函数写测试。

发现规则：文件名 `test_*.py` 或 `*_test.py`；函数名 `test_*`（无需继承、无需注解）。
    同目录的 `day07_cli.py` 不叫 `test_*`，不会被 pytest 收集 —— 这正是 ⑤ 薄壳的用处：
    import 它不会执行 CLI。

运行：uv run pytest learning/
    （本文件与 day07_cli.py 同目录；无 __init__.py 时 pytest 会把该目录加进 sys.path，直接 import 即可）
"""

from pathlib import Path

import day07_cli
import pytest

# TODO ⑥ —— 用 pytest 测纯函数（普通 assert，不用 assertEquals）
# 目标：在下方作答区写 3 个测试函数：
#  ① test_count_words_counts_repeats —— 给一段含重复词的文本，断言返回 dict 的词频正确
#  ② test_count_words_min_chars_filters —— 断言 min_chars 能把短词滤掉
#  ③ test_iter_files_file_branch —— 以「本目录的 day07_cli.py」为 root：
#       后缀 "py" → 返回只含该文件的单元素 list；后缀 "md" → 空 list
# 起跑点（可直接用）：
#   def test_xxx() -> None:
#       ...
# 提示：断言写裸 `assert 实际 == 期望`；一个测试只盯一个关注点，函数名说明「测什么行为」。
# 交卷前自检：先跑 `uv run ruff check learning/test_day07_cli.py`，清到 All checks passed 再交。

# 作答区（在下面写你的测试函数）：
def test_count_words_counts_repeats() -> None:
    result = day07_cli.count_words("a b a c a")
    assert result == {"a": 3, "b": 1, "c": 1}


# ⑦a 填空：下面框架已搭好（装饰器/签名/断言都由我写好），你只需在 [] 里填 3 行数据。
@pytest.mark.parametrize(
    "text,min_chars,expected",
    [
        # 每行一个 (text, min_chars, expected) 元组，逗号结尾；至少含 min_chars=0 与 text="" → {}
        ("a bb a ccc", 0, {"a": 2, "bb": 1, "ccc": 1}),
        ("a bb a ccc", 2, {"bb": 1, "ccc": 1}),
        ("", 0, {}),
    ],
)
def test_count_words_min_chars_filters(
    text: str, min_chars: int, expected: dict[str, int]
) -> None:
    assert day07_cli.count_words(text, min_chars) == expected


def test_iter_files_file_branch() -> None:
    root = Path(__file__).parent / "day07_cli.py"
    assert day07_cli.iter_files(root, "py") == [root]
    assert day07_cli.iter_files(root, "md") == []

def test_read_missing_file_raises() -> None:
    with pytest.raises(FileNotFoundError):
        Path("no_such_file.txt").read_text(encoding="utf-8")

# TODO ⑦ —— pytest 进阶：parametrize（表驱动多组用例）+ raises（断言异常）
# 目标：
#  ① 用 @pytest.mark.parametrize 把上面的 test_count_words_min_chars_filters 改写成表驱动：
#     参数三件套 (text, min_chars, expected)，至少 3 组，含：
#       · 一组 min_chars=0（代表不过滤）
#       · 一组 text="" → {}
#     提示：parametrize 第一个参数是「参数名串」（如 "text,min_chars,expected"），
#           第二个参数是「每组一个元组的列表」；文件顶部记得 import pytest。
#  ② 新增 test_read_missing_file_raises：用 pytest.raises 断言
#       Path("no_such_file.txt").read_text(encoding="utf-8")
#     会抛 FileNotFoundError。
#     起跑点：with pytest.raises(FileNotFoundError):
#  ③ 运行验证（必须跑）：uv run pytest learning/ -v
#     · 应全绿；并在 -v 输出里确认参数化用例被展开成多行（每行一个用例）。
#
# 交卷前自检：先跑 `uv run ruff check learning/test_day07_cli.py`，清到 All checks passed 再交。
