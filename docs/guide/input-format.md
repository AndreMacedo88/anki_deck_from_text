# Input Format

`anki_deck_from_text` reads plain text files and extracts annotated lines to create flashcards.

## Basic rules

1. **Marker** -- each line that should become a card must start with a marker character (default: `-`)
2. **Separator** -- the marker line must contain a separator character (default: `=`) that splits the front and back of the card
3. **Unmarked lines are ignored** -- any line that does not start with the marker is skipped, so you can freely mix notes and vocabulary

## Example input file

```text
Chapter 3 - Food vocabulary

- bread = pan
- water = agua
- milk = leche

These lines are ignored because they don't start with the marker.

- rice = arroz
```

This produces four cards:

| Front  | Back  |
|--------|-------|
| pan    | bread |
| agua   | water |
| leche  | milk  |
| arroz  | rice  |

!!! note
    The text **before** the separator becomes the *back* of the card, and the text **after** the separator becomes the *front*. This matches the common pattern of writing the foreign word first.

## Custom markers and separators

Use `--marker` and `--separator` to change the default characters:

```bash
anki_deck_from_text vocab.txt output "My Deck" --marker ">" --separator ":"
```

With an input file like:

```text
> house : casa
> dog : perro
```

## Encoding

The tool tries UTF-8 first. If that fails, it uses [chardet](https://github.com/chardet/chardet) to detect the file encoding automatically. For best results, save your files as UTF-8.

If the detected encoding has low confidence (below 60%), a warning is printed. In that case, re-save your file as UTF-8 and try again.

## Whitespace handling

- Leading and trailing whitespace around the marker, separator, question, and answer is stripped automatically.
- Empty lines are ignored.
