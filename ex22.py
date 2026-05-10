"""
スクリプト課題 22: 累積 — 累積和 (cumsum) を毎回出す（スクラッチ）

実行方法:
    cat samples/scores.txt | uv run ex22.py

--- 解説 ---

ex19 では、全ての行を読み終わってから合計を **1回だけ** 表示しました。
今回は、1行読むごとに **その時点までの合計** を表示します。
これは「累積和（cumulative sum、cumsum）」と呼ばれる定番の出力です。

ループの中身が `total = total + number` のところまでは ex19 と同じですが、
**`print(total)` をループの内側に置く** だけで、毎回の途中経過が出ます。

--- 課題 ---

標準入力から1行ずつ整数を読み込み、毎回その時点までの累積和を表示してください。

例:
    cat samples/scores.txt | uv run ex22.py
    （samples/scores.txt: 80 ↵ 65 ↵ 90 ↵ 72 ↵ 55 ↵）
    出力: 80
          145         ← 80 + 65
          235         ← 145 + 90
          307         ← 235 + 72
          362         ← 307 + 55

ヒント:
    - total = 0 で初期化
    - while True + try-except EOFError
    - 1行ごとに total = total + int(line) して、すぐ print(total)
"""

# ここにコードを書いてください
