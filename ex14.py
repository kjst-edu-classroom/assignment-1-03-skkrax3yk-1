"""
スクリプト課題 14: 状態を覚える — 行番号をつける（穴埋め少）

実行方法:
    cat samples/fruits.txt | uv run ex14.py

--- 解説 ---

これまでは「いま読んだ1行」だけを見て処理を決めていました。
ここからは、ループの中で **「今までの様子を覚えながら」** 進める書き方を学びます。

行番号をつけるには、ループの**外**で番号用の変数を 1 で初期化し、
ループの中で1行読むごとに 1 ずつ増やします。

    number = 1
    while True:
        ...
        print(f"{number}: {line}")
        number = number + 1

「ループ全体を通して値を覚えておく変数」を **状態変数** と呼びます。

--- 課題 ---

標準入力から1行ずつ読み込み、各行の前に「行番号: 」をつけて表示してください。
行番号は 1 から始めます。

例:
    cat samples/fruits.txt | uv run ex14.py
    （samples/fruits.txt の中身: apple ↵ banana ↵ orange ↵）
    出力: 1: apple
          2: banana
          3: orange
"""

number = ____                  # ヒント: 1から始める
while True:
    try:
        line = input()
    except EOFError:
        break
    print(f"{number}: {line}")
    number = ____ + 1          # ヒント: 今の番号に1を足す
