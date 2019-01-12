from ..engine.board import Board


def test_new_board():
    width = 6
    height = 4
    board = Board(width=width, height=height)
    for x in range(width):
        for y in range(height):
            cell = board.at(x, y)
            assert cell._char == ' '


def test_put_stone():
    board = Board(3, 3)
    board.put_stone(column=0, stone_color='blue')
    cell = board.at(x=0, y=2)
    assert cell._char == 'O'
    assert cell._color == 'blue'
    """
    four_in_a_row.put_stone(board, 0, four_in_a_row.PLAYER_1_COLOR)
    assert set(board.values()) == {four_in_a_row.EMPTY_COLOR, four_in_a_row.PLAYER_1_COLOR}
    """


"""
def test_line_end_game_condition():
    board = four_in_a_row.create_board()
    for i in range(4):
        four_in_a_row.put_stone(board, 1 + i, four_in_a_row.PLAYER_1_COLOR)
    assert four_in_a_row.get_winner(board) == four_in_a_row.PLAYER_1_COLOR


def test_column_end_game_condition():
    board = four_in_a_row.create_board()
    for k in range(4):
        four_in_a_row.put_stone(board, 2, four_in_a_row.PLAYER_1_COLOR)
    assert four_in_a_row.get_winner(board) == four_in_a_row.PLAYER_1_COLOR


def test_diagonal_end_game_condition():
    board = four_in_a_row.create_board()

    four_in_a_row.put_stone(board, 1, four_in_a_row.PLAYER_1_COLOR)

    four_in_a_row.put_stone(board, 2, four_in_a_row.PLAYER_2_COLOR)
    four_in_a_row.put_stone(board, 2, four_in_a_row.PLAYER_1_COLOR)

    four_in_a_row.put_stone(board, 3, four_in_a_row.PLAYER_1_COLOR)
    four_in_a_row.put_stone(board, 3, four_in_a_row.PLAYER_2_COLOR)
    four_in_a_row.put_stone(board, 3, four_in_a_row.PLAYER_1_COLOR)

    four_in_a_row.put_stone(board, 4, four_in_a_row.PLAYER_2_COLOR)
    four_in_a_row.put_stone(board, 4, four_in_a_row.PLAYER_1_COLOR)
    four_in_a_row.put_stone(board, 4, four_in_a_row.PLAYER_2_COLOR)
    four_in_a_row.put_stone(board, 4, four_in_a_row.PLAYER_1_COLOR)

    assert four_in_a_row.get_winner(board) == four_in_a_row.PLAYER_1_COLOR
"""

