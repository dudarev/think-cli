"""
Fan out sections in a Markdown file based on the links mentioned in the sections
"""
from pathlib import Path

import click

from think.markdown import get_links, MarkdownFile

from think.sort_timestamps import sort_timestamps_in_text


def do_fanning(input_path: Path):
    click.echo(f"Fanning {input_path}...")
    input_file = MarkdownFile(input_path)
    touched_link_paths = set()
    for section in input_file.get_h2_sections():
        links = get_links(str(section))
        for link in links:
            # do not replace extension if it already exists, add .md
            link_path = input_path.parent / (link + ".md")
            if not link_path.exists():
                link_path.touch()
            link_file = MarkdownFile(link_path)
            link_file.add_section(section)
            touched_link_paths.add(link_path)
    for link_path in touched_link_paths:
        content = link_path.read_text()
        sorted_content = sort_timestamps_in_text(content)
        link_path.write_text(sort_timestamps_in_text(sorted_content))


@click.command(
    "fan",
    help="Fan out sections in a Markdown file based on the links mentioned in the sections",
)
@click.argument(
    "input",
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
)
def fan_sections(input):
    input_path = Path(input)
    do_fanning(input_path)
