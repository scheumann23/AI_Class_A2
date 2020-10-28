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

wparakeet = [[  0,   0,   0,   0,   0,   0,   0,   0],
 [ 50,  50,  50,  50,  50,  50,  50,  50],
 [ 10,  10,  20,  30,  30,  20,  10,  10],
 [  5,   5,  10,  25,  25,  10,   5,   5],
 [  0,   0,   0,  20,  20,   0,   0,   0],
 [  5,  -5, -10,   0,   0, -10,  -5,   5],
 [  5,  10,  10, -20, -20,  10,  10,   5],
 [  0,   0,   0,   0,   0,   0,   0,   0]]

bparakeet = wparakeet[::-1]

wnighthawk = [[-50, -40, -30, -30, -30, -30, -40, -50],
 [-40, -20,   0,   0,   0,   0, -20, -40],
 [-30,   0,  10,  15,  15,  10,   0, -30],
 [-30,   5,  15,  20,  20,  15,   5, -30],
 [-30,   0,  15,  20,  20,  15,   0, -30],
 [-30,   5,  10,  15,  15,  10,   5, -30],
 [-40, -20,   0,   5,   5,   0, -20, -40],
 [-50, -40, -30, -30, -30, -30, -40, -50]]

bnighthawk = wnighthawk[::-1]

wbluejay = [[-20, -10, -10, -10, -10, -10, -10, -20],
 [-10,   0,   0,   0,   0,   0,   0, -10],
 [-10,   0,   5,  10,  10,   5,   0, -10],
 [-10,   5,   5,  10,  10,   5,   5, -10],
 [-10,   0,  10,  10,  10,  10,   0, -10],
 [-10,  10,  10,  10,  10,  10,  10, -10],
 [-10,   5,   0,   0,   0,   0,   5, -10],
 [-20, -10, -10, -10, -10, -10, -10, -20]]

bbluejay = wbluejay[::-1]

wrobin = [[ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 5, 10, 10, 10, 10, 10, 10,  5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [ 0,  0,  0,  5,  5,  0,  0,  0]]

brobin = wrobin[::-1]

wquetzal = [[-20, -10, -10,  -5,  -5, -10, -10, -20],
 [-10,   0,   0,   0,   0,   0,   0, -10],
 [-10,   0,   5,   5,   5,   5,   0, -10],
 [ -5,   0,   5,   5,   5,   5,   0,  -5],
 [  0,   0,   5,   5,   5,   5,   0,  -5],
 [-10,   5,   5,   5,   5,   5,   0, -10],
 [-10,   0,   5,   0,   0,   0,   0, -10],
 [-20, -10, -10,  -5,  -5, -10, -10, -20]]

bquetzal = wquetzal[::-1]

wkingfisher = [[-30, -40, -40, -50, -50, -40, -40, -30],
 [-30, -40, -40, -50, -50, -40, -40, -30],
 [-30, -40, -40, -50, -50, -40, -40, -30],
 [-30, -40, -40, -50, -50, -40, -40, -30],
 [-20, -30, -30, -40, -40, -30, -30, -20],
 [-10, -20, -20, -20, -20, -20, -20, -10],
 [ 20,  20,   0,   0,   0,   0,  20,  20],
 [ 20,  30,  10,   0,   0,  10,  30,  20]]

bkingfisher = wkingfisher[::-1]


def getVal(piece, row, col):
    if piece == 'p':
        return (bparakeet[row][col])
    elif piece == 'P':
        return (wparakeet[row][col])
    elif piece == 'n':
        return (bnighthawk[row][col])
    elif piece == 'N':
        return (wnighthawk[row][col])
    elif piece == 'B':
        return (wbluejay[row][col])
    elif piece == 'b':
        return (bbluejay[row][col])
    elif piece == 'R':
        return (wrobin[row][col])
    elif piece == 'r':
        return (brobin[row][col])
    elif piece == 'Q':
        return (wquetzal[row][col])
    elif piece == 'q':
        return (bquetzal[row][col])
    elif piece == 'K':
        return (wkingfisher[row][col])
    elif piece == 'k':
        return (bkingfisher[row][col])




def getPoint(piece):
    return points[piece]

def numEval(board, friend, foe):
    favor = 0
    against = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            if board[x][y] in friend:
                favor += 1
            elif board[x][y] in foe:
                against += 1
    return abs((favor - against))

def pieceEval(board, friend, foe):
    favor = 0
    against = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            if board[x][y] in friend:
                favor += getPoint(board[x][y])
            elif board[x][y] in foe:
                against += getPoint(board[x][y])
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

def posEval(board, friend, foe):
    favor = 0
    against = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            if board[x][y] in friend:
                favor += getVal(board[x][y], x, y)
            elif board[x][y] in foe:
                against += getVal(board[x][y], x, y)
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
    numPieces = numEval(board,friend,foe)
    positionalValue = posEval(board, friend, foe)

    return positionalValue + rowWeight + pieceWeight + numPieces

