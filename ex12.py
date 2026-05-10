"""
スクリプト課題 12: フィルター not in — DEBUG を含む行を削除する（穴埋め多）

実行方法:
    cat samples/sample_log.txt | uv run ex12.py

--- 解説 ---

ex11 では「`ERROR` を含む行**だけ**残す」処理でした。
今度は逆で、「`DEBUG` を含む行**以外**を残す」処理です。

「含まれていない」は `not in` で書けます。

    if "DEBUG" not in line:
        print(line)

検索する語を変数 `keyword` に入れると、あとで他の語を検索したくなったときに
1箇所書き換えるだけで済みます。

--- 課題 ---

標準入力から1行ずつ読み込み、変数 `keyword` で指定した語を**含まない**行だけを
表示してください。

例:
    cat samples/sample_log.txt | uv run ex12.py

    出力:
        INFO 2026-05-01 09:00:12 start
        INFO 2026-05-01 09:00:15 ready
        ERROR 2026-05-01 09:01:02 failed to connect
        ERROR 2026-05-01 09:01:05 timeout
        INFO 2026-05-01 09:02:00 finished
"""

keyword = "____"               # ヒント: 削除したい語
while True:
    try:
        line = ____            # ヒント: 標準入力から1行
    except EOFError:
        break
    if keyword ____ line:      # ヒント: 「含まれていない」を表す演算子
        print(____)            # ヒント: 表示するのは line
