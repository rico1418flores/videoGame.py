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

    print("\nWelcome")

    #google is awesome 

    
