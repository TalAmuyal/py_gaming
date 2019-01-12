# Py Gaming

This is an exercise project to learn python.

## Requirements

- Python 3.7
- pytest
- click

## Progress

Split out board code into it's own module (`from board import Board`).
Make a test file for `board`, but thus far converted only the first 2 tests.

TODO:

- Finish up tests for `board`
- Adjust tests for `four_in_a_row.py`

Currently, `four_in_a_row.py` has bugs.
Specifically for a row.

## Commands:

`tree` - print a recursive directory and file tree

`python game/four_in_a_row/four_in_a_row.py` - Run the Four-in-a-row game.
`python game/xo/xo.py` - Run the X/O game.

`pytest -f ./test/` (`python3 -m pytest -f ./test/` on Tals PC) - Run all the tests in the `./test/` directory (`-f` means re-run on file save).

