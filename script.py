"""
Clean PDF text from the clipboard:
- Merge hard line breaks inside paragraphs
- Preserve paragraph breaks
- Fix hyphenation (gen- der → gender)

Designed for macOS clipboard workflows.
"""

pbpaste | python3 -c '
import sys

text = sys.stdin.read()
lines = [l.rstrip() for l in text.replace("\r", "").split("\n")]

out = []
current = ""

i = 0
while i < len(lines):
    line = lines[i].strip()

    if not line:
        if current:
            out.append(current)
            current = ""
        i += 1
        continue

    if not current:
        current = line
        i += 1
        continue

    # Paragraph break:
    # 1) sentence end + Uppercase
    # 2) short heading line + Uppercase
    if (
        (current.endswith((".", "?", "!")) and line[0].isupper())
        or (len(current) <= 60 and line[0].isupper())
    ):
        out.append(current)
        current = line
        i += 1
        continue

    # Hyphenation join (NO space)
    if current.endswith("-") and line[0].islower():
        current = current[:-1] + line
    else:
        current += " " + line

    i += 1

if current:
    out.append(current)

print("\n\n".join(out))
' | pbcopy
