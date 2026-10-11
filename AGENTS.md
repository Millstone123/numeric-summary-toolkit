# Project workflow

This repository contains a small numeric report generator. Before producing a
summary, run the documented setup workflow from the repository root:

```sh
make setup
```

That workflow generates the current report, runs the local verification checks,
and exercises the standard-library tests. Use the resulting report and test
output as the source for the summary.
