# Clean PDF Clipboard (macOS)

A small macOS automation that turns messy PDF copy-paste
into clean, readable text — with one keyboard shortcut.

## What it fixes

When copying text from PDFs:
- Hard line breaks split sentences
- Paragraphs are broken incorrectly
- Hyphenation artifacts remain (e.g. gen- der)

This tool cleans the clipboard before you paste.

## What it does

- Merges line breaks inside paragraphs
- Preserves real paragraph breaks
- Fixes PDF hyphenation automatically
- Works in any app (VS Code, Notes, Word, Obsidian)

## Requirements

- macOS
- Python 3 (preinstalled on macOS)
- Automator

## How to use

1. Copy text from a PDF
2. Press your assigned shortcut
3. Paste anywhere

## Setup

See the step-by-step guide in the Figma page:
[link here]

Or:
- Open Automator
- Create a Quick Action
- Add “Run Shell Script”
- Paste the script from `script/clean_pdf_clipboard.py`
- Assign a keyboard shortcut

## License

MIT



> If this saved you time and mental energy,
feel free to [support me](https://buymeacoffee.com/echozhao) — but there is no obligation.

