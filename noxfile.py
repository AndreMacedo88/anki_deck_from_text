import os
import nox
import nox_poetry

APP_DIR = os.path.join("src", "anki_deck_from_text")

nox.options.reuse_existing_virtualenvs = True

@nox_poetry.session(python=["3.11", "3.12"])
def tests(session):
    session.install("pytest", ".")
    session.run("pytest")

@nox_poetry.session
def format(session):
    session.install("autopep8", ".")
    session.run("autopep8", "--in-place", "--recursive", "tests")
    session.run("autopep8", "--in-place", "--recursive", APP_DIR)