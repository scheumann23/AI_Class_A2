#finds best move for a yahtzee roll

def exp_value(roll, reroll):
    if len(reroll) == 0:
        return get_score(roll)
    elif len(reroll) == 1:
        total_pos = []
        for i in range(1,7):
            test = roll.copy()
            test[reroll[0]] = i
            total_pos.append(get_score(test) * (1/6))
        return sum(total_pos)
    elif len(reroll) == 2:
        total_pos = []
        for j in range(1, 7):
            for k in range(1, 7):
                test = roll.copy()
                test[reroll[0]] = j
                test[reroll[1]] = k
                total_pos.append(get_score(test) * (1/36))
        return sum(total_pos)
    elif len(reroll) == 3:
        #precomputed value
        return 10.902777777777779
    
            

#get score of roll
def get_score(roll):
    if len(set(roll)) == 1:
        return 25
    else:
        return sum(roll)

if __name__ == '__main__' :
    try:
        initial_roll = list(map(int, input('Please input three numbers seperated by spaces, that represent your roll: ').split()))
    except:
        raise(Exception("Input should be three numbers seperated by spaces, i.e. \'2 3 4\'"))

    roll_poss = [[], [0], [1], [2], [0,1], [0,2], [1,2], [0,1,2]]
    max_ex_value = 0
    best_move = []
    for pos in roll_poss:
        curr_value = exp_value(initial_roll, pos)
        if curr_value > max_ex_value:
            max_ex_value = curr_value
            best_move = pos
    print("Current score is", str(get_score(initial_roll)))
    if len(best_move) == 0:
        print("Your best move is to not change anything!", end ='')
    elif len(best_move) == 1:
        print("Your best move is to reroll die number: ", best_move[0] + 1)
        print("This gives you an expected value of", round(max_ex_value, 2), end ='')
    elif len(best_move) == 2:
        print("Your best move is to reroll die number", best_move[0] + 1, "and", best_move[1] + 1)
        print("This gives you an expected value of", round(max_ex_value, 2), end ='')
    elif len(best_move) == 3:
        print("The best move is to reroll all dice")
        print("This gives you an expected value of around 10.9", end ='')
