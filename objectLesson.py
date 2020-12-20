

def goodbye():
    print("Thankyou for playing. Enjoy the real world!")

def drawBox(string):
    amt = len(string) + 4
    print("*" * amt)
    print("* " + string + " *")
    print("*" * amt)

class Map:
    
    def __init__(self):
        self.rooms = []
        self.doors = []
        self.index = 0

    def add_room(self, room):
        self.rooms.append(room)

    def show_current(self):
        drawBox(self.rooms[self.index].name)
        print(self.rooms[self.index].desc)
        self.rooms[self.index].exit_display()
        print(len(self.rooms[self.index].exits))
        print()
        self.parser()

    def parser(self):
        cmd = input("Type the direction you wish to go or 'get' an item.")
        if cmd.lower() == "north" or cmd.lower() == "n":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "North" in self.rooms[self.index].exits[i].dir:
                    print("You go North")
                    self.index = self.rooms[self.index].exits[i].link
                i += 1
        if cmd.lower() == "east" or cmd.lower() == "e":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "East" in self.rooms[self.index].exits[i].dir:
                    print("You go East")
                    self.index = self.rooms[self.index].exits[i].link    
                i += 1
        if cmd.lower() == "south" or cmd.lower() == "s":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "South" in self.rooms[self.index].exits[i].dir:
                    print("You go South")
                    self.index = self.rooms[self.index].exits[i].link
                    cmd = ""
                i += 1
        if cmd.lower() == "west" or cmd.lower() == "w":
            i = 0
            while i < len(self.rooms[self.index].exits):
                if "West" in self.rooms[self.index].exits[i].dir:
                    print("You go West")
                    self.index = self.rooms[self.index].exits[i].link
                i += 1      
        else:
            print("Please enter a valid command")
        cmd = ""
        self.show_current() 

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.exits = []

    def exit_display(self):
        i = 0
        nav = ""
        while i < len(self.exits):
            nav += self.exits[i].dir + " "
            i += 1
        print(nav)
    
    def add_exit(self, exit):
        self.exits.append(exit)
        
class Exit:
    def __init__(self, dir, link):
        self.dir = dir
        self.link = link


Game = Map()
r1 = Room("Cave","The tunnel stretches out before you leading deeper into darkness to the north, while the sunlight filters in through the exit to the south.")
d1 = Exit("North", 2)
r1.add_exit(d1)
d2 = Exit("South", 1)
r1.add_exit(d2)
Game.add_room(r1)
r2 = Room("Outside","The mouth of a cave digs deeply into the northern face of the hillside you're on. The forest stretches to the east, west, and south but you promised to go in and retrieve some glowing mushrooms for your eccentric wizard friend.")
d1 = Exit("North",0)
r2.add_exit(d1)
Game.add_room(r2)
r3 = Room("Deeper In","You have walked deeper into the tunnel going north.")
d4 = Exit("South", 0)
r3.add_exit(d4)
Game.add_room(r3)
Game.index = 2
Game.show_current()

