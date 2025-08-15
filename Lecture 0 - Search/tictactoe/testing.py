import copy
from math import ceil

X = "X"
O = "O"
EMPTY = None

board =[[1, X, X],
        [O, X, O],
        [X, O, 3]]


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

        #print(diagonal_numbers)
        for i in range(ceil(len(diagonal_numbers)/2)):
            diagonal_possibilities = diagonal_numbers[i*3:i*3+3]
            #print(diagonal_possibilities)

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


winners = winner(board)
print(winners)
    
    
