class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(self.energy + 5, 10)

    def play(self):
        print(f"{self.name} is playing...")
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)

    def get_status(self):
        print(f" {self.name}'s Current Status:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10\n")

    def train(self, trick):
        print(f"{self.name} is learning '{trick}'")
        self.tricks.append(trick)
        self.happiness = min(self.happiness + 2, 10)
        self.energy = max(self.energy - 1, 0)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {','.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet")
