import click
from .parse_input import generate_question_answer_dict
from .generate_deck import generate_deck, write_package


@click.command()
@click.argument("input")
@click.argument("output")
@click.argument("deck_name")
@click.option("--separator", default=" = ", help="Characters that separate the front and back of the cards")
@click.option("--card_model", default="sound", help="Characters that separate the front and back of the cards")
def cli(input, output, deck_name, separator, card_model):
    """Generate and Anki deck from annotations on a text file"""

    question_answer_dict = generate_question_answer_dict(
        input=input,
        separator=separator,
    )

    deck = generate_deck(
        question_answer_dict=question_answer_dict,
        deck_name=deck_name,
        card_model=card_model,
    )

    write_package(deck, output)

    click.echo("Finished generating the deck")
