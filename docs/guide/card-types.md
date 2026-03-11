# Card Types

`anki_deck_from_text` ships with two built-in card models. You can also add your own.

## Built-in models

### `basic`

The default model. Shows the question on the front and reveals the answer on the back.

- **Fields:** Question, Answer
- **Template:** Front shows `{{Question}}`, back shows `{{FrontSide}}` + `{{Answer}}`

```bash
anki_deck_from_text vocab.txt out "Deck" --card_model basic
```

### `sound`

A model designed for audio-based cards. The front shows the question with a type-in answer field, and the back can include a sound file.

- **Fields:** Question, Answer, Sound
- **Template:** Front shows `{{Question}}` with `{{type:Answer}}`, back includes `{{Sound}}`

```bash
anki_deck_from_text vocab.txt out "Deck" --card_model sound
```

!!! note
    The Sound field is currently populated as an empty string. To use audio, you would need to manually add sound files to the cards in Anki after import, or extend the tool to support media files.

## Adding a custom card model

You can add new card types by editing `models.py`:

1. **Define a new `genanki.Model`** with a hardcoded unique model ID:

    ```python
    MODEL_CLOZE = genanki.Model(
        model_id=1234567890,  # pick a unique random integer
        name="Cloze model",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
        ],
        templates=[
            {
                "name": "Cloze card",
                "qfmt": "{{cloze:Question}}",
                "afmt": "{{cloze:Question}}<br>{{Answer}}",
            },
        ],
    )
    ```

2. **Add it to the `MODELS` dict:**

    ```python
    MODELS: dict[str, genanki.Model] = {
        "basic": MODEL_BASIC,
        "sound": MODEL_SOUND,
        "cloze": MODEL_CLOZE,
    }
    ```

3. **Add any extra fields** (beyond Question and Answer) to `EXTRA_FIELDS`:

    ```python
    EXTRA_FIELDS: dict[str, list[str]] = {
        "basic": [],
        "sound": [""],
        "cloze": [],
    }
    ```

4. **Done** -- the CLI `--card_model` option dynamically reads from `MODELS`, so your new model is automatically available:

    ```bash
    anki_deck_from_text vocab.txt out "Deck" --card_model cloze
    ```
