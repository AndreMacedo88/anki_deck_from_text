import os
import pytest
from unittest.mock import MagicMock
import itertools
import time
import genanki
from anki_deck_from_text.models import MODEL_SOUND

PARENT_DIR = os.path.dirname(os.path.realpath(__file__))


def test_model_sound_ok():
    n = genanki.Note(
        model=MODEL_SOUND,
        fields=["House", "das Haus", ""]
    )

    n.write_to_db(
        MagicMock(), MagicMock(), MagicMock(),
        itertools.count(int(time.time() * 1000))
    )
    # test passes if code gets to here without raising


def test_model_sound_wrong_number_of_fields():
    n = genanki.Note(
        model=MODEL_SOUND,
        fields=["House", "das Haus"]  # missing one (empty) field for Sound
    )

    with pytest.raises(ValueError):
        n.write_to_db(
            MagicMock(), MagicMock(), MagicMock(),
            itertools.count(int(time.time() * 1000))
        )
