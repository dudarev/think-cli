"""
Testing convert command from convert_wikilinks_to_markdown.py
"""
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import (
    FILE_1_CONVERTED_CONTENT,
    FILE_2_CONVERTED_CONTENT,
    FILE_2_CONTENT,
)
from think import convert_wikilinks


def test_convert(cli_runner_and_dir: tuple[CliRunner, Path], two_files):
    cli_runner, test_dir = cli_runner_and_dir
    result = cli_runner.invoke(convert_wikilinks, [str(test_dir)])
    assert result.exit_code == 0
    file_1, file_2 = two_files
    assert (
        file_1.path.read_text() == FILE_1_CONVERTED_CONTENT
    ), "File 1 converted not as expected"
    assert (
        file_2.path.read_text() == FILE_2_CONVERTED_CONTENT
    ), "File 2 converted not as expected"


def test_convert_file(cli_runner_and_dir: tuple[CliRunner, Path], two_files):
    cli_runner, _ = cli_runner_and_dir
    file_1, file_2 = two_files
    result = cli_runner.invoke(convert_wikilinks, [str(file_1.path)])
    assert result.exit_code == 0
    assert (
        file_1.path.read_text() == FILE_1_CONVERTED_CONTENT
    ), "File 1 converted not as expected"
    assert file_2.path.read_text() == FILE_2_CONTENT, "File 2 changed unexpectedly"
