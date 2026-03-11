# anki_deck_from_text

[![PyPI version](https://img.shields.io/pypi/v/anki_deck_from_text)](https://pypi.org/project/anki_deck_from_text/)
[![CI Tests](https://github.com/AndreMacedo88/anki_deck_from_text/actions/workflows/ci-tests.yml/badge.svg)](https://github.com/AndreMacedo88/anki_deck_from_text/actions/workflows/ci-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)

**Generate Anki flashcard decks (.apkg) from annotated text files.**

Mark vocabulary lines in any text file, and `anki_deck_from_text` will turn them into a ready-to-import Anki deck.

## Quick example

Given an input file `vocab.txt`:

```text
Some notes you don't want as cards...

- casa = house
- gato = cat
- perro = dog

More notes here...
```

Run:

```bash
anki_deck_from_text vocab.txt spanish_vocab "Spanish Vocabulary"
```

This creates `spanish_vocab.apkg` with three cards, ready to import into Anki.

## Features

- **Simple annotation format** -- mark lines with a character (default `-`) and separate front/back with another (default `=`)
- **Automatic encoding detection** -- handles UTF-8, Latin-1, and other encodings via chardet
- **Multiple card types** -- built-in `basic` and `sound` models, with support for custom models
- **Reverse cards** -- swap front and back with `--reverse`
- **Dry run / preview** -- see what cards would be generated before writing the file
- **Tags** -- add comma-separated Anki tags to all cards
- **Merge multiple files** -- combine several input files into one deck with `-i`

## Next steps

- [Installation](installation.md) -- install via pip, pipx, or from source
- [Input Format](guide/input-format.md) -- learn the annotation rules
- [CLI Usage](guide/cli-usage.md) -- explore all command-line options
- [Examples](guide/examples.md) -- end-to-end usage examples
- [API Reference](api/index.md) -- module and function documentation
