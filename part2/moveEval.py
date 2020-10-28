import sys
import time
import re
import numpy as np

#
# The points and board weights have been taken 
# from https://www.chessprogramming.org/Simplified_Evaluation_Function
#
#points = [100,320,330,500,900,20000]

points = {'p': 100,'n': 320,'b': 330,'r': 500,'q': 900,'k': 20000, 'P': 100,'N': 320,'B': 330,'R': 500,'Q': 900,'K': 20000}

def getVal(piece):
    return points[piece]


def pieceEval(board, friend, foe):
    favor = 0
    against = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            if board[x][y] in friend:
                favor += getVal(board[x][y])
            elif board[x][y] in foe:
                against += getVal(board[x][y])
    return abs((favor - against))

def rowEval(board, friend, foe):
    favor = 0
    against = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            if board[x][y] in friend:
                favor += x
            elif board[x][y] in foe:
                against += 7-x
    return abs((favor - against))


def evalBoard(color,board):
    if color == 'w':
        friend = 'PNBRQK'
        foe = 'pnbrqk'
    else:
        friend = 'pnbrqk'
        foe = 'PNBRQK'
    rowWeight = rowEval(board, friend, foe)
    pieceWeight = pieceEval(board,friend,foe)
    return rowWeight + pieceWeight

