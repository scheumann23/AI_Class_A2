
import sys
import time
import numpy as np



# def get_col(board,col):
#     for val in board:
#         return [val[col] for val in board]



def getStraightMoves(friend,bird,row,col,board):
    moves = []
# Horizontal moves
    for x in range(col-1,-1,-1):
        board1 = np.copy(board)
        if board[row][x] in friend:
            break
        else:
            if board[row][x] == '.':
                board1[row][x] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[row][x] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break

    for x in range(col+1,8):
        board1 = np.copy(board)
        if board[row][x] in friend:
            break
        else:
            if board[row][x] == '.':
                board1[row][x] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[row][x] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break

# Vertical Moves
    for x in range(row-1,-1,-1):
        board1 = np.copy(board)
        if board[x][col] in friend:
            break
        else:
            if board[x][col] == '.':
                board1[x][col] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[x][col] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break

    for x in range(row+1,8):
        board1 = np.copy(board)
        if board[x][col] in friend:
            break
        else:
            if board[x][col] == '.':
                board1[x][col] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[x][col] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break
    return moves


def getDiagonalMoves(friend,bird,row,col,board):
    moves = []
# Left Upper Diagonal moves
    x = row - 1
    y = col - 1
    while x > -1 and y > -1:
        board1 = np.copy(board)
        if board[x][y] in friend:
            break
        else:
            if board[x][y] == '.':
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break
        x = x - 1
        y = y - 1


# Right Upper Diagonal moves
    x = row - 1
    y = col + 1
    while x > -1 and y < 8:
        board1 = np.copy(board)
        if board[x][y] in friend:
            break
        else:
            if board[x][y] == '.':
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break
        x = x - 1
        y = y + 1

# Left Lower Diagonal moves
    x = row + 1
    y = col - 1
    while x < 8 and y > -1:
        board1 = np.copy(board)
        if board[x][y] in friend:
            break
        else:
            if board[x][y] == '.':
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break
        x = x + 1
        y = y - 1


# Right Lower Diagonal moves
    x = row + 1
    y = col + 1
    while x < 8 and y < 8:
        board1 = np.copy(board)
        if board[x][y] in friend:
            break
        else:
            if board[x][y] == '.':
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
            else:
                board1[x][y] = bird
                board1[row][col] = '.'
                moves.append(board1)
                break
        x = x + 1
        y = y + 1

    return moves

def getKingfisherMoves(friend,bird,row,col,board):
    pos = []
    moves = []
    pos.append((row - 1,col))
    pos.append((row + 1,col))
    pos.append((row - 1,col - 1))
    pos.append((row - 1,col + 1))
    pos.append((row,col - 1))
    pos.append((row,col + 1))
    pos.append((row + 1,col - 1))
    pos.append((row + 1,col + 1))

    for p in pos:
        if p[0] >= 0 and p[0] <= 7 and p[1] >= 0 and p[1] <= 7:
            if board[p[0]][p[1]] not in friend:
                board1 = np.copy(board)
                board1[p[0]][p[1]] = bird
                board1[row][col] = '.'
                moves.append(board1)

    return moves

def getNightMove(friend,bird,row,col,board):
    pos = []
    moves = []
    pos.append((row - 1,col - 2))
    pos.append((row + 1,col - 2))
    pos.append((row - 1,col + 2))
    pos.append((row + 1,col + 2))
    pos.append((row - 2,col - 1))
    pos.append((row + 2,col - 1))
    pos.append((row - 2,col + 1))
    pos.append((row + 2,col + 1))

    for p in pos:
        if p[0] >= 0 and p[0] <= 7 and p[1] >= 0 and p[1] <= 7:
            if board[p[0]][p[1]] not in friend:
                board1 = np.copy(board)
                board1[p[0]][p[1]] = bird
                board1[row][col] = '.'
                moves.append(board1)

    return moves

def getParakeetMove(color,friend,bird,row,col,board):
    pos = []
    moves = []
    Quetzal = ['Q' if color == 'w' else 'q']
    if (row > 0 and row < 6):
        board1 = np.copy(board)
        if (board[row + 1][col - 1] not in friend and board[row + 1][col - 1] != '.'):
            board1[row + 1][col - 1] = bird
            board1[row][col] = '.'
            pos.append((row + 1, col - 1, board1))
        elif (board[row + 1][col + 1] not in friend and board[row + 1][col + 1] != '.'):
            board1[row + 1][col + 1] = bird
            board1[row][col] = '.'
            pos.append((row + 1, col + 1, board1))
        elif board[row + 1][col] == '.':
            board1[row + 1][col] = bird
            board1[row][col] = '.'
            pos.append((row + 1, col, board1))
    
    if row == 1:
        board1 = np.copy(board)
        if (board[row + 1][col] == '.' and board[row + 2][col] == '.'): 
            board1[row + 2][col] = bird
            board1[row][col] = '.'
            pos.append((row + 2, col, board1))

    if row == 6:
        board1 = np.copy(board)
        if (board[7][col - 1] not in friend and board[row + 1][col - 1] != '.'):
            board1[7][col - 1] = Quetzal 
            board1[row][col] = '.'
            pos.append((7, col - 1, board1))
        elif (board[7][col + 1] not in friend and board[row + 1][col + 1] != '.'):
            board1[7][col + 1] = Quetzal
            board1[row][col] = '.'
            pos.append((7, col + 1, board1))
        elif board[7][col] == '.':
            board1[7][col] = Quetzal
            board1[row][col] = '.'
            pos.append((7, col, board1))

    for p in pos:
        if p[0] >= 0 and p[0] <= 7 and p[1] >= 0 and p[1] <= 7:
            moves.append(p[2])
    return moves


def moveBird(color,friend,bird,row,col,board):
    if bird in ('rR'):
        return getStraightMoves(friend,bird,row,col,board)
    elif bird in ('bB'):
        return getDiagonalMoves(friend,bird,row,col,board)
    elif bird in ('qQ'):
        return getDiagonalMoves(friend,bird,row,col,board) + getStraightMoves(friend,bird,row,col,board)
    elif bird in ('kK'):
        return getKingfisherMoves(friend,bird,row,col,board)
    elif bird in ('nN'):
        return getNightMove(friend,bird,row,col,board)
    elif bird in ('pP'):
        return getParakeetMove(color,friend,bird,row,col,board)