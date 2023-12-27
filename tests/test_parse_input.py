from anki_deck_from_text.parse_input import question_answer_split, generate_question_answer_dict


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
