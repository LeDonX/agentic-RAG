# Day 6 · Block B ⑤ —— uv 工作流（动手改真实项目文件）
# 本文件不含代码：把「动手结果」与「口头答案」写在各作答区。
# 前置：所有命令都在项目根目录执行。

# TODO ⑤-1（动手 · 真实项目文件）：给项目加开发期依赖 mypy
#   —— 执行：uv add --dev mypy
#   —— 做法：执行后打开 pyproject.toml，把「新增的那一整段」原样贴到下面
#
# ？？ 作答区（贴 pyproject.toml 新增片段）
# [dependency-groups]
# dev = [
# "mypy>=2.4.0",
# ]
#
# TODO ⑤-2（动手）：再加一个 dev 依赖 ruff，观察 dev 组是「追加」还是「覆盖」
#   —— 执行：uv add --dev ruff
#   —— 写下结论（追加还是覆盖？），并贴出 dev 组最终内容
#
# ？？ 作答区
# 追加
# [dependency-groups]
# dev = [
# "mypy>=2.4.0",
# "ruff>=0.17.1",
# ]
#
# TODO ⑤-3（观察）：确认环境真装上了
#   —— 依次执行：uv run mypy --version、uv tree
#   —— 把两条命令的真实输出贴回来
#
# ？？ 作答区
# mypy 2.4.0 (compiled: yes)

# Resolved 8 packages in 0.73ms
# agentic-rag v0.1.0
# ├── mypy v2.4.0 (group: dev)
# │   ├── ast-serialize v0.13.1
# │   ├── librt v0.16.0
# │   ├── mypy-extensions v1.1.0
# │   ├── pathspec v1.1.1
# │   └── typing-extensions v4.16.0
# └── ruff v0.17.1 (group: dev)
#
# TODO ⑤-4（判断项，不必真改，但必须给结论 + 依据）：
#   build-system 里为什么写成 `uv_build>=0.12.24,<0.13.0`？本机需要改这个上限吗？什么情况下才需要改？
#
# ？？ 作答区
# 用来限制uv版本的范围，次版本号可能带来未知的问题。本机不需要改，需要使用更高版本的功能时可以改
#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：`uv add --dev mypy` 之后，pyproject.toml / uv.lock / .venv 三处各发生了什么？`uv sync` 又是干什么的？
#   # A1：uv 会在 pyproject.toml 中新增一个 [dependency-groups] 表，并创建一个 dev 组来存放 mypy。uv 会重新解析依赖关系，并在 uv.lock 中记录 mypy 及其所有传递依赖的精确版本、哈希值，以及在不同平台/ Python 版本下的解析结果。uv 会将 mypy 及其依赖实际安装到项目的虚拟环境 .venv 中。
#   # Q2（根因）：为什么 dev 依赖要和运行期依赖分开写？为什么 `uv run python xxx.py` 不用手动 activate 虚拟环境？
#   # A2：运行期依赖是“别人用你的包时需要的”，dev 依赖是“你自己开发时需要的”，两者的受众完全不同。activate 是改环境（当前 shell 变脏，需手动还原），uv run 是给子进程穿衣服（父进程干净，子进程用完即弃）
#   # Q3（Java 对比）：uv 的 pyproject.toml / uv.lock / .venv 三件套，分别对应 Java 世界里的什么？和 Maven 的本地仓库（~/.m2）相比，关键差异是什么？
#   # A3：pyproject对应pom，其他两个没有。maven是全局缓存，项目用哪个取哪个加载，uv是跟着项目走
