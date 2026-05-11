"""
スクリプト課題 04: try-except EOFError — 入力が終わったら抜ける（穴埋め少）

実行方法:
    
--- 解説 ---

ファイルやパイプから入力を受けるときは、q のような終了文字は使えません。
入力が尽きたとき、`input()` は `EOFError` という例外を発生させます。
これを `try-except` で受け取って `break` すれば、入力が終わったところで
ループを抜けられます。

    while True:
        try:
            line = input()
        except EOFError:
            brecat 
        # 1行ごとの処理

`try-except` は「やってみて、ダメだったら別の処理」というイメージです。
`if-else` は「先に条件を調べてから処理を分ける」、
`try-except` は「先に処理を実行してみて、失敗したら処理を分ける」点が違います。

--- 課題 ---

標準入力から1行ずつ読み込み、入力が終わるまで各行をそのまま表示してください。

例:
    cat samples/sample_text.txt | uv run ex04.py
    → samples/sample_text.txt の中身がそのまま表示される
"""

while True:
    try:
        line = input()
    except EOFError:       # ヒント: どの例外を受け取る？
        break
    print(line)            # ヒント: 読み込んだ1行
