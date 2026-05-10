"""
スクリプト課題 20: 変換 replace — カンマを取り除く（穴埋め少）

実行方法:
    cat samples/amounts.txt | uv run ex20.py

--- 解説 ---

文字列の `replace()` メソッドは、文字列の中の特定の文字を別の文字に置き換えます。

    "hello".replace("l", "L")     # → "heLLo"
    "1,200".replace(",", "")      # → "1200"  （カンマを「何もなし」に置き換え＝削除）

「`,` を `""`（空文字列）に置き換える」 = 「カンマを消す」、という言い換えです。

このセッションでは、カンマ付きの金額（`"1,200"`）を `int()` で数値化する
前処理として replace() を使います。

--- 課題 ---

標準入力から1行ずつカンマ付きの数字を読み込み、カンマを取り除いた文字列を
そのまま表示してください（まだ合計はとりません）。

例:
    cat samples/amounts.txt | uv run ex20.py
    （samples/amounts.txt の中身: 1,200 ↵ 3,500 ↵ 800 ↵ ２５０ ↵）
    出力: 1200
          3500
          800
          ２５０       ← カンマがないのでそのまま
"""

while True:
    try:
        line = input()
    except EOFError:
        break
    text = line.____("____", "____")    # ヒント: replace, 消したい文字, 置き換え後（空文字列）
    print(text)
