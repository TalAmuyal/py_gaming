import click

import sys
sys.path.append("..")

from engine.board import Board


"""
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
"""

PLAYER_1_COLOR = 'blue'
PLAYER_2_COLOR = 'red'
EMPTY_COLOR = None

ROWS = 4
COLS = 6

STONE = 'O'


def ask_player_col():
    col = 0
    while not(0 < col <= COLS):
        col = click.prompt('Choose column', type=int)
    return col


'''
def game_loop_v1(board_):
    """
    Method: Look at the board and use
    the sone-color count to discern the player turn
    """
    click.echo('Version 1')
    def count_color_in_board(board_, color):
        """
        Set comprehension
        {
            element
            for element in collection
            if condition
        }
        """
        return len([
            cell_color
            for cell_color in board_.values()
            if cell_color == color
        ])

    print_board(board)
    while True:
        p1_count = count_color_in_board(board, PLAYER_1_COLOR)
        p2_count = count_color_in_board(board, PLAYER_2_COLOR)
        if p1_count == p2_count:
            color = PLAYER_1_COLOR
        else:
            color = PLAYER_2_COLOR
        put_stone(board, ask_player_col() - 1, color)
        print_board(board)


method_v2_global_variable = PLAYER_1_COLOR


def game_loop_v2(board_):
    """
    Method: Use a global variable to track player turn
    Quick and dirty
    """
    click.echo('Version 2')
    global method_v2_global_variable
    print_board(board)
    while True:
        put_stone(board, ask_player_col() - 1, method_v2_global_variable)
        print_board(board)
        if method_v2_global_variable == PLAYER_1_COLOR:
            method_v2_global_variable = PLAYER_2_COLOR
        else:
            method_v2_global_variable = PLAYER_1_COLOR
'''


def game_loop_v3(board):
    """
    Method: Using an inner loop to the pairs or turns
    """
    click.echo('Version 3')
    board.print()
    while True:
        for color in [PLAYER_1_COLOR, PLAYER_2_COLOR]:
            column = ask_player_col() - 1
            board.put_stone(column=column, stone_color=color)
            board.print()
            winner = get_winner(board)
            click.echo(f'{winner} is the winner!')
            if winner is not None:
                click.echo(f'{color} is the winner!')
                exit()


def get_others(board_, x, y, x_step, y_step):
    x_end = x + (3 * x_step)
    if not(0 <= x_end < COLS):
        return set()

    y_end = y + (3 * y_step)
    if not(0 <= y_end < ROWS):
        return set()

    return {
        board_[f'{x+(i+1)*x_step},{y+(i+1)*y_step}']
        for i in range(3)
    }


def get_winner(board: Board):
    """
    Return the color of the winner if such exists,
    Otherwise return None
    """
    for xy, color in board._b.items():
        if color == EMPTY_COLOR:
            continue
        str_x, str_y = xy.split(',')
        x = int(str_x)
        y = int(str_y)

        for x_step, y_step in [(1, 0), (0, 1), (1, 1), (1, -1)]:
            if get_others(board._b, x, y, x_step, y_step) == {color}:
                return color
    return None


if __name__ == '__main__':
    board = Board(width=COLS, height=ROWS)
    game_loop_v3(board)


"""
print_board(board)
put_stone(board, 0, 'blue')
print_board(board)
put_stone(board, 2, 'blue')
print_board(board)
put_stone(board, 0, 'blue')
print_board(board)
"""

