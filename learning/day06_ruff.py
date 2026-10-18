# Day 6 · Block C ⑥ —— ruff：lint 与格式化
# 前置：ruff 已在 ⑤ 装好（dev 组）。命令都在项目根目录执行。
#
# 【格式约定·必读】作答区内容必须是合法 Python：
#   (a) 长输出 / 片段 → 统一写进下面这个「答卷 docstring」里；
#   (b) 短答 / 口头答 → 写在对应 # 后。
#   严禁直接粘贴裸文本（否则 .py 立刻变成非法语法）。

r"""⑥ 作答区（命令输出贴这里）

—— ⑥-1 `uv run ruff check learning/ --statistics`
（待填）
C:\Users\LeDon\Desktop\Ai Space\python project>uv run ruff check learning/ --statistics
8       I001    [*] unsorted-imports
3       UP039   [*] unnecessary-class-parentheses
1       PLR0124 [ ] comparison-with-itself
1       FURB136 [*] if-expr-min-max
1       B006    [ ] mutable-argument-default
1       PLW0127 [ ] self-assigning-variable
1       F823    [ ] undefined-local
1       C417    [ ] unnecessary-map
1       PIE790  [*] unnecessary-placeholder
1       F401    [*] unused-import
1       F841    [ ] unused-variable
Found 20 errors.
[*] 14 fixable with `--fix` (3 unsafe fixes available with `--fix --unsafe-fixes`).
—— ⑥-2 格式化前后对比 + `git status --short`
（待填）
C:\Users\LeDon\Desktop\Ai Space\python project>git status --short
 M NOTES.txt
 M learning/day01_indent.py
 M learning/day02_calculator.py
 M learning/day03_containers.py
 M learning/day04_functions.py
 M learning/day05_oop.py
 M learning/day05_oop_b.py
 M pyproject.toml
 M uv.lock
?? learning/day06_cache.py
?? learning/day06_deps.py
?? learning/day06_modules.py
?? learning/day06_pkg/
?? learning/day06_pkg_demo.py
?? learning/day06_ruff.py
?? learning/day06_utils.py
?? learning/day06_uv.py
—— ⑥-3 加了 [tool.ruff] 之后的 `--statistics`
（待填）
"""

# TODO ⑥-1（先修流程，再观察）：
#   先把 day06_uv.py 里那几段裸粘贴的作答内容移进它的 docstring（或整段加 #），让文件重新合法；
#   然后执行：uv run ruff check learning/ --statistics
#   —— 观察目标：invalid-syntax 那 58 条还剩多少？剩下的报错分哪几类？

# TODO ⑥-2（动手·格式化）：
#   依次执行：
#     uv run ruff format --check learning/
#     uv run ruff format learning/
#     uv run ruff format --check learning/
#     git status --short
#   —— 观察目标：format 改的是「风格」还是「逻辑」？两次 --check 的数字怎么变？
# 风格，第二次就固定了
# TODO ⑥-3（动手·配置）：在项目根 pyproject.toml 末尾加：
#     [tool.ruff]
#     line-length = 100
#
#     [tool.ruff.lint]
#     select = ["E", "F", "W", "I"]
#   然后重跑 uv run ruff check learning/ --statistics，对比 ⑥-1 的数字（变多还是变少？）
#   —— 观察目标：显式 select 之后，生效的规则集是变宽还是变窄？
# 变窄
#
# TODO ⑥-4（修 bug）：本文件第 13 行那条 invalid-syntax 从哪来？
#   本轮 `uv run ruff check learning/` 只剩 1 条 invalid-syntax，就在**本文件**里：
#       learning\day06_ruff.py:13:5: invalid-syntax: Got unexpected unicode
#   线索：第 13 行是命令行提示符里的 Windows 路径 C:\Users\...，而它躺在**非 raw** 的三引号串里
#   —— 在普通（非 raw）字符串里，反斜杠 + U 是「8 位十六进制 Unicode 转义」的开头 → 直接语法错误。
#   要求：把本文件顶部那个答卷 docstring 改成 **raw** 写法（三引号前加 r），重跑 ruff，确认这条消失。
#
# ？？ 作答区（改完把 ruff 输出的前几行贴回上面答卷区）

#
# TODO ⑥-5（动手·配置）：给「教学文件」加豁免，让统计只剩真问题
#   现象：本轮 58 条里，43 条 E501（行超长）+ 9 条 E402（import 不在文件顶部）
#         —— 这两类主要由**学习文件的排版**造成（长注释、作答区把 import 交错在语句中间），
#         不是真实业务代码的问题。ruff 支持按文件豁免：
#         [tool.ruff.lint.per-file-ignores]
#         "learning/*.py" = ["E501", "E402"]
#   做法：把这段加进 pyproject.toml，重跑 `uv run ruff check learning/ --statistics`
#   —— 观察目标：剩下的是哪几条？各自在哪个文件、是什么代码问题？
#
# ？？ 作答区（剩下的统计贴回上面答卷区）

#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：lint（check）与 format 分别管什么？为什么这两个命令要分开跑？
#   # A1：语义质量和风格。作用不同
#   # Q2（根因）：`select = ["E","F","W","I"]` 里每个前缀各代表什么？不写 select 时生效的是哪一套？
#   # A2：分别对应 pycodestyle 风格错误、Pyflakes 逻辑错误、pycodestyle 风格警告、isort 导入排序。默认以 F (全部) + E (部分子集) 为基础
#   # Q3（Java 对比）：ruff check / ruff format 分别对应 Java 生态里的什么工具？`[tool.ruff.lint] select` 又对应什么？
#   # A3：没有严格对应
