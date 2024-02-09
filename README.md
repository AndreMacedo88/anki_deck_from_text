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
- `sound`: TODO: write a short description of the sound card type

# Installation
Make sure you have python installed (recommended version >= 3.10) and then run in the terminal/command-line:
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

  Generate and Anki deck from annotations on a text file

Options:
  --separator TEXT   Character(s) that separate the text to be written to the
                     front and back of the cards  [default: =]
  --marker TEXT      Character(s) marking this line to be included in the deck
                     [default: -]
  --card_model TEXT  Anki card model to build the deck with. Available options
                     are: `sound`  [default: sound]
  -h, --help         Show this message and exit.
```

# Extending the tool
## Add card types
To add extra card types follow the instructions in the `models.py` file docstring and then update the current available card types both in the docstring of `generate_deck.py` and [in the relevant section](#current-card-types) of this README.

Refer to [the Anki docs](https://docs.ankiweb.net/getting-started.html#card-types) for how to design Anki card type structures.
