from pathlib import Path

from click.testing import CliRunner
import pytest
from tests.assets.sort_timestamps import (
    CONTENT_TO_SORT,
    SORTED_CONTENT,
    SORTED_CONTENT_REVERSED,
    CONTENT_TO_SORT_WITH_NON_TIMESTAMP,
    CONTENT_WITH_NON_TIMESTAMP_SORTED,
    CONTENT_WITH_DATE_TO_SORT,
    CONTENT_WITH_DATE_SORTED_REVERSED,
)

from tests.conftest import FixtureFile
from think import sort_timestamps


@pytest.mark.parametrize(
    "file_with_content, flags, sorted_content",
    [
        pytest.param("", "", "", id="sort-empty"),
        pytest.param("# Some title", "-r", "# Some title", id="sort-no-timestamp"),
        pytest.param(CONTENT_TO_SORT, "", SORTED_CONTENT, id="sort"),
        pytest.param(CONTENT_TO_SORT, "-r", SORTED_CONTENT_REVERSED, id="sort-reverse"),
        pytest.param(
            CONTENT_TO_SORT_WITH_NON_TIMESTAMP,
            "",
            CONTENT_WITH_NON_TIMESTAMP_SORTED,
            id="sort-non-timestamp",
        ),
        pytest.param(
            CONTENT_WITH_DATE_TO_SORT,
            "-r",
            CONTENT_WITH_DATE_SORTED_REVERSED,
            id="sort-date",
        ),
    ],
    indirect=["file_with_content"],
)
def test_sort(
    cli_runner_and_dir: tuple[CliRunner, Path],
    file_with_content: FixtureFile,
    flags: str,
    sorted_content: str,
):
    cli_runner, _ = cli_runner_and_dir
    params = ["-i", str(file_with_content.path)]
    if flags:
        params.append(flags)
    result = cli_runner.invoke(sort_timestamps, params)
    assert result.exit_code == 0
    assert file_with_content.path.read_text() == sorted_content
