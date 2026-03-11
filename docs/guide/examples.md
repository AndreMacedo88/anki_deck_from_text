# Examples

## 1. Basic usage

Create a simple vocabulary deck:

```bash
anki_deck_from_text vocab.txt spanish_vocab "Spanish Vocabulary"
```

Input file (`vocab.txt`):

```text
- casa = house
- gato = cat
- perro = dog
```

Output: `spanish_vocab.apkg` with 3 cards.

## 2. Custom separator and marker

Use `:` as separator and `>` as marker:

```bash
anki_deck_from_text vocab.txt output "My Deck" --separator ":" --marker ">"
```

Input file:

```text
> house : casa
> water : agua
```

## 3. Dry run / preview

See what cards would be generated without creating a file:

```bash
anki_deck_from_text vocab.txt output "My Deck" --dry-run
```

Output:

```
Front: house
Back:  casa
---
Front: cat
Back:  gato
---
2 card(s) would be generated.
```

## 4. Reverse cards

Swap front and back of every card:

```bash
anki_deck_from_text vocab.txt output "My Deck" --reverse
```

If the input has `- casa = house`, the card front becomes `casa` and the back becomes `house` (instead of the default).

## 5. Add tags

Tag all cards with Anki tags:

```bash
anki_deck_from_text vocab.txt output "My Deck" --tags "spanish,beginner,chapter1"
```

## 6. Merge multiple input files

Combine several files into one deck:

```bash
anki_deck_from_text chapter1.txt full_course "Course" -i chapter2.txt -i chapter3.txt
```

All marked lines from all three files end up in a single deck.

## 7. Sound card model

Use the sound card model for audio-based study:

```bash
anki_deck_from_text vocab.txt listening_deck "Listening Practice" --card_model sound
```
