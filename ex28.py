"""
スクリプト課題 28: split — 404 の件数を数える（スクラッチ）

実行方法:
    cat samples/access_log.txt | uv run ex28.py

--- 課題 ---

標準入力から1行ずつアクセスログを読み込み、
ステータスコードが **404** の行が何件あるかを数えて、最後に件数を1行で表示してください。

例:
    cat samples/access_log.txt | uv run ex28.py
    出力: 1

ヒント:
    - status を取り出す方法は ex27 と同じ
    - count を 0 で初期化し、status == 404 のときに 1 ずつ増やす（ex23 と同じ累積）
    - 最後に count を表示
"""

# ここにコードを書いてください
