import os
from datetime import datetime, timezone
from pathlib import Path
from random import choice

import click

LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo


@click.group()
def cli():
    pass


MARKDOWN_FILE_EXTENSIONS = {
    "md",
    "mkd",
    "mdwn",
    "mdown",
    "mdtxt",
    "mdtext",
    "markdown",
    "text",
    "txt",
}


def is_markdown(p: Path):
    extension = p.suffix.lower().replace(".", "")
    return extension in MARKDOWN_FILE_EXTENSIONS


def is_modified_today(p: Path):
    today_local = datetime.now().replace(
        hour=0, minute=0, second=0, tzinfo=LOCAL_TIMEZONE
    )
    mtime = datetime.fromtimestamp(os.path.getmtime(p)).replace(tzinfo=LOCAL_TIMEZONE)
    return mtime > today_local


def iter_markdown_files_modified_today():
    for p in Path().iterdir():
        if is_markdown(p) and is_modified_today(p):
            yield p


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


cli.add_command(count)
cli.add_command(ls)
cli.add_command(random)
