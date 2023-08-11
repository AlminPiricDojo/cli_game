# Now let's build a player class for our CLI game
'''
    attributes: name, health, attack, items, weapons, equipped, last_move
    methods: pick_up_item, pick_up_weapon, use_item, equip_weapon, show_items, show_weapons
'''
class Player:
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health
        self.attack = 10
        self.items = []
        self.weapons = []
        self.equipped = None
        self.last_move = None

    def pick_up_item(self, item):
        self.items.append(item)
        print(f"You pick up {item.name}")

    def pick_up_weapon(self, weapon):
        self.weapons.append(weapon)
        print(f"You pick up {weapon.name}")

    def use_item(self, item):
        if item in self.items:
            self.health += item.use()
            print(f"Current Health: {self.health}")
            self.items.remove(item)
            
    def equip_weapon(self, weapon):
        if weapon in self.weapons:
            self.equipped = weapon.equip()
            self.attack += weapon.damage
            print(f"Your attacks now do {self.attack} damage.")
            self.weapons.remove(weapon)

    def show_items(self):
        print("You have the following items:")
        for i in range(len(self.items)):
            print(f"{i}: {self.items[i].name}")
        selection = input("Select item to use: ")
        try:
            self.use_item(self.items[int(selection)])
        except:
            print("Item not found")

    def show_weapons(self):
        print("You have the following weapons:")
        for i in range(len(self.weapons)):
            print(f"{i}: {self.weapons[i].name}")
        selection = input("Select weapons to equip: ")
        try:
            self.equip_weapon(self.weapons[int(selection)])
        except:
            print("Weapon not found")

class Item:
    def __init__(self, name, heal_amount) -> None:
        self.name = name
        self.heal_amount = heal_amount

    def use(self):
        print(f"You use the {self.name} and your health increases by {self.heal_amount}.")
        return self.heal_amount

class Weapon:
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

    def equip(self):
        print(f"You equip {self.name}, increasing your damage by {self.damage}.")
        return self

    def break_weapon(self):
        print(f"Your {self.name} breaks.")
