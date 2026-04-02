class player():

    inventory =[]

    def __init__(self):
        self.name = ""
        self.health = 100
    
    def get_name(self):
        self.name = input("What is your name, adventurer?: ")
        
    def add_to_inventory(self, item):
        self.inventory.append(item)
        self.has_lantern = True
        print(f"You picked up {item}, it has been to your inventory")
    def is_item_in_inventory(self, item):
        for item in self.inventory:
            return True
        return False

