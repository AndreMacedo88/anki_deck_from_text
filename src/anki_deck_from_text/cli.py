"""
Command-line interface for anki_deck_from_text
"""

import click
from .parse_input import generate_question_answer_dict
from .generate_deck import generate_deck, write_package

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    show_default=True,
)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("input")
@click.argument("output")
@click.argument("deck_name")
@click.option("--separator", default="=", help="Character(s) that separate the text to be written to the front and back of the cards")
@click.option("--marker", default="-", help="Character(s) marking this line to be included in the deck")
@click.option("--card_model", default="basic",
              help="""Anki card model to build the deck with. Available options are:
              `basic`,
              `sound`
              """
              )
def cli(input, output, deck_name, separator, marker, card_model):
    """Generate and Anki deck from annotations on a text file.\n
    INPUT is the text file.
    OUTPUT is the desired name for the .apkg file with the deck.
    DECK_NAME is the deck name that will be displayed in Anki.
    """

    question_answer_dict = generate_question_answer_dict(
        input=input,
        separator=separator,
        marker=marker,
    )

    deck = generate_deck(
        question_answer_dict=question_answer_dict,
        deck_name=deck_name,
        card_model=card_model,
    )

    write_package(deck, output)

    click.echo("Finished generating the deck")
