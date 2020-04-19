import os
import time

print("Hi, Wlecome to Inventory Management")

inventory = []

def addItemToInventory():
    
    item = None

    itemName = input("enter item's mame:")
    itemCost = input("enter itemss cost price: R")
    itemPrice = input("enter item's selling price: R")
    unitsAdded = input(" how many "+itemName+"(s) are you adding to the inventory" ) #one form of string concat
    
    # I am not doing convert to int at this stage becuase we are not doing calculations

    item = [itemName, itemCost, itemPrice, unitsAdded]

    inventory.append(item) 

    print("An Item has been added to Inventory!")

    print("Printing Item detials....")

    time.sleep(3) # a neat little sleep function

    print(inventory)

    return None


addItemToInventory()

