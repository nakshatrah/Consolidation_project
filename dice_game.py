import random 
import pandas as pd 
import time 

def initialize_game():
    """I wrote the code below to be the setup for the game, which will define the target score to win (25) and ask players to enter their names, which can be a fun way to personalize the game for each round if a bigger group of players wants to take turns."""
    target_score = 25
    players = input("Enter player names separated by commas:").split(',')
    players = [player.strip().replace(" ", "") for player in players]
    scores = {player: 0 for  player in players}
    """Edit: Now using the pandas library, the players' names will be stored in a DataFrame so that player names will be """
    scores_df = pd.DataFrame(list(scores.items()), columns = ['Player','Score'])
    return target_score, scores_df
    # test: 
    # test input: "John, Jane, Adam" 
    # output expected: target_score = 25, scores_df w/ columns for Player and Score
    # target_score, scores_df = initialize_game()
    # print(f"Target Score: {target_score}")
    # print(scores_df)

def roll_dice():
    """This function will roll three dice and will return each value rolled in a list."""
    return tuple(random.randint(1, 6) for _ in range(3)) #changed to tuple to create unchangeable dice values unless player demands a reroll of what they generated
    # test: 
    # output expected: 1 tuple with 3 integers, between 1 and 6
    # dice = roll_dice()
    # print(f"Rolled dice: {dice}")

def play_turn(player):
    """This function controls the scores by rolling the dice and adding up the score value. It also controls what counts as "tupling out" and printing the results to the terminal."""
    """Here, f-strings will be used to concatenate the list of the values rolled to the name of the player. This will print: "[player name] rolled: [number rolled]." If 3 values match, it will be returned that the player has tupled out. If a number was rolled twice, that will be printed to the terminal and the user will be asked if they want to tre-roll the non-fixed number. """
    while True: 
        start_time = time.process_time() #edit: Here, I'm now using time to start timing each dice roll.
        dice = roll_dice()
        print(f"{player} rolled: {dice}")
        end_time = time.process_time() 
        elapsed_time = end_time - start_time 
        print(f"The dice roll took {elapsed_time: .4f} seconds.")

        if dice[0] == dice[1] == dice[2]:
            print("Tupled out! Zero points for this turn.") 
            return 0 
        
        elif dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]:
            # This will identify and print the number that was rolled twice so it can be assigned to the fixed number.
            if dice[0] == dice[1]:
                fixed_number = dice[0]
            elif dice[1] == dice[2]:
                fixed_number = dice[1]
            else:
                fixed_number = dice[0]

            print(f"Fixed dice: Number {fixed_number} was rolled twice.")

            while True:
                try: 
                    reroll = input("Do you want to reroll the non-fixed dice? (yes/no)").strip().lower()
                    if reroll == "yes":
                        # should now change the tuple back to the way it originally was (a list) to change the non-fixed dice
                        dice_list = list(dice)
                        unfixed_indices = [i for i in range(3) if dice[i] != fixed_number]
                        for index in unfixed_indices:
                            dice_list[index] = random.randint(1, 6)
                        # now it can convert back to a tuple to be fixed after the changes are made!
                        dice = tuple(dice_list)
                        print(f"{player} rerolled: {dice}")
                        if dice[0] == dice[1] == dice[2]:
                            print("Tupled out! Zero points for this turn.")
                            return 0
                    elif reroll == "no":
                        break
                    else: 
                        print("Invalid input. Please enter 'yes' or 'no'.") 
                except Exception as err: 
                    print(f"An error occurred: {err}")
                    continue 
            return sum(dice)
        
        else:
            try:
                stop = input("Do you want to stop and score your current roll? (yes/no): \n").strip().lower()
                if stop == "yes":
                    return sum(dice)
                elif stop == "no":
                    continue
                else:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.\n")
            except ValueError as valueerror:
                print(valueerror)

    # test:
    # input: "Nakshatra"
    # output expected: can be different, depends on the roll results & user input
    # player_score = play_turn("Nakshatra")
    # print(f"Nakshatra's score: {player_score}")

def play_game(target_score, scores_df):
    """This function keeps track of the players' scores and compares them to the target score set in the intialize_game function above. The return values are different based on whether the target score of 25 is reached or not. """
    current_player_index = 0
    while all(scores_df['Score'] < target_score):
        player = scores_df.at[current_player_index, 'Player']
        print(f"\n{player}'s turn (Current score: {scores_df.at[current_player_index, 'Score']})")
        points = play_turn(player)
        scores_df.at[current_player_index, 'Score'] += points
        print(f"{player}'s new score: {scores_df.at[current_player_index, 'Score']}")

        if scores_df.at[current_player_index, 'Score'] >= target_score:
            print(f"{player} wins!")
            break

        current_player_index = (current_player_index + 1) % len(scores_df)
    # test:
    # input: 25 & DataFrame containing players & scores
    # output expected: game will play until a player reaches the target score. 
    # test_target_score = 10
    # test_players = ["John", "Jane", "Adam"]
    # test_scores_df = pd.DataFrame({"Player": test_players, "Score": [0, 0, 0]})
    # play_game(test_target_score, test_scores_df)
    # print(test_scores_df)

#This will be used to initialize the game, allowing the initialize_game funtion I wrote in the beginning to set the player names and initialize the scores. 
target_score, scores_df = initialize_game()

#Edit for final project: I added the lines below because I thought it would be fun to include as a little extra feature before starting the game to make it look like one whole process put together, from the start (where the starting message displays) to the end, where the time stamps are printed.
time.sleep(1)
print("\nStarting the game...")

#This will start the game by taking in the max score, two different player names, and their scores as the parameters. 
play_game(target_score, scores_df)

#The lines below will display the timestamp for whem the game ended in Year-Month-Day + Hour-Minute-Second format to finish off that specific round.
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"\nRound ended at {timestamp}.")