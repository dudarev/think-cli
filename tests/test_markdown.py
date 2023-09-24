import pytest
from think.markdown import get_links, MarkdownSection, MarkdownFile


@pytest.mark.parametrize(
    "text, expected_links",
    [
        pytest.param("", set(), id="empty"),
        pytest.param(
            "Some text",
            set(),
            id="no-links",
        ),
        pytest.param(
            "[[Link]]",
            {"Link"},
            id="one-link",
        ),
        pytest.param(
            "[[Link|Alias]]",
            {"Link"},
            id="one-link-with-alias",
        ),
        pytest.param(
            "[[Link]] [[Link]]",
            {"Link"},
            id="two-links",
        ),
        pytest.param(
            "[[Link]] [[Link|Alias]]",
            {"Link"},
            id="two-links-with-alias",
        ),
        pytest.param(
            "[[Link.com]]",
            {"Link.com"},
            id="link-with-dot",
        ),
    ],
)
def test_get_links(text, expected_links):
    assert get_links(text) == expected_links


@pytest.mark.parametrize(
    "title, content, level, expected_repr",
    [
        pytest.param("Title", "Content", 2, "## Title\nContent", id="level-2"),
        pytest.param("Title", "Content", 3, "### Title\nContent", id="level-3"),
    ],
)
def test_markdown_section(title, content, level, expected_repr):
    assert str(MarkdownSection(title, content, level)) == expected_repr


def test_markdown_section_in_set():
    section_1 = MarkdownSection("Title", "Content")
    section_2 = MarkdownSection("Title", "Content")
    assert not section_1 == "## Title\nContent"
    assert section_1 is not section_2
    assert section_1 == section_2
    assert section_1 in {section_2}
    assert section_2 in {section_1}
    assert len({section_1, section_2}) == 1
