"""Day 09 —— 直连 Ollama API：messages 结构。

运行：uv run python learning/day09_ollama_api.py
"""

import httpx

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3.5:9b"
SYSTEM_PROMPT = "你是企业知识库助手，回答简洁。"

# ---------------------------------------------------------------- TODO 1
# 目标：向 /api/chat 发一次「非流式」请求，返回模型回答的纯文本。
# 上下文：messages 的 role 只能是 system / user / assistant，顺序即对话顺序；
#        本次只放 system（人设）+ user（问题）两条。
# 要求：stream 关掉、think 关掉、temperature=0、超时给足 120 秒。
# 输出格式（运行脚本时）形如：Q: 什么是RAG → A: RAG 是……
#
# 交卷前先跑 uv run ruff check learning/day09_ollama_api.py，清到 All checks passed 再交。
#
#   # Q1（观察）：timeout 不传（用默认值）时，第一次请求很可能报 ReadTimeout。
#   #   结合实测 load_duration（约 5.7 秒）说明原因。
#   # A1：默认 timeout 只有 5 秒
#   #
#   # Q2（为什么）：resp.json() 为什么能直接解析？httpx 依据什么判断响应是 JSON？
#   # A2：因为它内部调用标准库的 json 模块对 response.content（原始字节）做 JSON 解码，并不依赖 Content-Type 头来判断是否"是 JSON"。
#   #
#   # Q3（Java 对比）：json= 与 data= 分别对应 Java 里的什么写法？差在哪一步？
#   # A3：RequestBody.create(jsonString, MediaType.get("application/json"))。RequestBody.create(formBody, MediaType.get("application/x-www-form-urlencoded"))
def ask_once(question: str) -> str:
    """发一次非流式请求，返回模型回答的纯文本。"""
    resp = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            "stream": False,
            "think": False,
            "options": {"temperature": 0},
        },
        timeout=120.0,
    )
    return resp.json()["message"]["content"]

# ---------------------------------------------------------------- TODO 2
# 目标：实现 chat()，让模型能「接上文」；再用两轮对话验证。
# 上下文：/api/chat 是无状态的，服务端不保存会话 —— 历史必须每次随请求带上。
#         role=assistant 的条目装的是「模型之前的回答」，靠它模型才记得上文。
# 要求：history 接在 system 之后、当前问题之前一起发；返回答案文本。
# 输出格式（运行脚本时）形如：第1轮: ... / 第2轮: ...
#
# 交卷前先跑 uv run ruff check learning/day09_ollama_api.py，清到 All checks passed 再交。
#
#   # Q1（观察）：第二轮发出去的 messages 一共几条？按顺序各自的 role 是什么？
#   # A1：4,system,user,assistant,user
#   #
#   # Q2（为什么）：如果把第一轮的 assistant 回复删掉，模型还能理解「它」吗？
#   #   这说明 assistant 历史实际在起什么作用？
#   # A2：具体机制是：`assistant` 历史给「它」提供了 指代对象 ，模型靠这条历史把「它」绑定到「RAG」；删掉它，指代就悬空（实测里被消解成不相关的东西）。
#   #
#   # Q3（Java 对比）：这和 Java Web 用 HttpSession 保存会话状态，本质区别在哪？
#   # A3：`/api/chat` 才是 无状态 （历史客户端全量重传），`HttpSession` 是 服务端有状态 （服务端存会话，客户端只带`JSESSIONID` ）

SYSTEM = "回答不超过25字"

def chat(question: str, history: list[dict]) -> str:
    """带上 history 发一轮请求，返回模型回答的纯文本。"""
    messages = [{"role": "system", "content": SYSTEM}]
    if history:
        messages.extend(history)
    messages.append({"role": "user", "content": question})
    resp = httpx.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": messages,
            "stream": False,
            "think": False,
            "options": {"temperature": 0},
        },
        timeout=120.0,
    )
    resp.raise_for_status()
    return resp.json()["message"]["content"]
if __name__ == "__main__":
    question = "用一句话说明什么是 RAG"
    answer = ask_once(question)
    print(f"Q: {question} → A: {answer}")

    # TODO 2 演示区：连续两轮对话并打印
    # 第 1 轮问「什么是 RAG？」，第 2 轮追问「那它和微调有什么区别？」
    history: list[dict] = []

    # 第 1 轮
    q1 = "用一句话说明什么是 RAG"
    a1 = chat(q1, history)
    print(f"第1轮: {a1}")
    history.append({"role": "user", "content": q1})
    history.append({"role": "assistant", "content": a1})
    q2 = "它最大的好处是什么？"
    a2 = chat(q2, history)
    print(f"第2轮: {a2}")
