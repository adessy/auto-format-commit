## Auto Format commit

This [pre-commit](https://pre-commit.com/) hook automatically adds the issue key from the branch name to the commit message (if it is missing). It also slightly refomat the commit message along the way.

## Requirements

- Python 3

## Installation

- Install `pre-commit`
- Add the following snippet to `.pre-commit-config.yaml` [file](https://pre-commit.com/#2-add-a-pre-commit-configuration):
```yaml
repos:
  - repo: https://github.com/adessy/auto-format-commit
    rev: v0.0.1
    hooks:
      - id: auto-format-commit
```
- Run `pre-commit install -c .pre-commit-config.yaml --hook-type prepare-commit-msg`
