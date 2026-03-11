# API Reference

`anki_deck_from_text` follows a simple pipeline:

```
Input File --> parse_input --> dict --> generate_deck --> .apkg
```

## Modules

| Module | Description |
|--------|-------------|
| [`cli`](cli.md) | Click command-line entry point |
| [`parse_input`](parse_input.md) | Read and parse input files into question/answer dicts |
| [`generate_deck`](generate_deck.md) | Build Anki decks and write `.apkg` packages |
| [`models`](models.md) | Anki card model (template) definitions |
