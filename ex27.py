"""
スクリプト課題 27: split + 条件 — アクセスログから 400 以上の行を抽出（穴埋め多）

実行方法:
    cat samples/access_log.txt | uv run ex27.py

--- 解説 ---

各行は次のように空白で区切られています。

    2026-05-01 09:01:45 /admin 403

`split()` で分けると 4 つの要素になります（インデックスは 0 から）:

    parts = "2026-05-01 09:01:45 /admin 403".split()
    # parts[0] = "2026-05-01"
    # parts[1] = "09:01:45"
    # parts[2] = "/admin"
    # parts[3] = "403"

ステータスコードは 4 番目の要素なので `parts[3]` で取り出せます。
ただし `split()` の結果は文字列なので、数値として比べるには `int()` で変換します。

--- 課題 ---

標準入力から1行ずつアクセスログを読み込み、
ステータスコードが **400 以上** の行だけを表示してください。

例:
    cat samples/access_log.txt | uv run ex27.py

    出力:
        2026-05-01 09:01:45 /admin 403
        2026-05-01 09:02:10 /not-found 404
        2026-05-01 09:04:01 /api/items 500
"""

while True:
    try:
        line = ____            # ヒント: 標準入力から1行
    except EOFError:
        break
    parts = line.____()        # ヒント: 空白で分ける
    status = int(parts[____])  # ヒント: ステータスコードは何番目？
    if status >= ____:         # ヒント: 何以上か？
        print(line)
