"""
スクリプト課題 02: while True と break — 大文字に変換しながら繰り返す（穴埋め）

実行方法:
    cat samples/q_demo.txt | uv run ex02.py

または手で実行（最後に q を入力すると終了）:
    uv run ex02.py

--- 解説 ---

ex01 と同じ「q で終了」の骨組みのまま、出力する内容だけ変えます。
今回は読み込んだ行を **大文字** に変換して表示します。

文字列の大文字化は `.upper()` メソッドで書けます（前回のセッションで学習済み）。

    "hello".upper()   # → "HELLO"

--- 課題 ---

q が入力されるまで、入力された行を大文字に変換して表示してください。

例:
    cat samples/q_demo.txt | uv run ex02.py
    （samples/q_demo.txt の中身: apple ↵ banana ↵ q ↵）
    出力: APPLE
          BANANA
"""

while True:                 # ヒント: 「ずっと繰り返す」
    line = input()             # ヒント: 標準入力から1行読む
    if line == "q":        # ヒント: 終了文字
        break
    print(line.capitalize())      # ヒント: 大文字化のメソッド
