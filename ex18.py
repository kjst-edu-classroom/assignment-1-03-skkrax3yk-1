"""
スクリプト課題 18: 状態を覚える — 同じ行が連続したら2回目以降を出さない（スクラッチ）

実行方法:
    cat samples/duplicates.txt | uv run ex18.py

--- 解説 ---

これも「直前の行を覚える」状態変数のパターンです。
今度は **直前の行の内容そのもの** を覚えておきます。
（「直前の行が空行か」ではなく「直前の行は何だったか」）

骨組み:

    previous_line = None    # まだ何も読んでいない印
    while True:
        ...
        if line != previous_line:
            print(line)
        previous_line = line   # 今読んだ行を覚える

`None` は「まだ値がない」ことを表す特別な値です（最初は previous_line が
何でもないので、必ず1行目は出力されます）。

--- 課題 ---

標準入力から1行ずつ読み込み、直前と同じ行が連続したら2回目以降を表示しません
（重複削除）。直前と違う内容の行だけ表示してください。

例:
    cat samples/duplicates.txt | uv run ex18.py
    （samples/duplicates.txt: apple ↵ apple ↵ banana ↵ banana ↵ banana ↵ orange ↵）
    出力: apple
          banana
          orange

ヒント: 最初は previous_line = None としておくと、1行目は必ず出力されます。
"""

# ここにコードを書いてください
