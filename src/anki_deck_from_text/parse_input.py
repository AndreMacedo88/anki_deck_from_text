"""
Contains functions to go from a path to a text file to a dictionary in the format
{question: answer}
"""


def question_answer_split(line, separator, marker):
    line = line.lstrip(marker)
    answer, question = line.split(separator)
    return question.strip(), answer.strip()


def generate_question_answer_dict(input, separator, marker):
    cards_details = dict()
    with open(input, encoding="utf-8") as FileObj:
        for line in FileObj:
            line = line.strip()
            if not line.startswith(marker):
                continue

            question, answer = question_answer_split(
                line=line,
                separator=separator,
                marker=marker,
            )
            cards_details[question] = answer
    return cards_details
