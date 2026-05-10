"""
スクリプト課題 15: 状態を覚える — 0埋め2桁の行番号（穴埋め多）

実行方法:
    cat samples/fruits.txt | uv run ex15.py

--- 解説 ---

f-string では、`{number:02d}` のように書くと、整数を **2桁・0埋め** で表示できます。

    number = 3
    print(f"{number:02d}")    # → "03"

ex14 と同じ「ループ外で初期化、ループ中で +1」という状態変数の使い方ですが、
出力の書式だけ変えます。

--- 課題 ---

標準入力から1行ずつ読み込み、行番号を 2桁・0埋め にして
「01: apple」のように表示してください。

例:
    cat samples/fruits.txt | uv run ex15.py
    （samples/fruits.txt の中身: apple ↵ banana ↵ orange ↵）
    出力: 01: apple
          02: banana
          03: orange
"""

number = ____                       # ヒント: 1から始める
while True:
    try:
        line = ____                 # ヒント: 標準入力から1行
    except ____:                    # ヒント: 入力終了の例外
        break
    print(f"{number:02d}: {____}")  # ヒント: 1行の内容
    number = number + ____          # ヒント: 1ずつ増やす
