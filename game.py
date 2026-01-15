# Writting my first code
"""
Adventure Game
Author: Hyppolite
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""
print("Welcome to the Adventure Game!")  
print("Your journey begins here...")

#Getting the Player's name
player_name = input("What is your name, advanture?:")

#print the name with the welcome message
print(f"Welcome, {player_name}! Your jpurney begins now")

# Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
"""
print(starting_area)

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ").lower()

# Respond based on the player's decision
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example
else:
    print("Confused, you stand still, unsure of what to do.")