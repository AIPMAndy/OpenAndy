"""Behaviour tests for openandy.py.

These assert behaviour, not just "the command returned 0":
broken links, missing indexed files, unregistered sources, sensitive values,
build idempotency and search ranking are each verified with a negative case.
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "openandy.py"

spec = importlib.util.spec_from_file_location("openandy", CLI)
openandy = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(openandy)


def run(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(CLI), "--root", str(root), *args],
        capture_output=True,
        text=True,
    )


def make_repo(base: Path, index: dict | None = None) -> dict:
    """Build a minimal but valid repository, with llms-full.txt generated."""
    (base / "data").mkdir(parents=True, exist_ok=True)
    idx = index or {
        "version": "0.1.0",
        "updated": "2026-11-07",
        "sources": {
            "S1": {"title": "source", "author": "a", "date": "d", "url": None, "kind": "k"}
        },
        "entries": [
            {
                "id": "story",
                "title": "时间线",
                "path": "STORY.md",
                "tags": ["时间线"],
                "summary": "[公开自述] 一段用于测试的摘要。",
                "sources": ["S1"],
            }
        ],
    }
    (base / "data" / "index.json").write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
    (base / "README.md").write_text("# OpenAndy\n\n[时间线](STORY.md)\n", encoding="utf-8")
    (base / "STORY.md").write_text(
        "# 时间线\n\n[公开自述] 这是一段用于测试的正文，用来验证索引与正文之间是否保持单一真源的关系。\n",
        encoding="utf-8",
    )
    for name in ("AGENTS.md", "CONTRIBUTING.md", "SOURCES.md", "llms.txt"):
        (base / name).write_text(f"# {name}\n", encoding="utf-8")
    built = run(base, "build")
    assert built.returncode == 0, built.stderr
    return idx


class RealRepoTests(unittest.TestCase):
    def test_check_passes_on_repository(self):
        result = run(ROOT, "check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("全部通过", result.stdout)

    def test_search_scoring_prefers_title_and_tags(self):
        idx = openandy.load_index(ROOT)
        results = openandy.search_entries(ROOT, idx, ["认知公理"])
        self.assertTrue(results)
        self.assertEqual(results[0][1]["id"], "principles")

    def test_search_unknown_term_returns_nothing(self):
        idx = openandy.load_index(ROOT)
        self.assertEqual(openandy.search_entries(ROOT, idx, ["zzzz-unknown-xyz"]), [])

    def test_ask_finds_specific_entry(self):
        result = run(ROOT, "ask", "眼睛手术")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("what-it-cost", result.stdout)

    def test_ask_unknown_term_says_no_match(self):
        result = run(ROOT, "ask", "zzzz-unknown-xyz")
        self.assertEqual(result.returncode, 0)
        self.assertIn("没有匹配的条目", result.stdout)

    def test_show_unknown_id_fails(self):
        result = run(ROOT, "show", "does-not-exist")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("未知 id", result.stderr)

    def test_index_holds_no_body_text(self):
        raw = (ROOT / "data" / "index.json").read_text(encoding="utf-8")
        story = (ROOT / "STORY.md").read_text(encoding="utf-8")
        self.assertNotIn("手术台上想起这一路", raw)
        self.assertIn("手术台上想起这一路", story)


class CheckerNegativeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        make_repo(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def output(self, result):
        return result.stdout + result.stderr

    def test_baseline_min_repo_passes(self):
        result = run(self.root, "check")
        self.assertEqual(result.returncode, 0, self.output(result))

    def test_detects_missing_indexed_file(self):
        (self.root / "STORY.md").unlink()
        result = run(self.root, "check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("STORY.md", self.output(result))

    def test_detects_broken_relative_link(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n[缺失](missing.md)\n", encoding="utf-8")
        run(self.root, "build")
        result = run(self.root, "check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("断链", self.output(result))

    def test_detects_phone_number(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8") + "\n联系电话 13800138000\n", encoding="utf-8")
        run(self.root, "build")
        result = run(self.root, "check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("mobile number", self.output(result))

    def test_detects_unregistered_source(self):
        idx = json.loads((self.root / "data" / "index.json").read_text(encoding="utf-8"))
        idx["entries"][0]["sources"] = ["S9"]
        (self.root / "data" / "index.json").write_text(json.dumps(idx, ensure_ascii=False), encoding="utf-8")
        run(self.root, "build")
        result = run(self.root, "check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("未登记来源", self.output(result))

    def test_detects_stale_llms_full(self):
        target = self.root / "llms-full.txt"
        target.write_text(target.read_text(encoding="utf-8") + "\nstale\n", encoding="utf-8")
        result = run(self.root, "check")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("不同步", self.output(result))

    def test_build_is_idempotent(self):
        first = (self.root / "llms-full.txt").read_bytes()
        result = run(self.root, "build")
        self.assertEqual(result.returncode, 0, self.output(result))
        self.assertIn("已是最新", result.stdout)
        self.assertEqual(first, (self.root / "llms-full.txt").read_bytes())

    def test_build_contains_every_entry_body(self):
        text = (self.root / "llms-full.txt").read_text(encoding="utf-8")
        self.assertIn("FILE: STORY.md", text)
        self.assertIn("用来验证索引与正文之间是否保持单一真源", text)
        self.assertIn("S1:", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
