import os

import click

from .files import iter_markdown_files_modified_today


@click.command(
    help="Prints the total number of files and number of files modified today"
)
def count():
    n_files = len(os.listdir())
    n_modified_day = 0
    for _ in iter_markdown_files_modified_today():
        n_modified_day += 1
    click.echo(f"Total files: {n_files}")
    click.echo(f"Modified today: {n_modified_day}")
