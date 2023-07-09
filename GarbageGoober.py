#!/usr/bin/env python
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#                            ⠀⠀⢀⣤⠶⠟⠛⠛⠛⠛⠛⠛⠛⠷⠶⢤⣄⣀
#                            ⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣠⣤⡀
#                            ⠀⠸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡄
#                            ⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷
#                            ⠀⠀⠀⠀⠉⠛⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢛⡀
#                            ⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇
#                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀
#                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇
#                            ⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⢀⣀⡈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀
#                            ⠀⢠⣶⣶⣤⣤⣤⣤⣤⣀⣈⡙⠛⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇
#                            ⠀⢸⣿⠿⠛⠋⠛⠻⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀
#                            ⠀⢸⡏⢠⣾⣿⣿⣦⠈⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣀
#                            ⠀⠀⠃⠘⣿⣿⣿⠟⠀⠿⠿⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⡀
#
#                                   Tools for Cleaning                                   
#                                   Github: mammaddrik

#::::: Library :::::
from GarbageGoober.library.clearscreen.clearscr import clearScr
from GarbageGoober.library.banner.banner import Banner
from GarbageGoober.library.slowprint.slowprint import slowprint
from GarbageGoober.library.color.color import Color,color_banner

#::::: Default Library :::::
import random
import webbrowser
import os
import sys
import time

try:
    import terminaltables
except:
    os.system("pip3 install -r requirements.txt")

#::::: again :::::
def again():
    GarbageGoober_again = input(Color.BCyan +"""\n    Do you want to continue? [Y/n]"""+ Color.End +"""\n    GarbageGoober:~# """)
    if GarbageGoober_again == "":
        clearScr()
        GarbageGoober()
    elif GarbageGoober_again.upper() == "Y":
        clearScr()
        GarbageGoober()
    elif GarbageGoober_again.upper() == "N":
        print("\n    Goodbye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()
    else:
        clearScr()
        GarbageGoober()

def first_time():
    clearScr()
    print(Banner.GarbageGoober_banner)
    time.sleep(1)
    slowprint(Color.BGreen+"Hi, I think I'm alive.")
    time.sleep(2)
    slowprint("My name is GarbageGoober and I'm here to clean your rooms."+Color.End)
    time.sleep(2)
    slowprint("\nSo How can I help you:") 
    time.sleep(2)
first_time()

#::::: GarbageGoober :::::
def GarbageGoober():
    clearScr()
    print(Banner.GarbageGoober_banner)
    choice = input("""
    {01}-Random trash
    {02}-Custom trash
    {00}-Github
    {99}-Exit\n
GarbageGoober:~# """)

    #::::: Random trash :::::
    if (choice == "01" or choice == "1"):
        clearScr()
        print(Banner.GarbageGoober_banner)
        def showInTable(rooms: list):
            "Table change function"
            table_instance = terminaltables.AsciiTable(rooms)
            table_instance.outer_border = False
            table_instance.inner_heading_row_border = False
            table_instance.inner_column_border = True
            table_instance.inner_row_border = True
            print(table_instance.table)
            
        def initialCheckRooms():
            "function to check initial rooms."
            global size
            correctness = False
            while not correctness:
                size = input("\nEnter the size of the house: ")
                if (size.isdigit()):
                    size = int(size)
                    correctness = True
                else:
                    slowprint(Color.BRed+"\n{-}--Enter a correct Number."+Color.End)
            array = []
            for i in range(size):
                array.append([])
                for j in range(size):
                    array[i].append(0)
            return array
        
        def isCheckedAllRooms():
            "Function to check all rooms."
            global size
            array = state["checkRooms"]
            flag = 1
            for i in range(size):
                for j in range(size):
                    item = array[i][j]
                    flag = item * flag
            return flag == 1
        
        def makeBoxes(boxesStatus: list = None):
            "Function to build a box, put garbage."
            global size
            boxes = []
            for i in range(size):
                boxes.append([])
                for j in range(size):
                    boxes[i].append(random.randint(0, 1))
            return boxes
        
        def showRooms():
            "Room display function"
            state["boxes"] = makeBoxes() if state["boxes"] == [] else state["boxes"]
            boxes = state["boxes"]
            rooms = []
            counter = 1
            for i in range(len(boxes)):
                rooms.append([])
                for _ in range(len(boxes)):
                    rooms[i].append(str(counter))
                    counter += 1
            showInTable(rooms)

        def setVacuumLocation():
            "function of placing a vacuum cleaner"
            global size
            correctness = False
            showRooms()
            while not correctness:
                place = input("\nIn which room is the vacuum cleaner: ")
                if place.isdigit():
                    place = int(place)
                    if (place <= (size*size)):
                        row = int(place % size)
                        if row == 0 :
                            row = int(place/size) - 1
                        else:
                            row = int(place/size)

                        index = int(place % size)
                        if index == 0:
                            index = size - 1
                        else: 
                            index -= 1

                        correctness = True
                        return [row, index]
                    else :
                        slowprint(Color.BRed+"{-}--Out of range."+Color.End)
                else:
                    slowprint(Color.BRed+"{-}--Enter a correct Number."+Color.End)
        
        def makeCanvas(boxes: list, agentLocation: list):
            "The function of displaying vacuum cleaners and garbage"
            global state
            clearScr()
            canvas = []
            for i in range(len(boxes)):
                canvas.append([])
                for j in range(len(boxes[i])):
                    canvas[i].append(               
                        Color.BGreen+"O"+Color.End
                        if i == agentLocation[0] and j == agentLocation[1]
                        else Color.BRed+"X"+Color.End
                        if boxes[i][j] == 1
                        else " "
                    )
            return canvas

        def moveAgent(currentLocation: list = None):
            "Vacuum cleaner movement function"
            global state
            if currentLocation == []:
                newLocation = setVacuumLocation()
            else:
                newLocation = [currentLocation[0], currentLocation[1]]
                state["checkRooms"][newLocation[0]][newLocation[1]] = 1

                if currentLocation[0] == 0:
                    state["changeRowTo"] = "down"
                elif currentLocation[0] == (size - 1):
                    state["changeRowTo"] = "up"

                if currentLocation[1] == (size - 1) and state["canChangeRow"] == True:
                    if state["changeRowTo"] == "up":
                        newLocation[0] = currentLocation[0] - 1
                    else:
                        newLocation[0] = currentLocation[0] + 1
                    newLocation[1] = currentLocation[1]
                    state["canChangeRow"] = False
                    state["goRight"] = False
                
                elif currentLocation[1] == 0 and state["canChangeRow"] == True:
                    if state["changeRowTo"] == "up":
                        newLocation[0] = currentLocation[0] - 1
                    else:
                        newLocation[0] = currentLocation[0] + 1
                    newLocation[1] = currentLocation[1]
                    state["canChangeRow"] = False
                    state["goRight"] = True
                
                elif currentLocation[1] < (size - 1) and state["goRight"] == True:
                    newLocation[0] = currentLocation[0]
                    newLocation[1] = currentLocation[1] + 1
                    state["canChangeRow"] = True

                elif currentLocation[1] > 0 and state["goRight"] == False:
                    newLocation[0] = currentLocation[0]
                    newLocation[1] = currentLocation[1] - 1
                    state["canChangeRow"] = True

            return newLocation
        
        def changeStatus(currentStatus: str, boxesStatus: list, agentLocation: list):
            "Status change function"
            print("")
            if currentStatus != "Finished.":
                if currentStatus == "Moving...":
                    newStatus = "Checking..."
                elif currentStatus == "Checking...":
                    if boxesStatus[agentLocation[0]][agentLocation[1]] == 1:
                        newStatus = "Cleaning..."
                    else:
                        newStatus = "Moving..."
                if currentStatus == "Cleaning...":
                    boxesStatus[agentLocation[0]][agentLocation[1]] = 0
                    newStatus = "Moving..."

            else:
                newStatus = currentStatus   
            return newStatus
        
        def action():
            "Vacuum cleaner performance check function"
            global state
            time.sleep(1)
            os.system(state["clearCommand"])
            state["agentLocation"] = (
                moveAgent(state["agentLocation"])
                if state["status"] == "Moving..."
                else state["agentLocation"]
            )
            state["boxes"] = makeBoxes() if state["boxes"] == [] else state["boxes"]
            canvas = makeCanvas(state["boxes"], state["agentLocation"])

            print("Room size: " + str(size) + "x" + str(size)+ "\n")
            showInTable(canvas)
            print("\nStatus: " + state["status"], sep="\n")

            state["status"] = changeStatus(
                state["status"], state["boxes"], state["agentLocation"]
            )

        def start(unlimitedMovement: bool):
            "Start function"
            if unlimitedMovement:
                while True:
                    action()
            else:
                while isCheckedAllRooms() == False:
                    action()

        def initialize():
            "initialization function"
            global state
            state = {
                "status": "Moving...",
                "clearCommand": "cls" if os.name == "nt" else "clear",
                "changeRowTo": "down",
                "canChangeRow": True,
                "goRight": True,
                "boxes": [],
                "canvas": "",
                "agentLocation": [],
                "checkRooms": []
            }
            state["checkRooms"] = initialCheckRooms()

            start(False)  
        initialize()
        clearScr()
        canvas = makeCanvas(state["boxes"], state["agentLocation"])
        print("Room size: " + str(size) + "x" + str(size)+ "\n")
        showInTable(canvas)
        print("\nStatus: Finished.", sep="\n")
        again()

    #::::: Custom trash  :::::
    elif (choice == "02" or choice == "2"):
        clearScr()
        print(Banner.GarbageGoober_banner)
        main()
        again()
        
    #::::: Exit :::::
    elif (choice == "99"):
        print("\nGoodBye :)")
        time.sleep(0.4)
        clearScr()
        sys.exit()
    
    elif (choice == "0" or choice == "00"):
        clearScr()
        time.sleep(0.4)
        print(Banner.github_banner)
        url = "https://github.com/mammaddrik"
        webbrowser.open(url)
        again()
    else:
        print(Color.BRed + "\n    It is wronge.")
        again()
        
def clean(floor): 
    i = 0
    j = 0
    try:
        row = len(floor)
        col = len(floor[0])
    except IndexError:
        slowprint(Color.BRed+"{-}--Row and Col must be greater than zero."+Color.End)
        again()
    
    for i in range(row):
        if (i % 2 == 0):
            for j in range(col):
                if (floor[i][j] == 1):
                    printfloor(floor, i, j)
                    floor[i][j] = 0
                printfloor(floor, i, j)
        else:
            for j in range(col-1, -1, -1):
                if (floor[i][j] == 1):
                    printfloor(floor, i, j)
                    floor[i][j] = 0
                printfloor(floor, i, j)
                

def printfloor(floor, row, col):
    time.sleep(1)
    clearScr()
    print("Room size:",len(floor),"x",len(floor[0]))
    print("")
    for r in range(len(floor)):
        for c in range(len(floor[r])):
            if r == row and c == col:
                print(f" \033[1;32m>\033[1;37m{floor[r][c]}\033[1;32m<\033[1;37m ", end = '')
            else:
                print(f"  {floor[r][c]}  ", end = '')
        print(end="\n")
    print(end="\n")
    
def main():
    floor = []
    try:
        row_size = int(input("Enter the Number of Row: "))
        col_size = int(input("Enter the Number of Col: "))
    except ValueError:
        slowprint(Color.BRed+"{-}--Row and Col must be Integer"+Color.End)
        again()
    except IndexError:
        slowprint(Color.BRed+"{-}--Row and Col must be greater than zero."+Color.End)
        again()
    slowprint(Color.BYellow+"dirty: 1 \nclean: 0\n"+Color.End)
    for i in range(row_size):
        try:
            f = list(map(int, input("Enter clean status for each cell: ").split(" ")))
            if len(f) == col_size:
                floor.append(f)
                for j,m in enumerate(f):
                    if m > 1:
                        f[j] = 1
                    elif m < 1:
                        f[j] = 0
            else:
                slowprint(Color.BRed+"{-}--Out of range."+Color.End)
                again()
        except ValueError:
            slowprint(Color.BRed+"\n{-}--Cell must be Integer"+Color.End)
            again()
    clean(floor)

try:
    GarbageGoober()
    main()
    again()
except KeyboardInterrupt:
    slowprint(Color.BRed+"Finishing up..."+Color.End)
    time.sleep(0.4) 
    clearScr()
    sys.exit()
    
