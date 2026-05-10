"""
スクリプト課題 11: フィルター in — ERROR を含む行だけ表示する（穴埋め少）

実行方法:
    cat samples/sample_log.txt | uv run ex11.py

--- 解説 ---

`in` 演算子を使うと、「ある文字列が別の文字列に含まれているか」を調べられます。

    "foo" in "foobar"     # → True
    "baz" in "foobar"     # → False

これを使うと、`grep` のように「特定の語を含む行だけ取り出す」処理ができます。

    if "ERROR" in line:
        print(line)

--- 課題 ---

標準入力から1行ずつ読み込み、`ERROR` という語を含む行だけを表示してください。

例:
    cat samples/sample_log.txt | uv run ex11.py
    → ERROR を含む行（2行）だけが表示される

    出力:
        ERROR 2026-05-01 09:01:02 failed to connect
        ERROR 2026-05-01 09:01:05 timeout
"""

while True:
    try:
        line = input()
    except EOFError:
        break
    if "____" ____ line:       # ヒント: 探したい語と、含まれているか調べる演算子
        print(line)
