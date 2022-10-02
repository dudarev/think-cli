import os
from datetime import datetime
from pathlib import Path

import click


@click.group()
def cli():
    pass


@click.command()
def count():
    n_files = len(os.listdir())
    n_modified_day = 0
    utcnow = datetime.utcnow()
    for p in Path().iterdir():
        if (utcnow - datetime.fromtimestamp(os.path.getmtime(p))).days < 1:
            n_modified_day += 1

    click.echo(f"Total files: {n_files}")
    click.echo(f"Modified in a day: {n_modified_day}")


cli.add_command(count)
