# Welcome

This repository is a Python based solved for the Waffle game.

It is an opportunity to learn Python with types, using `uv` as the package manager, and using the [textual](https://textual.textualize.io/) framework for a nice tui.

# Initial setup

Created the repository using:

``` sh
uv init waffle-solver
```

Added textual using (sideeffect is to create the virtual environment):

``` sh
uv add textual
uv add --dev textual-dev
uv add --dev pytest
uv sync
uv lock
```
