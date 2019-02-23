from ..game import four_in_a_row


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


def test_winning_regression():
    board = four_in_a_row.create_board()

    four_in_a_row.put_stone(board, 0, four_in_a_row.PLAYER_1_COLOR)
    four_in_a_row.put_stone(board, 0, four_in_a_row.PLAYER_2_COLOR)
    four_in_a_row.put_stone(board, 0, four_in_a_row.PLAYER_1_COLOR)
    four_in_a_row.put_stone(board, 0, four_in_a_row.PLAYER_2_COLOR)

    four_in_a_row.put_stone(board, 1, four_in_a_row.PLAYER_1_COLOR)
    four_in_a_row.put_stone(board, 1, four_in_a_row.PLAYER_2_COLOR)

    four_in_a_row.put_stone(board, 2, four_in_a_row.PLAYER_1_COLOR)
    four_in_a_row.put_stone(board, 2, four_in_a_row.PLAYER_2_COLOR)

    four_in_a_row.put_stone(board, 3, four_in_a_row.PLAYER_1_COLOR)

    assert four_in_a_row.get_winner(board) == four_in_a_row.PLAYER_1_COLOR
"""

