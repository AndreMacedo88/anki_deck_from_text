import os
import tempfile
import pytest
from click.testing import CliRunner
from anki_deck_from_text.cli import cli

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "test_data")


@pytest.fixture()
def runner():
    return CliRunner()


@pytest.fixture()
def utf8_file():
    return os.path.join(TEST_DATA_DIR, "txt_utf8.txt")


@pytest.fixture()
def md_file():
    return os.path.join(TEST_DATA_DIR, "md.md")


class TestCLIHelp:
    def test_help(self, runner):
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "INPUT" in result.output

    def test_help_short(self, runner):
        result = runner.invoke(cli, ["-h"])
        assert result.exit_code == 0
        assert "INPUT" in result.output


class TestCLIVersion:
    def test_version(self, runner):
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "anki_deck_from_text" in result.output


class TestCLIBasicExecution:
    def test_basic_run(self, runner, utf8_file):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = os.path.join(tmpdir, "out")
            result = runner.invoke(
                cli, [utf8_file, out, "TestDeck"]
            )
            assert result.exit_code == 0
            assert "Finished generating the deck" in result.output
            assert os.path.exists(f"{out}.apkg")

    def test_custom_separator_marker(self, runner):
        with tempfile.TemporaryDirectory() as tmpdir:
            infile = os.path.join(tmpdir, "input.txt")
            with open(infile, "w") as f:
                f.write("* back | front\n")
            out = os.path.join(tmpdir, "out")
            result = runner.invoke(
                cli,
                [infile, out, "TestDeck",
                 "--separator", "|", "--marker", "*"]
            )
            assert result.exit_code == 0

    def test_card_model_sound(self, runner, utf8_file):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = os.path.join(tmpdir, "out")
            result = runner.invoke(
                cli,
                [utf8_file, out, "TestDeck", "--card_model", "sound"]
            )
            assert result.exit_code == 0

    def test_invalid_card_model(self, runner, utf8_file):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = os.path.join(tmpdir, "out")
            result = runner.invoke(
                cli,
                [utf8_file, out, "TestDeck", "--card_model", "nonexistent"]
            )
            assert result.exit_code != 0


class TestCLIDryRun:
    def test_dry_run(self, runner, utf8_file):
        result = runner.invoke(
            cli, [utf8_file, "unused_output", "TestDeck", "--dry-run"]
        )
        assert result.exit_code == 0
        assert "Front:" in result.output
        assert "Back:" in result.output
        assert "card(s) would be generated" in result.output

    def test_preview_alias(self, runner, utf8_file):
        result = runner.invoke(
            cli, [utf8_file, "unused_output", "TestDeck", "--preview"]
        )
        assert result.exit_code == 0
        assert "card(s) would be generated" in result.output


class TestCLIReverse:
    def test_reverse_with_dry_run(self, runner, utf8_file):
        normal = runner.invoke(
            cli, [utf8_file, "unused", "TestDeck", "--dry-run"]
        )
        reversed_result = runner.invoke(
            cli,
            [utf8_file, "unused", "TestDeck", "--dry-run", "--reverse"]
        )
        assert normal.exit_code == 0
        assert reversed_result.exit_code == 0
        assert normal.output != reversed_result.output


class TestCLITags:
    def test_tags(self, runner, utf8_file):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = os.path.join(tmpdir, "out")
            result = runner.invoke(
                cli,
                [utf8_file, out, "TestDeck", "--tags", "lang,german"]
            )
            assert result.exit_code == 0
            assert "Finished generating the deck" in result.output


class TestCLIExtraInput:
    def test_extra_input(self, runner, utf8_file, md_file):
        with tempfile.TemporaryDirectory() as tmpdir:
            out = os.path.join(tmpdir, "out")
            result = runner.invoke(
                cli, [utf8_file, out, "TestDeck", "-i", md_file]
            )
            assert result.exit_code == 0
            assert "Finished generating the deck" in result.output


class TestCLIInputValidation:
    def test_nonexistent_file(self, runner):
        result = runner.invoke(
            cli, ["/nonexistent/file.txt", "out", "TestDeck"]
        )
        assert result.exit_code != 0
