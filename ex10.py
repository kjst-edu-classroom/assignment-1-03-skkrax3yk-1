"""
スクリプト課題 10: 文字列の加工 — replace() で特定の文字を削除（スクラッチ）

実行方法:
    cat samples/questions.txt | uv run ex10.py

--- 解説 ---

ex08/ex09 では、**「行ごと」** 削除する処理を書きました（空行を取り除く）。
今回は **「行の中の特定の文字だけ」** を削除します。

そのために `replace()` メソッドを使います。

    "hello".replace("l", "")     # → "heo"   ← l を全部消す
    "Are you OK?".replace("?", "") # → "Are you OK"

「ある文字を空文字列 `""` に置き換える」 = 「その文字を消す」、という言い換えです。

--- 課題 ---

標準入力から1行ずつ読み込み、各行から `?` を削除して表示してください。
（空行はそのまま空行として残します。今回は行を消す処理ではありません）

例:
    cat samples/questions.txt | uv run ex10.py
    （samples/questions.txt: Are you OK? ↵ Yes! ↵ Are you sure? ↵ Why? ↵）
    出力: Are you OK
          Yes!
          Are you sure
          Why

ヒント:
    - while True + try-except EOFError
    - line.replace("?", "") の結果を print
"""

# ここにコードを書いてください
