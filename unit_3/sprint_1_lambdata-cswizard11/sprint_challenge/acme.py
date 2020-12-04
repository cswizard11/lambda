import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = flammability
        self.identifier = int(random.uniform(1000000, 9999999))

    def stealability(self):
        value = self.price / self.weight
        if value < 0.5:
            return 'Not so stealable...'

        elif 0.5 <= value < 1:
            return 'Kinda stealable.'

        else:
            return 'Very stealable!'

    def explode(self):
        value = self.weight * self.flammability
        if value < 10:
            return '..fizzle.'

        elif 10 <= value < 50:
            return '...boom!'

        else:
            return '...BABOOM!!'

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        
        elif 5 <= self.weight < 15:
            return 'Hey that hurt!'

        else:
            return 'OUCH!'
