import os

import pytest
from pathlib import Path

from click.testing import CliRunner

FILE_1_NAME = "file-1.md"
FILE_2_NAME = "file-2.md"
OBSIDIAN_DIR_NAME = ".obsidian"
FILE_1_CONTENT = "FILE 1 CONTENT"
FILE_2_CONTENT = "FILE 2 CONTENT"


@pytest.fixture
def cli_runner_and_dir(tmp_path) -> tuple[CliRunner, Path]:
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path) as cli_runner_dir:
        yield runner, Path(cli_runner_dir)


@pytest.fixture
def two_files(cli_runner_and_dir):
    _, tmp_dir = cli_runner_and_dir
    (tmp_dir / FILE_1_NAME).write_text(FILE_1_CONTENT)
    (tmp_dir / FILE_2_NAME).write_text(FILE_2_CONTENT)


@pytest.fixture
def obsidian_dir(cli_runner_and_dir):
    _, tmp_dir = cli_runner_and_dir
    (tmp_dir / OBSIDIAN_DIR_NAME).mkdir()
