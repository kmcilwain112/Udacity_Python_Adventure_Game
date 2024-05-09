'''The main file'''
#Author: Kevin McIlwain
#Email: kmcilwain112@gmail.com
import random
import time
from player import Player
from enemy import Enemy
from weapon import Weapon
#Enemy declaration
bg_enemy = Enemy('Bene Gesserit',25,100)
hh_enemy = Enemy('Harkonnen House',20,100)
sw_enemy = Enemy('Sandworm',15,100)
sa_enemy = Enemy('Sardukar Army',10,100)
em_enemy = Enemy('Evil Mentat',5,100)
emperor = Enemy('Emperor',200,300)
#Weapon declaration
dartgun = Weapon('Dartgun',5,0)
crysknife = Weapon('Crysknife',25,50)
cellgun = Weapon('Cellgun',20,40)
spicegun = Weapon('Spicegun',15,30)
needlegun = Weapon('Needlegun',10,20)
paul = Player("Paul",dartgun,100,10,0)

def print_pause(prompt, seconds):
    """Function to pause console printing at various intervals"""
    print(prompt)
    time.sleep(seconds)

def valid_input(prompt, option1, option2, option3 = "None", option4 = "None", option5 = "None"):
    """Function to check the user input for errors"""
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        if option2 in response:
            break
        if option3 in response:
            break
        if option4 in response:
            break
        if option5 in response:
            break
        else:
            print("Opps! Stop messing around Paul!")
    return response

#Add a soldier to the army
def army_add():
    """Function to add a Soldier to Players Army"""
    paul.army += 1
    if paul.army >= 10:
        print_pause("Your Army is ready for the Emperor!",1)
    else:
        print_pause("An Army of 10 can fight the Emperor and you'll take control of the planet!", 2)
def player_stats():
    """Function to function to print players health,coins,and weapons"""
    print_pause(f"Your Solari:${paul.coins}",1)
    print_pause(f"Your weapon: {paul.weapon.name} and Power: {paul.weapon.power}",1)
    print_pause(f"Your health: {paul.health}",1)
    print_pause(f"Your Army size: {paul.army}",1)

#Roll dice for surprises
def dice_roll(action,number):
    """Function where a random number is guessed and the player gets surprises"""
    guess = random.choice([1,2,3,4,5])
    if action == 'army' and guess == number:
        print_pause("You've found a Freemen and added them to your Army!", 1)
        print_pause(f"Your Army size: {paul.army}", 1)
        army_add()
    if action == 'north' and guess == number:
        paul.weapon.power += 5
        print_pause("You've stolen Spice to upgrage your weapon! +5 Weapon Power.",1)
        print_pause(f"Your Weapon: {paul.weapon.name} Power: {paul.weapon.power}", 2)
    if action == 'south' and guess == number and paul.army > 0:
        paul.army -= 1
        print_pause(f"You've lost a Soldier to a sand storm!\n Your Army size: {paul.army}", 2)
    if action == 'east' and guess == number:
        paul.health -= 10
        if paul.health <= 0:
            print_pause("The Reverend Mother poisened you and killed you!", 1)
            return
        else:
            print_pause("The Reverend Mother has poisened you! -10 Health.", 1)
            print_pause(f"Your Health: {paul.health}", 1)

    if action == 'west' and guess == number:
        paul.coins -= 10
        print_pause(f"You've lost Solari to swindlers! .\n Your Solari: ${paul.coins}", 2)
    if action == 'gift' and guess == number and paul.weapon.power != 35:
        paul.weapon = crysknife
        paul.weapon.power += 10
        print_pause("You found the hidden passageway. You'll find many weapons makers.\n", 1)
        print_pause("The enitire planet's been waiting for you! You'll recieve a special gift.", 2)
        print_pause(f"Wow! You've been gifted a {paul.weapon.name} with +10 power!", 2)
        print_pause(f"Your weapon power: {paul.weapon.power}", 2)
def market():
    """Function where Player can shop for weapons and health"""
    if paul.coins >= 20:
        print("Hi Paul! Welcome to Freemen Market")
        print_pause(f"You have ${paul.coins} Solari to spend. What would you like?",2)
        print_pause(f"(1)Crysknife: $50, Power: {crysknife.power}",1)
        print_pause(f"(2)Cellgun: $40, Power: {cellgun.power}",1)
        print_pause(f"(3)Spicegun: $30, Power: {spicegun.power}",1)
        print_pause(f"(4)Needlegun: $20, Power: {needlegun.power}",1)
        print_pause("(5)+30 Health: $30",1)
        choice = valid_input("(Enter 1, 2, 3, 4, 5)","1","2","3","4","5")
        print("")
        if choice == '1' and paul.coins >= 50:
            paul.weapon = crysknife
            print_pause("Ecellent choice sir! The most powerful weapon on the planet!\n",1)
            paul.coins -= paul.weapon.price
        elif choice == '2' and paul.coins >= 40:
            paul.weapon = cellgun
            print_pause("Smart move sir! A very fine weapon!\n",1)
            paul.coins -= paul.weapon.price
        elif choice == '3' and paul.coins >= 30:
            paul.weapon = spicegun
            print_pause("Awesome sir! the power is in the spice!\n",1)
            paul.coins -= paul.weapon.price
        elif choice == '4' and paul.coins >= 20:
            paul.weapon = needlegun
            paul.coins -= paul.weapon.price
            print_pause("Way to go sir! Watch those needles.\n",1)
        elif choice == '5' and paul.coins >= 30:
            paul.health += 30
            paul.coins -= 30
            print_pause("Awesome decision! Lets stay healthy!\n",1)
    else:
        print_pause("You don't have enough Solari! You must fight to earn more!",1)
    player_stats()
    travel()

def fight():
    """Function where Player fights Enemy"""
    enemy = random.choice(enemies)
    enemy.health = 100
    #Emporer Fight
    if paul.army >= 10:
        print_pause("Your Army is now strong enough to fight the Emporer! What will you do?",2)
        print_pause("(1)Fight the Emperor (2)Keep Traveling",1)
        choice = valid_input("(Enter 1 or 2)\n","1","2")
        print_pause("",1)
        if choice == "1":
            enemy = emperor
            paul.health += (paul.army * 20)
            paul.weapon.power += (paul.army * 20)
        if choice == "2":
            travel()
    if enemy.name != 'Emperor':
        print_pause(f"Lookout! {enemy.name} through the dust!", 2)
        print_pause(f"The {enemy.name} is on the attack!", 2)
        choice = valid_input("Are you going to: (1) fight or (2) run away?\n","1","2")
    if choice == '1':
        while paul.health > 0:
            #Player Strike
            print_pause(f"{random.choice(verbs)}! you've hit the {enemy.name}", 1)
            enemy.health -= paul.weapon.power
            print(f"Your health:{paul.health}, The {enemy.name}'s health:{enemy.health}\n")
            if enemy.health <= 0:
                #Check if the emperor is fighting
                if enemy.name != 'Emperor':
                    print_pause(f"Wow! You defeated The {enemy.name} and rescued a Freemen!", 2)
                    print("")
                    print_pause("You've earned health, Solari, and a soldier!", 2)
                else:
                    print_pause(f"Wow! You defeated The {enemy.name} and saved the planet!", 2)
                    print("")
                    print_pause("I knew you were the saviour!", 2)
                    return
                paul.health += enemy.power * 2
                paul.coins += enemy.power * 2
                army_add()
                print("")
                break
            #Enemy Strike
            print_pause(f"{random.choice(verbs)}! The {enemy.name} hit back!", 1)
            paul.health -= enemy.power
            print(f"Your health:{paul.health}, The {enemy.name}'s health:{enemy.health}\n")
            if paul.health <= 0:
                print_pause(f"Oh No! The {enemy.name} prevailed!", 1)
                print_pause("", 2)
                return
        print_pause("", 2)
        travel()
    elif choice == '2':
        print_pause("The savior would never run! But there's still hope.", 2)
        travel()

def play_again():
    """Function where user is asked to play again"""
    choice = valid_input("Will you try to save this planet again? (y/n)\n","y","n")
    if choice == 'n':
        print_pause("So long Paul!", 2)
        return 'game_over'
    elif choice == 'y':
        print_pause("Lets's try this again...", 2)
        print("")
        paul.weapon = dartgun
        paul.coins = 10
        paul.health = 100
        paul.army = 0
        paul.weapon.power = 5
        return 'running'

def intro():
    """Intro function"""
    print_pause("Hmmm Paul Atreidis, I never thought I'd see you on planet Arrakis. ", 3)
    print_pause("Your galaxy's Emperor sent you here to take over the Spice harvesting trade. ", 3)
    print_pause("There are Arrakians who believe you will save them from the Emperors reign.",3)
    print_pause("There are others who will do anything to take over the Spice harvesting.", 3)
    print_pause("You must save the people!", 2)
    print_pause("The Freemen live underground and to find them will be a dangerous mission.", 2)
    print_pause(f"You're equipped with a {paul.weapon.name} and $10 in Solari. Good luck!", 2)


def travel():
    """Travel function"""
    print_pause("", 1)
    print_pause("Enter 1 to travel North Arrakis", 2)
    print_pause("Enter 2 to travel South Arrakis", 2)
    print_pause("Enter 3 to travel East Arrakis", 2)
    print_pause("Enter 4 to travel West Arrakis", 2)
    print_pause("Enter 5 to find a merchant at Freemen Market", 2)
    print("What would you like to do?")
    print("")
    player_stats()
    choice = valid_input("(Enter 1, 2, 3, 4 or 5.)\n","1","2","3","4","5")
    if choice == '1':
        north()
    elif choice == '2':
        south()
    elif choice =='3':
        east()
    elif choice =='4':
        west()
    elif choice =='5':
        market()


def south():
    """Function to travel south."""
    print_pause("Welcome to South Arrakis. The most dangerous land on the planet.", 2)
    dice_roll('army',2)
    print_pause("The sand storms make this land hard to navigate!", 2)
    dice_roll('south',2)
    print_pause("", 2)
    fight()

def east():
    """Function to travel east."""
    print_pause("Welcome to East Arrakis. The east is belongs to the Reverend Mother.", 2)
    dice_roll('army',5)
    print_pause("Don't eat anything Reverend Mother gives you!", 2)
    dice_roll('east',5)
    print_pause("", 2)
    fight()

def west():
    """Function to travel west."""
    print_pause("Welcome to West Arrakis. Lookout for swindlers out west!", 2)
    dice_roll('army',3)
    dice_roll('west',3)
    print_pause("", 2)
    fight()

def north():
    """Function to travel north."""
    print_pause("Welcome to Far North Arrakis where all of the Spice harvesting happens.", 2)
    dice_roll('army',4)
    print_pause("This is where you'll need your Soldiers stationed to challenge the Emperor.", 2)
    dice_roll('north',4)
    dice_roll("gift",2)
    print_pause("You have to continue traveling!", 2)
    travel()
#Took inspiration from the sample adventure game and made it my own
GAME_STATUS = 'running'
while GAME_STATUS == 'running':
    verbs = ['Bang','Smack','Pow','Wham','Boom','Whack']
    enemies = [bg_enemy, hh_enemy, sw_enemy, em_enemy]
    intro()
    travel()
    GAME_STATUS = play_again()
