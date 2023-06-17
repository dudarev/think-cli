import os

import click

from .files import iter_markdown_files_modified_today

CONVERTER_FOR_LINKS_PARAMETER = {
    True: lambda x: f'[[{str(x).replace(".md", "")}]]',
    False: lambda x: x,
}


@click.command(help="List files changed today")
@click.option("-l", "--links", is_flag=True, help="Formats files as wiki links")
def ls(links):
    files = [(os.path.getmtime(p), p) for p in iter_markdown_files_modified_today()]
    files.sort(reverse=True)
    for f in files:
        click.echo(CONVERTER_FOR_LINKS_PARAMETER[links](f[1]))
