"""
スクリプト課題 09: フィルター strip — 空行削除＋前後の空白も除く（穴埋め多）

実行方法:
    cat samples/whitespace_demo.txt | uv run ex09.py

--- 解説 ---

ex08 では、空行を取り除いたあと **元の line をそのまま** 出力していました。
今回は、出力する前に **strip した結果**（前後の空白を除いた文字列）を
変数 `text` に取り出し、それを判定にも出力にも使います。

    text = line.strip()
    if text != "":
        print(text)

`strip()` を1度だけ呼んで、その結果を使い回す書き方です。

--- 課題 ---

標準入力から1行ずつ読み込み、各行の前後の空白を除いた結果を変数 text に入れます。
text が空文字列でなければ text を表示してください。

例:
    cat samples/whitespace_demo.txt | uv run ex09.py
    （samples/whitespace_demo.txt: 前後に空白付きの行や、空白だけの行が混じる）
    出力: apple
          banana
"""

while True:
    try:
        line = ____            # ヒント: 標準入力から1行
    except EOFError:
        break
    text = line.____()         # ヒント: 前後の空白を除く
    if ____ != "":             # ヒント: text が空文字列でないか
        print(____)            # ヒント: 出力するのは text
