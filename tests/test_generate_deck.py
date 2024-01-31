import os
import pytest
from unittest.mock import MagicMock
import itertools
import time
from anki_deck_from_text.generate_deck import create_note, generate_deck

PARENT_DIR = os.path.dirname(os.path.realpath(__file__))


def test_note():
    note = create_note(
        question="House",
        answer="das Haus",
        model_type="sound",
    )

    note.write_to_db(
        MagicMock(), MagicMock(), MagicMock(),
        itertools.count(int(time.time() * 1000))
    )
    # test passes if code gets to here without raising


def test_note_incorrect_model():
    with pytest.raises(ValueError):
        _ = create_note(
            question="House",
            answer="das Haus",
            model_type="incorrect_type",
        )


@pytest.fixture()
def deck_test():
    question_answer_dict = {
        "the girls": "die Mädchen",
        "the house": "das Haus"
    }
    deck = generate_deck(
        question_answer_dict=question_answer_dict,
        deck_name="test_name",
        card_model="sound",
    )
    yield deck


class TestGenerateDeckTypeSound():
    def test_notes_number(self, deck_test):
        assert len(deck_test.notes) == 2

    def test_notes_fields(self, deck_test):
        fields = [field for note in deck_test.notes for field in note.fields]
        assert fields == [
            "the girls", "die Mädchen", "", "the house", "das Haus", ""
        ]

    def test_notes_model(self, deck_test):
        models_name = [note.model.name for note in deck_test.notes]
        assert models_name == ["Sound model", "Sound model"]
