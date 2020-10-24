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
    
    # Code taken from Sebastian.py
    def roll_score(self, dice, category):
        numbers = { "primis" : 1, "secundus" : 2, "tertium" : 3, "quartus" : 4, "quintus" : 5, "sextus" : 6 }
        counts = [dice.count(i) for i in range(1,7)]
        if category in numbers:
            score = counts[numbers[category]-1] * numbers[category]
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
        score_dict = dict([(category, self.roll_score(dice, category)) for category in self.open_cats])
        return max(score_dict.items(), key=lambda i: i[1])[0]
    
    # Un-used but would be good to use in expected values
    def store_open_cats(self, scorecard):
        self.open_cats = [cats for cats in self.all_cats if cats not in scorecard.scorecard.keys()]  
        return
    
    # Following function is modeled off of combos3() function from 
    # Module 10.6 in CSSI 551 Fall 2020
    def combo(self, rolls): 
        return [(a1, a2, a3, a4, a5) for a1 in rolls[0] for a2 in rolls[1] for a3 in rolls[2] for a4 in rolls[3] \
                for a5 in rolls[4]]
    
    # Following function is modeled off of expectation_of_reroll() function from 
    # Module 10.6 in CSSI 551 Fall 2020
    def expected_value(self, roll, reroll):
        outcomes = self.combo([((roll[die],) if not reroll[die] else range(1, 7)) for die in range(0,5)])
        return sum([self.roll_score(outcome, cat) for cat in self.open_cats for outcome in outcomes]) / len(outcomes)
    
    # Following function is modeled off of max_layer() function from 
    # Module 10.6 in CSSI 551 Fall 2020
    def best_strat(self, roll):
        best_roll = max([(reroll, self.expected_value(roll, reroll)) for reroll in self.combo(((True, False),) * 5)], key = lambda item:item[1])
        return [i for i in range(0,5) if best_roll[0][i]]
    
    def __init__(self):
        self.open_cats = []
        self.all_cats = ["primis", "secundus", "tertium", "quartus", "quintus", "sextus", "company", "prattle", \
                         "squadron", "triplex", "quadrupla", "quintuplicatam", "pandemonium"]
        pass  
    
    def first_roll(self, dice, scorecard):
        self.store_open_cats(scorecard)
        return self.best_strat(dice.dice) # always re-roll first die (blindly)
    
    def second_roll(self, dice, scorecard):
        self.store_open_cats(scorecard)
        return self.best_strat(dice.dice) # always re-roll second and third dice (blindly)
    
    def third_roll(self, dice, scorecard):
        return self.choose_score(dice.dice, scorecard)
