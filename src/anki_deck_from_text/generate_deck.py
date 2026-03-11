"""
Contains functions that take a dictionary {question: answer} and write an Anki
package (.apkg) with a deck containing cards with questions and answers.

The current available card types (models) are:
- `basic`
- `sound`

Check the models.py file for all models structure and implementation
"""

import random

import genanki

from .models import MODELS, EXTRA_FIELDS


def create_note(
    question: str,
    answer: str,
    model_type: str,
    tags: list[str] | None = None,
) -> genanki.Note:
    """Create a genanki Note for the given question/answer pair."""
    model = MODELS.get(model_type)
    extra_fields = EXTRA_FIELDS.get(model_type)

    if model is None:
        raise ValueError("model_type does not exist in the current models.")
    elif extra_fields:
        note = genanki.Note(
            model=model,
            fields=[question, answer, *extra_fields],
            tags=tags or [],
        )
    else:
        note = genanki.Note(
            model=model,
            fields=[question, answer],
            tags=tags or [],
        )
    return note


def create_deck(deck_name: str) -> genanki.Deck:
    """Create a new genanki Deck with a random ID."""
    deck_id = random.randrange(1 << 30, 1 << 31)
    deck = genanki.Deck(
        deck_id=deck_id,
        name=deck_name,
    )
    return deck


def generate_deck(
    question_answer_dict: dict[str, str],
    deck_name: str,
    card_model: str,
    tags: list[str] | None = None,
) -> genanki.Deck:
    """Generate a complete deck from a question/answer dictionary."""
    deck = create_deck(deck_name=deck_name)

    for key, value in question_answer_dict.items():
        note = create_note(
            question=key,
            answer=value,
            model_type=card_model,
            tags=tags,
        )
        deck.add_note(note)

    return deck


def write_package(deck: genanki.Deck, out: str) -> None:
    """Write the deck to an .apkg file."""
    out = out.removesuffix(".apkg")
    genanki.Package(deck).write_to_file(f"{out}.apkg")
