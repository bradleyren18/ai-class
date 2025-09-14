from random import *
class Animal:
    def __init__(self, chance: int, is_carnivore: bool):
        self.chance = chance
        self.hunger = 5
        self.is_carnivore = is_carnivore
    
    def catch(self):
        self.chance
        if self.is_carnivore:
            num = randint(1, self.chance)
            if num == 1:
                if self.hunger <= 5:
                    self.hunger += 5
                self.chance += 1
            else:
                self.hunger -= 1
        else:
            if self.hunger <= 9:
                self.hunger += 1

dog = Animal(2, True)
worm = Animal(2, False)
for i in range(10):
    dog.catch()
    worm.catch()
print(dog.hunger, dog.chance, worm.hunger)