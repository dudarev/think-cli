import os
from datetime import datetime
from pathlib import Path
from random import choice

import click

DAYS_TO_SELECT = 1


@click.group()
def cli():
    pass


@click.command()
def count():
    n_files = len(os.listdir())
    n_modified_day = 0
    utcnow = datetime.utcnow()
    for p in Path().iterdir():
        if (utcnow - datetime.fromtimestamp(os.path.getmtime(p))).days < DAYS_TO_SELECT:
            n_modified_day += 1

    click.echo(f"Total files: {n_files}")
    click.echo(f"Modified in a day: {n_modified_day}")


@click.command()
def ls():
    files = []
    utcnow = datetime.utcnow()
    for p in Path().iterdir():
        if (utcnow - datetime.fromtimestamp(os.path.getmtime(p))).days < DAYS_TO_SELECT:
            if str(p).endswith(".md"):
                files.append((os.path.getmtime(p), p))
    files.sort(reverse=True)
    for f in files:
        click.echo(f[1])


@click.command()
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


cli.add_command(count)
cli.add_command(ls)
cli.add_command(random)
