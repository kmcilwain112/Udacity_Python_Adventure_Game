'''The Player class'''
#Author: Kevin McIlwain
#Email: kmcilwain112@gmail.com
class Player:
    '''The Player class creates a Player object'''
    def __init__(self,name,weapon,health,coins,army):
        self.name = name
        self.weapon = weapon
        self.health = health
        self.coins = coins
        self.army = army
