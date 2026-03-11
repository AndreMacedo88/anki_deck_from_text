"""
Command-line interface for anki_deck_from_text
"""

import click
from . import __version__
from .models import MODELS
from .parse_input import generate_question_answer_dict
from .generate_deck import generate_deck, write_package

CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    show_default=True,
)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=__version__, prog_name="anki_deck_from_text")
@click.argument("input_file", metavar="INPUT", type=click.Path(exists=True))
@click.argument("output")
@click.argument("deck_name")
@click.option("--separator", default="=",
              help="Character(s) that separate the text to be written to the front and back of the cards")
@click.option("--marker", default="-",
              help="Character(s) marking this line to be included in the deck")
@click.option("--card_model", default="basic",
              type=click.Choice(list(MODELS.keys()), case_sensitive=False),
              help="Anki card model to build the deck with")
@click.option("--reverse", is_flag=True, default=False,
              help="Swap front and back of each card")
@click.option("--dry-run", "--preview", is_flag=True, default=False,
              help="Preview cards that would be generated without writing a file")
@click.option("--tags", default=None,
              help="Comma-separated tags to add to all cards")
@click.option("--extra-input", "-i", multiple=True,
              type=click.Path(exists=True),
              help="Additional input files to merge into the deck (repeatable)")
def cli(
    input_file: str,
    output: str,
    deck_name: str,
    separator: str,
    marker: str,
    card_model: str,
    reverse: bool,
    dry_run: bool,
    tags: str | None,
    extra_input: tuple[str, ...],
) -> None:
    """Generate an Anki deck from annotations on a text file.\n
    INPUT is the text file.
    OUTPUT is the desired name for the .apkg file with the deck.
    DECK_NAME is the deck name that will be displayed in Anki.
    """

    question_answer_dict = generate_question_answer_dict(
        file_path=input_file,
        separator=separator,
        marker=marker,
    )

    for extra_file in extra_input:
        extra_dict = generate_question_answer_dict(
            file_path=extra_file,
            separator=separator,
            marker=marker,
        )
        question_answer_dict.update(extra_dict)

    if reverse:
        question_answer_dict = {v: k for k, v in question_answer_dict.items()}

    if dry_run:
        for front, back in question_answer_dict.items():
            click.echo(f"Front: {front}")
            click.echo(f"Back:  {back}")
            click.echo("---")
        click.echo(f"{len(question_answer_dict)} card(s) would be generated.")
        return

    tag_list: list[str] | None = None
    if tags:
        tag_list = [t.strip() for t in tags.split(",")]

    deck = generate_deck(
        question_answer_dict=question_answer_dict,
        deck_name=deck_name,
        card_model=card_model,
        tags=tag_list,
    )

    write_package(deck, output)

    click.echo("Finished generating the deck")
