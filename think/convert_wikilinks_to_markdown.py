"""
Given a Markdown file,
convert all wikilinks to Markdown links.

For example:
[[2020-01-01 - Some title]] -> [2020-01-01 - Some title](2020-01-01 - Some title.md)
[[Link|Alias]] -> [Alias](Link.md)
"""

from pathlib import Path
import click

from think.markdown import convert_wikilinks_to_markdown


def convert_file(input_path: Path):
    output_path = input_path.with_suffix(".md")
    click.echo(f"Converting {input_path}...")
    text = input_path.read_text()
    text = convert_wikilinks_to_markdown(text)
    output_path.write_text(text)


@click.command(
    "convert",
    help="Convert all wikilinks to Markdown links in a Markdown file.",
)
@click.argument(
    "input",
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
)
def convert_wikilinks(input):
    input_path = Path(input)
    if input_path.is_dir():
        # iterate over all files in the directory recursively
        files = input_path.glob("**/*.md")
    else:
        files = [input_path]

    for file in files:
        convert_file(file)
