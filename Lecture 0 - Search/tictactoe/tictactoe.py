"""
Tic Tac Toe Player
"""

import math
import copy

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
    nr_x = 0
    nr_o = 0
    for i in board:
        for j in i:
            if j == X:
                nr_x += 1
            elif j == O:
                nr_o += 1
    if board == initial_state():
        return X
    elif nr_x > nr_o:
        return O
    elif nr_x <= nr_o:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action = (i, j)
                actions_set.add(action)
    return actions_set



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    if i not in [0, 1, 2] or j not in [0, 1, 2]:
      raise Exception
    elif board[i][j] != EMPTY:
      raise Exception

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][1]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][1]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][2]
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[1][1]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[1][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[2][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == EMPTY: 
                    return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        val, move = max_value(board)
        return move
    elif player(board) == O:
        val, move = min_value(board)
        return move

def max_value(board):
    if terminal(board):
        return utility(board), None
    val = -100
    best_move = None
    for action in actions(board):
        aux, move = min_value(result(board, action))
        if aux > val:
            val = aux
            best_move = action
    return val, best_move

def min_value(board):
    if terminal(board):
        return utility(board), None
    val = 100
    best_move = None
    for action in actions(board):
        aux, move = max_value(result(board, action))
        if aux < val:
            val = aux
            best_move = action
    return val, best_move

