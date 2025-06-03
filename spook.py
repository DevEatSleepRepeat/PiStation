import json

class Room:
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits  # Dict of direction -> room name
        self.items = items or []

class Game:
    def __init__(self):
        self.rooms = self.create_world()
        self.current_room = "Foyer"
        self.inventory = []
        self.running = True

    def create_world(self):
        return {
            "Foyer": Room(
                "Foyer",
                "You stand in a dusty old foyer. A chandelier flickers above. A ghost dog winks at you.",
                {"north": "Library", "east": "Kitchen"},
                ["ghost biscuit"]
            ),
            "Library": Room(
                "Library",
                "Tall shelves of books loom around you. One whispers your name.",
                {"south": "Foyer"},
                ["haunted book"]
            ),
            "Kitchen": Room(
                "Kitchen",
                "The fridge hums with ominous energy. A pot stirs itself.",
                {"west": "Foyer"},
                ["spooky spoon"]
            ),
        }

    def describe_current_room(self):
        room = self.rooms[self.current_room]
        print(f"\n== {room.name} ==")
        print(room.description)
        if room.items:
            print("You see:", ", ".join(room.items))
        print("Exits:", ", ".join(room.exits.keys()))

    def handle_command(self, command):
        parts = command.lower().split()
        if not parts:
            return

        verb = parts[0]

        if verb in ["go", "move"] and len(parts) > 1:
            self.move(parts[1])
        elif verb == "look":
            self.describe_current_room()
        elif verb == "take" and len(parts) > 1:
            self.take_item(parts[1])
        elif verb == "inventory":
            self.show_inventory()
        elif verb == "quit":
            self.running = False
            print("Goodbye, brave (and slightly scared) adventurer!")
        else:
            print("I don't understand that command.")

    def move(self, direction):
        room = self.rooms[self.current_room]
        if direction in room.exits:
            self.current_room = room.exits[direction]
            self.describe_current_room()
        else:
            print("You can't go that way.")

    def take_item(self, item):
        room = self.rooms[self.current_room]
        if item in room.items:
            room.items.remove(item)
            self.inventory.append(item)
            print(f"You picked up the {item}.")
        else:
            print("That item isn't here.")

    def show_inventory(self):
        if self.inventory:
            print("You have:", ", ".join(self.inventory))
        else:
            print("You're carrying nothing but your courage.")

    def play(self):
        print("Welcome to the Lighthearted Spooky Adventure! Type 'look' to look around, 'go north' to move, 'take item' to pick something up.")
        self.describe_current_room()
        while self.running:
            command = input("\n> ")
            self.handle_command(command)

if __name__ == "__main__":
    game = Game()
    game.play()
