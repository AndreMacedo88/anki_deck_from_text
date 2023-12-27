import os
from anki_deck_from_text.parse_input import question_answer_split, generate_question_answer_dict


PARENT_DIR = os.path.dirname(os.path.realpath(__file__))


class TestQuestionAnswerSplit:
    line = "- answer = question"
    question, answer = question_answer_split(
        line=line,
        separator=" = "
    )

    def test_answer(self):
        assert self.answer == "answer"

    def test_question(self):
        assert self.question == "question"


class TestQuestionAnswerSplitUtf8:
    line = "- änswer = questiön"
    question, answer = question_answer_split(
        line=line,
        separator=" = "
    )

    def test_answer(self):
        assert self.answer == "änswer"

    def test_question(self):
        assert self.question == "questiön"


class TestGenerateQuestionAnswerDict:
    file_str = os.path.join(PARENT_DIR, "test_md.md")

    def test_dict(self):
        dict_expected = {
            "the girls": "die Mädchen",
            "the house": "das Haus"
        }
        dict_results = generate_question_answer_dict(
            input=self.file_str,
            separator=" = "
        )
        assert dict_results == dict_expected
