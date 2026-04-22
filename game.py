"""
Adventure Game
Author: Hyppolite
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

from Player import player

def welcome_player(): 
    print("------------------------------")
    print("Welcome to the Adventure Game!")  
    print("Your journey begins here...")
    print("------------------------------")

def describe_area():
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

def explore_the_dark_woods(player):
    print(f"Brave choice, {player.name}! You take the left path into the dark woods.")
    player.add_to_inventory("lantern")

def explore_the_mountain_pass(player):
    print(f"Brave choice, {player.name}! You take the right path toward the mountain pass.")
    player.add_to_inventory("map")

def explore_the_cave(player):
    if player.is_item_in_inventory("lantern"):
        print(f"Brave choice, {player.name}, you've entered the cave.")
        player.add_to_inventory("treasure")
    else:
        print(f"It is too dark to go into the cave")
        player.health -= 10
        print(f"Your health is now {player.health}") 

def explore_the_hidden_valley(player):
    if player.is_item_in_inventory("map") and player.is_item_in_inventory("treasure"):
        print(f"Brave choice, {player.name}! You entered a hidden valley.")
        player.add_to_inventory("rare herbs")
    else:
        print(f"{player.name}, you don't have the required items to enter the hidden valley.")
        player.health -= 10
        print(f"Your health is now {player.health}") 

def stay_still(player):
    print("You stand still, unsure of what to do...")
    player.health -= 10  
    print(f"Your health is now {player.health}")  

def check_win(player):
    if player.is_item_in_inventory("rare herbs"):
        print(f"{player.name}, you have won the game!")
        return True
    return False

def check_lose(player):
    if player.health <= 0:
        print(f"{player.name} you have died")
        return True
    else:
        return False
# Main game execution
welcome_player()

player = player()
player.get_name()

print(f"Welcome, {player.name}! Your journey begins now.")
describe_area()

while True:
    decision = input("What will you do (1,2,3,4,5,i,q): ").lower()
    
    if decision == "1": 
        explore_the_dark_woods(player)
    elif decision == "2":
        explore_the_mountain_pass(player)
    elif decision == "3":
        explore_the_cave(player)
    elif decision == "4":
        explore_the_hidden_valley(player)
    elif decision == "5": 
        print(f"Brave choice, {player.name}! You stay where you are.")
        stay_still(player)
    elif decision == "i":
        print(f"Inventory: {player.inventory}")
    elif decision == "q":
        print("Thanks for playing!")
        break
    else:
        print("Confused, you stand still, unsure of what to do.")
    
    if check_win(player):
        break
    if check_lose(player):
        break