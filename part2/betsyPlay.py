import sys
import time
import re
import numpy as np
from moveBetsy import moveBird

#
# The points weightage has been taken from https://www.chessprogramming.org/Simplified_Evaluation_Function
#
points = [100,320,330,500,900,20000]
p,n,b,r,q,k = points
P,N,B,R,Q,K = points
maxPlayer = False


def validBoard(board):
    return False if re.search('[^pnbrqkPNBRQK.]', board) else True


def arrangeBoard(board):
    brd = np.reshape(board,(8,8))
    return brd

def play(color,board,timeout):
    nextMoves = []
    if color == 'w':
        maxPlayer = True
        friend = 'PNBRQK'        
    else:
        maxPlayer = False
        friend = 'pnbrqk'
        board = "".join(reversed(board))      
    brd = arrangeBoard(list(board))
    nextMoves += [moveBird(color,friend,j,i//8,i%8,brd) for i,j in enumerate(list(board)) if j in friend]
    
    # for move in nextMoves:
    #  print(move)
    # print(len(nextMoves))
    return board if color == 'w' else "".join(reversed(board)) 

