import os

from datetime import datetime, timedelta, timezone
from uuid import uuid4

import pytest
from pathlib import Path

from click.testing import CliRunner


LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo


FILE_1_NAME = "file-1.md"
FILE_2_NAME = "file-2.md"
FILE_1_CONTENT = "FILE 1 CONTENT"
FILE_2_CONTENT = "FILE 2 CONTENT"

OBSIDIAN_DIR_NAME = ".obsidian"


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
def random_markdown_file(cli_runner_and_dir) -> Path:
    _, tmp_dir = cli_runner_and_dir
    random_str = str(uuid4())
    p = tmp_dir / (random_str + ".md")
    p.write_text(random_str)
    return p


@pytest.fixture
def one_file_modified_before_midnight(random_markdown_file):
    stat = os.stat(random_markdown_file)
    local_one_day_ago = datetime.now() - timedelta(days=1)
    new_mtime = local_one_day_ago.replace(
        hour=23, minute=59, second=59, tzinfo=LOCAL_TIMEZONE
    )
    os.utime(random_markdown_file, times=(stat.st_atime, new_mtime.timestamp()))


@pytest.fixture
def one_file_modified_after_midnight(random_markdown_file):
    stat = os.stat(random_markdown_file)
    local_one_day_ago = datetime.now()
    new_mtime = local_one_day_ago.replace(
        hour=0, minute=0, second=1, tzinfo=LOCAL_TIMEZONE
    )
    os.utime(random_markdown_file, times=(stat.st_atime, new_mtime.timestamp()))


@pytest.fixture
def obsidian_dir(cli_runner_and_dir):
    _, tmp_dir = cli_runner_and_dir
    (tmp_dir / OBSIDIAN_DIR_NAME).mkdir()
