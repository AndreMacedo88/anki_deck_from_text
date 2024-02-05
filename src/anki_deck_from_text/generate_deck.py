"""
Contains functions that take a dictionary {question: answer} and write an Anki
package (.apkg) with a deck containing cards with questions and answers.

The current available card types (models) are:
- "sound"

Check the models.py file for all models structure and implementation
"""

import random
import genanki
from anki_deck_from_text.models import MODELS


def create_note(question, answer, model_type):
    model = MODELS.get(model_type)
    if model is None:
        raise ValueError("model_type does not exist in the current models.")
    note = genanki.Note(
        model=model,
        fields=[question, answer, ""]
    )
    return note


def create_deck(deck_name):
    deck_id = random.randrange(1 << 30, 1 << 31)
    deck = genanki.Deck(
        deck_id=deck_id,
        name=deck_name,
    )
    return deck


def generate_deck(question_answer_dict, deck_name, card_model):
    deck = create_deck(deck_name=deck_name)

    for key, value in question_answer_dict.items():
        note = create_note(
            question=key,
            answer=value,
            model_type=card_model,
        )
        deck.add_note(note)

    return deck


def write_package(deck, out):
    out = out.removesuffix(".apkg")
    genanki.Package(deck).write_to_file(f"{out}.apkg")
