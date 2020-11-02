import sys
from moveBetsy import moveBird
import random
import numpy as np
from moveEval import evalBoard

# The general idea for how to implement the minimax algorithm in actual Python came from 
# https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
# We adapted the concepts from their code that was originally created for playing Tic-Tac-Toe

# convert the board string into a nicer data structure 
def arrangeBoard(board):
    brd = np.reshape(board,(8,8))
    return brd

# our code to move the pieces always assumes the player currently moving is on top
# so we need to rotate the board in order correctly move the pieces
def rotate_board(board):
    brd = board.copy()
    for i in range(len(board)):
        for j in range(len(board[0])):
            brd[i, len(board[0])-1-j] = board[len(board)-1-i, j]
    return brd

# generates a list of possible next moves to take given a board state and a color (i.e. which player is currently moving)
def successor(color, board):
    nextMoves = []
    friend = 'PNBRQK' if color == 'w' else 'pnbrqk'
    board_list = [(col + len(board)*row, board[row][col]) for row in range(len(board)) for col in range(len(board[0]))]
    for i,j in board_list:
        if j in friend:
            for move in moveBird(color,friend,j,i//8,i%8,board):
                nextMoves.append(move)
    return nextMoves

# this is one half of the minimax algorithm
def maximize(depth, board, color, max_depth, alpha, beta):
    max_value = -1000000
    best_move = board
    # when passing the set of moves to minimize we need to swap colors/players 
    op_color = 'w' if color == 'b' else 'b'
    # this stops the recursive calls back and forth to min/max and instead runs the evaluation function
    if depth == max_depth:
        return evalBoard(color, board)
    # for each possible move for the given player choose the move the maximizes the score given from the 
    # the set of possible moves that the opposing player just minimized over
    for move in successor(color, board):
        score, _ = minimize(depth+1, rotate_board(move), op_color, max_depth, alpha, beta)
        if score > max_value:
            max_value = score
            best_move = move
        # if the max value exceeds the value of beta, there is no need to continue searching through the tree 
        if max_value >= beta:
            return (max_value, best_move)
        # if a larger alpha value has been found make sure to update for the next pass through minimize
        if max_value > alpha:
            alpha = max_value
    return (max_value, best_move)

# this is the other half of the minimax algorithm
# it is identical to maximize mutatis mutandis but tries to choose the minimum score from available boards
# instead of the maximum
def minimize(depth, board, color, max_depth, alpha, beta):
    min_value = 1000000
    best_move = board
    op_color = 'w' if color == 'b' else 'b'
    if depth == max_depth:
        return evalBoard(color, board)
    for move in successor(color, board):
        score, _ = maximize(depth+1, rotate_board(move), op_color, max_depth, alpha, beta)
        if score < min_value:
            min_value = score
            best_move = move
        if min_value <= alpha:
            return (min_value, best_move)
        if min_value < beta:
            beta = min_value
    return (min_value, best_move)


# we need to convert the numpy array back into acceptable output for the next player to make their move
def nice_output(board,color):
    if color == 'b':
        board = rotate_board(board)
    out = ''
    for row in range(len(board)):
        for col in range(len(board[0])):
            out += board[row][col]
    return out


# a simple function that is used to kick off the minimax algorithm and actually choose the next move
def choose(board, color, max_depth, alpha, beta):
    best_choice = maximize(1, board, color, max_depth, alpha, beta)
    return nice_output(best_choice[1],color)
        

if __name__ == "__main__":
    
    ### Error handling of command line inputs ###
    if(len(sys.argv) != 4):
        raise(Exception("Error: Expected player(b/w), initial board and time out value. No Spaces in Arguments!"))

    if(sys.argv[1] not in ['b', 'w']):
        raise(Exception("Error: Player can be only black(b) or white(w)"))

    if(len(sys.argv[2]) != 64):
        raise(Exception("Error: Board should be exact 64 squares"))
    
    color = str(sys.argv[1])
    board = arrangeBoard(list(sys.argv[2]))
    timeout = sys.argv[3]
    
    #set the initial levels for alpha and beta
    alpha = -1000000
    beta = 1000000

    #everything assumes that the person currently moving is on "top" and since white is on top by default we need to rotate the board
    if color == 'b':
        board = rotate_board(board)
    # we know we can quickly get through a depth of 3 so we run that just in case we run out of time for the deeper tree
    max_depth = 3
    print(choose(board, color, max_depth, alpha, beta))
    max_depth = 5
    print(choose(board, color, max_depth, alpha, beta))
