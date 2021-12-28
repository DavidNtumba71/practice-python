
import os
from datetime import datetime
##Building a todo app that writes to a text file - using a procedural approach

def createTextFile(filename): 
    return open(filename, "w+")

def addEntry(date, task, comment,status):
    ## hmm maybe use this for a item object
    return None

def ShowToDoList(list):
    return None

def SaveListToText(list, filename):
    return None

def ValidateResponse(respone):
    return False ## or True

print("{} Welcome to the To-Do List App!!!".format(datetime.now()))
todolist = []
proceed = True

filename = "mytasks.txt"
textfile = open(filename, "w+")

while proceed == True:
    date = (datetime.now()).strftime("%Y-%m-%d")
    task = input("What needs to be done?")
    comment = input("any commnets?")
    status = input("is the task '{}' completed, in progress or done? ".format(task))

    itemdDict = {
       "date" : date
       ,"task": task
       ,"comment": comment
       ,"status": status
    }
    todolist.append(itemdDict)

    print("captured details as follows...")
    print(todolist)
    
    print(todolist[0]["date"])
    content = str(itemdDict["date"]+ " " +itemdDict["task"]+" "+itemdDict["status"]+" "+itemdDict["comment"]) 
    ## it gets tricky reading from a list of dictionaries todolist[0]["Date"], and keys are case sensitive
    textfile.write(content)  ## \n adds a new 
    
    response  = input("task captued, would you like to continue? (Y/N) ")

    if (response == "y" or response == "Y"):
        proceed = True
    else:   
        proceed = False
        ## you can put other code here to 

else:
    print("You have {} task(s) saved in {}".format(len(todolist), filename))
    print("Thank you for using the todolist app")






 
