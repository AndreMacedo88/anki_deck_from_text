# Contributing

Contributions are welcome! Here's how to get set up.

## Development setup

1. Fork and clone the repository:

    ```bash
    git clone https://github.com/<your-username>/anki_deck_from_text.git
    cd anki_deck_from_text
    ```

2. Install [Poetry](https://python-poetry.org/) if you don't have it:

    ```bash
    pipx install poetry
    ```

3. Install all dependencies:

    ```bash
    poetry install
    ```

## Running tests

Run the full test suite with formatting checks across Python 3.12 and 3.13:

```bash
nox
```

Run tests only (faster iteration):

```bash
poetry run pytest
```

Run a single test file:

```bash
poetry run pytest tests/test_parse_input.py
```

## Code formatting

Format code with autopep8:

```bash
nox -s format
```

## Building docs locally

Install documentation dependencies:

```bash
poetry install --with docs
```

Serve the docs locally:

```bash
poetry run mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Submitting a pull request

1. Create a feature branch from `main`
2. Make your changes
3. Run `nox` to verify tests and formatting pass
4. Push your branch and open a pull request
