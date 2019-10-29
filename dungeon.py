from random import randint, choice
import subprocess #allows you to spawn new processes; uses Popen constructor
import platform #queries python interpreter for architecture information
import time #module provides time-related fxns


class MapGrid:     #creating a class called MapGrid
    def __init__(self, width, height):
        self.width = width   #access class attribute with self keyword
        self.height = height
        self.mobs = [] #initialized as an empty list; occupy one space on grid; represented as
                        # (x,y) tuple will be drawn in using carot symbol ^
        self.walls = []#initialized as an empty list; occupy one space on grid; represented as
                        # (x,y) tuple will be drawn in using hashtag symbol #
        self.start = (0, 0)
        self.goal = (width-1, height-1)
        self.player = (0, 0)

#_init_ is a constructor that initializes; creates object of class
#the attributes are in "self.name_of_attribute" to tell Python we are referring to data
#within the object -self means "this object"
#width and height are parameters to the constructor

    def move_player(self, d):
        x = self.player[0]
        y = self.player[1]
        pos = None

        if d[0] == 'r':
            pos = (x + 1, y)
        if d[0] == 'l':
            pos = (x - 1, y)
        if d[0] == 'u':
            pos = (x, y - 1)
        if d[0] == 'd':
            pos = (x, y + 1)

        if pos not in self.walls:
            self.player = pos

        if pos == self.mobs:
            print("Here lies a mob")

            #calls the combat and loot modules and return back

        if pos == self.goal:
            print("This is the end!")



def draw_grid(g, width=3):
    for y in range(g.height):
        for x in range(g.width):
            if (x, y) in g.mobs:
                symbol = '^'
            elif (x, y) in g.walls:
                symbol = '#'
            elif (x, y) == g.player:
                symbol = '$'
            elif (x, y) == g.start:
                symbol = '<'
            elif (x, y) == g.goal:
                symbol = '>'
            else:
                symbol = '.'
            print("%%-%ds" % width % symbol, end="")
        print()


def get_mobs(g: MapGrid, pct=.20) -> list: #arguments are the grid and percent of map as mobs
        out = []
        diff=int(input("Difficulty level from 1-10 with 10 being easiest? "))

        for i in range(int(g.height*g.width*pct)//diff): #randomly place mobs; height*width*pct

            x = randint(1, g.width-2)
            y = randint(1, g.height-2)

            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
        return out

def get_walls(g: MapGrid, pct=.10) -> list:  #arguments are the grid and percent of map as mobs
        out = []
        for i in range(int(g.height*g.width*pct)//2):  #randomly place walls; height*width*pct

            x = randint(1, g.width-2)
            y = randint(1, g.height-2)

            out.append((x, y))
            out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
        return out

def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
     # Popen opens pipe to access other pipes; will clear the screen
    time.sleep(.01) #suspends execution of the calling thread by x seconds


def main():
    howwide=int(input("How many columns? ")) #this will determine the size of our dungeon
    howhigh=int(input("How many rows? "))    #this will determine the size of our dungeon

    g = MapGrid(howwide, howhigh)
    g.mobs = get_mobs(g)    # random mobs can be imported here for selection
    g.walls = get_walls(g)  # other hazardous variables like lava pits
                            # can also be included and placed randomly

    while g.player != g.goal:
        draw_grid(g)
        d = input("Which way? (r, l, u, d)") #needs a check to ensure correct input of (r,l,u,d)
        g.move_player(d)
        clear() #clears interpreter console
    print("You made it!")


if __name__ == '__main__':
    main()

# from https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
#grid code constructed using this as reference:
#https://medium.com/@angellom/writing-a-python-dungeon-game-part-i-47e35668f16b
#1) Every Python module has it’s __name__ defined and if this is ‘__main__’, it implies that
#   the module is being run standalone and we can do corresponding appropriate actions
#2) If you import this script as a module in another script, the __name__ is set
#   to the name of the script/module.
#3) Python files can act as either reusable modules, or as standalone programs.
#4) if __name__ == “main”: this is used to execute some code only if file was run directly,
#   and not imported
