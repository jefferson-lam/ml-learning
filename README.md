# ML Learning

A local, reproducible workspace for learning machine learning with scikit-learn and PyTorch.

## Start

```bash
uv sync
uv run ml-learning
uv run jupyter lab
```

VS Code should automatically detect `.venv`. For notebooks, select the interpreter at:

```text
.venv/bin/python
```

Open the project root—not only the `notebooks/` folder—in VS Code:

```bash
code /Users/jeffersonlam/code/ml-learning
```

Then select the **ml-learning** kernel if VS Code prompts you.

## Simple chapter workflow

Each chapter has two notebooks:

1. `chapters/NN-title.ipynb`: rewrite and run textbook code.
2. `exercises/NN-exercises.ipynb`: complete the chapter exercises.

In the chapter notebook, add a short Markdown note beneath each code section:

```markdown
**Notes**

- What the code does:
- Why it matters:
- What confused me:
```

After finishing the chapter, summarize only the durable ideas in Obsidian. Keep datasets out of Git.

```text
chapters/        rewritten textbook code and inline notes
exercises/       one exercise notebook per chapter
data/raw/        original local datasets
data/processed/  generated datasets
artifacts/       generated models and figures
```

## Commands

```bash
uv run jupyter lab
uv run ruff check .
uv run ruff format .
```