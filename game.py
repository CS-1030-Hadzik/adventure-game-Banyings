"""
Adventure Game
Author: Hyppolite
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""
inventory = []

def welcome_Player(): 
    print("------------------------------")
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")
    print("------------------------------")

    #Getting the Player's name
    name = input("What is your name, adventurer?: ")
    return name

def describe_area():

    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest...
    You see two paths ahead:
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Stay where you are.
    Type 'i' to view your inventory.
    """
    print(starting_area)

def add_to_inventory(item):
    inventory.append(item)
    print(f"Item was picked up {item}")

player_name = welcome_Player()
#print the name with the welcome message
print(f"Welcome, {player_name}! Your journey begins now.")

# Ask the player for their first decision
describe_area()
decision = input("What will you do (1,2,3, or i): ").lower()


# Respond based on the player's decision
if decision == "1":
    print(f"Brave choice, {player_name}! Take the left path into the dark woods. ")
    add_to_inventory("lantern")
elif decision == "2":
    print(f"Brave choice, {player_name}!  Take the right path toward the mountain pass." )
    add_to_inventory("map")
elif decision == "3": 
    print(f"Brave choice, {player_name}! Stay where you are. ")
else:
    print(f"Your Inventory {inventory}")