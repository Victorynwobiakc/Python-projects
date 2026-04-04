# RPG Stats Roulette
import random

print("Welcome to the tower of GOD player from another world")

name = input("What's your name? ")
height = input("What's your height? ")
weight = input("what's your weight")

class_selection = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]
stat_rank =["S", "A", "B","C","D","E"]

print(f'''

Player: {name}\n
Height: {height}\n
Weight: {weight}\n
Class: {random.choice(class_selection)}\n

Strength: {random.choice(stat_rank)}
Speed: {random.choice(stat_rank)}
Holy_power: {random.choice(stat_rank)}
Intelligence: {random.choice(stat_rank)}
Endurance: {random.choice(stat_rank)}
 ''')