#! /usr/bin/env/python

from random import randint


class Product:
    def __init__(self,
                 name,
                 price=10,
                 weight=20,
                 flammability=.5,
                 identifier=randint(10000, 9000000)):

        self.name = name
        self.weight = weight
        self.price = price
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        s_ratio = self.price/self.weight
        if (s_ratio < 0.5):
            return('Not so stealable.')
        elif ((s_ratio >= 0.5) & (s_ratio < 1)):
            return('Kin da stealable.')
        else:
            return('Very stealable.')

    def explode(self):
        boom = self.weight * self.flammability
        if (boom < 10):
            return('...fizzle.')
        elif((boom >= 10) & (boom < 50)):
            return('...boom!')
        else:
            return('...BABOOM!!')


class BoxingBlove(Product):
    def __init__(self, name, price=10, weight=10,
                 flammability=.5, identifier=randint(10000, 9000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        return("...It's a glove.")

    def punch(self):
        if(self.weight < 5):
            return("...That tickles")
        elif((self.weight >= 5) & (self.weight < 15)):
            return("Hey that hurt!")
        else:
            return("OUCH!")
