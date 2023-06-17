import click

from .count import count
from .ls import ls
from .sort_timestamps import sort
from .random import random


@click.group()
def cli():
    pass  # pragma: no cover


cli.add_command(count)
cli.add_command(ls)
cli.add_command(sort)
cli.add_command(random)
