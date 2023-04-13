import emoji
import random
import time
import platform

# Welcome message

#prompt for user name
name = str(input("What is your name? "))
#prompt for user age
age = int(input("How old are you? "))
#ask user for starting location in game, and store in variable. city, forest, wilderness or beach
location = input("Where would you like to start (town, forest, wilderness or beach)? ")
town = 'Eldham'
forest = 'Eldham Forest'
wilderness = 'Eldham Wilderness'
beach = 'Eldham Beach'
health = 100
inventory = []
equipment = []
died = "You died"

if age < 18:
    print("Sorry, you are too young to play this game")
    exit()

if input == "health":
    print('Your health is', health)
if health <= 0:
    print(died)
    exit()

#set up a while loop to check if user has entered a valid location
while location != "town" and location != "forest" and location != "wilderness" and location != "beach":
    location = input("Please enter a valid location (town, forest, wilderness or beach): ")
while investigate != "y" and investigate != "n":
    investigate = input("Please enter a valid option (y/n): ")
while attack != "y" and attack != "n":
    attack = input("Please enter a valid option (y/n): ")
while open_chest != "y" and open_chest != "n":
    open_chest = input("Please enter a valid option (y/n): ")

if location == "town":
    print(f"You wake up in a dark cottage, you are in a town called {town}, You have no idea how you got there, but you know you need to get out. You look around and see a door, and a window. Which do you choose?")
    #ask user for input, and store in variable. door or window
    door_or_window = input("Door or window? ")
    #set up a while loop to check if user has entered a valid location
    while door_or_window != "door" and door_or_window != "window":
        door_or_window = input("Please enter a valid location (door or window): ")
    if door_or_window == "door":
        print('The door is locked, you need to find a key')
    if door_or_window == "window":
        print('The window opens, you climb out and find yourself in a dark alleyway, there are strange noises coming from behind a bale of hay. Do you investigate?')
        #ask user for input, and store in variable. yes or no
        investigate = input("y/n? ")
        #set up a while loop to check if user has entered a valid location
        if investigate == "y":
            print('A dog jumps out and bites your leg')
            print('You lose 10 health')
            health = health - 10
            print(f'Your health is now {health}%')
            attack = input("Do you want to attack the dog? y/n? ")
            if attack == "y":
                print('You kick the dog and it runs away')
                print('')
                if health <= 0:
                    print(died)
                    exit()
            if attack == "n":
                print('You run away')
        if investigate == "n":
            print('Probably a good choice to stay away from that until you find a weapon')

    print('You continue down the alleyway and spot a chest, do you want to open it?')
    open_chest = input("y/n? ")
    if open_chest == "y":
        print('You open the chest and find a key')
        inventory.append('key to armory')
        print('You now have a key to the armory')
    if open_chest == "n":
        print('You decide to leave the chest alone')
    print('You continue down the alleyway and find a door, the sign above the door says "Armory"')
    if inventory == "key to armory":
        print('You open the door and find a sword')
        inventory.append('sword')
        print('You now have a sword')
    if inventory != "key to armory":
        print('You need a key to open the door')
