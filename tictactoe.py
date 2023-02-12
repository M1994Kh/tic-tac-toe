"""
Tic Tac Toe Player
"""

import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xs = 0
    os = 0
    es = 0
    for row in board:
        for item in row:
            if item == "X":
                xs += 1
            elif item == "O":
                os += 1
            else:
                es += 1
    if xs == os:
        return "X"
    elif es != 0:
        return "O"
    else:
        return None
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ac = []
    for j in range(3):
        for i in range(3):
            if board[i][j] == EMPTY:
                ac.append((i, j))
    return ac
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    I = initial_state()
    for j in range(3):
        for i in range(3):
            I[i][j] = board[i][j]
            I[action[0]][action[1]] = player(board)
    return(I)
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][2] == board[i][1] and board[i][1] != EMPTY:
            return board[i][1]
        elif board[0][i] == board[1][i] and board[2][i] == board[1][i] and board[1][i] != EMPTY:
            return board[1][i]
        elif board[0][0] == board[1][1] and board[2][2] == board[1][1] and board[1][1] != EMPTY:
            return board[1][1]
        elif board[2][0] == board[1][1] and board[0][2] == board[1][1] and board[1][1] != EMPTY:
            return board[1][1] 
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    es = 0
    for row in board:
        for item in row:
            if item == EMPTY:
                es += 1
    if es == 0 or winner(board) != None:
        return True
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal:
        if winner == X:
            return 1
        elif winner == O:
            return -1
    return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    attack =list()
    defense = list()
    def invert(pl):
        if pl == X:
            return O
        if pl == O:
            return X
    for action in actions(board):
        I = initial_state()
        for j in range(3):
            for i in range(3):
                I[i][j] = board[i][j]
        I[action[0]][action[1]] = player(board)
        if winner(I) == player(board):
            attack.append(action)
        I[action[0]][action[1]] = invert(player(board))
        if winner(I) == invert(player(board)):
            defense.append(action)
    for item in attack:
        print(f"Attack:{item}")
        return item
    for item in defense:
        print(f"Defense:{item}")
        return item
    return random.choice(actions(board))
    raise NotImplementedError
