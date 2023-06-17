from pathlib import Path
from unittest import mock

from click.testing import CliRunner

from conftest import FILE_1_NAME
from think import random


def test_random_empty(cli_runner_and_dir: tuple[CliRunner, Path]):
    cli_runner, tmp_dir = cli_runner_and_dir
    result = cli_runner.invoke(random)
    assert result.exit_code == 0
    assert result.output == "No files available\n"


@mock.patch("think.random.choice", return_value=FILE_1_NAME)
def test_random_two_files(
    mock_random_choice, cli_runner_and_dir: tuple[CliRunner, Path], two_files
):
    cli_runner, tmp_dir = cli_runner_and_dir
    result = cli_runner.invoke(random)
    assert result.exit_code == 0
    assert result.output == FILE_1_NAME + "\n"
