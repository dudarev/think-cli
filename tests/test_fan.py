from pathlib import Path

from click.testing import CliRunner
import pytest

from think import fan_sections

from tests.conftest import FixtureFile
from tests.assets.fan_sections import (
    EXISTING_FILE_NAME,
    FILES_IN,
    FILES_OUT,
    FILE_NAME_TO_FAN,
    FILES_IN_WITH_DOT,
    FILES_OUT_WITH_DOT,
)


@pytest.mark.parametrize(
    "files_with_content, file_name_to_fan, expected_files",
    [
        pytest.param(FILES_IN, FILE_NAME_TO_FAN, FILES_OUT, id="fan-out"),
        pytest.param(FILES_IN, EXISTING_FILE_NAME, FILES_IN, id="fan-out-not-changed"),
        pytest.param(
            FILES_IN_WITH_DOT,
            FILE_NAME_TO_FAN,
            FILES_OUT_WITH_DOT,
            id="fan-out-with-dot",
        ),
    ],
    indirect=["files_with_content"],
)
def test_fan(
    cli_runner_and_dir: tuple[CliRunner, Path],
    files_with_content: FixtureFile,
    file_name_to_fan: str,
    expected_files: str,
):
    cli_runner, tmp_dir = cli_runner_and_dir
    result = cli_runner.invoke(fan_sections, [file_name_to_fan])
    assert result.exit_code == 0
    for file_name, content in expected_files.items():
        assert (
            tmp_dir / file_name
        ).read_text() == content, f"{file_name} not as expected"
