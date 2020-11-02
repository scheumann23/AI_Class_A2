# Automatic Sebastian game player
# B551 Fall 2020
# Cody Harris - Neelan Scheumann - Vishal Bhalla
#
# Based on skeleton code by D. Crandall
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
        # initialize with some basic lists/dictionaries that will be used when picking a category
        self.numbers = { "primis" : 1, "secundus" : 2, "tertium" : 3, "quartus" : 4, "quintus" : 5, "sextus" : 6 }
        self.upper_cats = [ "primis", "secundus", "tertium", "quartus", "quintus", "sextus" ]
        self.lower_cats = [ "triplex", "quadrupla", "squadron", "prattle", "company", "quintuplicatam", "pandemonium" ]
    
    # Idea derived from combos3() function in program examined in 
    # Module 10.6 of CSCI 551 - Fall 2020
    def combo(self, rolls): 
        return [(a1, a2, a3, a4, a5) for a1 in rolls[0] for a2 in rolls[1] for a3 in rolls[2] for a4 in rolls[3] \
                for a5 in rolls[4]]
    
    # Function built using code from SebastionState.py 
    # This is used to determine the correct score for a given set of dice and a particular category
    def roll_score(self, dice, category, bonus):
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
    

    # Since for a given roll, there is often not one particular score (unlike the simplified version we did earlier)
    # it is necessary to pick a score to return for a given set of dice to be used in the expected_value function
    def choose_score(self, dice, scorecard, bonus):
        # determine which categories are still available to choose when assigning the third roll
        available_upper_cats = [category for category in self.upper_cats if category not in scorecard]
        available_lower_cats = [category for category in self.lower_cats[:-1] if category not in scorecard]
        # for each category calculate what the score would be for that turn if the category was chosen 
        score_dict = dict([(category, self.roll_score(dice, category, bonus)) for category in available_upper_cats+available_lower_cats if category not in scorecard])
        # split the score_dict into the upper section categories and the lower section categories
        upper_score_dict = dict([(category, score_dict[category]) for category in available_upper_cats])
        lower_score_dict = dict([(category, score_dict[category]) for category in available_lower_cats])
        # split out all of the upper section categories into the ones that are non-zero
        non_zero_uppers = dict(filter(lambda elem: elem[1] > 0, upper_score_dict.items()))
        # if quintuplicatam ever comes up always choose that
        if 'quintuplicatam' in available_lower_cats and lower_score_dict['quintuplicatam'] == 50:
            return 50
        # if squandron ever comes up always choose that
        if 'squadron' in available_lower_cats and lower_score_dict['squadron'] == 25:
            return 25
        # now search through the upper categories to see if there are any 3 or 4 of a kind to add
        # we want to prioritize the upper categories to try to get the 35 point bonus
        for cat in available_upper_cats:
            if upper_score_dict[cat] >= self.numbers[cat] * 3:
                return upper_score_dict[cat]
        # first check if there is an available category in the lower section that would return a non-zero score
        # if there isn't then look to the top section and try to minimize the available non-zero scores
        # the intent here is to keep trying to get at least 3 of a kind for each number in the top section 
        # in order to get the bonus
        # if that doesn't pan out then just return the category with the greatest score
        if len(lower_score_dict) > 0:
            if max(lower_score_dict.items(), key=lambda i: i[1])[1] == 0:
                if len(non_zero_uppers) > 0:
                    return min(non_zero_uppers.items(), key=lambda i: i[1])[1]
                else:
                    return max(score_dict.items(), key=lambda i: i[1])[1]   
            else:
                return max(score_dict.items(), key=lambda i: i[1])[1]
        else:
            return max(score_dict.items(), key=lambda i: i[1])[1]

    
    # this is identical mutatis mutandis to the choose_score, but returns the category instead of the score
    # this is used after roll three whereas choose_score is used after rolls one and two
    def choose_category(self, dice, scorecard, bonus):
        available_upper_cats = [category for category in self.upper_cats if category not in scorecard]
        available_lower_cats = [category for category in self.lower_cats if category not in scorecard]
        score_dict = dict([(category, self.roll_score(dice, category, bonus)) for category in available_upper_cats+available_lower_cats if category not in scorecard])
        upper_score_dict = dict([(category, score_dict[category]) for category in available_upper_cats])
        lower_score_dict = dict([(category, score_dict[category]) for category in available_lower_cats])
        non_zero_uppers = dict(filter(lambda elem: elem[1] > 0, upper_score_dict.items()))
        if 'quintuplicatam' in available_lower_cats and lower_score_dict['quintuplicatam'] == 50:
            return 'quintuplicatam'
        if 'squadron' in available_lower_cats and lower_score_dict['squadron'] == 25:
            return 'squadron'
        for cat in available_upper_cats:
            if upper_score_dict[cat] >= self.numbers[cat] * 3:
                return cat
        if len(lower_score_dict) > 0:
            if max(lower_score_dict.items(), key=lambda i: i[1])[1] == 0:
                if len(non_zero_uppers) > 0:
                    return min(non_zero_uppers.items(), key=lambda i: i[1])[0]
                else:
                    return max(score_dict.items(), key=lambda i: i[1])[0]
            else:
                return max(score_dict.items(), key=lambda i: i[1])[0]
        else:
            return max(score_dict.items(), key=lambda i: i[1])[0]


    # Idea derived from expectation_of_reroll() function in program examined in 
    # Module 10.6 of CSCI 551 - Fall 2020
    def expected_value(self, roll, reroll, scorecard, bonus):
        outcomes = self.combo([((roll[die],) if not reroll[die] else range(1, 7)) for die in range(0,5)])
        return sum([self.choose_score(outcome, scorecard, bonus) for outcome in outcomes]) / len(outcomes)
        
    # Idea derived from max_layer() function in program examined in 
    # Module 10.6 of CSCI 551 - Fall 2020
    def best_strat(self, roll, scorecard, bonus):
        best_roll = max([(reroll, self.expected_value(roll, reroll, scorecard, bonus)) for reroll in self.combo(((True, False),) * 5)], key = lambda item:item[1])
        return [i for i in range(0,5) if best_roll[0][i]]

    def first_roll(self, dice, scorecard):
        return self.best_strat(dice.dice, scorecard.scorecard, scorecard.bonusflag)

    def second_roll(self, dice, scorecard):
        return self.best_strat(dice.dice, scorecard.scorecard, scorecard.bonusflag)
    
    def third_roll(self, dice, scorecard):
        return self.choose_category(dice.dice, scorecard.scorecard, scorecard.bonusflag)
