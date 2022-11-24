from readData import readFilms
from insertData import addfilms
from updateData import updatefilms
from deleteData import deletefilm
from printOptions import optionsFilms

# create a function
def menuOptions():
    options = 0  # flag variable

    while options not in ["1", "2", "3", "4", "5", "6"]:
        print(
            "Films Menu Options\nEnter:\n1. To Print.\n2. To Add.\n3. To Update.\n4. To Delete.\n5. Database details.\n6. To Exit"
        )
        # re-assign a new value to the options variable
        options = input("\nEnter one of the options above: ")
        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice")
    return options


mainProgram = True  # flag variable
"""name = "Jane"
while name == "Jane"""
while mainProgram:  #  == True
    mainmenu = menuOptions()
    if mainmenu == "1":
        readFilms()
    elif mainmenu == "2":
        addfilms()
    elif mainmenu == "3":
        updatefilms()
    elif mainmenu == "4":
        deletefilm()
    elif mainmenu == "5":
        optionsFilms()
    else:  # re-assign  the value of main program to False
        mainProgram = False

input("press enter to Exit: ")
