# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 18:16:20 2015

@author: Mahmoud
"""
farmAnimals = {'cow': 4, 'horse': 6, 'goat': 3, 'dog': 2}
key = ""
value =0
total = 0

# we will add 24 chicken to the farm and update the cow's num
# then we will print our new farmlist

if key not in farmAnimals:
    farmAnimals["chicken"]= 24
    farmAnimals['cow'] = 6
    print (farmAnimals)

#we will print a list of the animals in the farm without their value (just names)

for key in farmAnimals :
    print ([key])

# ask the user if he is looking for how many specific animal he has
# in the farm

#if he ask for an existing animal, we will output how many of that
#specific animals are in the farm

value_wanted = input("Do you want to know how many of a particular animal is on the farm?\nif so which one?")
if value_wanted in farmAnimals :
    value_wanted = farmAnimals[value_wanted]
    print (value_wanted)

#if the user input is not one of the existing animals,we will let
# the user know that he does not have any of that specific kind

else:
    print("you don't have any", value_wanted, "in your farm")

#print out the total of animals in the farm

for value in farmAnimals:
    total = sum(farmAnimals.values())
print("the total number of animals you have in your farm is" ,total)


