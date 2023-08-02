from pathlib import Path
import pytest

from think.markdown import MarkdownFile, MarkdownSection


MARKDOWN_FILE_IN = """# Title
## Section 1
Content 1"""


@pytest.fixture
def markdown_file(tmp_path: Path):
    path = tmp_path / "file.md"
    path.write_text(MARKDOWN_FILE_IN)
    return MarkdownFile(path)


def test_get_h2_sections(markdown_file: MarkdownFile):
    assert markdown_file.get_h2_sections() == [
        MarkdownSection("Section 1", "Content 1"),
    ], "should return only h2 sections"
    markdown_file.add_section(MarkdownSection("Section 2", "Content 2"))
    assert markdown_file.get_h2_sections() == [
        MarkdownSection("Section 1", "Content 1"),
        MarkdownSection("Section 2", "Content 2"),
    ], "should return all h2 sections"


def test_markdown_file(markdown_file: MarkdownFile):
    assert markdown_file.path.name == "file.md"
    markdown_file.add_section(MarkdownSection("Section 1", "Content 1"))
    assert markdown_file.path.read_text() == MARKDOWN_FILE_IN, "should not change"
    markdown_file.add_section(MarkdownSection("Section 2", "Content 2"))
    assert (
        markdown_file.path.read_text()
        == MARKDOWN_FILE_IN + "\n\n## Section 2\nContent 2"
    ), "should add section"
