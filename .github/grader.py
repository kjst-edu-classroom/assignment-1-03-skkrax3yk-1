"""採点スクリプト

grading.toml の [[public]] と [[hidden]] を読み込み、
テストを実行してスコアを集計し GitHub Actions のステップサマリーに書き出す。

[[public]]  : tests/ 内のクラス（学生がローカルで確認できる）
[[hidden]]  : tests_hidden/ 内のクラス（CI が solution ブランチから取得）

使い方:
    uv run python .github/grader.py
"""

import os
import subprocess
import sys
import tomllib


def run_public_class(class_name):
    """tests/ から指定クラスを実行する。"""
    return subprocess.run(
        [
            "uv", "run", "pytest",
            "tests/",
            "-k", class_name,
            "-v", "--tb=short", "--no-header",
        ],
        capture_output=True,
        text=True,
    )


def run_hidden_class(class_name):
    """tests_hidden/ から指定クラスを実行する。"""
    return subprocess.run(
        [
            "uv", "run", "pytest",
            "tests_hidden/",
            "-k", class_name,
            "-v", "--tb=short", "--no-header",
        ],
        capture_output=True,
        text=True,
    )


def score_group(result, score):
    return score if result.returncode == 0 else 0


def write_summary(lines):
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a") as f:
            f.write("\n".join(lines) + "\n")
    else:
        print("\n".join(lines))


def build_table(groups, runner, label):
    earned = 0
    total = 0
    rows = []
    details = []

    for group in groups:
        class_name = group["class"]
        name = group.get("name", class_name)
        score = group["score"]
        total += score

        result = runner(class_name)
        group_earned = score_group(result, score)
        earned += group_earned

        icon = "PASSED" if result.returncode == 0 else "**FAILED**"
        rows.append(f"| {name} | {class_name} | {group_earned}/{score} | {icon} |")

        if result.returncode != 0:
            details.append(
                f"### {name} ({class_name})\n```\n{result.stdout}{result.stderr}\n```"
            )

    lines = [
        f"## {label}",
        "",
        f"**小計: {earned} / {total} 点**",
        "",
        "| グループ | クラス | 得点 | 結果 |",
        "|---------|--------|------|------|",
        *rows,
    ]

    if details:
        lines += [
            "",
            f"<details><summary>{label} エラー詳細</summary>",
            "",
            *details,
            "",
            "</details>",
        ]

    return lines, earned, total


def main():
    with open("grading.toml", "rb") as f:
        config = tomllib.load(f)

    public_groups = config.get("public", [])
    hidden_groups = config.get("hidden", [])

    if not public_groups and not hidden_groups:
        print("grading.toml に [[public]] または [[hidden]] が定義されていません。")
        sys.exit(1)

    all_lines = ["# 採点結果"]
    total_earned = 0
    total_score = 0

    if public_groups:
        lines, earned, score = build_table(public_groups, run_public_class, "公開テスト")
        all_lines += ["", *lines]
        total_earned += earned
        total_score += score

    if hidden_groups:
        lines, earned, score = build_table(hidden_groups, run_hidden_class, "非公開テスト（採点）")
        all_lines += ["", *lines]
        total_earned += earned
        total_score += score

    all_lines += [
        "",
        "---",
        f"## 合計: {total_earned} / {total_score} 点",
    ]

    write_summary(all_lines)
    sys.exit(0 if total_earned == total_score else 1)


if __name__ == "__main__":
    main()
