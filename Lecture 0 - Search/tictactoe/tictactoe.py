"""
Tic Tac Toe Player
"""

import math
from math import ceil
import copy
import random
import time

X = "X"
O = "O"
EMPTY = None


def initial_state(): #Done
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): #Done
    """
    Returns player who has the next turn on a board.
    """

    X_count=0
    O_count=0
    EMPTY_Count=0

    for rows in board:
        for values in rows:
            if values == X:
                X_count +=1
            if values == O:
                O_count +=1
            if values == EMPTY:
                EMPTY_Count +=1

    if EMPTY_Count == 9:
        return X
    
    if EMPTY_Count %2 == 0:
        return O
    
    if EMPTY_Count %2 > 0:
        return X


def actions(board): #Done
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))

    #returning possible_actions in the form: {(0, 2), (1, 2)}
    
    return possible_actions


def result(board, action): #Done
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    column = action[1]

    board_copy = copy.deepcopy(board)
    whos_action = player(board)

    if action not in actions(board):
        raise Exception("Invalid Move")

    def valid_space(board):
        if board[row][column] == EMPTY:
            return True

    if whos_action == X and valid_space:
        board_copy[row][column] = X
    
    if whos_action == O and valid_space:
        board_copy[row][column] = O

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    def horizontal_win(board):
        horizontal_numbers=[]

        for j in range(len(board)):
            for i in range(len(board)):
                horizontal_numbers.append(board[j][i])
        
        for i in range(ceil(len(horizontal_numbers)/3)):
            horizontal_possibilities = horizontal_numbers[i*3:i*3+3]
            if set(horizontal_possibilities) == set('X'):
                return True, X
            elif set(horizontal_possibilities) == set("O"):
                return True, O

        return False, None
    
    def vertical_win(board):
        vertical_numbers = []

        for j in range(len(board)):
            for i in range(len(board)):
                vertical_numbers.append(board[i][j])
        

        for i in range(ceil(len(vertical_numbers)/3)):
            vertical_possibilities = vertical_numbers[i*3:i*3+3]
            if set(vertical_possibilities) == set("X"):
                return True, X
            elif set(vertical_possibilities) == set("O"):
                return True, O
        
        return False, None

    def diagonal_win(board):
        diagonal_numbers = []

        for n in range(len(board)):
            TLBR = board[n][n]
            diagonal_numbers.append(TLBR)
        
        for n in range(len(board)):
            TRBL = board[n][len(board) - 1 - n]
            diagonal_numbers.append(TRBL)

        for i in range(ceil(len(diagonal_numbers)/2)):
            diagonal_possibilities = diagonal_numbers[i*3:i*3+3]
            if set(diagonal_possibilities) == set("X"):
                return True, X
            elif set(diagonal_possibilities) == set("O"):
                return True, O

        return False, None


    win, who = horizontal_win(board)
    if win:
        return who

    win, who = vertical_win(board)
    if win:
        return who
    
    win, who = diagonal_win(board)
    if win:
        return who
    
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    possible_actions = actions(board)

    if winner(board) == X or winner(board) == O:
        return True

    if len(possible_actions) == 0 and winner(board) == None: 
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None


    def Max_Value(board):
        action_maxv_mapping={}
        v=-1000000000

        if terminal(board):
            return utility(board),{}
        
        for action in actions(board):
            val, _ = Min_value(result(board,action))
            v = max(v, val)
            action_maxv_mapping.update({action:val})
        
        return v, action_maxv_mapping
    

    def Min_value(board):
        action_minv_mapping={}
        v = 1000000000

        if terminal(board):
            return utility(board), {}
        
        for action in actions(board):
            val, _ = Max_Value(result(board,action))
            v = min(v, val)
            action_minv_mapping.update({action:val})

        return v, action_minv_mapping

    
    if player(board) == X:
        start_time=time.time()
        v, action_maxv_mapping = Max_Value(board)
        best_action = max(action_maxv_mapping, key=action_maxv_mapping.get)
        print("Action Took:", time.time()-start_time, "seconds")
        return best_action
    
    if player(board) == O:
        start_time = time.time()
        v, action_minv_mapping = Min_value(board)
        best_action = min(action_minv_mapping, key=action_minv_mapping.get)
        print("Action Took:", time.time()-start_time, "seconds")
        return best_action
        
