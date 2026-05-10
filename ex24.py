"""
スクリプト課題 24: 累積 — 数値の平均を出す（穴埋め多）

実行方法:
    cat samples/scores.txt | uv run ex24.py

--- 解説 ---

平均 = 合計 ÷ 件数 です。
ex19 の「合計」と ex23 の「件数」を **同時に** 累積するだけで作れます。

    total = 0
    count = 0

    while True:
        ...
        total = total + number
        count = count + 1

    平均 = total / count

ただし、データが1件もない場合（count == 0）に `total / count` を計算すると
ゼロ除算でエラーになります。`if count > 0:` でガードして、
データがなければメッセージを表示します。

    if count > 0:
        print(total / count)
    else:
        print("データがありません")

--- 課題 ---

標準入力から1行ずつ整数を読み込み、平均を表示してください。
入力が1件もないときは `データがありません` と表示してください。

例:
    入力: 80 ↵ 65 ↵ 90 ↵ 72 ↵ 55 ↵
    出力: 72.4
"""

total = ____                   # ヒント: 0 から始める
count = ____                   # ヒント: 0 から始める
while True:
    try:
        line = ____            # ヒント: 標準入力から1行
    except EOFError:
        break
    number = int(line)
    total = total + ____       # ヒント: 数値を足す
    count = count + ____       # ヒント: 件数を1増やす

if count > 0:
    print(total / ____)        # ヒント: 平均の計算
else:
    print("____")              # ヒント: データなしのメッセージ
