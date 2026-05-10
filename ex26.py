"""
スクリプト課題 26: split で行を分解する（穴埋め少）

実行方法:
    cat samples/people.txt | uv run ex26.py

--- 解説 ---

`split()` は、文字列を空白で区切って **リスト** にして返します。

    "Alice 17".split()
    # → ['Alice', '17']

リストの個々の要素は `[番号]` で取り出します（番号は **0 から始まる**ことに注意）。

    parts = "Alice 17".split()
    parts[0]    # → 'Alice'
    parts[1]    # → '17'

リスト本体はあとの回でしっかり扱います。今回は
「`split()` で分けて、`[番号]` で取り出す」だけに留めます。

--- 課題 ---

各行は「名前 年齢」の形式です（空白区切り）。
名前だけを表示してください。

例:
    cat samples/people.txt | uv run ex26.py
    （samples/people.txt の中身: Alice 17 ↵ Bob 22 ↵ Charlie 30 ↵）
    出力: Alice
          Bob
          Charlie
"""

while True:
    try:
        line = input()
    except EOFError:
        break
    parts = line.____()        # ヒント: 空白で分けるメソッド
    print(parts[____])         # ヒント: 名前は何番目？（0始まり）
