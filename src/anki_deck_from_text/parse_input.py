"""
Contains functions to go from a path to a text file to a dictionary in the format
{question: answer}
"""

import warnings
from pathlib import Path
from typing import IO

import chardet


def generate_question_answer_dict(
    file_path: str, separator: str, marker: str
) -> dict[str, str]:
    """Parse an input file and return a {question: answer} dict.

    Tries UTF-8 first, then falls back to chardet-detected encoding.
    """
    try:
        # we try to open the file first assuming UTF-8
        cards_details = get_card_details(
            file_path=file_path,
            encoding="UTF-8",
            marker=marker,
            separator=separator,
        )
    except UnicodeDecodeError:
        # if UTF-8 is incorrect, incur a performance penalty trying to decode
        encoding, confidence = detect_encoding(file_path)
        try:
            cards_details = get_card_details(
                file_path=file_path,
                encoding=encoding,
                marker=marker,
                separator=separator,
            )
        except UnicodeDecodeError as err:
            raise ValueError(
                f"File encoding not able to be automatically determined. "
                f"Estimated encoding is {encoding} "
                f"with confidence of {confidence}. "
                f"Please try to encode your file in UTF-8 and re-run."
            ) from err
        if confidence < 0.6:
            warnings.warn(
                f"File encoding not able to be automatically determined. "
                f"Estimated encoding is {encoding} "
                f"with confidence of {confidence}. "
                f"Card text characters may be incorrectly decoded. "
                f"Either check all cards for accuracy, or "
                f"please try to encode your file in UTF-8 and re-run."
            )

    return cards_details


def get_card_details(
    file_path: str, encoding: str, marker: str, separator: str
) -> dict[str, str]:
    """Open a file with the given encoding and extract card details."""
    cards_details: dict[str, str] = dict()
    with open(file_path, "r", encoding=encoding) as file_obj:
        return fill_question_answer_dict(
            file_obj=file_obj,
            cards_details=cards_details,
            marker=marker,
            separator=separator,
        )


def fill_question_answer_dict(
    file_obj: IO[str],
    cards_details: dict[str, str],
    marker: str,
    separator: str,
) -> dict[str, str]:
    """Filter marked lines from file_obj and split into question/answer pairs."""
    for line in file_obj:
        line = line.strip()
        if not line.startswith(marker):
            continue

        front, back = question_answer_split(
            line=line,
            separator=separator,
            marker=marker,
        )
        cards_details[front] = back
    return cards_details


def question_answer_split(
    line: str, separator: str, marker: str
) -> tuple[str, str]:
    """Split a marked line into (front, back) card content.

    Strips the marker from the left, splits on the separator, and returns
    (right-of-separator, left-of-separator) as (front, back).
    """
    line = line.lstrip(marker)
    back, front = line.split(separator)
    return front.strip(), back.strip()


def detect_encoding(file_path: str) -> tuple[str, float]:
    """Detect encoding and return encoding and confidence level."""
    file_path_obj = Path(file_path)

    # We must read as binary (bytes) because we don't yet know the encoding
    file_binary = file_path_obj.read_bytes()

    detection = chardet.detect(file_binary)
    encoding: str = detection["encoding"]
    confidence: float = detection["confidence"]

    return encoding, confidence
