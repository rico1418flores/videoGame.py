import random

# Character base class
class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.xp = 0
        self.level = 1

    def move(self, direction):
        print(self.name, "walks to the", direction)

    def fight(self, enemy):
        damage = random.randint(10, 20)
        enemy.hp -= damage
        print(self.name, "hits", enemy.name, "for", damage, "damage.")
        print(enemy.name, "has", enemy.hp, "HP left.\n")

    def gain_xp(self, points):
        self.xp += points
        print(self.name, "gains", points, "XP. Total XP:", self.xp)
        if self.xp >= 100:
            self.level += 1
            self.hp += 20
            self.xp -= 100
            print("LEVEL UP! Now level", self.level, "with", self.hp, "HP!")

# Wizard class
class Wizard(Character):
    def special(self):
        print(self.name, "uses a magic spell!")

# Brawler class
class Brawler(Character):
    def special(self):
        print(self.name, "throws a strong punch!")

# KnifeFighter class
class KnifeFighter(Character):
    def special(self):
        print(self.name, "slashes with a knife!")

# Simple dialogue question
class Dialogue:
    def __init__(self, question):
        self.question = question

    def ask(self):
        print("\n" + self.question)
        print("1 - Yes")
        print("2 - No")
        answer = input("Choose 1 or 2: ")
        if answer == "1":
            return "You said yes. Interesting!"
        elif answer == "2":
            return "You said no. That's okay!"
        else:
            return "Not a valid choice."

# The game itself
def play_game():
    print("Pick a class:")
    print("1 - Wizard")
    print("2 - Brawler")
    print("3 - Knife Fighter")
    class_pick = input("Enter 1, 2, or 3: ")

    name = input("What is your character's name? ")

    if class_pick == "1":
        player = Wizard(name)
    elif class_pick == "2":
        player = Brawler(name)
    elif class_pick == "3":
        player = KnifeFighter(name)
    else:
        print("Not valid, you are now a Brawler.")
        player = Brawler(name)

    print("\nWelcome", player.name + "!")
    print("Level:", player.level, "| HP:", player.hp)

    while True:
        print("\nWhere do you want to go?")
        print("Type: north, south, east, west, or quit")
        direction = input("Your move: ").lower()

        if direction == "quit":
            print("Game over. Goodbye!")
            break

        if direction in ["north", "south", "east", "west"]:
            player.move(direction)
        else:
            print("That is not a real direction.")
            continue

        # Random event: talk to someone
        if random.choice([True, False]):
            talk = Dialogue("You meet a traveler. Talk to them?")
            print(talk.ask())

        # Random fight
        if random.randint(1,2) == 1:
            enemy = Character("Goblin")
            print("\nA wild Goblin appears!")

            while enemy.hp > 0 and player.hp > 0:
                player.fight(enemy)
                if enemy.hp <= 0:
                    print("You beat the Goblin!")
                    player.gain_xp(50)
                    break

                enemy.fight(player)
                if player.hp <= 0:
                    print("You were defeated by the Goblin...")
                    return

# Start the game
play_game()
    #google is awesome 


