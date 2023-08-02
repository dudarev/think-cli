from pathlib import Path
import re


def does_start_from_timestamp(text: str) -> bool:
    """
    Determines if the text is a timestamp header.

    Examples:
    2021-01-01
    2021-01-01 - Some title
    2021-01-01 12:00:00 - Some title
    """
    return re.match(r"^\d{4}-\d{2}-\d{2}", text.strip()) is not None


def convert_wikilinks_to_markdown(text: str) -> str:
    """
    Replace all wikilinks with Markdown links.
    [[Link]] -> [Link](Link.md)
    [[Link|Alias]] -> [Alias](Link.md)
    """
    return re.sub(
        r"\[\[(?P<filename>[^\]|]+)(\|(?P<alias>[^\]]+))?\]\]",
        lambda match: f"[{match.group('alias') or match.group('filename')}]({match.group('filename')}.md)",
        text,
    )


def get_links(text: str) -> set[str]:
    """
    Get all links in the text.
    """
    # iterate over all matches and return the filename
    res = set()
    for match in re.finditer(
        r"\[\[(?P<filename>[^\]|]+)(\|(?P<alias>[^\]]+))?\]\]", text
    ):
        res.add(match.group("filename"))
    return res


class MarkdownSection:
    def __init__(self, title, content, level=2):
        self.title = title.strip()
        self.content = content.strip()
        self.level = level

    def __hash__(self) -> int:
        return hash((self.title, self.content))

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, MarkdownSection):
            return False
        return self.title == o.title and self.content == o.content

    def __str__(self) -> str:
        return f"{'#' * self.level} {self.title}\n{self.content}"


class MarkdownFile:
    def __init__(self, path: Path) -> None:
        self.path = path

    def get_h2_sections(self) -> list[MarkdownSection]:
        text = self.path.read_text()
        # split the text based on `^## ` (h2 header)
        sections = re.split(r"^## ", text, flags=re.MULTILINE)
        # if first section is not h2, remove it
        if not sections[0].strip().startswith("##"):
            sections.pop(0)
        # iterate over each section
        res = []
        for section_text in sections:
            if not section_text.strip():
                continue
            # get the title of the section
            section_lines = section_text.split("\n")
            # create the section
            res.append(
                MarkdownSection(
                    title=section_lines[0],
                    content="\n".join(section_lines[1:]),
                )
            )
        return res

    def add_section(self, section: MarkdownSection) -> None:
        """
        Add a new section to the file.
        """
        sections = self.get_h2_sections()
        if section in sections:
            return
        self.path.write_text(self.path.read_text() + "\n\n" + str(section))
