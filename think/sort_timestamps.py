"""
Sorts sections in a Markdown file based on timestamps in the header.
It goes header by header and determines if an h2 header has a timestamp in the beginning in ISO format.
Optionally there may be dash and some other text after the timestamp.
It sorts all those sections based on the timestamps at the end of the returned text.
Reverse option is available.
"""
from pathlib import Path
import re
import sys

import click


def does_start_from_timestamp(text: str) -> bool:
    """
    Determines if the text is a timestamp header.

    Examples:
    2021-01-01
    2021-01-01 - Some title
    2021-01-01 12:00:00 - Some title
    """
    return re.match(r"^\d{4}-\d{2}-\d{2}", text.strip()) is not None


def do_sort(text: str, reverse=False) -> str:
    """Sorts all timestamps in the text."""

    # split the text based on `^## ` (h2 header)
    sections = re.split(r"^## ", text, flags=re.MULTILINE)
    is_first_h2_header = "## " in text[:3]
    first_section = ""
    if not is_first_h2_header:
        first_section, sections = sections[0].strip(), sections[1:]

    # for each section, check if it starts with a timestamp
    non_timestamp_sections = []
    timestamp_sections = []
    for s in sections:
        if not s.strip():
            continue
        if does_start_from_timestamp(s):
            timestamp_sections.append(s.strip())
        else:
            non_timestamp_sections.append(s.strip())

    timestamp_sections.sort(reverse=reverse)

    all_sections = [first_section] + non_timestamp_sections + timestamp_sections

    # return the text
    return "\n\n\n## ".join(all_sections).strip()


@click.command(
    "sort", help="Sort sections in a Markdown file based on timestamps in the header."
)
@click.option(
    "-i",
    "--input-file",
    help="File to read input from, default is `sys.stdin`.",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    default=sys.stdin,
)
@click.option(
    "-r",
    "--reverse",
    help="Reverse the order of the sorted timestamps.",
    is_flag=True,
    default=False,
)
def sort_timestamps(input_file: click.Path, reverse: bool):
    input_path = Path(input_file)
    out = do_sort(input_path.read_text(), reverse=reverse)
    input_path.write_text(out)
