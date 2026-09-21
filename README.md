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

## Learning loop

For each concept:

1. Predict what should happen before running code.
2. Explore the concept in `notebooks/`.
3. Rebuild the important part in `src/ml_learning/`.
4. Test it in `tests/`.
5. Solve a related problem in `exercises/` without looking at the chapter.
6. Explain the idea in Obsidian and connect it to prior concepts.

Use notebooks as scratchpads. Move reusable code into `src/`, and keep datasets out of Git.

## Commands

```bash
uv run jupyter lab
uv run pytest
uv run ruff check .
uv run ruff format .
```

## Structure

```text
notebooks/       chapter exploration
src/             reusable implementations
exercises/       retrieval-practice exercises
tests/           executable understanding
data/raw/        original local datasets
data/processed/  generated datasets
artifacts/       generated models and figures
```