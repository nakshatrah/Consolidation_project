# Consolidation_project : Dice Game! 

Functionality & How to Run: 
1. Upon running the program, it will prompt you for player names. At this point, enter the names of the players playing the game, seperated by a commma. For this game, you can have more than 2 players! 
2. Once you enter the names, the game starts. It will first display the name of the first player followed by score, after which it will print the current score of the first player (which should be 0 at this point).
3. After that, it will present player 1's first roll. The three numbers rolled on each of the three die will be printed to the screen in parentheses. 
4. Next, it will ask you if you'd like to stop your turn and score the three numbers you have already rolled. To this, you must respond with a yes or no. 
5. If you choose to reroll (by entering in "no"), it will generate another random set of 3 numbers, and will ask you the same question again. However, if you answer "yes" to that question instead, it will print the player's name and the score they have received upon adding up the numbers they rolled. 
6. After this, it will move on to the next player, by printing their name to the terminal again, followed by their score. Then, it'll present the 3 numbers rolled by that player. 
7. At some point in this game, you may end up with "fixed dice". This happens when two of the three numbers you rolled are of the same value. If this happens, it will simply ask the question "Do you want to reroll the non-fixed dice? (yes/no):". Here, you can choose to reroll the number that is not fixed. If you choose not to, it will stop and add up your score. 
8. However, if you choose to reroll the non-fixed dice, you are taking a risk, as the reroll can result in the same value being rolled as the fixed dice, which will cause a case known as "tupling out". This means that all three numbers rolled have the same value. This will give you 0 points for THAT round, so you won't have any new points to add to your score. 
9. This process will continue, and at the turn of each player, it will print the player's name followed by their score at that point in the game. 
10. When the max score is reached (25), it will end the game, but before doing so, it will print the winning player's name followed by "wins!" on the terminal. 


Sample play: 

Enter player names separated by commas: player 1, player 2, player 3

player 1's score: 0 player 1 rolled: (3, 1, 6) Do you want to stop and score your current roll? (yes/no): yes 
player 1's score: 10

player 2's score: 0 
player 2 rolled: (4, 4, 2) Fixed dice: Number 4 was rolled twice. Do you want to reroll the non-fixed dice? (yes/no) yes 
player 2 rerolled: (4, 4, 1) Do you want to reroll the non-fixed dice? (yes/no) yes 
player 2 rerolled: (4, 4, 6) Do you want to reroll the non-fixed dice? (yes/no) no 
player 2's score: 14

player 3's score: 0 
player 3 rolled: (1, 6, 2) Do you want to stop and score your current roll? (yes/no): no 
player 3 rolled: (6, 5, 3) Do you want to stop and score your current roll? (yes/no): yes 
player 3's score: 14

player 1's score: 10 
player 1 rolled: (3, 4, 4) Fixed dice: Number 4 was rolled twice. Do you want to reroll the non-fixed dice? (yes/no) yes 
player 1 rerolled: (3, 4, 4) Do you want to reroll the non-fixed dice? (yes/no) yes 
player 1 rerolled: (4, 4, 4) Tupled out! Zero points for this turn. 
player 1's score: 10

player 2's score: 14 
player 2 rolled: (5, 4, 1) Do you want to stop and score your current roll? (yes/no): no 
player 2 rolled: (4, 4, 4) Tupled out! Zero points for this turn. 
player 2's score: 14

player 3's score: 14 
player 3 rolled: (1, 6, 5) Do you want to stop and score your current roll? (yes/no): no 
player 3 rolled: (2, 3, 5) Do you want to stop and score your current roll? (yes/no): no 
player 3 rolled: (1, 1, 4) Fixed dice: Number 1 was rolled twice. Do you want to reroll the non-fixed dice? (yes/no) yes 
player 3 rerolled: (1, 1, 4) Do you want to reroll the non-fixed dice? (yes/no) yes 
player 3 rerolled: (1, 1, 6) Do you want to reroll the non-fixed dice? (yes/no) no 
player 3's score: 22

player 1's score: 10 player 1 rolled: (4, 3, 2) Do you want to stop and score your current roll? (yes/no): no 
player 1 rolled: (3, 6, 2) Do you want to stop and score your current roll? (yes/no): yes 
player 1's score: 21

player 2's score: 14 
player 2 rolled: (5, 1, 6) Do you want to stop and score your current roll? (yes/no): yes 
player 2's score: 26 
player 2 wins!
