import click
from .parse_input import generate_question_answer_dict


@click.command()
@click.argument('input')
@click.option('--separator', default=" = ", help="Characters that separate the front and back of the cards")
def cli(input, separator):
    """Generate Anki decks and cards from annotations on a text file"""
    generate_question_answer_dict(
        input=input,
        separator=separator
    )
    click.echo("Finished")
