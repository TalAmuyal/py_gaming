import click

import typing


BORDER_COLOR = 'green'

# C:\YAKOV\Documents\python-kaki\pipi\gaming


class Cell:
    def __init__(
            self,
            char: str = ' ',
            color: str = None,
            ) -> None:
        self._char = char
        self._color = color

    def print(self) -> None:
        print_colored(self._char, self._color)


class Board:
    def __init__(
            self,
            width: int,
            height: int,
            ) -> None:
        self._width = width
        self._height = height
        self._b = {
            f'{x},{y}': Cell()
            for x in range(width)
            for y in range(height)
        }

    def print(self):
        print_column_numbers(self._width)
        for y in range(self._height):
            row = [
                self.at(x, y)
                for x in range(self._width)
            ]
            print_row(row)
            new_row()
        new_row()

    def at(
            self,
            x: int,
            y: int,
            ) -> Cell:
        return self._b[f'{x},{y}']

    def put_stone(
            self,
            column: int,
            stone_color: str,
            ) -> None:
        row = self._height - 1
        while self.at(x=column, y=row)._char != ' ':
            row -= 1
        cell = self.at(x=column, y=row)
        cell._char = 'O'
        cell._color = stone_color


def print_column_numbers(cols: int) -> None:
    print_colored(' ', None)
    for x in range(cols):
        print_colored(f'{x+1} ', BORDER_COLOR)
    new_row()


def print_colored(s, color) -> None:
    click.secho(s, fg=color, nl=False)


def new_row() -> None:
    click.echo()


def print_row(row: typing.List[Cell]) -> None:
    print_colored('|', BORDER_COLOR)
    for cell in row:
        cell.print()
        print_colored('|', BORDER_COLOR)

