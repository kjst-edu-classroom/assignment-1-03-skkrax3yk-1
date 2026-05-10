"""
スクリプト課題 17: 状態を覚える — 連続空行をまとめる（穴埋め多）

実行方法:
    cat samples/sample_text.txt | uv run ex17.py

--- 解説 ---

ex16 と同じ「連続する空行を1つに」を、**より多くの穴を埋めて** 完成させます。
状態変数 `previous_blank` の使い方をしっかり手に染み込ませましょう。

--- 課題 ---

ex16 と同じ仕様（連続する空行を1つにまとめる）を実装してください。

例:
    入力: a ↵ (空行) ↵ (空行) ↵ (空行) ↵ b ↵
    出力: a
          (空行)
          b
"""

previous_blank = ____                   # ヒント: 最初は「直前は空行ではない」

while True:
    try:
        line = ____                     # ヒント: 標準入力から1行
    except ____:                        # ヒント: 入力終了の例外
        break

    if line.____() == "":               # ヒント: 前後の空白を除いて判定
        if previous_blank == False:
            print("")
        previous_blank = ____           # ヒント: 直前は空行
    else:
        print(line)
        previous_blank = ____           # ヒント: 直前は空行ではない
