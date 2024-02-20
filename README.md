# Purpose
The purpose of this tool is to generate an Anki deck from annotations on a text file.
This was specially developed for those who use Anki to learn language vocabulary. 

# Input structure
1. The input must be some sort of non-compressed text file (.txt, .md, etc.)
2. Every line to be converted to an Anki card must start with a marker, such as `-`. Use the `marker` option to set a custom marker. Every other line will be ignored.
3. The front and back of the cards are separated by a separator, such as `=`. Use the `separator` option to set a custom separator.

Example: 
```
- die Katze = the cat
- das Haus = the house
```

Outside of these rules, you are free to populate your text file with other annotations which will be ignored when creating the deck.

# Current card types
Currently, the output deck will be populated with cards from one type at a time.
The currently implemented types are:
- `basic`: The [Basic](https://docs.ankiweb.net/getting-started.html#card-types) card type in Anki. Each line's text is split between front and back of one card by the `separator`
- `sound`: Similar to the [Basic (type in the answer)](https://docs.ankiweb.net/getting-started.html#card-types) card type, but with an added empty field on the back of the card that can be filled up afterwards with (for example) sound files by using an add-on such as [HyperTTS](https://ankiweb.net/shared/info/111623432)

# Installation
Make sure you have python installed (recommended version >= 3.12) and then run in the terminal/command-line:
```
pip install anki_deck_from_text
```

# How to run
Open a terminal/command-line instance and follow the general structure:
```
anki_deck_from_text file_name.md output_name amazing_deck_name
```

For all options run:
```
anki_deck_from_text --help
```

You will get the following documentation:

```
anki_deck_from_text [OPTIONS] INPUT OUTPUT DECK_NAME

  Generate and Anki deck from annotations on a text file.

  INPUT is the text file. OUTPUT is the desired name for the .apkg file with
  the deck. DECK_NAME is the deck name that will be displayed in Anki.


Options:
  --separator TEXT   Character(s) that separate the text to be written to the
                     front and back of the cards  [default: =]
  --marker TEXT      Character(s) marking this line to be included in the deck
                     [default: -]
  --card_model TEXT  Anki card model to build the deck with. Available options
                     are: `basic`, `sound`  [default: basic]
  -h, --help         Show this message and exit.
```

# Further development
## Contributing
To contribute to this project:
1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this project
2. Install [Poetry](https://python-poetry.org/docs/#installation)
3. Install [Nox](https://nox.thea.codes/en/stable/) (optional but recommended for automated tests and code formatting)
4. Change to the project directory and run `$ poetry install`

This should get your system setup to:
- Test that your changes didn't break the tool with `$ nox` or `poetry run pytest`
- Build with `$ poetry build` (optional)
- Test run with `$ poetry run anki_deck_from_text ...`

Once you're happy with your changes and tests:
5. Create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) to be reviewed

## Extending the tool
### Add card types
To add extra card types follow the instructions in the `models.py` file docstring and then update the current available card types both in the docstring of `generate_deck.py` and [in the relevant section](#current-card-types) of this README.

Refer to [the Anki docs](https://docs.ankiweb.net/getting-started.html#card-types) for how to design Anki card type structures.
