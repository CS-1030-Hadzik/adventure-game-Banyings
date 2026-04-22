class player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.inventory = []
        self.has_lantern = False
    
    def get_name(self):
        self.name = input("What is your name, adventurer?: ")
        return self.name
        
    def add_to_inventory(self, item):
        self.inventory.append(item)
        if item == "lantern":
            self.has_lantern = True
        print(f"You picked up {item}, it has been added to your inventory")
        
    def is_item_in_inventory(self, item):
        for inv_item in self.inventory:
            if inv_item == item:
                return True
        return False

