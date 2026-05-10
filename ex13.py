"""
スクリプト課題 13: 複数キーワード — or で組み合わせる（スクラッチ）

実行方法:
    cat samples/sample_log.txt | uv run ex13.py

--- 解説 ---

ここまでで、

  - ex11: ある語を **含む** 行を表示（`in`）
  - ex12: ある語を **含まない** 行を表示（`not in`）

を学びました。今回は、複数の条件を `or`（「どちらか」）で組み合わせます。

    if "ERROR" in line or "INFO" in line:
        print(line)

これは「`ERROR` を含む **または** `INFO` を含む」ときに表示する、という意味です。

`or` の他に `and`（「両方」）もあります。
たとえば `if "ERROR" in line and "DEBUG" not in line:` のように
複数条件を組み合わせて、もっと複雑なフィルターも書けます。

--- 課題 ---

標準入力から1行ずつ読み込み、`ERROR` **または** `INFO` を含む行だけを表示してください。
（`DEBUG` を含む行は表示しません）

例:
    cat samples/sample_log.txt | uv run ex13.py

    出力:
        INFO 2026-05-01 09:00:12 start
        INFO 2026-05-01 09:00:15 ready
        ERROR 2026-05-01 09:01:02 failed to connect
        ERROR 2026-05-01 09:01:05 timeout
        INFO 2026-05-01 09:02:00 finished
"""

# ここにコードを書いてください
