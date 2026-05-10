"""
スクリプト課題 05: try-except EOFError — 大文字で出力（穴埋め）

実行方法:
    cat samples/greetings.txt | uv run ex05.py

--- 課題 ---

ex04 と同じ「EOF まで繰り返す」骨組みのまま、出力を大文字に変えます。
入力が尽きるまで、各行を大文字に変換して表示してください。

例:
    cat samples/greetings.txt | uv run ex05.py
    （samples/greetings.txt の中身: hello ↵ world ↵）
    出力: HELLO
          WORLD
"""

while True:
    try:
        line = ____         # ヒント: 標準入力から1行
    except EOFError:
        ____                # ヒント: ループを抜ける
    print(line.____())      # ヒント: 大文字化
