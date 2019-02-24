# Py Gaming

This is an exercise project to learn python using game-writing.
The projects breakdown is thus:

- `terminal_games` - A collection of games written with basic terminal interaction
- `pyxel_games` - A collection of games written using Pyxel for 2D retro graphics


## Requirements

- Python
- `pipenv`
  - Manages a virtual environment that contains the Python dependenceis
  - Installation: `pip install pipenv`
- `pyxel` low-level library
  - Required only for `pyxel`-based projects
  - Installation: TBD


## Running

Before running a project for the first time:
1. `cd` to the project's root folder
2. Run `pip install`

After the initial setup, run `pipenv run src`.


# Cheatsheet

## Shell Commands

- `pwd` - Print the current working directory
- `cd PATH` - Change the (current) directory to the specified path `PATH`
  - Example: `cd ~/Documents` changes the current working directory to the `Documents` folder in the user's home folder
- `tree` - Print a recursive directory and file tree
- `pytest -f ./test/` - Run all the tests in the `./test/` directory (`-f` means re-run on file save)

