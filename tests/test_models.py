import os
import pytest
from unittest.mock import MagicMock
import itertools
import time
import genanki
from anki_deck_from_text.models import (
    MODEL_SOUND, MODEL_BASIC, MODELS, EXTRA_FIELDS,
)

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")


""" Tests for the basic model """


def test_model_basic_ok():
    n = genanki.Note(
        model=MODEL_BASIC,
        fields=["House", "das Haus"]
    )

    n.write_to_db(
        MagicMock(), MagicMock(), MagicMock(),
        itertools.count(int(time.time() * 1000))
    )
    # test passes if code gets to here without raising


def test_model_basic_wrong_number_of_fields():
    n = genanki.Note(
        model=MODEL_BASIC,
        fields=["House", "das Haus", ""]  # extra (empty) field for basic model
    )

    with pytest.raises(ValueError):
        n.write_to_db(
            MagicMock(), MagicMock(), MagicMock(),
            itertools.count(int(time.time() * 1000))
        )


""" Tests for the sound model """


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


""" Tests for MODELS and EXTRA_FIELDS dicts """


class TestModelsDict:
    def test_keys_exist(self):
        assert "basic" in MODELS
        assert "sound" in MODELS

    def test_values_are_genanki_models(self):
        for model in MODELS.values():
            assert isinstance(model, genanki.Model)

    def test_extra_fields_keys_match_models(self):
        assert set(EXTRA_FIELDS.keys()) == set(MODELS.keys())

    def test_model_ids_in_valid_range(self):
        for model in MODELS.values():
            assert (1 << 30) <= model.model_id < (1 << 31)

    def test_model_ids_are_different(self):
        ids = [model.model_id for model in MODELS.values()]
        assert len(ids) == len(set(ids))
