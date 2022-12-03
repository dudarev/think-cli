from pathlib import Path

from click.testing import CliRunner

from think import ls

from conftest import FILE_1_NAME, FILE_2_NAME


def test_list_zero(cli_runner_and_dir: tuple[CliRunner, Path]):

    cli_runner, _ = cli_runner_and_dir
    result = cli_runner.invoke(ls)
    assert result.exit_code == 0
    assert result.output == ""


def test_list_two_with_hidden(
    cli_runner_and_dir: tuple[CliRunner, Path], two_files, obsidian_dir
):
    cli_runner, _ = cli_runner_and_dir
    result = cli_runner.invoke(ls)
    assert result.exit_code == 0
    assert result.output == f"{FILE_2_NAME}\n{FILE_1_NAME}\n"


def test_list_two_with_and_one_yesterday(
    cli_runner_and_dir: tuple[CliRunner, Path],
    two_files,
    one_file_modified_before_midnight,
):
    cli_runner, _ = cli_runner_and_dir
    result = cli_runner.invoke(ls)
    assert result.exit_code == 0
    assert result.output == f"{FILE_2_NAME}\n{FILE_1_NAME}\n"
