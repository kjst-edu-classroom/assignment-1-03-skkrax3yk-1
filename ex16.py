"""
スクリプト課題 16: 状態を覚える — 連続する空行を1つにまとめる（穴埋め少、状態の本格導入）

実行方法:
    cat samples/sample_text.txt | uv run ex16.py

--- 解説 ---

ここから本セッションで一番大事な考え方が出てきます。

ex08（空行を全部消す）と違って、こちらは「**連続する**空行を1つにする」処理です。
そのためには、**今の行だけでは判断できません**。
「直前の行が空行だったかどうか」を覚えておく必要があります。

そこで、True / False を覚える状態変数 `previous_blank` を導入します。

  - 空行が来たとき:
      - 前の行も空行なら、何も出力しない
      - 前の行が空行でなかったなら、空行を1つ出力する
      - いずれにせよ「直前は空行」として previous_blank を True に更新する
  - 空行でない行が来たとき:
      - そのまま出力する
      - 「直前は空行ではない」として previous_blank を False に更新する

骨組みは次の通りです:

    previous_blank = False

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "":
            if previous_blank == False:
                print("")
            previous_blank = True
        else:
            print(line)
            previous_blank = False

`previous_blank` のような **「ループの外で用意して、ループの中で更新する」** 変数が
状態を覚える書き方の核心です。

--- 課題 ---

標準入力から1行ずつ読み込み、連続する空行を1つだけ残して表示してください。
1つだけの空行はそのまま残します。空白だけの行も空行として扱います。

例:
    入力: りんご ↵ (空行) ↵ みかん ↵ (空行) ↵ (空行) ↵ バナナ ↵
    出力: りんご
          (空行)
          みかん
          (空行)        ← 連続する空行は1つにまとめられる
          バナナ
"""

previous_blank = ____          # ヒント: 最初は「直前は空行ではない」

while True:
    try:
        line = input()
    except EOFError:
        break

    if line.strip() == "":
        if previous_blank == False:
            print("")
        previous_blank = ____  # ヒント: 今読んだ行は空行だった
    else:
        print(line)
        previous_blank = ____  # ヒント: 今読んだ行は空行ではなかった
