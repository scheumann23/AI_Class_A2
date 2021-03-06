# Part 1: The Game of Sebastian

## Problem Formulation

The problem is split into three main parts, the first, second and third roll. The first roll refers to the point in the game in which the initial roll of all 5 dice has been done, and the player is working to decide which die/dice need to bee re-rolled. The second roll is after the selected die have been re-rolled and then the player has to again select which die/dice should be re-rolled. Lastly, the player must look at this third roll and determine which score their roll should be attributted to.

## How the Program Works

After 5 fair dice are rolled, their values are passed to the first roll function. Within this function, each possible re-roll scenario is evaluated. These scenerios are the different ways the dice can be selected to be re-rolled, and with 5 dice there are 32 ways that dice can be selected from re-roll. Then within each of these scenarios each of the selected die could take on 6 different values, each of these possible combinations are scored and then summed and divided by the total number of combinations. 

The scoring that is done, is not just simply checking to see which of the categories gives the highest score. To get the score of a possible outcome, the program uses the same logic that it uses later in the program to select the score for a certain roll. This is done to prevent scenarios where the program sees that a quintuplicatam has already been marked on the score card, but a possible outcome is a five of a kind. In this case the program will only consider open categories. After finding the combintation of rolls that gives the best possible expected value, the program returns the indices of the die/dice that should be re-rolled.

The second roll works just like the first roll. We brainstormed ideas on how to make these two different, and those will be discussed in the following section. Our ideas were not feasible within the time constraints. 

Moving on to the third roll, the program includes some logic in selecing a category to try to maximize the end score. To begin, the program builds lists of the avaliable upper and lower categories, as well as a dictionary that contains the score that the roll would get in each category. 

Logically we wanted to make sure that if we rolled a quintuplicatam, that the program would select it. While this would always be the case if we choose the highest possible score, we wanted to include logic to try to fill the top of the scorecard with high scores to try to get the bonus. This is also done with the squadron, if the roll is a squadron and that is an avaliable category, then it is selected for the roll. This logic is all necessary due to the next logic, without it, our next logic could mark a roll of five 1's as a primis instead of a quintuplicatam, which would be bad because getting a quintuplicatam or squadron is harder than acceptable rolls in the upper score card categories.

To get the bonus, we need the primis to sextus categories to average three or more of each specific number. This means that we want to force the program to choose one of these categories, even if the score is lower in these categories. For example, we would rather put the roll of [1,1,1,1,6] as a primis instead of a quadrupla, even though the quadrupla would result in a higher score, because if we do this for all six categories we will get the bonus 35. 

Lastly, if none of the above logic is satisfied, then the category with the highest score is chosen.

## Problems, Assumptions, Simplifications, and Design Choices

The main assumption we make that simplifies this program is that on the first roll, we do not do anything different than we will subsequently do in the second roll. We discussed that possibly the program should consider that it is the first roll and then know that it should not only enumerate all possible scenarios to select, but also look at all the possible scenarios that come from that first roll. The problem was, that when looking two moves ahead the program was much too slow to be viable because of the vast amount of possibilites that occur from looking two rolls ahead.


# Part 2: Betsy

## Problem Formulation

The game of Betsy is a simplified version of chess where the chess pieces are replaced by various Bird species and complicated moves like Castling are not allowed. The input board to the program will be provided, along with the color of the player the program represents and the time limit within which the move should be completed

## How the Program Works

There are three parts of the program based on the kind of work they perform, one is the driver, which accepts the input, performs minimax with alpha beta pruning and prints the output. The 2nd part of the program is the one which identifies the moves that the pieces can make. These form the successor for any given move under consideration. The third and the final part is the one that evaluates the board based on the evaluation algorithm built into the program.

The program first generates the tree up to the max depth level specified and then calls the evaluation function to get the evaluation of the leaf nodes and based on the same identifies the best move by quickly pruning the tree and traversing over it and returning the best move.

For our evaluation function we have tried multiple algorithms, based on the number of pieces on the board, number of rows moved, piece weights, position weights(this we got from https://www.chessprogramming.org/Simplified_Evaluation_Function) and we also tried to load the weightage heavily when the move would mean a loss of king. 

## Problems, Assumptions, Simplifications, and Design Choices
Due to the huge branching factor involved we are facing issues going beyond the depth of level 4 and most of the times are restricted to 3 levels. We are looking at making that working better. Further we are currently using an evaluation function in which we have merged both piece and position weights in one function, we need to see if it can further be improved. The other majir issue we see is that our AI seems to shy away from attacking the other AI, we need to work on the same.