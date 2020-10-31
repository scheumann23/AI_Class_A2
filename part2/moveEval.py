import sys
import time
import numpy as np


#
# The points and board weights have been taken 
# from https://www.chessprogramming.org/Simplified_Evaluation_Function
#
#points = [100,320,330,500,900,20000]

def rotate_board(board):
    brd = board.copy()
    for i in range(len(board)):
        for j in range(len(board[0])):
            brd[i][len(board[0])-1-j] = board[len(board)-1-i][j]
    return brd

points = {'p': 100,'n': 320,'b': 330,'r': 500,'q': 900,'k': 20000, 'P': 100,'N': 320,'B': 330,'R': 500,'Q': 900,'K': 20000}

wparakeet = [[  0,   0,   0,   0,   0,   0,   0,   0],
 [ 50,  50,  50,  50,  50,  50,  50,  50],
 [ 10,  10,  20,  30,  30,  20,  10,  10],
 [  5,   5,  10,  25,  25,  10,   5,   5],
 [  0,   0,   0,  20,  20,   0,   0,   0],
 [  5,  -5, -10,   0,   0, -10,  -5,   5],
 [  5,  10,  10, -20, -20,  10,  10,   5],
 [  0,   0,   0,   0,   0,   0,   0,   0]]

wnighthawk = [[-50, -40, -30, -30, -30, -30, -40, -50],
 [-40, -20,   0,   0,   0,   0, -20, -40],
 [-30,   0,  10,  15,  15,  10,   0, -30],
 [-30,   5,  15,  20,  20,  15,   5, -30],
 [-30,   0,  15,  20,  20,  15,   0, -30],
 [-30,   5,  10,  15,  15,  10,   5, -30],
 [-40, -20,   0,   5,   5,   0, -20, -40],
 [-50, -40, -30, -30, -30, -30, -40, -50]]

wbluejay = [[-20, -10, -10, -10, -10, -10, -10, -20],
 [-10,   0,   0,   0,   0,   0,   0, -10],
 [-10,   0,   5,  10,  10,   5,   0, -10],
 [-10,   5,   5,  10,  10,   5,   5, -10],
 [-10,   0,  10,  10,  10,  10,   0, -10],
 [-10,  10,  10,  10,  10,  10,  10, -10],
 [-10,   5,   0,   0,   0,   0,   5, -10],
 [-20, -10, -10, -10, -10, -10, -10, -20]]

wrobin = [[ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 5, 10, 10, 10, 10, 10, 10,  5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [-5,  0,  0,  0,  0,  0,  0, -5],
 [ 0,  0,  0,  5,  5,  0,  0,  0]]

wquetzal = [[-20, -10, -10,  -5,  -5, -10, -10, -20],
 [-10,   0,   0,   0,   0,   0,   0, -10],
 [-10,   0,   5,   5,   5,   5,   0, -10],
 [ -5,   0,   5,   5,   5,   5,   0,  -5],
 [  0,   0,   5,   5,   5,   5,   0,  -5],
 [-10,   5,   5,   5,   5,   5,   0, -10],
 [-10,   0,   5,   0,   0,   0,   0, -10],
 [-20, -10, -10,  -5,  -5, -10, -10, -20]]

wkingfisher = [[-30, -40, -40, -50, -50, -40, -40, -30],
 [-30, -40, -40, -50, -50, -40, -40, -30],
 [-30, -40, -40, -50, -50, -40, -40, -30],
 [-30, -40, -40, -50, -50, -40, -40, -30],
 [-20, -30, -30, -40, -40, -30, -30, -20],
 [-10, -20, -20, -20, -20, -20, -20, -10],
 [ 20,  20,   0,   0,   0,   0,  20,  20],
 [ 20,  30,  10,   0,   0,  10,  30,  20]]


# Reversing the points board for Black Pieces

#bparakeet = wparakeet[::-1]
bparakeet = rotate_board(wparakeet)
#bnighthawk = wnighthawk[::-1]
bnighthawk = rotate_board(wnighthawk)
#bbluejay = wbluejay[::-1]
bbluejay = rotate_board(wbluejay)
#brobin = wrobin[::-1]
brobin = rotate_board(wrobin)
#bquetzal = wquetzal[::-1]
bquetzal = rotate_board(wquetzal)
#bkingfisher = wkingfisher[::-1]
bkingfisher = rotate_board(wkingfisher)

def getVal(piece, clr, row, col):
    if piece == 'p':
        return (bparakeet[row][col]) + 100*clr
    elif piece == 'P':
        return (wparakeet[row][col]) + 100*clr
    elif piece == 'n':
        return (bnighthawk[row][col]) + 320*clr
    elif piece == 'N':
        return (wnighthawk[row][col]) + 320*clr
    elif piece == 'B':
        return (wbluejay[row][col]) + 330*clr
    elif piece == 'b':
        return (bbluejay[row][col]) + 330*clr
    elif piece == 'R':
        return (wrobin[row][col]) + 500*clr
    elif piece == 'r':
        return (brobin[row][col]) + 500*clr
    elif piece == 'Q':
        return (wquetzal[row][col]) + 900*clr
    elif piece == 'q':
        return (bquetzal[row][col]) + 900*clr
    elif piece == 'K':
        return (wkingfisher[row][col]) + 20000*clr
    elif piece == 'k':
        return (bkingfisher[row][col]) + 20000*clr
    else:
        return 0



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
    return (favor - against)

def pieceEval(board, friend, foe):
    favor = 0
    against = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            if board[x][y] in friend:
                favor += getPoint(board[x][y])
            elif board[x][y] in foe:
                against += getPoint(board[x][y])
    return (favor - against)

def rowEval(board, friend, foe):
    favor = 0
    against = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            if board[x][y] in friend:
                favor += x
            elif board[x][y] in foe:
                against += 7-x
    return (favor - against)

def posEval(board, color):
    clr = 1 if color == 'w' else -1
    total = 0
    for x in range(0,board.shape[1]):
        for y in range(0,board.shape[0]):
            total += getVal(board[x][y],clr, x, y)
    return total

def evalBoard(color,board):
    '''
    if color == 'w':
        friend = 'PNBRQK'
        foe = 'pnbrqk'
        kingval = 1000000 if 'k' not in board else -1000000 if 'K' not in board else 0
    else:
        friend = 'pnbrqk'
        foe = 'PNBRQK'
        kingval = -1000000 if 'k' not in board else 1000000 if 'K' not in board else 0
    '''

    #rowWeight = rowEval(board, friend, foe)
    #pieceWeight = pieceEval(board,friend,foe)
    #numPieces = numEval(board,friend,foe)
    #positionalValue = posEval(board, friend, foe)

    return (posEval(board, color) , board)
    #return (numPieces + pieceWeight, board)

