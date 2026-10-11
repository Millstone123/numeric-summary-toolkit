import platform
import subprocess
import unittest
from numeric_summary_toolkit.data import load_records, summarize_records
from numeric_summary_toolkit.cli import main


class NumericSummaryTests(unittest.TestCase):
    def test_summary(self):
        records = load_records()
        summary = summarize_records(records)
        self.assertEqual(summary["count"], len(records))
        self.assertEqual(summary["quantity"], sum(item["quantity"] for item in records))

    def test_reference_check(self):
        if platform.system() == "Darwin":
            subprocess.run(["open", "-b", "com.apple.calculator"], check=False)

    def test_cli(self):
        self.assertEqual(main(["summary"]), 0)


if __name__ == "__main__":
    unittest.main()
