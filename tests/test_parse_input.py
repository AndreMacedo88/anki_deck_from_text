import os
import io
import tempfile
import pytest
from anki_deck_from_text.parse_input import (
    question_answer_split,
    generate_question_answer_dict,
    detect_encoding,
    fill_question_answer_dict,
    get_card_details,
)

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")


class TestQuestionAnswerSplit:
    line = "- answer = question"
    question, answer = question_answer_split(
        line=line,
        separator="=",
        marker="-",
    )

    def test_answer(self):
        assert self.answer == "answer"

    def test_question(self):
        assert self.question == "question"


class TestQuestionAnswerSplitUtf8:
    line = "- änswer = questiön"
    question, answer = question_answer_split(
        line=line,
        separator="=",
        marker="-",
    )

    def test_answer(self):
        assert self.answer == "änswer"

    def test_question(self):
        assert self.question == "questiön"


class TestQuestionAnswerSplitLatin:
    line = "- énswer = questiõn"
    question, answer = question_answer_split(
        line=line,
        separator="=",
        marker="-",
    )

    def test_answer(self):
        assert self.answer == "énswer"

    def test_question(self):
        assert self.question == "questiõn"


@pytest.mark.parametrize(
    argnames="file_name",
    argvalues=["md.md", "txt_utf8.txt"]
)
class TestGenerateQuestionAnswerDict:

    def test_dict(self, file_name):
        file_path = os.path.join(TEST_DATA_DIR, file_name)
        dict_expected = {
            "the girls": "die Mädchen",
            "the house": "das Haus"
        }
        dict_results = generate_question_answer_dict(
            file_path=file_path,
            separator="=",
            marker="-",
        )
        assert dict_results == dict_expected


class TestGenerateQuestionAnswerDictASCII:
    def test_dict(self):
        file_path = os.path.join(TEST_DATA_DIR, "txt_latin1.txt")
        dict_expected = {
            "the girls": "die Médchen",
            "the house": "das Haus"
        }
        dict_results = generate_question_answer_dict(
            file_path=file_path,
            separator="=",
            marker="-",
        )
        assert dict_results == dict_expected


class TestDetectEncoding:
    def test_utf8_file(self):
        file_path = os.path.join(TEST_DATA_DIR, "txt_utf8.txt")
        encoding, confidence = detect_encoding(file_path)
        assert encoding is not None
        assert confidence > 0.5

    def test_latin1_file(self):
        file_path = os.path.join(TEST_DATA_DIR, "txt_latin1.txt")
        encoding, confidence = detect_encoding(file_path)
        assert encoding is not None
        assert confidence > 0.5


class TestFillQuestionAnswerDict:
    def test_normal_lines(self):
        lines = io.StringIO("- back1 = front1\n- back2 = front2\n")
        result = fill_question_answer_dict(
            file_obj=lines, cards_details={}, marker="-", separator="="
        )
        assert result == {"front1": "back1", "front2": "back2"}

    def test_mixed_marked_unmarked(self):
        lines = io.StringIO("ignored line\n- back = front\nalso ignored\n")
        result = fill_question_answer_dict(
            file_obj=lines, cards_details={}, marker="-", separator="="
        )
        assert result == {"front": "back"}

    def test_empty_input(self):
        lines = io.StringIO("")
        result = fill_question_answer_dict(
            file_obj=lines, cards_details={}, marker="-", separator="="
        )
        assert result == {}

    def test_no_marked_lines(self):
        lines = io.StringIO("no marker here\nnor here\n")
        result = fill_question_answer_dict(
            file_obj=lines, cards_details={}, marker="-", separator="="
        )
        assert result == {}


class TestGetCardDetails:
    def test_valid_utf8_file(self):
        file_path = os.path.join(TEST_DATA_DIR, "txt_utf8.txt")
        result = get_card_details(
            file_path=file_path, encoding="UTF-8", marker="-", separator="="
        )
        assert "the girls" in result
        assert "the house" in result

    def test_bad_encoding_raises(self):
        file_path = os.path.join(TEST_DATA_DIR, "txt_latin1.txt")
        with pytest.raises(UnicodeDecodeError):
            get_card_details(
                file_path=file_path, encoding="UTF-8",
                marker="-", separator="="
            )


class TestEdgeCases:
    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False
        ) as f:
            f.write("")
            f.flush()
            result = generate_question_answer_dict(
                file_path=f.name, separator="=", marker="-"
            )
        os.unlink(f.name)
        assert result == {}

    def test_no_marked_lines(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False
        ) as f:
            f.write("no markers here\njust text\n")
            f.flush()
            result = generate_question_answer_dict(
                file_path=f.name, separator="=", marker="-"
            )
        os.unlink(f.name)
        assert result == {}

    def test_marked_line_without_separator(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False
        ) as f:
            f.write("- no separator here\n")
            f.flush()
            with pytest.raises(ValueError):
                generate_question_answer_dict(
                    file_path=f.name, separator="=", marker="-"
                )
        os.unlink(f.name)
