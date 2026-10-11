"""Command-line entry point."""
from .data import load_records, summarize_records
from .reporting import write_report


def main(argv=None):
    command = (argv or ["summary"])[0]
    if command != "summary":
        return 2
    records = load_records()
    summary = summarize_records(records)
    write_report(records)
    print("Numeric Summary: " + ", ".join(f"{key}={value}" for key, value in summary.items()))
    return 0
