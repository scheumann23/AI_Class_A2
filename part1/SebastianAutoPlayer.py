# Automatic Sebastian game player
# B551 Fall 2020
# PUT YOUR NAME AND USER ID HERE!
#
# Based on skeleton code by D. Crandall
#
#
# This is the file you should modify to create your new smart player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from SebastianState import Dice
from SebastianState import Scorecard
import random

class SebastianAutoPlayer:


    def __init__(self):
        self.numbers = { "primis" : 1, "secundus" : 2, "tertium" : 3, "quartus" : 4, "quintus" : 5, "sextus" : 6 }
        self.upper_cats = [ "primis", "secundus", "tertium", "quartus", "quintus", "sextus" ]
        self.lower_cats = [ "triplex", "quadrupla", "squadron", "prattle", "company", "quintuplicatam", "pandemonium" ]

    def combo(self, rolls): 
        return [(a1, a2, a3, a4, a5) for a1 in rolls[0] for a2 in rolls[1] for a3 in rolls[2] for a4 in rolls[3] \
                for a5 in rolls[4]]

    def roll_score(self, dice, category):
        counts = [dice.count(i) for i in range(1,7)]
        if category in self.numbers:
            score = counts[self.numbers[category]-1] * self.numbers[category]
        elif category == "company":
            score = 40 if sorted(dice) == [1,2,3,4,5] or sorted(dice) == [2,3,4,5,6] else 0
        elif category == "prattle":
            score = 30 if (len(set([1,2,3,4]) - set(dice)) == 0 or len(set([2,3,4,5]) - set(dice)) == 0 or len(set([3,4,5,6]) - set(dice)) == 0) else 0
        elif category == "squadron":
            score = 25 if (2 in counts) and (3 in counts) else 0
        elif category == "triplex":
            score = sum(dice) if max(counts) >= 3 else 0
        elif category == "quadrupla":
            score = sum(dice) if max(counts) >= 4 else 0
        elif category == "quintuplicatam":
            score = 50 if max(counts) == 5 else 0
        elif category == "pandemonium":
            score = sum(dice)
        return score

    def choose_score(self, dice, scorecard):
        available_upper_cats = [category for category in self.upper_cats if category not in scorecard]
        available_lower_cats = [category for category in self.lower_cats[:-1] if category not in scorecard]
        score_dict = dict([(category, self.roll_score(dice, category)) for category in available_upper_cats + available_lower_cats if category not in scorecard])
        if self.roll_score(dice, 'quintuplicatam')  == 50 and 'quintuplicatam' in available_lower_cats:
            return 50
        if self.roll_score(dice, 'squadron')  == 25 and 'squadron' in available_lower_cats:
            return 25
        for cat in available_upper_cats:
            if self.roll_score(dice, cat) >= self.numbers[cat] * 4:
                return self.roll_score(dice, cat)
            elif self.roll_score(dice, cat) >= self.numbers[cat] * 3:
                return self.roll_score(dice, cat)
        return max(score_dict.items(), key=lambda i: i[1])[1]
    
    def choose_category(self, dice, scorecard):
        available_upper_cats = [category for category in self.upper_cats if category not in scorecard]
        available_lower_cats = [category for category in self.lower_cats if category not in scorecard]
        score_dict = dict([(category, self.roll_score(dice, category)) for category in available_upper_cats+available_lower_cats if category not in scorecard])
        if self.roll_score(dice, 'quintuplicatam')  == 50 and 'quintuplicatam' in available_lower_cats:
            return 'quintuplicatam'
        if self.roll_score(dice, 'squadron')  == 25 and 'squadron' in available_lower_cats:
            return 'squadron'
        for cat in available_upper_cats:
            if self.roll_score(dice, cat) >= self.numbers[cat] * 4:
                return cat
            elif self.roll_score(dice, cat) >= self.numbers[cat] * 3:
                return cat
        return max(score_dict.items(), key=lambda i: i[1])[0]

    def expected_value(self, roll, reroll, scorecard):
        outcomes = self.combo([((roll[die],) if not reroll[die] else range(1, 7)) for die in range(0,5)])
        return sum([self.choose_score(outcome, scorecard) for outcome in outcomes]) / len(outcomes)
        
    def best_strat(self, roll, scorecard):
        best_roll = max([(reroll, self.expected_value(roll, reroll, scorecard)) for reroll in self.combo(((True, False),) * 5)], key = lambda item:item[1])
        return [i for i in range(0,5) if best_roll[0][i]]


    def first_roll(self, dice, scorecard):
        return self.best_strat(dice.dice, scorecard.scorecard)

    def second_roll(self, dice, scorecard):
        return self.best_strat(dice.dice, scorecard.scorecard)
    
    def third_roll(self, dice, scorecard):
        return self.choose_category(dice.dice, scorecard.scorecard)
