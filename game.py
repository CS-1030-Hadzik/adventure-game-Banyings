"""
Adventure Game
Author: Hyppolite
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""



from Player import player


def welcome_Player(): 
    print("------------------------------")
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")
    print("------------------------------")

    #Getting the Player's name
    
def describe_area():

    # Describe the starting area
    starting_area = """
    You find yourself in a dark forest...
    You see two paths ahead:
    1. Take the left path into the dark woods.
    2. Take the right path toward the mountain pass.
    3. Take the center path towards the cave
    4. Take the path to the hidden valley
    5. Stay where you are.
    Type 'i' to view your inventory.
    Type 'q' to quit
    """
    print(starting_area)

def add_to_inventory(item):
    player.inventory.append(item)
    print(f"Item was picked up {item}, it has been added to your inventory")

player_name = welcome_Player()

player = player()
player.get_name()

#print the name with the welcome message
print(f"Welcome, {player.name}! Your journey begins now.")

# Ask the player for their first decision
describe_area()

while True:
    decision = input("What will you do (1,2,3,4,5,i, q (quit)): ").lower()
    # Respond based on the player's decision
    if decision == "1": 
        print(f"Brave choice, {player.name}! take the left path into the dark woods. ")
        player.add_to_inventory("lantern")
    elif decision == "2":
        print(f"Brave choice, {player.name}! take the right path toward the mountain pass." )
        player.add_to_inventory("map")
    elif decision == "3":
        if player.is_item_in_inventory("lantern"):
            print(f"Brave choice, {player.name}, you've entered the cave. ")
            player.add_to_inventory("treasure")
        else:
            print(f"It is too dark to go into the cave")
    elif decision == "4": # Hidden valley
        # Go in the valley if they have a map and the treaure
        if player.is_item_in_inventory("map") and player.is_item_in_inventory("treasure"):
            print(f"Brave choice, {player.name}! you enterred a hidden valley. ")
            player.add_to_inventory("rare herbs")
        else:
            print(f"{player.name}, you don't have the required items to enter the hidden valley.")
    elif decision == "5": 
        print(f"Brave choice, {player.name}! you stay where you are. ")
    elif decision == "i":
        print(player.inventory)
    elif decision == "q":
        print("Thanks for playing")
        break
    else:
        print(f"Confused, you still, unsure of what to do.")