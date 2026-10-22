"""Day 09 Block B —— 流式输出：/api/chat 的 NDJSON。

运行：uv run python learning/day09_ollama_api_b.py
"""

import json

import httpx

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3.5:9b"
SYSTEM_PROMPT = "回答不超过25字"


# ---------------------------------------------------------------- TODO 3
# 目标：开启流式，边生成边打印，最后返回完整答案并报告 token 数。
# 上下文：stream=true 时服务端按行下发，每行是一个独立 JSON（NDJSON），不是标准 SSE；
#         一条消息会被拆成几十个碎片，最后一行 done=true（content 为空串）。
# 要求：逐行解析、实时打印碎片、累加出完整文本，并打印形如 [tokens=31] 的统计。
# 提示：httpx.stream("POST", ...) + resp.iter_lines()
# 输出格式（运行脚本时）形如：RAG（检索增强生成）…… 然后 [tokens=31]
#
# 交卷前先跑 uv run ruff check learning/day09_ollama_api_b.py，清到 All checks passed 再交。
#
#   # Q1（观察）：每个 chunk 里的 content 是什么粒度？done=true 那一行的 content 是什么？
#   # A1：token 级。done=true 那行 content 是空串 ""，只携带统计字段（eval_count 等）。
#   #
#   # Q2（为什么）：先 httpx.post() 拿整包、再 iter_lines()，为什么"看起来一样"却没有流式效果？
#   # A2：httpx.post() 默认会把响应体整个读完才返回 Response，此时 iter_lines() 迭代的是内存里已完整的内容，本地逐行遍历没有"边收边给"，网络层早已结束。
#   #
#   # Q3（Java 对比）：iter_lines() 对应 Java 里哪种写法？为什么 Python 用 for 就够？
#   # A3：对应 BufferedReader.readLine() 的 while 循环，因为 iter_lines() 返回生成器，实现 __iter__/__next__，for 自动驱动 next() 直到StopIteration；Java 的流对象需要显式 readLine() 或 Stream.forEach 才等价。


def stream_answer(question: str) -> str:
    """流式请求，边打印边累加，返回完整答案。"""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        "stream": True,
        "think": False,
        "options": {"temperature": 0},
    }

    parts: list[str] = []
    tokens = 0
    with httpx.stream("POST", OLLAMA_URL, json=payload, timeout=120.0) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():
            if not line:                      # 理论上 NDJSON 没有空行，防御一下
                continue
            chunk = json.loads(line)
            piece = chunk.get("message", {}).get("content", "")
            if piece:
                print(piece, end="", flush=True)   # 实时输出，必须 flush
                parts.append(piece)
            if chunk.get("done"):
                tokens = chunk.get("eval_count", 0)

    print(f"\n[tokens={tokens}]")
    return "".join(parts)

# ---------------------------------------------------------------- TODO 5
# 目标：把网络失败转成可读提示，绝不让异常穿透到调用方。
# 上下文：三类失败对应三个异常 —— ConnectError（连不上）、ReadTimeout（读超时）、
#         HTTPStatusError（4xx/5xx，必须先 raise_for_status 才会抛）。
# 要求：成功返回答案文本；失败返回以「出错：」开头的中文提示（三类分别给不同措辞）。
# 提示：url 的默认值指向模块常量 OLLAMA_URL，便于测试「连不上」分支。
# 输出格式（运行脚本时）形如：出错：无法连接 Ollama……
#
# 交卷前先跑 uv run ruff check learning/day09_ollama_api_b.py，清到 All checks passed 再交。
#
#   # Q1（为什么）：ReadTimeout 为什么不是「总时长上限」？流式下这个区别会导致什么实际差异？
#   # A1：它是多久时间没收到新消息，流式下只要收到消息就重置
#   #
#   # Q2（为什么）：为什么必须调用 raise_for_status() 才能捕到 HTTPStatusError？
#   # A2：HTTPStatusError 不是 HTTP 层"发生"的错误，是 raise_for_status() 根据状态码人为"宣布"的错误。
#   #
#   # Q3（结构）：为什么 try 要包住整个 with 块，而不是只包 httpx.stream(...) 这一行？
#   # A3：因为异常可能出现在with块中


def safe_answer(question: str, url: str = OLLAMA_URL) -> str:
    """带错误兜底的单轮问答；失败时返回中文提示而不是抛异常。"""
    try:
        resp = httpx.post(
            url,
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
            timeout=httpx.Timeout(10.0, read=30.0),   # 连接 10s、读 30s
        )
        resp.raise_for_status()                        # 4xx/5xx 在这里抛 HTTPStatusError
        return resp.json()["message"]["content"]

    except httpx.ConnectError:
        return f"出错：无法连接 Ollama，请确认服务已启动（{url}）"
    except httpx.TimeoutException:
        return "出错：Ollama 响应超时（连接/读取阶段超时）"
    except httpx.HTTPStatusError as exc:
        # exc.response 一定存在；尽量取服务端 error 字段，取不到就退回状态码
        detail = ""
        try:
            detail = exc.response.json().get("error", "")
        except Exception:                              # noqa: BLE001 — 错误体不是 JSON 时兜底
            detail = exc.response.text[:200]
        return f"出错：Ollama 返回 {exc.response.status_code}，{detail or '无详细信息'}"


if __name__ == "__main__":
    print("A: ", end="")
    answer = stream_answer("用一句话说明什么是 RAG")
    print(f"\n[完整答案] {answer}")

    print(safe_answer("什么是 RAG"))
    print(safe_answer("什么是 RAG", "http://127.0.0.1:11435/api/chat"))
