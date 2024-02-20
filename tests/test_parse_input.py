import os
import pytest
from anki_deck_from_text.parse_input import question_answer_split, \
    generate_question_answer_dict


PARENT_DIR = os.path.dirname(os.path.realpath(__file__))


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
    argvalues=["test_md.md", "test_txt.txt"]
)
class TestGenerateQuestionAnswerDict:

    def test_dict(self, file_name):
        file_path = os.path.join(PARENT_DIR, file_name)
        dict_expected = {
            "the girls": "die Mädchen",
            "the house": "das Haus"
        }
        dict_results = generate_question_answer_dict(
            input=file_path,
            separator="=",
            marker="-",
        )
        assert dict_results == dict_expected


class TestGenerateQuestionAnswerDictASCII:
    def test_dict(self):
        file_path = os.path.join(PARENT_DIR, "test_txt_ascii.txt")
        dict_expected = {
            "the girls": "die Madchen",
            "the house": "das Haus"
        }
        dict_results = generate_question_answer_dict(
            input=file_path,
            separator="=",
            marker="-",
        )
        assert dict_results == dict_expected
