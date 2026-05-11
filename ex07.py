"""
スクリプト課題 07: try-except EOFError — 行末に "!" をつける（スクラッチ）

実行方法:
    cat samples/greetings.txt | uv run ex07.py

--- 課題 ---

標準入力から1行ずつ読み込み、入力が終わるまで各行の末尾に "!" をつけて表示してください。
今度は骨組みから自分で書きます。ex04〜06 を見ながら、

  - while True
  - try-except EOFError で break
  - 1行ごとに print

の構造を再現してください。

例:
    cat samples/greetings.txt | uv run ex07.py
    （samples/greetings.txt の中身: hello ↵ world ↵）
    出力: hello!
          world!
"""

# ここにコードを書いてください
while True:
  try:
    line=input()
  except EOFError:
    break

  print(line+"!")