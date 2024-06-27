import random
from art import vs
from game_data import data

def display_biography(selection):
    name = selection["name"]
    description = selection["description"]
    country = selection["country"]
    
    biography = f"{name}, a {description}, from {country}"
    return biography

score = 0
game_on = True

# Initialize an "empty/unassigned" variable
previous_selection = None

while game_on is True:
    
    if previous_selection is not None: # Checks if a previous selection exists
        first_selection = previous_selection # If YES, it's assigned to 'first_selection'
    else:
        first_selection = random.choice(data) # Otherwise choose a new selection from 'data'    
    second_selection = random.choice(data)    
    # Ensure that second_selection is different from first_selection
    while first_selection == second_selection:
        second_selection = random.choice(data)    
      
    print(f"Compare A: {display_biography(first_selection)}")
    print(vs)
    print(f"Compare B: {display_biography(second_selection)}")
    
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    if first_selection["follower_count"] > second_selection["follower_count"]:
        # If true,  and the second selection as the previous loser
        previous_winner = first_selection # Assign the first selection as the previous winner
        previous_loser = second_selection # # Assign the second selection as the previous loser
    else:    
        # Assign 'second selection as the previous winner' and 'first selection as the previous loser'
        previous_winner = second_selection
        previous_loser = first_selection
    
    if (user_guess == 'A' and first_selection["follower_count"] > second_selection["follower_count"]) or (user_guess == 'B' and second_selection["follower_count"] > first_selection["follower_count"]):
        print("Correct!")
        score += 1
        previous_selection = previous_winner
    else:
        print(f"Nope, you're wrong! Your final score is: {score}")
        game_on = False
        break
    
    print(f"Your current score is: {score}")

