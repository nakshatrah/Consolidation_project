import random
import pandas as pd

def initialize_game():
    """I wrote the code below to be the setup for the game, which will define the target score to win (25) and ask players to enter their names, which can be a fun way to personalize the game for each round if a bigger group of players wants to take turns."""
    target_score = 25
    players = input("Enter player names separated by commas:").split(',')
    scores = {player: 0 for  player in players}
    """Edit: Now using the pandas library, the players' names will be stored in a DataFrame so that player names will be """
    scores_df = pd.DataFrame(list(scores.items()), columns = ['Player','Score'])
    return target_score, scores_df

def roll_dice():
    """This function will roll three dice and will return each value rolled in a list."""
    return tuple(random.randint(1, 6) for _ in range(3)) #changed to tuple to create unchangeable dice values unless player demands a reroll of what they generated

def play_turn(player):
    """Here, f-strings will be used to concatenate the list of the values rolled to the name of the player. This will print: "[player name] rolled: [number rolled]." If 3 values match, it will be returned that the player has tupled out. If a number was rolled twice, that will be printed to the terminal and the user will be asked if they want to tre-roll the non-fixed number. """
    while True: 
        dice = roll_dice()
        print(f"{player} rolled: {dice}")

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
                        # now it can convert bak to a tuple to be fixed after the changes are made!
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
                stop = input("Do you want to stop and score your current roll? (yes/no): ").strip().lower()
                if stop == "yes":
                    return sum(dice)
                elif stop == "no":
                    continue
                else:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
            except ValueError as valueerror:
                print(valueerror)

def play_game(target_score, scores_df):
    """This function keeps track of the players' scores and compares them to the target score set in the intialize_game function above. The return values are different based on whether the target score of 25 is reached or not. """
    current_player_index = 0
    while all(scores_df['Score'] < target_score):
        player = scores_df.at[current_player_index, 'Player']
        print(f"\n{player}'s turn (Current score: {scores_df.at[current_player_index, 'Score']})")
        points = play_turn(player)
        scores_df.at[current_player_index, 'Score'] += points
        print(f"{player}'s new score: {scores_df.at[current_player_index, 'Score']})")
        
        if scores_df.at[current_player_index, 'Score'] >= target_score:
            print(f"{player} wins!")
            break

        current_player_index = (current_player_index + 1) % len(scores_df)

#This will be used to initialize the game, allowing the initialize_game funtion I wrote in the beginning to set the player names and initialize the scores. 
target_score, scores_df = initialize_game()

#This will start the game by taking in the max score, two different player names, and their scores as the parameters. 
play_game(target_score, scores_df) 