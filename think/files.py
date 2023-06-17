import os
from datetime import datetime, timezone
from pathlib import Path

LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo


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
