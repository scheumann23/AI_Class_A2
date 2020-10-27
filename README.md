# Part 1: The Game of Sebastian

## Problem Formulation

The problem is split into three main parts, the first, second and third roll. The first roll refers to the point in the game in which the initial roll of all 5 dice has been done, and the player is working to decide which die/dice need to bee re-rolled. The second roll is after the selected die have been re-rolled and then the player has to again select which die/dice should be re-rolled. Lastly, the player must look at this third roll and determine which score their roll should be attributted to.

## How the Program Works

After 5 fair dice are rolled, their values are passed to the first roll function. Within this function, each possible re-roll scenario is evaluated. These scenerios are the different ways the dice can be selected to be re-rolled, and with 5 dice there are 32 ways that dice can be selected from re-roll. Then within each of these scenarios each of the selected die could take on 6 different values, each of these possible combinations are scored and then summed and divided by the total number of combinations. 

The scoring that is done, is not just simply checking to see which of the categories gives the highest score. To get the score of a possible outcome, the program uses the same logic that it uses later in the program to select the score for a certain roll. This is done to prevent scenarios where the program sees that a quintuplicatam has already been marked on the score card, but a possible outcome is a five of a kind. In this case the program will only consider open categories. After finding the combintation of rolls that gives the best possible expected value, the program returns the indices of the die/dice that should be re-rolled.

The second roll works just like the first roll. We brainstormed ideas on how to make these two different, and those will be discussed in the following section. Our ideas were not feasible within the time constraints. 

Moving on to the third roll, the program includes some logic in selecing a category to try to maximize the end score. 
