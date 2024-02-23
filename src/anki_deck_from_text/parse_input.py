"""
Contains functions to go from a path to a text file to a dictionary in the format
{question: answer}
"""
from pathlib import Path
import chardet


def generate_question_answer_dict(file_path, separator, marker):
    try:
        # we try to open the file first assuming UTF-8
        cards_details = get_card_details(
            file_path=file_path,
            encoding="UTF-8",
            marker=marker,
            separator=separator,
        )
    except UnicodeEncodeError:
        # if UTF-8 is incorrect, incur a performance penalty trying to decode
        encoding, confidence = detect_encoding(file_path)
        try:
            cards_details = get_card_details(
                file_path=file_path,
                encoding=encoding,
                marker=marker,
                separator=separator,
            )
        except UnicodeEncodeError as err:
            message = (
                "File encoding not able to be automatically determined. ",
                f"Estimated encoding is {encoding} ",
                f"with confidence of {confidence}. ",
                "Please try to encode your file in UTF-8 and re-run."
            )
            raise err(message)
        if confidence < 0.6:
            print(
                (
                    "File encoding not able to be automatically determined. ",
                    f"Estimated encoding is {encoding} ",
                    f"with confidence of {confidence}. ",
                    "Card text characters may be incorrectly decoded. ",
                    "Either check all cards for accuracy, or ",
                    "please try to encode your file in UTF-8 and re-run."
                )
            )

    return cards_details


def get_card_details(file_path, encoding, marker, separator):
    cards_details = dict()
    with open(file_path, "r", encoding=encoding) as file_obj:
        return fill_question_answer_dict(
            file_obj=file_obj,
            cards_details=cards_details,
            marker=marker,
            separator=separator,
        )


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


def question_answer_split(line, separator, marker):
    line = line.lstrip(marker)
    answer, question = line.split(separator)
    return question.strip(), answer.strip()


def detect_encoding(file_path):
    """Detect encoding and return encoding and confidence level."""
    file_path = Path(file_path)

    # We must read as binary (bytes) because we don't yet know the encoding
    file_binary = file_path.read_bytes()

    detection = chardet.detect(file_binary)
    encoding = detection["encoding"]
    confidence = detection["confidence"]

    return encoding, confidence
