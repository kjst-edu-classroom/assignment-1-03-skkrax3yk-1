"""
スクリプト課題 19: 累積 — 数値の合計を出す（穴埋め少）

実行方法:
    cat samples/scores.txt | uv run ex19.py

--- 解説 ---

集計（合計を出す）も状態変数の応用です。次の3ステップで書けます。

  1. ループの**外**で、合計を入れる変数を 0 で用意する
  2. ループの中で、1行読むたびに合計に足す
  3. ループが終わったあとで、合計を表示する

    total = 0

    while True:
        try:
            line = input()
        except EOFError:
            break
        number = int(line)
        total = total + number

    print(total)

`total = total + number` は「いまの total に number を足したものを、
新しい total にする」という意味です。
（数学の等式ではなく、右辺を計算してから左辺の変数に入れ直す代入文）

--- 課題 ---

標準入力から1行ずつ読み込みます。各行には1つだけ整数が書かれています。
全ての行を読み終わったら、合計を1行で表示してください。

例:
    入力: 80 ↵ 65 ↵ 90 ↵ 72 ↵ 55 ↵
    出力: 362
"""

total = ____                   # ヒント: 0 から始める
while True:
    try:
        line = input()
    except EOFError:
        break
    number = int(line)
    total = total + ____       # ヒント: 今読んだ数値を足す
print(total)
