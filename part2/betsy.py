import sys
from moveBetsy import moveBird
import random
import numpy as np
from moveEval import evalBoard

def arrangeBoard(board):
    brd = np.reshape(board,(8,8))
    return brd


def evaluation_function(board):
    return (random.randint(1,5), board)


def rotate_board(board):
    brd = board.copy()
    for i in range(len(board)):
        for j in range(len(board[0])):
            brd[i, len(board[0])-1-j] = board[len(board)-1-i, j]
    return brd


def successor(color, board):
    nextMoves = []
    friend = 'PNBRQK' if color == 'w' else 'pnbrqk'
    board_list = [(col + len(board)*row, board[row][col]) for row in range(len(board)) for col in range(len(board[0]))]
    for i,j in board_list:
        if j in friend:
            for move in moveBird(color,friend,j,i//8,i%8,board):
                nextMoves.append(move)
    return nextMoves


def maximize(depth, board, color, max_depth, alpha, beta):
    max_value = -1000000
    best_move = board
    op_color = 'w' if color == 'b' else 'b'
    if depth == max_depth:
        return evalBoard(color, board)
    for move in successor(color, board):
        score, _ = minimize(depth+1, rotate_board(move), op_color, max_depth, alpha, beta)
        if score > max_value:
            max_value = score
            best_move = move
        if max_value >= beta:
            return (max_value, best_move)
        if max_value > alpha:
            alpha = max_value

    return (max_value, best_move)


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


def nice_output(board):
    out = ''
    for row in range(len(board)):
        for col in range(len(board[0])):
            out += board[row][col]
    return out


def choose(board, color, max_depth, alpha, beta):
    best_choice = maximize(1, board, color, max_depth, alpha, beta)
    return nice_output(best_choice[1])
        

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
    max_depth = 5
    alpha = -1000000
    beta = 1000000

    print(choose(board, color, max_depth, alpha, beta))
    

    
