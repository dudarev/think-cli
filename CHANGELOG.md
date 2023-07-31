# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.1.8 (2023-07-31)

### Added

- `sort` - Sort sections in a Markdown file based on timestamps in the header. The `--reverse` option allows reversing the order of the sorted timestamps. Example usage: `t sort -i filename.md`. The command can also be used with `stdin`.
- `convert` - Convert all wikilinks in a Markdown file to Markdown links. For example, `[[2020-01-01 - Some title]]` is converted to `[2020-01-01 - Some title](2020-01-01 - Some title.md)`. Similarly, `[[Link|Alias]]` is converted to `[Alias](Link.md)`. The command can be used with a single file or a directory containing Markdown files. Usage: `t convert filename.md` or `t convert path/to/directory`.
- Github workflow with tests on PRs to the main branch

## 0.1.7 (2023-06-17)

### Changed

- Migrated from setup.py to pyproject.toml.
- Introduced package instead of a script
- Refactored commands to be more modular

## 0.1.6 (2023-02-13)

### Added

- `Makefile`
- `requirements-dev.txt` for development
- help to every command

### Changed

- Documentation is moved to [docs/](docs/README.md)

## 0.1.5 (2023-01-07)

### Added

- `ls -l` list files as wiki links

## 0.1.4 (2022-12-03)

### Changed

- `count` command by default counts file modified from midnight of today in local time
- `ls` command by default lists files modified today in local time

## 0.1.3

### Added

- `random` returns a random file

## 0.1.2

### Changed

- `ls` command shows only `.md` files

## 0.1.1

### Added

- `ls` command to list files modified in last 24 hours in reverse chronological order

## 0.1.0

### Added

- `count` command
- tests
