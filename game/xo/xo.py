import click


EMPTY = '#'


def run():
    board = make_board()
    while not game_ended(board):
        redraw(board)
        play_turn(board)
    redraw(board)
    announce_winner(board)


def make_board():
    return {
        at(x, y): EMPTY
        for x in range(3)
        for y in range(3)
    }


def at(x, y):
    return f'{x},{y}'


def game_ended(board):
    return EMPTY not in board.values() or get_winner(board) is not None


def redraw(board):
    click.clear()
    for x in range(3):
        for y in range(3):
            click.echo(board[f'{x},{y}'], nl=False)
        click.echo('')


def play_turn(board):
    xy = click.prompt('Choose a place')
    board[xy] = player(board)


def player(board):
    empty_slots = len([k for k, v in board.items() if v == EMPTY])
    return 'O' if empty_slots % 2 == 0 else 'X'


def get_winner(board):
    triplets = []
    for x in range(3):
        row = {
            board[at(x, y)]
            for y in range(3)
        }
        triplets.append(row)
        col = {
            board[at(y, x)]
            for y in range(3)
        }
        triplets.append(col)
    diag = {
        board[at(0, 0)],
        board[at(1, 1)],
        board[at(2, 2)],
    }
    triplets.append(diag)
    neg_diag = {
        board[at(0, 2)],
        board[at(1, 1)],
        board[at(0, 2)],
    }
    triplets.append(neg_diag)
    for triplet in triplets:
        win = get_triplet_winner(triplet)
        if win is not None:
            return win
    return None


def get_triplet_winner(triplet):
    if EMPTY in triplet:
        return None
    if len(triplet) == 1:
        return triplet.pop()
    return None


def announce_winner(board):
    winner = get_winner(board)
    if winner is None:
        click.echo('Tie')
    else:
        click.echo(f'The winner is {winner}')


if __name__ == '__main__':
    run()

