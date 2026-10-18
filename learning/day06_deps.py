# Day 6 · Block B ④ —— pyproject.toml 解剖（≈ Java 的 pom.xml）
# 运行：uv run python learning/day06_deps.py（在项目根目录下跑；脚本用相对路径读 pyproject.toml）
# 说明：用标准库 tomllib 把项目根的 pyproject.toml 读成 dict，逐层取值打印。

# TODO ④-1（三项，各有独立观察目标）：
#   1) 用 tomllib 读取 pyproject.toml，打印 [project] 下的 name 与 dependencies
#      —— 提示：`import tomllib`；`tomllib.load()` 需要**二进制**文件对象（open 时用 "rb"）
#      —— 输出格式：形如  name -> agentic-rag
#
# ？？ 作答区（项1）
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
print("name -> " + f"{data['project']['name']}")
print("dependencies -> " + f"{data['project']['dependencies']}")
#
#   2) 打印 [project] 下的 scripts，以及整个 [build-system] 表
#      —— 观察目标：`agentic-rag = "agentic_rag:main"` 进到数据结构里长什么样（嵌套 dict）
#
# ？？ 作答区（项2）
print(data["project"]["scripts"])
print(data["build-system"])
#
#   3) 打印 [project].requires-python
#      —— 观察目标：版本约束在配置里怎么写的
#
# ？？ 作答区（项3）
print(data["project"]["requires-python"])
#
# 口头作答（写在 # 后；难度递增，前一条为后一条铺路）：
#   # Q1（观察）：pyproject.toml 读进来是什么 Python 类型？各个 [表] 对应什么结构？
#   # A1：dict,dict
#   # Q2（根因）：运行期依赖写在哪个键下？[project.scripts] 又是干什么的？
#   # A2：dependencies,定义入口函数，将入口函数绑定在一个命令名上
#   # Q3（Java 对比）：pyproject.toml 对应 Java 的什么？[project.scripts] + src/agentic_rag/ 这套「命令行入口」机制，Java 靠什么实现？
#   # A3：pom.xml,main方法，jar包
