import os


def test_entrypoint():
    exit_status = os.system("anki_deck_from_text --help")
    assert exit_status == 0

# TODO: test all arguments to the CLI
