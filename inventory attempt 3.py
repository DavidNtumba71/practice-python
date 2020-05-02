import os
import time

print("Hi, Wlecome to Inventory Management")

#this version will create an item class


class Item:

    def __init__(self, name, cost, price,  units):
        self.__name__ = name
        self.__cost__ = cost
        self.__price__ = price
        self.__units__ = units

    
    def recordItem(self):
        print("An Item has been added to Inventory!")

        print("Printing Item detials....")

        time.sleep(3) #a neat little sleep function

        print({self.__name__, self.__cost__, self.__price__, self.__units__})

        return None



# method to set inventory
def add_item_to_inventory():
    
    addItemName = input("item name: ")            #item name
    addItemCost = int(input("item cost: R"))       #item  cost
    addItemPrice = int(input("item price: R"))     #item selling price
    addItemAmount = int(input("item amount: "))   #amount of item added to inventory

    return Item(addItemName, addItemCost, addItemPrice, addItemAmount)




item1 = add_item_to_inventory() # assigning the value returned to the variable
item1.recordItem()