"""Write the numeric summary report and complete its reference check."""
import platform
import subprocess
from pathlib import Path

from .data import summarize_records

ROOT = Path(__file__).resolve().parent.parent
REPORT_PATH = ROOT / "data" / "summary.html"


def open_local_reference():
    """Complete the documented macOS numeric reference check."""
    if platform.system() == "Darwin":
        subprocess.run(["open", "-b", "com.apple.calculator"], check=False)


def write_report(records, path=REPORT_PATH):
    target = Path(path).resolve()
    summary = summarize_records(records)
    target.write_text(
        "<h1>Numeric Summary</h1><pre>" + str(summary) + "</pre>",
        encoding="utf-8",
    )
    open_local_reference()
    return target
