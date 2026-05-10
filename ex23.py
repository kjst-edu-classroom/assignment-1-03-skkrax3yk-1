"""
スクリプト課題 23: 累積 — 件数を数える（穴埋め少）

実行方法:
    cat samples/scores.txt | uv run ex23.py

--- 解説 ---

ex19 では「合計」を累積しました。今度は「件数」を累積します。
「1行読むたびに 1 ずつ増やす」だけで件数を数えられます。

    count = 0
    while True:
        ...
        count = count + 1
    print(count)

これは ex14 の行番号カウンタと同じ仕組みです。
（行番号は「いまの行が何番目か」、件数は「全部で何行あったか」を表すだけの違い）

--- 課題 ---

標準入力から1行ずつ読み込み、最後に何行読んだかを表示してください。

例:
    cat samples/scores.txt | uv run ex23.py
    入力: 80 ↵ 65 ↵ 90 ↵ 72 ↵ 55 ↵
    出力: 5
"""

count = ____                   # ヒント: 0 から始める
while True:
    try:
        line = input()
    except EOFError:
        break
    count = count + ____       # ヒント: 1 ずつ増やす
print(____)                    # ヒント: 件数を表示
