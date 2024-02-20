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
    try:
        with open(input, "r", encoding="utf-8") as file_obj:
            cards_details = fill_question_answer_dict(
                file_obj=file_obj,
                cards_details=cards_details,
                marker=marker,
                separator=separator,
            )
    except UnicodeEncodeError:
        with open(input, "r", encoding="ISO-8859-1") as file_obj:
            cards_details = fill_question_answer_dict(
                file_obj=file_obj,
                cards_details=cards_details,
                marker=marker,
                separator=separator,
            )

    return cards_details


def fill_question_answer_dict(file_obj, cards_details, marker, separator):
    for line in file_obj:
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
