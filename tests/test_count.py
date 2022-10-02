import os
from pathlib import Path


from click.testing import CliRunner


from think import count


def test_count_zero(cli_runner_and_dir: tuple[CliRunner, Path]):

    cli_runner, tmp_dir = cli_runner_and_dir
    assert len(os.listdir(tmp_dir)) == 0

    result = cli_runner.invoke(count)
    assert result.exit_code == 0
    assert result.output == "Total files: 0\nModified in a day: 0\n"


def test_count_two(cli_runner_and_dir: tuple[CliRunner, Path], two_files):

    cli_runner, tmp_dir = cli_runner_and_dir
    assert len(os.listdir(tmp_dir)) == 2

    result = cli_runner.invoke(count)
    assert result.exit_code == 0
    assert result.output == "Total files: 2\nModified in a day: 2\n"
