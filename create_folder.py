from pathlib import Path

root = Path("Atcoder/ABC-contests")

for i in range(1, 405):
    contest_path = root / f"abc{i:03}"
    for problem in ["A", "B", "C", "D", "E", "F", "G"]:
        problem_dir = contest_path / problem
        problem_dir.mkdir(parents=True, exist_ok=True)
        
        # 空ファイルの作成
        (problem_dir / "main.py").touch()
        (problem_dir / "input.txt").touch()
        (problem_dir / "README.md").write_text(f"# abc{i:03} - {problem} 問題\n\n感想・方針・メモなどを書く。")
