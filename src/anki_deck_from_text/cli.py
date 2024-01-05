import click
from .parse_input import generate_question_answer_dict
from .generate_deck import generate_deck_type_sound, write_package


@click.command()
@click.argument('input')
@click.argument("deck_name")
@click.option('--separator', default=" = ", help="Characters that separate the front and back of the cards")
def cli(input, deck_name, separator, out):
    """Generate and Anki deck from annotations on a text file"""

    question_answer_dict = generate_question_answer_dict(
        input=input,
        separator=separator
    )

    deck = generate_deck_type_sound(
        question_answer_dict=question_answer_dict,
        deck_name=deck_name,
    )

    write_package(deck, out)

    click.echo("Finished")
