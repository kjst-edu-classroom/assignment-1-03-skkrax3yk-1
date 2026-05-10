"""
スクリプト課題 21: 累積 + replace — 金額を合計する（穴埋め多）

実行方法:
    cat samples/amounts.txt | uv run ex21.py

--- 解説 ---

ex19（合計）と ex20（カンマ削除）を組み合わせます。
カンマ付きの金額を `replace()` で前処理 → `int()` で数値化 → `total` に足す
という流れです。

なお Python の `int()` は `２５０` のような全角数字もそのまま整数に変換できます。
全角数字を半角にする処理は不要です。

--- 課題 ---

標準入力から1行ずつ金額を読み込み、合計を1行で表示してください。
カンマ付きの数字（"1,200"）にも対応します。

例:
    cat samples/amounts.txt | uv run ex21.py
    入力: 1,200 ↵ 3,500 ↵ 800 ↵ ２５０ ↵
    出力: 5750
"""

total = ____                            # ヒント: 0 から始める
while True:
    try:
        line = ____                     # ヒント: 標準入力から1行
    except EOFError:
        break
    text = line.replace("____", "____") # ヒント: 「カンマを空文字列に」
    number = int(____)                  # ヒント: 数値に変換するもとの文字列
    total = ____ + number               # ヒント: 累積
print(total)
