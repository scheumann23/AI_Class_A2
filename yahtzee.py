import numpy as np

def score(d1, d2, d3):
    if d1 == d2 and d2 == d3:
        return 25
    else:
        return d1 + d2 + d3

def yahtzee_pick(d1, d2, d3):
    dice = [d1, d2, d3]
    if len(set(dice))== 1:
        return "Don't roll any of the dice."
    #hold none i.e. reroll all
    hold_none_best_value = 10.5
    #hold one die
    total = 0
    hold_one= np.array([])
    for die in dice:
        for i in range(1,7):
            for j in range(1,7):
                total += score(die, i, j)
        roll_score = total / 36
        hold_one = np.append(hold_one, roll_score)
        total = 0
    hold_one_best = np.argmax(hold_one)
    hold_one_best_value = max(hold_one)
    #hold two die
    picks = [(d1, d2), (d1, d3), (d2, d3)]
    hold_two = np.array([])
    for pick in picks:
        die1, die2 = pick
        for i in range(1,7):
            total += score(die1, die2, i)
        roll_score = total / 6
        hold_two = np.append(hold_two, roll_score)
        total = 0
    hold_two_best = np.argmax(hold_two)
    hold_two_best_value = max(hold_two)
    #hold three
    hold_three_best_value = score(d1, d2, d3)
    choice = np.argmax([hold_none_best_value, hold_one_best_value, hold_two_best_value, hold_three_best_value])
    if choice == 0:
        return "Roll all three"
    elif choice == 1:
        pick = hold_one_best + 1
        return f"Keep die {pick} and reroll the others." 
    elif choice ==2:
        if hold_two_best == 0:
            return "Keep die 1 and die 2 and reroll die 3."
        elif hold_two_best == 1:
            return "Keep die 1 and die 3 and reroll die 2."
        else:
            return "Keep die 2 and die 3 and reroll die 1."
    else:
        return "Don't roll any of the dice."