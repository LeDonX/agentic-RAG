"""把项目里的 Markdown 笔记转成适合手机阅读的纯文本（无 Markdown 语法）。"""

import re
from pathlib import Path

HR = "────────────────"


def inline(text: str) -> str:
    """处理一行内的 Markdown 行内语法（先保护行内代码，避免把 **kwargs 当粗体）。"""
    codes: list[str] = []

    def stash(match: re.Match[str]) -> str:
        codes.append(match.group(1))
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: m.group(1)
        if m.group(2).startswith("#")
        else f"{m.group(1)}（{m.group(2)}）",
        text,
    )
    text = re.sub(r"\*\*(.+?)\*\*", r"【\1】", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", text)
    text = text.replace("~~", "")
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text.rstrip()


def convert(markdown: str) -> str:
    out: list[str] = []
    in_code = False
    quote_mode = False

    for raw in markdown.splitlines():
        line = raw.rstrip()
        probe = re.sub(r"^(?:\s*>\s?)+", "", line).strip()

        if probe.startswith("```"):
            if not in_code:
                in_code = True
                quote_mode = line.lstrip().startswith(">")
                if out and out[-1].strip():
                    out.append("")
            else:
                in_code = False
                quote_mode = False
                out.append("")
            continue

        if in_code:
            if quote_mode:
                line = re.sub(r"^\s*>\s?", "", line)
            out.append(line)
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level = len(heading.group(1))
            title = inline(heading.group(2))
            if level == 1:
                out.extend(["", "════════════════════════", title, "════════════════════════", ""])
            elif level == 2:
                out.extend(["", "■ " + title, HR, ""])
            elif level == 3:
                out.extend(["", "◆ " + title])
            else:
                out.extend(["", "· " + title])
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", line.strip()):
            out.append("")
            continue

        if re.fullmatch(r"\|[\s:|-]+\|", line.strip()):
            continue

        if line.strip().startswith("|") and line.strip().endswith("|"):
            cells = [inline(c.strip()) for c in line.strip().strip("|").split("|")]
            out.append("  |  ".join(cells))
            continue

        if line.startswith(">"):
            quoted = inline(re.sub(r"^>\s?", "", line))
            out.append("    " + quoted if quoted else "")
            continue

        item = re.match(r"^(\s*)[-*+]\s+(.*)$", line)
        if item:
            out.append(item.group(1) + "· " + inline(item.group(2)))
            continue

        out.append(inline(line) if line.strip() else "")

    cleaned: list[str] = []
    blanks = 0
    for line in out:
        if not line.strip():
            blanks += 1
            if blanks > 2:
                continue
        else:
            blanks = 0
        cleaned.append(line)

    return "\n".join(cleaned).strip() + "\n"


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    for src_name, dst_name in (("NOTES.md", "NOTES.txt"), ("MISTAKES.md", "MISTAKES.txt")):
        src = root / src_name
        dst = root / dst_name
        dst.write_text(convert(src.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"{src_name} -> {dst_name} ({dst.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
