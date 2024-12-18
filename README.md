# Consolidation_project : Dice Game! 
Functionality & How to Run: 

1. Upon running the program, it will prompt you for player names. At this point, enter the names of the players playing the game, seperated by a commma. For this game, you can have more than 2 players! After this, it will display the message "Starting the game...". This signifies that a round has started. 
2. The game will first display the name of the first player followed by score, after which it will print the current score of the first player (which should be 0 at this point).
3. After that, it will present player 1's first roll. The three numbers rolled on each of the three die will be printed to the screen in parentheses. After the numbers are printed, the game will print how long it took to role the dice. 
4. Next, it will either print the fixed dice (whichever number was drawn twice in one roll) and ask you if you want to reroll the non-fixed dice, or will ask you if you'd like to stop your turn and score the three numbers you have already rolled. To both questions, you must respond with a yes or no. 
5. For the fixed dice scenario, based on your response, it will either generate a new roll or will tally up your current score and print it to the screen. For the scenario where it asks if you'd like to stop and score, there are the following outputs: if you chose to reroll (by entering in "no"), it will generate another random set of 3 numbers, and will ask you the same question again. However, if you answer "yes" to that question instead, it will print the player's name and the score they have received upon adding up the numbers they rolled. 
6. After this, it will move on to the next player, by printing their name to the terminal again, followed by their score. Then, it'll present the time it took to roll the dice and the 3 numbers rolled by that player. 
7. At some point in this game, you may end up with "fixed dice". This happens when two of the three numbers you rolled are of the same value. If this happens, it will simply ask the question "Do you want to reroll the non-fixed dice? (yes/no):". The way you respond will change the output, as described in the two scenarios above. 
8. Remember that if you choose to reroll the non-fixed dice, you are taking a risk, as the reroll can result in the same value being rolled as the fixed dice, which will cause a case known as "tupling out". This means that all three numbers rolled have the same value. This will give you 0 points for that SPECIFIC roll, so you won't have any new points to add to your score. 
9. This process will continue, and at the turn of each player, it will print the player's name followed by their score at that point in the game. 
10. When the max score is reached (25), it will end the game, but before doing so, it will print the winning player's name followed by "wins!" on the terminal. After that, it will print "Round ended at" followed by the date in Y-M-D format, along with the time in H-M-S format. This can help the user keep track of each round and their timings. 

Sample play: 

Enter player names separated by commas:1, 2, 3 

Starting the game...

1's turn (Current score: 0)
1 rolled: (2, 2, 6)
The dice roll took  0.0000 seconds.
Fixed dice: Number 2 was rolled twice.
Do you want to reroll the non-fixed dice? (yes/no)no
1's new score: 10

 2's turn (Current score: 0)
 2 rolled: (3, 4, 4)
The dice roll took  0.0000 seconds.
Fixed dice: Number 4 was rolled twice.
Do you want to reroll the non-fixed dice? (yes/no)yes
 2 rerolled: (4, 4, 4)
Tupled out! Zero points for this turn.
 2's new score: 0

 3 's turn (Current score: 0)
 3  rolled: (4, 1, 4)
The dice roll took  0.0000 seconds.
Fixed dice: Number 4 was rolled twice.
Do you want to reroll the non-fixed dice? (yes/no)no
 3 's new score: 9

1's turn (Current score: 10)
1 rolled: (3, 3, 4)
The dice roll took  0.0000 seconds.
Fixed dice: Number 3 was rolled twice.
Do you want to reroll the non-fixed dice? (yes/no)no
1's new score: 20

 2's turn (Current score: 0)
 2 rolled: (6, 6, 6)
The dice roll took  0.0000 seconds.
Tupled out! Zero points for this turn.
 2's new score: 0

 3 's turn (Current score: 9)
 3  rolled: (4, 4, 2)
The dice roll took  0.0000 seconds.
Fixed dice: Number 4 was rolled twice.
Do you want to reroll the non-fixed dice? (yes/no)yes
 3  rerolled: (4, 4, 1)
Do you want to reroll the non-fixed dice? (yes/no)yes
 3  rerolled: (4, 4, 2)
Do you want to reroll the non-fixed dice? (yes/no)yes
 3  rerolled: (4, 4, 5)
Do you want to reroll the non-fixed dice? (yes/no)no
 3 's new score: 22

1's turn (Current score: 20)
1 rolled: (6, 3, 6)
The dice roll took  0.0000 seconds.
Fixed dice: Number 6 was rolled twice.
Do you want to reroll the non-fixed dice? (yes/no)no
1's new score: 35
1 wins!

Round ended at 2024-12-17 20:44:21.