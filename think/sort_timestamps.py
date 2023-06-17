"""
Sorts sections in a Markdown file based on timestamps in the header.
It goes header by header and determines if an h2 header has a timestamp in the beginning in ISO format.
Optionally there may be dash and some other text after the timestamp.
It sorts all those sections based on the timestamps at the end of the returned text.
"""
import re
import sys

import click

TEST_TEXT = """
Some text
# Main title

## 2020-01-03 - Some other title
Some other text

## 2020-01-01 - Some title
Some text
## Some non-timestamp title
non-timestamp text
## 2020-01-02 - Some other title
Some other text
"""


def does_start_from_timestamp(text: str):
    """Determines if the text is a timestamp header."""
    # check if the text starts with a timestamp in ISO format
    # return True or False
    return re.match(r"^\d{4}-\d{2}-\d{2}.+", text)


def sort_timestamps(text: str, reverse=False):
    """Sorts all timestamps in the text."""

    # split the text based on `^## ` (h2 header)
    sections = re.split(r"^## ", text, flags=re.MULTILINE)
    is_first_h2_header = "## " in text[:3]
    first_section = ""
    if not is_first_h2_header:
        first_section, sections = sections[0], sections[1:]

    # for each section, check if it starts with a timestamp
    non_timestamp_sections = []
    timestamp_sections = []
    for s in sections:
        if does_start_from_timestamp(s):
            timestamp_sections.append(s)
        else:
            non_timestamp_sections.append(s)

    timestamp_sections.sort(reverse=reverse)

    # return the text
    return "## ".join(
        [
            first_section,
        ]
        + non_timestamp_sections
        + timestamp_sections
    )


@click.command(
    help="Sort sections in a Markdown file based on timestamps in the header."
)
@click.option(
    "-i",
    "--input-file",
    help="File to read input from, default is `sys.stdin`.",
    type=click.File("r"),
    default=sys.stdin,
)
def sort(input_file):
    with input_file:
        text = input_file.read()
        click.echo(sort_timestamps(text))


if __name__ == "__main__":
    print(sort_timestamps(TEST_TEXT, reverse=True))
