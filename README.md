# Purpose
The purpose of this tool is to generate an Anki deck from annotations on a text file.
This was specially developed for those who use Anki to learn language vocabulary. 

# Input structure
1. The input must be some sort of non-compressed text file (.txt, .md, etc.)
2. Every line to be converted to an Anki card must start with a dash and space `- `. Everything other line will be ignored
3. The front and back of the cards are separated by a separator, such as ` = `

Example: 
```
- die Katze = the cat
- das Haus = the house
```

Outside of these rules, you are free to populate your text file with other annotations which will be ignored when creating the deck.

# Installation

```bash
pip install anki_deck_from_text
```

# How to run

```bash
anki_deck_from_text file.md out amazing_deck
```
