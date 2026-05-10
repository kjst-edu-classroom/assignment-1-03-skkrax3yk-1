"""
スクリプト課題 06: try-except EOFError — 行頭に "> " をつける（穴埋め多）

実行方法:
    cat samples/greetings.txt | uv run ex06.py

--- 課題 ---

EOF まで、各行の前に "> " をつけて表示してください。
今度は骨組みの空欄が増えています。ex04・ex05 を見ながら埋めましょう。

例:
    cat samples/greetings.txt | uv run ex06.py
    （samples/greetings.txt の中身: hello ↵ world ↵）
    出力: > hello
          > world
"""

while True:
    try:
        line = ____             # ヒント: 標準入力から1行
    except ____:                # ヒント: どの例外を受け取る？
        ____                    # ヒント: ループを抜ける
    print("> " + ____)          # ヒント: 読んだ1行
