import click

from .count import count
from .ls import ls
from .sort_timestamps import sort_timestamps
from .random import random
from .convert_wikilinks_to_markdown import convert_wikilinks


@click.group()
def cli():
    pass  # pragma: no cover


cli.add_command(count)
cli.add_command(ls)
cli.add_command(sort_timestamps)
cli.add_command(random)
cli.add_command(convert_wikilinks)
