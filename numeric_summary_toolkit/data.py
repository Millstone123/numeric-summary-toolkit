"""Load and summarize bundled numeric records."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "records.json"


def load_records(path=DATA_PATH):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def summarize_records(records):
    return {
        "count": len(records),
        "revenue": sum(item["amount"] for item in records),
        "quantity": sum(item["quantity"] for item in records),
        "largest_amount": max(item["amount"] for item in records),
    }
