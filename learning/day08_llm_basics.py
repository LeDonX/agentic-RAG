"""Day 08 — LLM 应用基础：token、prompt 结构、采样参数、RAG 动机。

今天不碰 API 调用（那是 Day 09），先把「模型的计量单位、消息结构、随机性、幻觉」搞明白。
"""

# ─────────────────────────────────────────────────────────────────
# TODO ①-a 动手：上下文窗口的 token 预算
#   背景：一次问答里，输入（system 提示 + 用户问题 + 检索到的 chunk）
#         和输出（模型回答）**共用**同一个上下文窗口。
#   要求：写一个函数 max_chunks(context_window, reserve_for_answer, tokens_per_chunk) -> int，
#         返回「扣掉回答预算后，最多还能塞下几个 chunk」。
#   形如：reserve=1024 -> <最多 chunk 个数>
#   提示：`//` 整数除法
#
# 交卷前先跑 `uv run ruff check learning/day08_llm_basics.py`，清到 All checks passed 再交


# ✅ 在此作答：
def max_chunks(context_window: int, reserve_for_answer: int, tokens_per_chunk: int) -> int:
    if tokens_per_chunk <= 0:
        raise ValueError("tokens_per_chunk 必须大于 0")
    remaining = context_window - reserve_for_answer
    return max(0, remaining // tokens_per_chunk)

# ─────────────────────────────────────────────────────────────────
# TODO ①-b 动手：把回答预算调大，观察 chunk 数的变化
#   要求：复用 ①-a 的函数，`tokens_per_chunk` 固定，把 reserve 从 1024 换成 8192，
#         两次都打印出来做对比。
#   形如：
#     reserve=1024 -> <个数>
#     reserve=8192 -> <个数>
#   提示：不用改函数，改调用时传的实参即可
#
# 交卷前先跑 `uv run ruff check learning/day08_llm_basics.py`，清到 All checks passed 再交


# ✅ 在此作答：



# ─────────────────────────────────────────────────────────────────
# TODO ①-c 口头：token 与「字符」的关系（两小问，前一问为后一问铺路）
#   # Q1：同一段文本，它的「字符数」和「token 数」为什么不是一回事？
#   #     先答「观察到什么」（谁大谁小、有没有跨语言通用的比例），再答「为什么」。
#   # A1：因为token有专门的统计方式，跟字符不一样。没有跨语言通用的比例。同一段文本换 tokenizer，token 数会变，字符数不变。
#   #
#   # Q2：Java 里不存在「按 token 计量」这套东西，为什么 LLM 应用绕不开它？
#   #     提示：想想 Java 里 String 的长度是怎么数出来的、又是谁在限制长度。
#   # A2：Java 的 String.length() 是 JVM 内部对 UTF-16 code unit 的计数；token 是外部模型词表对文本的切分。约束方不同、单位不同，所以 Java 应用只要对接 LLM，就必须自己把 token 计量这一层补上。

# ─────────────────────────────────────────────────────────────────
# TODO ②-a 动手：拼出符合角色结构的 messages
#   背景：Chat 接口吃的是「消息列表」，每条消息带一个 role，不是一段大字符串。
#   要求：写一个纯函数 build_messages(question, system_prompt) -> list[dict[str, str]]，
#         返回「一条 system + 一条 user」的消息列表。
#   形如：[{'role': 'system', 'content': '...'}, {'role': 'user', 'content': '...'}]
#   提示：注意 system 消息要在列表的第 0 位
#
# 交卷前先跑 `uv run ruff check learning/day08_llm_basics.py`，清到 All checks passed 再交


# ✅ 在此作答：
def build_messages(question: str, system_prompt: str) -> list[dict[str, str]]:
    return [{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': question}]

# ─────────────────────────────────────────────────────────────────
# TODO ②-b 动手：追加一轮对话，且不能改动传进来的原列表
#   背景：模型无状态，多轮对话 = 每次把「历史 + 本轮」整段重发。
#   要求：写 append_turn(messages, question, answer)，返回一个「含新增 user + assistant 两条」的**新列表**，
#         且调用前后原始 messages 的长度不变。
#   形如：原 2 条 -> append_turn(...) 返回 4 条 / 原列表仍是 2 条
#   提示：`+` 与 `append` 在这里的行为不一样，选一个不会改到入参的
#
# 交卷前先跑 `uv run ruff check learning/day08_llm_basics.py`，清到 All checks passed 再交


# ✅ 在此作答：
def append_turn(messages: list[dict[str, str]], question: str, answer: str) -> list[dict[str, str]]:
    user = {'role': 'user', 'content': question}
    assistant = {'role': 'assistant', 'content': answer}
    return messages + [user, assistant,]

# ─────────────────────────────────────────────────────────────────
# TODO ②-c 口头：为什么要分 role（三小问，逐层递进）
#   # Q1：把「你是一个严格的文档助手，只输出 JSON」这条约束写进 system 与写进 user，
#   #     实际效果有什么差别？先想你观察到过的现象，再解释机制。
#   # A1：system比user的优先级高。职责不同：system 定规则和输出格式，user 给本轮输入。
#   #
#   # Q2：模型「不记得上一轮」这件事，跟你熟悉的 HttpSession 有什么本质区别？
#   #     提示：状态到底存在哪一边。
#   # A2：httpsession会保存状态信息，保存在服务端。
#   #
#   # Q3：如果每轮都追加历史，早晚会撞上上下文窗口。你预计撞上时会发生什么？
#   #     （提示：回想 ① 讲的「静默截断」，再想想被丢掉的会是哪一段。）
#   # A3：会将最开始的聊天历史丢掉一部分来容纳新增的聊天记录


if __name__ == "__main__":
    CONTEXT_WINDOW = 8192
    TOKENS_PER_CHUNK = 512

    for reserve in (1024, 8192):
        n = max_chunks(CONTEXT_WINDOW, reserve, TOKENS_PER_CHUNK)
        print(f"reserve={reserve} -> {n}")

# ─────────────────────────────────────────────────────────────────
# TODO ③-a 动手：两套采样参数预设
#   背景：同一个模型，干「抽取/评测」和干「生成回答」需要完全不同的参数。
#   要求：写两个函数，各自返回一个 options 字典（键名用 Ollama 的写法）：
#           stable_options()   —— 面向评测 / 打分 / 结构化抽取
#           creative_options() —— 面向给人看的自然语言回答
#         两套都要显式包含 temperature / top_p / num_predict 三个键，且两套的 temperature 不同。
#   形如：{'temperature': …, 'top_p': …, 'num_predict': …}
#   提示：评测那套的关键诉求是「可复现」，想想 temperature 该给几
#
# 交卷前先跑 `uv run ruff check learning/day08_llm_basics.py`，清到 All checks passed 再交


# ✅ 在此作答：
def stable_options() -> dict:
    """评测 / 打分 / 结构化抽取：可复现优先。"""
    return {
        "temperature": 0.0,
        "top_p": 1.0,
        "num_predict": 512,
    }

def creative_options() -> dict:
    """面向人看的自然语言回答：自然、有变化。"""
    return {
        "temperature": 0.7,
        "top_p": 0.9,
        "num_predict": 1024,
    }

# ─────────────────────────────────────────────────────────────────
# TODO ③-b 动手：合并参数，且不改动任何入参
#   背景：项目里会有「全局默认参数」+「单个调用点的临时覆盖」。
#   要求：写 merge_options(base, override)，返回合并后的**新字典**，override 的同名键胜出；
#         调用后两个入参字典都不能变。
#   形如：base={'temperature': 0.7, 'top_p': 0.9}、override={'temperature': 0}
#         -> 合并结果里 temperature 是 0，且 base 仍是 0.7
#   提示：字典解包 `{**a, **b}`；顺序决定谁覆盖谁
#
# 交卷前先跑 `uv run ruff check learning/day08_llm_basics.py`，清到 All checks passed 再交


# ✅ 在此作答：
def merge_options(base: dict, override: dict) -> dict:
    """合并全局默认参数与单次调用覆盖参数，返回新字典，不改入参。"""
    return {**base, **override}

# ─────────────────────────────────────────────────────────────────
# TODO ③-c 口头：采样参数与「可信度」的关系（三小问，逐层递进）
#   # Q1：把 temperature 从 0 调高，模型的「知识」变了吗？那变的是什么？
#   # A1：没变，变的是相似度的严格程度，越高会显得越宽松
#   #
#   # Q2：为什么评测 / 结构化抽取这类场景必须把 temperature 压到 0？
#   #     提示：想想如果你每天跑一次回归，指标却天天不一样，还能不能归因。
#   # A2：因为这种场景下要求严谨，可复现。
#   #
#   # Q3：`seed` 设成固定值，是不是就能保证「100% 复现」？为什么？
#   #     提示：想想 seed 到底固定了哪一步，而模型推理还有哪些地方会引入差异。
#   # A3：不能，因为大模型本身就是一个概率预测的运行机制，每次都会有变数，而且还有temp这种参数

# ─────────────────────────────────────────────────────────────────
# TODO ④ 口头：幻觉与 RAG 的立项理由（三小问，逐层递进）
#   # Q1：模型为什么会对「它没读过的东西」给出很确定的答案？这是 bug 还是训练目标的副产品？
#   # A1：是**训练目标的副产品**，不是 bug。模型训练时只被奖励「预测下一个 token 要像人写的」，
#   #     从未被要求「不确定就闭嘴」。它没有「我不知道」这个稳定出口 —— 对它来说，
#   #     编一段语法通顺的文字和答对一道题，在损失函数上是一回事。
#   #     今天实测：问《Attention Is All You Need》的训练配置，它输出「single P100 GPU for 30,000 steps」
#   #     并声称是原文引用 —— 真实是 8×P100、100,000 步。编造还带「自我确认」的注解。
#   #
#   # Q2：要解决「模型不知道公司内部文档」，调参 / 微调 / RAG 三条路各解决什么、各有什么代价？
#   #     提示：先问自己「知识到底存在哪」—— 参数里还是上下文里。
#   # A2：
#   #   · 调参（temperature 等）：**完全不解决**。它只改采样随机性，不改参数里的知识。
#   #   · 微调：把知识**写进参数**。改风格/格式效果好；但更新一次要重训、成本高、周期长，
#   #     而且新事实照样会忘、照样会编 —— 知识是「压进权重」的，无法保证逐字准确。
#   #   · RAG：把知识**放进上下文**（参数不动）。文档改了只需重建索引，不重训；
#   #     能给出原文引用；但依赖检索质量 —— 检索不到，模型照样只能瞎答。
#   #   一句话：微调改「怎么说」，RAG 改「依据什么说」。
#   #
#   # Q3：为什么企业场景里，「答案对」还不够，必须带「引用来源」？
#   #     提示：想想出了问题谁来担责、审计要查什么。
#   # A3：因为「看起来对」和「有据可查」是两件事。带引用 = 把答案降级成**可验证的断言**：
#   #     ① 审计能顺着一路查到原始文档第几段；② 出错时能定位是检索错了还是生成错了（Day 34 归因）；
#   #     ③ 用户能自己判断要不要信；④ 责任可追溯到制度原文，而不是「AI 说的」。
#   #     这就是 RAGFlow / bisheng 这类企业级产品的硬指标 —— 没有引用的问答在 To B 场景不能上线。

# ─────────────────────────────────────────────────────────────────
# TODO ⑤ 口头：Ollama 的架构与模型管理（三小问，逐层递进）
#   # Q1：敲下 `ollama run qwen3.5:9b` 之后，实际上是哪两个进程在配合？模型文件放在哪一边？
#   #     （提示：回想今天导出的 `load duration` 与 `eval rate` 分别属于哪个阶段。）
#   # A1：两个进程：`ollama`（CLI 客户端，敲命令的那个）和 `ollama serve`（常驻服务，监听 127.0.0.1:11434）。
#   #     模型文件存在 **server 那一侧** —— `%USERPROFILE%\.ollama\models`（blobs 权重 + manifests 元信息）。
#   #     CLI 只负责发 HTTP 请求、把结果打印出来，它自己不含权重。
#   #
#   # Q2：同一模型第二次调用几乎秒回，第一次却要 6 秒多。这 6 秒花在哪？靠什么机制省掉的？
#   #     提示：关键词 keep_alive；再想想 10GB 显存被占满时会发生什么。
#   # A2：6 秒是 `load duration` —— 把 6.6GB 权重从磁盘读进显存、建好推理上下文，属于**加载阶段**；
#   #     之后的 `eval rate: 49.74 tokens/s` 才是真正的推理阶段。
#   #     省掉它靠 keep_alive：模型用完后默认在显存驻留 5 分钟，期间再调直接复用。
#   #     反例：10GB 显存被别的模型占满时，server 必须先卸载旧模型再加载新的 → 又付一次 6 秒，
#   #     这就是要用 `ollama ps` 看「谁在占显存」的原因。
#   #
#   # Q3：为什么项目代码里要写 `qwen3.5:9b`，而不是只写 `qwen3.5`？
#   #     提示：想想「评测基线突然变了、但你没改一行代码」这种事故怎么发生。
#   # A3：不写 tag 等价于 `qwen3.5:latest`，而 `latest` 会被上游重新指向新版本/新量化。
#   #     一旦你 `ollama pull` 过，线上跑的模型就换了，但 git 里一行代码都没变
#   #     → 评测分数突变却无法归因。锁死带 tag 的完整名（甚至记下 `ollama show` 的 ID / 量化等级），
#   #     才能保证「同代码 = 同模型 = 可复现基线」。
