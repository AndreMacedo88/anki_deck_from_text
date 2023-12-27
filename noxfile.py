import os
import nox_poetry

APP_DIR = os.path.join("src", "anki_deck_from_text")

@nox_poetry.session
def tests(session):
    session.install("pytest", ".")
    session.run("pytest")

@nox_poetry.session
def format(session):
    session.install("autopep8", ".")
    session.run("autopep8", "--in-place", "--recursive", "tests")
    session.run("autopep8", "--in-place", "--recursive", APP_DIR)