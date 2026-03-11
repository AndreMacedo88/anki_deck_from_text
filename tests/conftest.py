import os
import pytest

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")


@pytest.fixture()
def test_data_dir():
    return TEST_DATA_DIR


@pytest.fixture()
def utf8_file_path():
    return os.path.join(TEST_DATA_DIR, "txt_utf8.txt")


@pytest.fixture()
def latin1_file_path():
    return os.path.join(TEST_DATA_DIR, "txt_latin1.txt")


@pytest.fixture()
def md_file_path():
    return os.path.join(TEST_DATA_DIR, "md.md")


@pytest.fixture()
def sample_qa_dict():
    return {
        "the girls": "die Mädchen",
        "the house": "das Haus",
    }
