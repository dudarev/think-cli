from pathlib import Path
from random import choice

import click


@click.command(help="Return a random .md file if it exists")
def random():
    files = []
    for p in Path().iterdir():
        if str(p).endswith(".md"):
            files.append(p)
    if not files:
        click.echo("No files available")
        return
    random_file = choice(files)
    click.echo(random_file)
