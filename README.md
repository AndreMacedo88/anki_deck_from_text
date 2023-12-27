# Purpose
The purpose of this tool is to generate Anki decks and cards from annotations on a text file.
This was specially developed for those who use Anki to learn language vocabulary.

# Input structure
1. The input must be some sort of non-compressed text file (.txt, .md, etc.)
2. Every line to be converted to an Anki card must start with a dash and space `- `. Everything else will be ignored
3. The front and back of the cards are separated by a ` = `

Example: 
```
- die Katze = the cat
- das Haus = the house
```