import sys
import time
import re
import numpy as np
from moveBetsy import moveBird
import random

#
# The points weightage has been taken from https://www.chessprogramming.org/Simplified_Evaluation_Function
#
points = [100,320,330,500,900,20000]
p,n,b,r,q,k = points
P,N,B,R,Q,K = points


def validBoard(board):
    return False if re.search('[^pnbrqkPNBRQK.]', board) else True


def arrangeBoard(board):
    brd = np.reshape(board,(8,8))
    return brd

max_depth = 2

def evaluation_function(board):
    random.randint(1,5)

def maximize(depth, board, color):
    max_value = -1000000
    best_move = board
    op_color = 'w' if color is 'b' else 'b'
    if depth == max_depth:
        return evaluation_function(board)
    for move in successor(color, board):
        score = minimize(depth+1, move, op_color)
        if score > max_value:
            max_value = score
            best_move = move
    return (max_value, best_move)

def minimize(depth, board, color):
    min_value = 1000000
    best_move = board
    op_color = 'w' if color is 'b' else 'b'
    if depth == max_depth:
        return evaluation_function(board)
    for move in successor(color, board):
        score = maximize(depth+1, move, op_color)
        if score < min_value:
            max_value = score
            best_move = move
    return (max_value, best_move)


def successor(color, board):
    nextMoves = []
    friend = 'PNBRQK' if color == 'w' else 'pnbrqk'
    nextMoves += [moveBird(color,friend,j,i//8,i%8,board) for i,j in enumerate(list(board)) if j in friend and j not in ('P', 'p')]
    return [move for move in nextMoves if len(move) > 0]


def play(color,board,timeout):
    nextMoves = []
    if color == 'w':
        friend = 'PNBRQK'        
    else:
        friend = 'pnbrqk'
        board = "".join(reversed(board))      
    brd = arrangeBoard(list(board))
    nextMoves += [moveBird(color,friend,j,i//8,i%8,brd) for i,j in enumerate(list(board)) if j in friend and j not in ('P', 'p')]
    return [move for move in nextMoves if len(move) > 0]
    
    # for move in nextMoves:
    #  print(move)
    # print(len(nextMoves))
    #return board if color == 'w' else "".join(reversed(board)) 

