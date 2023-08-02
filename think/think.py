import click

from .count import count
from .ls import ls
from .sort_timestamps import sort_timestamps
from .random import random
from .convert_wikilinks_to_markdown import convert_wikilinks
from .fan_sections import fan_sections


@click.group()
def cli():
    pass  # pragma: no cover


cli.add_command(convert_wikilinks)
cli.add_command(count)
cli.add_command(fan_sections)
cli.add_command(ls)
cli.add_command(random)
cli.add_command(sort_timestamps)
