import sys
from betsyPlay import play


if __name__ == "__main__":
    
    ### Error handling of command line inputs ###
    if(len(sys.argv) != 4):
        raise(Exception("Error: Expected player(b/w), initial board and time out value. No Spaces in Arguments!"))

    if(sys.argv[1] not in ['b', 'w']):
        raise(Exception("Error: Player can be only black(b) or white(w)"))

    if(len(sys.argv[2]) != 64):
        raise(Exception("Error: Board should be exact 64 squares"))

    player = sys.argv[1]
    init_board = sys.argv[2]
    timeout = sys.argv[3]
    next_move = play(player,init_board,timeout)
    print(next_move)

    

    