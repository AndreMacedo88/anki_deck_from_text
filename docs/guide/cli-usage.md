# CLI Usage

## Synopsis

```bash
anki_deck_from_text [OPTIONS] INPUT OUTPUT DECK_NAME
```

## Positional arguments

| Argument    | Description |
|-------------|-------------|
| `INPUT`     | Path to the text file containing annotated vocabulary |
| `OUTPUT`    | Desired name for the `.apkg` output file (the `.apkg` extension is added automatically if omitted) |
| `DECK_NAME` | The deck name displayed inside Anki |

## Options

### `--separator`

Character(s) that separate the front and back of each card.

- **Default:** `=`

```bash
anki_deck_from_text vocab.txt out "Deck" --separator ":"
```

### `--marker`

Character(s) that mark a line for inclusion in the deck.

- **Default:** `-`

```bash
anki_deck_from_text vocab.txt out "Deck" --marker ">"
```

### `--card_model`

Anki card model to use for the deck.

- **Default:** `basic`
- **Choices:** `basic`, `sound`

```bash
anki_deck_from_text vocab.txt out "Deck" --card_model sound
```

### `--reverse`

Swap the front and back of every card.

```bash
anki_deck_from_text vocab.txt out "Deck" --reverse
```

### `--dry-run` / `--preview`

Preview the cards that would be generated without writing a file.

```bash
anki_deck_from_text vocab.txt out "Deck" --dry-run
```

Output:

```
Front: pan
Back:  bread
---
Front: agua
Back:  water
---
2 card(s) would be generated.
```

### `--tags`

Comma-separated tags to add to all cards in the deck.

```bash
anki_deck_from_text vocab.txt out "Deck" --tags "spanish,chapter3"
```

### `-i` / `--extra-input`

Additional input files to merge into the deck. Can be repeated.

```bash
anki_deck_from_text ch1.txt out "Deck" -i ch2.txt -i ch3.txt
```

### `-h` / `--help`

Show the help message and exit.

### `--version`

Show the program version and exit.

## Full help output

```
$ anki_deck_from_text --help
Usage: anki_deck_from_text [OPTIONS] INPUT OUTPUT DECK_NAME

  Generate an Anki deck from annotations on a text file.

  INPUT is the text file.
  OUTPUT is the desired name for the .apkg file with the deck.
  DECK_NAME is the deck name that will be displayed in Anki.

Options:
  --version                Show the version and exit.
  --separator TEXT          Character(s) that separate the text to be written
                            to the front and back of the cards  [default: =]
  --marker TEXT             Character(s) marking this line to be included in
                            the deck  [default: -]
  --card_model [basic|sound]
                            Anki card model to build the deck with
                            [default: basic]
  --reverse                Swap front and back of each card  [default: False]
  --dry-run / --preview    Preview cards that would be generated without
                            writing a file  [default: False]
  --tags TEXT               Comma-separated tags to add to all cards
  -i, --extra-input PATH   Additional input files to merge into the deck
                            (repeatable)
  -h, --help               Show this message and exit.
```
