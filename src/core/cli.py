"""
Khatwa (خطوة) - CLI Interface
Allows running the engine via CLI: python -m src.core.cli
"""
import io
import json
import sys

from src.core.engine import analyze


def main():
    # Ensure stdout/stdin handle UTF-8 cleanly on Windows
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8")

    try:
        input_raw = sys.stdin.read()
        if not input_raw.strip():
            payload = {}
        else:
            payload = json.loads(input_raw)
    except Exception as e:
        payload = {"text": None, "_error": str(e)}

    result = analyze(payload)
    print(json.dumps(result, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
