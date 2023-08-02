from dataclasses import dataclass
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import uuid4

import pytest
from click.testing import CliRunner

LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo


# TODO: extract to assets
FILE_1_NAME = "file-1.md"
FILE_2_NAME = "file-2.md"
FILE_1_CONTENT = "FILE 1 CONTENT [[file-2]] [[Another file]]"
FILE_2_CONTENT = "FILE 2 CONTENT [[Link|Alias]]"
FILE_1_CONVERTED_CONTENT = (
    "FILE 1 CONTENT [file-2](file-2.md) [Another file](Another file.md)"
)
FILE_2_CONVERTED_CONTENT = "FILE 2 CONTENT [Alias](Link.md)"

OBSIDIAN_SETTINGS_DIR_NAME = ".obsidian"

FILE_WITH_TIMESTAMPS_CONTENT = """
"""


@dataclass
class FixtureFile:
    path: Path
    content: str


@pytest.fixture
def cli_runner_and_dir(tmp_path) -> tuple[CliRunner, Path]:
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path) as cli_runner_dir:
        yield runner, Path(cli_runner_dir)


@pytest.fixture
def file_with_content(cli_runner_and_dir, request: str) -> FixtureFile:
    _, tmp_dir = cli_runner_and_dir
    original_content = request.param
    path = tmp_dir / "file.md"
    path.write_text(original_content)
    return FixtureFile(path=path, content=original_content)


@pytest.fixture
def files_with_content(
    cli_runner_and_dir, request: dict[str, str]
) -> list[FixtureFile]:
    _, tmp_dir = cli_runner_and_dir
    files = []
    for file_name, content in request.param.items():
        path = tmp_dir / file_name
        path.write_text(content)
        files.append(FixtureFile(path=path, content=content))
    return files


@pytest.fixture
def two_files(cli_runner_and_dir) -> tuple[FixtureFile, FixtureFile]:
    _, tmp_dir = cli_runner_and_dir
    path_1 = tmp_dir / FILE_1_NAME
    path_2 = tmp_dir / FILE_2_NAME
    path_1.write_text(FILE_1_CONTENT)
    path_2.write_text(FILE_2_CONTENT)
    file_1 = FixtureFile(path=path_1, content=FILE_1_CONTENT)
    file_2 = FixtureFile(path=path_2, content=FILE_2_CONTENT)
    return (file_1, file_2)


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
def obsidian_settings_dir(cli_runner_and_dir):
    _, tmp_dir = cli_runner_and_dir
    (tmp_dir / OBSIDIAN_SETTINGS_DIR_NAME).mkdir()
