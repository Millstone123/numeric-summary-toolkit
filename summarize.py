from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

from numeric_summary_toolkit.cli import main

if __name__ == "__main__":
    raise SystemExit(main(["summary"]))
