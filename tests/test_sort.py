from pathlib import Path

from click.testing import CliRunner
import pytest
from tests.assets import CONTENT_TO_SORT, SORTED_CONTENT, SORTED_CONTENT_REVERSED

from tests.conftest import FixtureFile
from think import sort_timestamps


@pytest.mark.parametrize(
    "file_with_content, flags, sorted_content",
    [
        pytest.param("", "", "", id="sort-empty"),
        pytest.param("# Some title", "-r", "# Some title", id="sort-no-timestamp"),
        pytest.param(CONTENT_TO_SORT, "", SORTED_CONTENT, id="sort"),
        pytest.param(CONTENT_TO_SORT, "-r", SORTED_CONTENT_REVERSED, id="sort-reverse"),
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
