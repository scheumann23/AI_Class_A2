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

bparakeet = wparakeet[::-1]
bnighthawk = wnighthawk[::-1]
bbluejay = wbluejay[::-1]
brobin = wrobin[::-1]
bquetzal = wquetzal[::-1]
bkingfisher = wkingfisher[::-1]
#bparakeet = rotate_board(wparakeet)
#bnighthawk = rotate_board(wnighthawk)
#bbluejay = rotate_board(wbluejay)
#brobin = rotate_board(wrobin)
#bquetzal = rotate_board(wquetzal)
#bkingfisher = rotate_board(wkingfisher)

centking = [[0,0,0,0,0,0,0,0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  10,  20,  20,  10,  0],
 [ 0,  0,  10,  20,  20,  10,  0,  0],
 [ 0,  0,  10,  20,  20,  10,  0,  0],
 [ 0,  0,  10,  10,  10,  10,  10,  0],
 [ 0,  0,  10,  20,  20,  20,  10,  0],
 [ 0,  0,  10,  20,  30,  20,  10,  0]]

center = [[0,0,0,0,0,0,0,0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  100,  100,  100,  100,  0,  0],
 [ 0,  0,  100,  200,  200,  100,  0,  0],
 [ 0,  0,  100,  200,  200,  100,  0,  0],
 [ 0,  0,  100,  100,  100,  100,  0,  0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],]

endgame = [[0,0,0,0,0,0,0,0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  0,  0,  0,  0,  0,  0],
 [ 0,  0,  100,  100,  100,  100,  100,  0],
 [ 0,  0,  100,  200,  200,  200,  100,  0],
 [ 0,  0,  100,  200,  300,  200,  100,  0]]


def getVal(piece, row, col):
    if piece == 'P':
        return (wparakeet[row][col]) + 100
    elif piece == 'p':
        return (bparakeet[row][col]) - 100
    elif piece == 'N':
        return (wnighthawk[row][col]) + 320
    elif piece == 'n':
        return (bnighthawk[row][col]) - 320
    elif piece == 'B':
        return (wbluejay[row][col]) + 330
    elif piece == 'b':
        return (bbluejay[row][col]) - 330
    elif piece == 'R':
        return (wrobin[row][col]) + 500
    elif piece == 'r':
        return (brobin[row][col]) - 500
    elif piece == 'Q':
        return (wquetzal[row][col]) + 900
    elif piece == 'q':
        return (bquetzal[row][col]) - 900
    elif piece == 'K':
        return (wkingfisher[row][col]) + 20000
    elif piece == 'k':
        return (bkingfisher[row][col]) - 20000
    else:
        return 0

def getPoint(piece):
    return points[piece]

# Returns the difference of number of pieces
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

# Returns the value based on the piece values assigned
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

# Returns the evaluation based on what row the piece is in
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

# combination of numEval and pieceEval function
def posEval(board,color, friend, foe):
    boardVal = 0
    for x in range(0,8):
        for y in range(0,8):
            boardVal += getVal(board[x][y], x, y)
    # For minimizing player return the -ve of the absolute value
    return boardVal if color=='w' else  -1*boardVal

# Attack on King weights
def endEval(board,color,friend):
    boardVal = 0
    for x in range(5,8):
        for y in range(2,7):
            boardVal += endgame[x][y] if board[x][y] in friend else 0
    # For minimizing player return the -ve of the absolute value
    return boardVal if color=='w' else  -1*boardVal


# Heuristic to determine the hold on central locations and attack on king
def endCenter(board,color,friend,foe):
    boardVal = 0
    for x in range(3,8):
        for y in range(2,7):
            #boardVal += center[x][y] if board[x][y] in friend else -1*center[x][y] if board[x][y] in foe else 0
            boardVal += centking[x][y] if board[x][y] in friend else -1*centking[x][y] if board[x][y] in foe else 0
    # For minimizing player return the -ve of the absolute value
    return boardVal if color=='w' else  -1*boardVal


def evalBoard(color,board):
    if color == 'w':
        friend = 'PNBRQK'
        foe = 'pnbrqk'
    else:
        friend = 'pnbrqk'
        foe = 'PNBRQK'

    #rowWeight = rowEval(board, friend, foe)
    #pieceWeight = pieceEval(board,friend,foe)
    #numPieces = numEval(board,friend,foe)
    #positionalValue = posEval(board, friend, foe)

    # Call the position evaluation function that returns both piece val and piece position val
    #return (kingval + posEval(board,color, friend, foe) + holdCenter(board,color,friend,foe) + endEval(board,color, friend), board)
    #return (kingval + posEval(board,color, friend, foe) + holdCenter(board,color,friend,foe), board)
    return (posEval(board,color, friend, foe) + endCenter(board,color,friend,foe), board)
