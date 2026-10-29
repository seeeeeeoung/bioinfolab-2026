# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A student's coursework repository for a bioinformatics lab course (생물정보학실험). Each `labNN/` folder is one week's exercises; there is no build system, package manifest, linter, or test suite. Scripts are small, standalone Bash and Python teaching exercises run directly from the terminal. README, comments, docstrings, and output messages are written in Korean — keep new code consistent with that.

## Layout conventions

- `lab-template/` is copied to create each week's folder (`cp -r lab-template labNN`). Every lab has:
  - `data/` — input data (mostly small FASTA files like `seqs.fasta`, `seqs2.fasta`)
  - `doc/` — outputs, results, reports, cheatsheets
  - `src/` — the scripts written that week
- `resources/` holds shared sample data and example scripts provided by the course.
- `prob03/` is a file-permissions exercise, not code.
- Labs are self-contained: code is copied forward between weeks rather than shared (e.g. `countseq.sh` → `countseq.py` → `countseq2.py`). Edit the file in the lab being worked on; don't refactor earlier labs.
- `bugN.sh` / `bugN.py` files are intentional debugging exercises.

## Running scripts

Scripts are run from inside the lab's `src/` directory with relative paths to data/doc:

```
cd lab07/src
python3 summary.py ../data/seqs.fasta ../doc/summary.tsv
bash ../../lab05/src/fastainfo.sh ../data/seqs.fasta
```

Python scripts take arguments via `sys.argv` (no argparse) and print a `사용법:` usage message on bad input. Bash scripts use `#!/usr/bin/bash`.

`lab07/src/fasta.py` is a reusable module (`read_fasta`, `gc_content`, `write_fasta`, `reverse_complement`, `length_stats`) imported by sibling scripts via `from fasta import ...` — this only works when running from `lab07/src/`. Its API and known limitations are documented in `lab07/src/README.md`. `read_fasta` returns `{name: SEQ}` with uppercase sequences and only the first word of the header as the name.

## Style

Code is intentionally beginner-level: plain loops, string concatenation, dicts, no third-party libraries, no type hints, no classes. Match that level rather than introducing idiomatic/advanced Python.

## Environment

Runs in GitHub Codespaces with dev container configs in `.devcontainer/` chosen per week:
1. `1-basic` — Python + Linux basics (weeks 02–07)
2. `2-conda` — micromamba only
3. `3-seq` — seqkit, blast, mafft, iqtree, fastqc, fastp (weeks 08–09, 12–14)
4. `4-genome` — above + shovill, prokka (weeks 10–11)

`bash .devcontainer/check.sh` shows which tools are available. `$MYHOME` points to the workspace root (bare `cd` returns there). Large sequencing data (`*.fastq*`, `*.sra`) and assembly/annotation output dirs are gitignored and re-downloaded with `wget` when needed.
