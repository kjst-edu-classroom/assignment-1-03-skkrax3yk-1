"""スクリプト課題の公開テスト

各 ex??.py は標準入力から1行ずつ読み込み、結果を標準出力に書く。
ここでは subprocess.run() の input= 引数で stdin を渡してテストする。

テストクラスは grading.toml の採点グループと対応:
  TestWhileBreak     ex01〜03
  TestEOFError       ex04〜07
  TestStripFilter    ex08〜10
  TestInFilter       ex11〜13
  TestState          ex14〜18
  TestAccumulator    ex19〜22
  TestAverage        ex23〜25
  TestSplit          ex26〜28
"""

import subprocess


def run_script(filename, stdin=""):
    """スクリプトを stdin 付きで実行し、CompletedProcess を返す。"""
    return subprocess.run(
        ["uv", "run", filename],
        input=stdin,
        capture_output=True,
        text=True,
        timeout=10,
    )


SAMPLE_TEXT = "りんご\n\nみかん\n\n\nバナナ\n価格は１００円です。\n個数は３個です。\n\n\n合計は３００円です。\n"
SAMPLE_LOG = (
    "INFO 2026-05-01 09:00:12 start\n"
    "DEBUG 2026-05-01 09:00:13 loading config\n"
    "INFO 2026-05-01 09:00:15 ready\n"
    "ERROR 2026-05-01 09:01:02 failed to connect\n"
    "DEBUG 2026-05-01 09:01:03 retry count = 1\n"
    "ERROR 2026-05-01 09:01:05 timeout\n"
    "INFO 2026-05-01 09:02:00 finished\n"
)
AMOUNTS = "1,200\n3,500\n800\n２５０\n"
SCORES = "80\n65\n90\n72\n55\n"
ACCESS_LOG = (
    "2026-05-01 09:00:12 /index.html 200\n"
    "2026-05-01 09:01:45 /admin 403\n"
    "2026-05-01 09:02:10 /not-found 404\n"
    "2026-05-01 09:04:01 /api/items 500\n"
    "2026-05-01 09:05:12 /about.html 200\n"
)


# ============================================================================
# グループ1: while True と break — ex01〜03
# ============================================================================

class TestWhileBreak:
    """while True と break"""

    def test_ex01_echoes_until_q(self):
        result = run_script("ex01.py", stdin="apple\nbanana\nq\n")
        assert result.returncode == 0, \
            f"ex01.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "apple" in out, "ex01.py: 'apple' が出力されていません"
        assert "banana" in out, "ex01.py: 'banana' が出力されていません"
        # q 自体は出力されないこと
        lines = [line for line in out.strip().split("\n") if line.strip()]
        assert "q" not in lines, "ex01.py: 'q' は出力されてはいけません"

    def test_ex02_uppercase_until_q(self):
        result = run_script("ex02.py", stdin="hello\nworld\nq\n")
        assert result.returncode == 0, \
            f"ex02.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "HELLO" in out, "ex02.py: 大文字 'HELLO' が出力されていません"
        assert "WORLD" in out, "ex02.py: 大文字 'WORLD' が出力されていません"

    def test_ex03_echoes_until_end(self):
        result = run_script("ex03.py", stdin="apple\nbanana\nend\norange\n")
        assert result.returncode == 0, \
            f"ex03.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "apple" in out
        assert "banana" in out
        assert "orange" not in out, \
            "ex03.py: 'end' 以降の行 'orange' は表示されてはいけません"


# ============================================================================
# グループ2: try-except EOFError — ex04〜07
# ============================================================================

class TestEOFError:
    """try-except EOFError による入力終了の扱い"""

    def test_ex04_echoes_all(self):
        result = run_script("ex04.py", stdin="hello\nworld\n")
        assert result.returncode == 0, \
            f"ex04.py がエラーで終了しました:\n{result.stderr}"
        assert "hello" in result.stdout
        assert "world" in result.stdout

    def test_ex04_handles_empty(self):
        """空入力でも EOFError でクラッシュせず正常終了"""
        result = run_script("ex04.py", stdin="")
        assert result.returncode == 0, \
            "ex04.py: 空入力でクラッシュしました。EOFError を try-except で受けてください"

    def test_ex05_uppercase_all(self):
        result = run_script("ex05.py", stdin="hello\nworld\n")
        assert result.returncode == 0, \
            f"ex05.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "HELLO" in out, "ex05.py: 'HELLO' が出力されていません"
        assert "WORLD" in out, "ex05.py: 'WORLD' が出力されていません"

    def test_ex06_prefix_arrow(self):
        result = run_script("ex06.py", stdin="apple\nbanana\n")
        assert result.returncode == 0, \
            f"ex06.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "> apple" in out, "ex06.py: '> apple' が出力されていません"
        assert "> banana" in out, "ex06.py: '> banana' が出力されていません"

    def test_ex07_suffix_bang(self):
        result = run_script("ex07.py", stdin="hello\nworld\n")
        assert result.returncode == 0, \
            f"ex07.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "hello!" in out, "ex07.py: 'hello!' が出力されていません"
        assert "world!" in out, "ex07.py: 'world!' が出力されていません"


# ============================================================================
# グループ3: フィルター strip — ex08〜10
# ============================================================================

class TestStripFilter:
    """空行・空白だけの行を削除するフィルター"""

    def test_ex08_removes_blank_lines(self):
        result = run_script("ex08.py", stdin=SAMPLE_TEXT)
        assert result.returncode == 0, \
            f"ex08.py がエラーで終了しました:\n{result.stderr}"
        for line in result.stdout.split("\n")[:-1]:
            assert line.strip() != "", \
                f"ex08.py: 空行が残っています: {line!r}"
        assert "りんご" in result.stdout
        assert "バナナ" in result.stdout

    def test_ex09_strips_and_removes_blanks(self):
        result = run_script("ex09.py", stdin="  apple  \n\n   \nbanana\n")
        assert result.returncode == 0, \
            f"ex09.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        # 出力は前後の空白が除かれている
        assert "apple" in out
        assert "banana" in out
        # 出力中の各行が空白だけになっていないこと
        for line in out.split("\n")[:-1]:
            assert line.strip() != ""

    def test_ex10_removes_question_marks(self):
        result = run_script(
            "ex10.py",
            stdin="Are you OK?\nYes!\nAre you sure?\nWhy?\n",
        )
        assert result.returncode == 0, \
            f"ex10.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        # ? が全て削除されていること
        assert "?" not in out, "ex10.py: '?' が残っています"
        # それ以外の文字は残っていること
        assert "Are you OK" in out
        assert "Yes!" in out
        assert "Are you sure" in out
        assert "Why" in out


# ============================================================================
# グループ4: フィルター in / not in — ex11〜13
# ============================================================================

class TestInFilter:
    """in / not in による含む・含まない判定"""

    def test_ex11_keeps_only_error(self):
        result = run_script("ex11.py", stdin=SAMPLE_LOG)
        assert result.returncode == 0, \
            f"ex11.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "failed to connect" in out
        assert "timeout" in out
        assert "INFO" not in out, "ex11.py: INFO 行は出力されてはいけません"
        assert "DEBUG" not in out, "ex11.py: DEBUG 行は出力されてはいけません"

    def test_ex12_removes_debug(self):
        result = run_script("ex12.py", stdin=SAMPLE_LOG)
        assert result.returncode == 0, \
            f"ex12.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "DEBUG" not in out, "ex12.py: DEBUG 行は出力されてはいけません"
        assert "INFO" in out
        assert "ERROR" in out

    def test_ex13_error_or_info(self):
        result = run_script("ex13.py", stdin=SAMPLE_LOG)
        assert result.returncode == 0, \
            f"ex13.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        # ERROR と INFO の両方が含まれる
        assert "INFO 2026-05-01 09:00:12 start" in out, \
            "ex13.py: INFO 行が表示されていません"
        assert "ERROR 2026-05-01 09:01:02 failed to connect" in out, \
            "ex13.py: ERROR 行が表示されていません"
        # DEBUG 行は除外される
        assert "DEBUG" not in out, "ex13.py: DEBUG 行は出力されてはいけません"


# ============================================================================
# グループ5: 状態を覚える — ex14〜18
# ============================================================================

class TestState:
    """状態変数を使う処理（行番号、連続空行、重複）"""

    def test_ex14_line_numbers(self):
        result = run_script("ex14.py", stdin="apple\nbanana\norange\n")
        assert result.returncode == 0, \
            f"ex14.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "1: apple" in out, "ex14.py: '1: apple' が出力されていません"
        assert "2: banana" in out, "ex14.py: '2: banana' が出力されていません"
        assert "3: orange" in out, "ex14.py: '3: orange' が出力されていません"

    def test_ex15_zero_padded_numbers(self):
        result = run_script("ex15.py", stdin="apple\nbanana\norange\n")
        assert result.returncode == 0, \
            f"ex15.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "01: apple" in out, "ex15.py: '01: apple' (0埋め2桁) が出力されていません"
        assert "02: banana" in out
        assert "03: orange" in out

    def test_ex16_compresses_blank_lines(self):
        result = run_script("ex16.py", stdin=SAMPLE_TEXT)
        assert result.returncode == 0, \
            f"ex16.py がエラーで終了しました:\n{result.stderr}"
        # "\n\n\n"（3連改行 = 2連空行）が残っていないこと
        assert "\n\n\n" not in result.stdout, \
            f"ex16.py: 連続する空行が圧縮されていません:\n{result.stdout!r}"
        assert "りんご" in result.stdout
        assert "バナナ" in result.stdout

    def test_ex17_compresses_blank_lines(self):
        result = run_script("ex17.py", stdin="a\n\n\n\nb\n")
        assert result.returncode == 0, \
            f"ex17.py がエラーで終了しました:\n{result.stderr}"
        assert "\n\n\n" not in result.stdout, \
            "ex17.py: 連続空行が圧縮されていません"
        assert "a" in result.stdout
        assert "b" in result.stdout

    def test_ex18_dedupe_consecutive(self):
        result = run_script(
            "ex18.py",
            stdin="apple\napple\nbanana\nbanana\nbanana\norange\n",
        )
        assert result.returncode == 0, \
            f"ex18.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        lines = [line for line in out.strip().split("\n")]
        assert lines == ["apple", "banana", "orange"], \
            f"ex18.py: 重複した連続行を1つにまとめてください。実際: {lines}"


# ============================================================================
# グループ6: 累積（合計）+ replace — ex19〜22
# ============================================================================

class TestAccumulator:
    """累積パターン（合計）と replace の組み合わせ"""

    def test_ex19_sums_numbers(self):
        result = run_script("ex19.py", stdin=SCORES)
        assert result.returncode == 0, \
            f"ex19.py がエラーで終了しました:\n{result.stderr}"
        # 80+65+90+72+55 = 362
        assert "362" in result.stdout, \
            f"ex19.py: 合計 362 が出力されていません:\n{result.stdout!r}"

    def test_ex20_removes_commas(self):
        result = run_script("ex20.py", stdin="1,200\n3,500\n800\n")
        assert result.returncode == 0, \
            f"ex20.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "1200" in out, "ex20.py: '1200' が出力されていません"
        assert "3500" in out, "ex20.py: '3500' が出力されていません"
        assert "800" in out
        # カンマが除去されていること
        assert "1,200" not in out, "ex20.py: カンマがそのまま残っています"

    def test_ex21_sums_with_commas(self):
        result = run_script("ex21.py", stdin=AMOUNTS)
        assert result.returncode == 0, \
            f"ex21.py がエラーで終了しました:\n{result.stderr}"
        # 1200 + 3500 + 800 + 250 = 5750
        assert "5750" in result.stdout, \
            f"ex21.py: 合計 5750 が出力されていません:\n{result.stdout!r}"

    def test_ex22_cumsum(self):
        result = run_script("ex22.py", stdin=SCORES)
        assert result.returncode == 0, \
            f"ex22.py がエラーで終了しました:\n{result.stderr}"
        # SCORES = 80, 65, 90, 72, 55 → cumsum = 80, 145, 235, 307, 362
        lines = result.stdout.strip().split("\n")
        assert lines == ["80", "145", "235", "307", "362"], \
            f"ex22.py: 累積和 (80, 145, 235, 307, 362) が出力されていません:\n{result.stdout!r}"


# ============================================================================
# グループ7: 累積の応用（平均） — ex23〜25
# ============================================================================

class TestAverage:
    """件数と平均"""

    def test_ex23_counts_lines(self):
        result = run_script("ex23.py", stdin=SCORES)
        assert result.returncode == 0, \
            f"ex23.py がエラーで終了しました:\n{result.stderr}"
        # SCORES は 5 行
        assert "5" in result.stdout, \
            f"ex23.py: 件数 5 が出力されていません:\n{result.stdout!r}"

    def test_ex24_average(self):
        result = run_script("ex24.py", stdin=SCORES)
        assert result.returncode == 0, \
            f"ex24.py がエラーで終了しました:\n{result.stderr}"
        # 平均 = 362 / 5 = 72.4
        assert "72.4" in result.stdout, \
            f"ex24.py: 平均 72.4 が出力されていません:\n{result.stdout!r}"

    def test_ex24_no_data(self):
        result = run_script("ex24.py", stdin="")
        assert result.returncode == 0, \
            f"ex24.py がエラーで終了しました:\n{result.stderr}"
        assert "データがありません" in result.stdout, \
            "ex24.py: データなしのとき「データがありません」と表示してください"

    def test_ex25_std_dev(self):
        result = run_script("ex25.py", stdin=SCORES)
        assert result.returncode == 0, \
            f"ex25.py がエラーで終了しました:\n{result.stderr}"
        # SCORES = 80, 65, 90, 72, 55
        # 母分散 = 145.04, 標準偏差 ≈ 12.0432
        assert "12.04" in result.stdout, \
            f"ex25.py: 標準偏差 12.04... が出力されていません:\n{result.stdout!r}"

    def test_ex25_no_data(self):
        result = run_script("ex25.py", stdin="")
        assert result.returncode == 0
        assert "データがありません" in result.stdout, \
            "ex25.py: データなしのとき「データがありません」と表示してください"


# ============================================================================
# グループ8: split + リスト[i] — ex26〜28
# ============================================================================

class TestSplit:
    """split() + リストインデックス"""

    def test_ex26_extracts_name(self):
        result = run_script("ex26.py", stdin="Alice 17\nBob 22\nCharlie 30\n")
        assert result.returncode == 0, \
            f"ex26.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "Alice" in out
        assert "Bob" in out
        assert "Charlie" in out
        # 年齢は出力に含まれないはず
        assert "17" not in out, "ex26.py: 年齢は出力しないでください"
        assert "22" not in out
        assert "30" not in out

    def test_ex27_status_400_or_more(self):
        result = run_script("ex27.py", stdin=ACCESS_LOG)
        assert result.returncode == 0, \
            f"ex27.py がエラーで終了しました:\n{result.stderr}"
        out = result.stdout
        assert "/admin" in out and "403" in out
        assert "/not-found" in out and "404" in out
        assert "/api/items" in out and "500" in out
        assert "/index.html" not in out, "ex27.py: 200 の行は出力されてはいけません"
        assert "/about.html" not in out

    def test_ex28_count_404(self):
        result = run_script("ex28.py", stdin=ACCESS_LOG)
        assert result.returncode == 0, \
            f"ex28.py がエラーで終了しました:\n{result.stderr}"
        # ACCESS_LOG には 404 が 1 件
        out = result.stdout.strip()
        assert "1" in out, \
            f"ex28.py: 404 の件数 1 が出力されていません:\n{result.stdout!r}"
