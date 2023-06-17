# Release checklist

## Before release

- [ ] tests pass (`make test`)
- [ ] [CHANGELOG](../CHANGELOG.md) is updated
- [ ] version is updated in [VERSION](../VERSION) and [pyproject.toml](../pyproject.toml)

## After release

- [ ] add a tag for the release in git:

```bash
git tag -a 0.1.0 -m "0.1.0"
git push origin 0.1.0
```
