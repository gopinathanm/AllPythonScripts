import random
class Dice:
    def __init__(self):
        self.dice1 = (1,2,3,4,5,6)
        self.dice2 = (1,2,3,4,5,6)


    def roll(self):
        return (random.choice(self.dice1), random.choice(self.dice2))


dice = Dice()

print(dice.roll())