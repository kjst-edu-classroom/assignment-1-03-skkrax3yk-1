"""
スクリプト課題 01: while True と break — 終了文字 q で止める（穴埋め）

実行方法:
    cat samples/q_demo.txt | uv run ex01.py

または手で:
    uv run ex01.py
    （何行か入力したあと、最後に q だけの行を入力すると終了します）

--- 解説 ---

`while True:` は「ずっと繰り返す」という意味です。
そのままでは無限ループになるので、`break` で抜けられるようにします。

    while True:
        ...
        if 終了の合図:
            break
        ...

ここでは「q だけが入力された行」を終了の合図にします。

--- 課題 ---

q が入力されるまで、入力された行をそのままの形で表示してください。
q が入力されたらループを抜けて終了します（q 自体は表示しません）。

例:
    入力: apple ↵ banana ↵ q ↵
    出力: apple
          banana
"""

while True:
    line = input()
    if line == "q":     # ヒント: 終了文字は何？
        break
    print(line)            # ヒント: 読み込んだ1行をそのまま表示

