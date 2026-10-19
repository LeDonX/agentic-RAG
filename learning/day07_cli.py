"""Day 07 —— CLI 小工具（文件批处理）+ 为 pytest 做准备。

产出目标：一个「统计目录/文件里文本词数」的小工具。
   · 位置参数：path（文件或目录）
   · 可选参数：--ext（后缀过滤）、--min-chars（字符数阈值）、--top（显示前 N 个）

设计原则（Block B ⑤ 展开）：把「能测的逻辑」写成纯函数，命令行部分只做解析与打印，
   这样 Block C 才能只测纯函数、不碰 stdin/stdout。
"""

# TODO ③ —— argparse 声明式解析
# 目标：实现 build_parser() -> argparse.ArgumentParser，返回一个已定义好参数的解析器：
#   · 位置参数 path（文件或目录路径）
#   · 可选参数 --ext（默认 "txt"）
#   · 可选参数 --min-chars（整数类型，默认 0）
# 然后在 `if __name__ == "__main__":` 里 parse 参数，并打印这三个值，形如 `path=<值>`。
# 提示：argparse 会把 `--xxx-yyy` 自动映射成一个属性名，留意它叫什么。
#
# 运行验证（两条都要跑）：
#   uv run python learning/day07_cli.py . --ext md --min-chars 5
#   uv run python learning/day07_cli.py --help

# 作答区（在下面写你的代码）：
import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="wordcount", description="统计文本文件的词数")
    p.add_argument("path", help="文件或目录路径")
    p.add_argument("--ext", default="txt", help="只处理该后缀")
    p.add_argument("--min-chars", type=int, default=0, help="最小字符数")
    p.add_argument("--top", type=int, default=10, help="显示前 N 个")
    return p



# TODO ④ —— pathlib：找出要处理的文件
# 目标：实现 iter_files(root: Path, ext: str) -> list[Path]
#   · root 是文件：后缀等于 `.<ext>` 就返回 [root]，否则返回 []
#   · root 是目录：递归找出所有后缀为 `.<ext>` 的文件，返回「排好序」的列表
#   · ext 传入时不带点（如 "md"）
# 然后在 __main__ 末尾临时加一行，打印 iter_files(Path(args.path), args.ext)[:3]
# 提示：pathlib 的递归通配是 rglob；它返回生成器，想能排序得先转成 list。
#
# 运行验证：
#   uv run python learning/day07_cli.py learning --ext py

# 作答区（在下面写你的代码）：

def iter_files(root: Path, ext: str) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix==f".{ext}" else []
    if root.is_dir():
        return sorted(root.rglob(f"*.{ext}"))
    return []

def count_words(text: str, min_chars: int = 0) -> dict[str, int]:
    freq: dict[str, int] = {}
    for word in text.split():
        if len(word) >= min_chars:
            freq[word] = freq.get(word, 0) + 1
    return freq

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    total: dict[str, int] = {}
    for path in iter_files(Path(args.path), args.ext):
        text = path.read_text(encoding="utf-8")
        for word, n in count_words(text, args.min_chars).items():
            total[word] = total.get(word, 0) + n

    for word, n in sorted(total.items(), key=lambda kv: (-kv[1], kv[0]))[: args.top]:
        print(f"{word} -> {n}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())


# TODO ⑤ —— 结构拆分：纯函数 + main() + `__main__` 薄壳
# 目标：把本文件改造成「可被 import 测试」的结构，同时仍是可运行 CLI。
#  ① 新增纯函数 count_words(text: str, min_chars: int = 0) -> dict[str, int]：
#     · 按空白切词；统计词频；只保留 len(word) >= min_chars 的词（不打印、不读文件）
#     · 提示：str 有一个方法能直接按「任意空白」切词
#  ② 新增 main(argv: list[str] | None = None) -> int：
#     · 用 build_parser().parse_args(argv) 解析参数
#     · 读 iter_files(...) 得到的每个文件（提示：Path.read_text(encoding="utf-8")），累加词频
#     · 打印 `--top` 指定的前 N 个，形如 `word -> count`；最后返回 0
#     · 删掉现有 __main__ 里的两行临时调试打印
#  ③ `if __name__ == "__main__":` 只留一行薄壳 `raise SystemExit(main())`；
#     并把两个 import（argparse / pathlib）提到文件顶部（消 ruff I001）
#
# 运行验证：
#   uv run python learning/day07_cli.py learning/day07_cli.py --ext py --min-chars 4 --top 5
#   uv run python learning/day07_cli.py learning --ext py --min-chars 4 --top 5

# 作答区（本任务以「改造上方代码」为主，直接在文件内修改；新增函数就近写在 iter_files 之后）：
