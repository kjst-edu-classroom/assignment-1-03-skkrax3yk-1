"""
スクリプト課題 08: フィルター strip — 空行を削除する（穴埋め少）

実行方法:
    cat samples/sample_text.txt | uv run ex08.py

--- 解説 ---

「中身がある行」だけ表示したいときは、`strip()` を使います。
`strip()` は文字列の前後の空白（スペース・タブ・改行など）を取り除いて返します。

    "  hello  ".strip()    # → "hello"
    "   ".strip()           # → ""
    "".strip()              # → ""

「strip した結果が空文字列でない」 = 「中身がある行」と判定できます。

    if line.strip() != "":
        print(line)

これで空行と「空白だけの行」をまとめて取り除けます。

--- 課題 ---

標準入力から1行ずつ読み込み、空行（および空白だけの行）以外を表示してください。

例:
    入力: りんご ↵ (空行) ↵ みかん ↵ (空行) ↵ バナナ ↵
    出力: りんご
          みかん
          バナナ
"""

while True:
    try:
        line = input()
    except EOFError:
        break
    if line.____() != ____:    # ヒント: 前後の空白除去メソッドと、空文字列リテラル
        print(line)
