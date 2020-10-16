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
            pass  

      def first_roll(self, dice, scorecard):
            return [0] # always re-roll first die (blindly)

      def second_roll(self, dice, scorecard):
            return [1, 2] # always re-roll second and third dice (blindly)
      
      def third_roll(self, dice, scorecard):
            # stupidly just randomly choose a category to put this in
            return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )

