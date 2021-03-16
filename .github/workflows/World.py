#
# Author: Michele Van Dyne
# Student/Editor: Michael Nelson
# ID#: 799056112
# Code from Lab 6 Solution utilized for this program
# Lab 7 - Ultima 0.1 (Topic: Threads)
# Referenced code from Python Crash Course - Chapter 10: Files and Exceptions
# Also referenced code from:
# https://thispointer.com/python-search-strings-in-a-file-and-get-line-numbers-of-lines-containing-the-string/
#
# Description: World class that holds all information about tiles and
#              characters (monster(s) and avatar) in the Ultima 0.1 games

from Tile import Tile
from Avatar import Avatar
import math
import sys
import StdDraw
import numpy
import Monster
import threading
import random

class World:


    # Constructor for the world
    #
    # Input parameter is a file name holding the configuration information
    #    for the world to be created
    #    The constructor reads in file data, stores it in appropriate
    #    attributes and sets up the window within which to draw.
    #    It also initializes the lighting in the world.
    def __init__(self, filename):
        with open(filename, 'r') as f:
            # Read in the first line of text
            line = f.readline().split()
            # Translate that line to width and height
            self.width = int(line[0])           # Create attributes for width, then height next line
            self.height = int(line[1])
            # Read in the second line of text
            line = f.readline().split()
            # Translate that into the avatar position
            self.avatar = Avatar(int(line[0]), int(line[1]), int(line[2]), int(line[3]), numpy.double(line[4]))
            # Create an empty dictionary to store tile information
            self.tiles = [[None for i in range(self.height)] for j in range(self.width)]
            # Read in the lines of text that give tile types and parse into color blocks
            line = f.readlines()
            index = 0
            for i in range(0, self.height):
                current_line = line[i].split()
                for j in range(0, self.width):
                    self.tiles[j][self.height - i - 1] = Tile(current_line[j])
                    index += 1
            self.monsters = []
            monster_index = self.height
            while monster_index < len(line):
                if line[monster_index]not in["\n",""," "]:
                    monster_line = line[monster_index].split()
                    self.monsters.append(Monster.Monster(self, (monster_line[0]), int(monster_line[1]), \
                        int(monster_line[2]), int(monster_line[3]), int(monster_line[4]), int(monster_line[5])))
                monster_index += 1
        self.threads = []
        for i in range(0, len(self.monsters)):
            self.threads.append(threading.Thread(target=self.monsters[i].run))
            self.threads[i].start()
        self.lock = threading.Lock()



        # Set up the window for drawing
        StdDraw.setCanvasSize(self.width * Tile.SIZE, self.height * Tile.SIZE)
        StdDraw.setXscale(0.0, self.width * Tile.SIZE)
        StdDraw.setYscale(0.0, self.height * Tile.SIZE)


        # Initial lighting
        self.light(self.avatar.getX(), self.avatar.getY(), self.avatar.getTorchRadius())
        self.draw()

    # Is the avatar alive? Returns bool(True) if Avatar's hp is > 0
    #
    def avatarAlive(self):
        if Avatar.getHitPoints() > 0:
            return True
        else:
            return False

    # Accept keyboard input and performs the appropriate action
    # 
    # Input parameter is a character that indicates the action to be taken
    def handleKey(self, ch):
        deltaX = 0
        deltaY = 0
        if ch == 'w':
            deltaY = 1
        elif ch == 's':
            deltaY = -1
        elif ch == 'a':
            deltaX = -1
        elif ch == 'd':
            deltaX = 1
        elif ch == '+':
            self.avatar.increaseTorch()
        elif ch == '-':
            self.avatar.decreaseTorch()

        # If the keyboard input was to move avatar
        if deltaX != 0 or deltaY != 0:
            x = self.avatar.getX() + deltaX
            y = self.avatar.getY() + deltaY

            if x >= 0 and x < self.width and \
               y >= 0 and y < self.height and \
               self.tiles[x][y].isPassable():
                # New location is in bounds and passable
                self.avatar.setLocation(x, y)
                self.avatar.hp -= Tile.getDamage()
        self.setLit(False)
        self.light(self.avatar.getX(), self.avatar.getY(), self.avatar.getTorchRadius())

    # Input parameters are the x and y position of the monster and the current monster
    # Called by Monster.run() which is a worker thread
    # If the proposed location is not valid or not passable, then nothing happens.
    # If there is currently another monster at the proposed location, then nothing happens.
    # If the Avatar is at the proposed location, then the monster gets to attack the Avatar and do the appropriate dmg.
    # In this case, the monster stays at its current location (Avatar and monsters never overlap).
    # Otherwise, the monster makes its move to the new location, incurring any damage associated with the new location
    # (i.e. if the new location is lava).
    # Note: since only the World object knows the outcome of the monster's call to monsterMove(), the World object must update the calling Monster object by calling setLocation() and/or incurDamage().

    def monsterMove(self, x, y, monster):
                threads = []
        workers = []
        for i in range(0, len(self.monsters)):
            workers.append(self.monster)
            threads.append(threading.Thread(target=workers[i-1].run()))
            threads[i-1].start()
            for i in range(1, len(self.monsters)):
                while self.monster.hp > 0:
                    self.monsterBearing = random.randint(0, 3)
                    if self.monsterBearing == 0:
                        if self.tiles[x][y+1].isPassable():
                            self.monster.setLocation(x, y+1)
                            for m in range(0, len(self.monsters)):
                                if self.monsters[m].getX() == x:
                                    if self.monsters[m].getY() == y+1:
                                        pass
                                    elif self.avatar.getX() == x:
                                        if self.avatar.getY() == y+1:
                                            self.avatar.hp -= self.monster.getDamage()
                                        else:
                                            self.monster.setLocation(x, y+1)

                    elif self.monsterBearing == 1:
                        if self.tiles[x+1][y].isPassable():
                            self.monster.setLocation(x+1, y)
                            for m in range(0, len(self.monsters)):
                                if self.monsters[m].getX() == x+1:
                                    if self.monsters[m].getY() == y:
                                        pass
                                    elif self.avatar.getX() == x+1:
                                        if self.avatar.getY() == self.y:
                                            self.avatar.hp -= self.monster.getDamage()
                                        else:
                                            self.monster.setLocation(x+1, y)

                    elif self.monsterBearing == 2:
                        if self.tiles[x][y - 1].isPassable():
                            self.monster.setLocation(x, y - 1)
                            for m in range(0, len(self.monsters)):
                                if self.monsters[m].getX() == x:
                                    if self.monsters[m].getY() == y - 1:
                                        pass
                                    elif self.avatar.getX() == x:
                                        if self.avatar.getY() == y - 1:
                                            self.avatar.hp -= self.monster.getDamage()
                                        else:
                                            self.monster.setLocation(x, y - 1)

                    elif self.monsterBearing == 3:
                        if self.tiles[x-1][y].isPassable():
                            self.monster.setLocation(x-1, y)
                            for m in range(0, len(self.monsters)):
                                if self.monsters[m].getX() == x-1:
                                    if self.monsters[m].getY() == y:
                                        pass
                                    elif self.avatar.getX() == x-1:
                                        if self.avatar.getY() == self.y:
                                            self.avatar.hp -= self.monster.getDamage()
                                        else:
                                            self.monster.setLocation(x-1, y)

    # How many monsters are still alive?
    def getNumMonsters(self):
        livingMonsters = 0
        for n in range(0, len(self.monsters)):
            if self.monsters[n].getHitPoints() > 0:
                livingMonsters += 1
        return int(livingMonsters)


    # Draw all the lit tiles
    #
    # Only action is to draw all the components associated with the world
    def draw(self):
        # First update the lighting of the world
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[x][y].draw(x, y)
                for a in range(0, len(self.monsters)):
                    self.monsters[a].draw()
        self.avatar.draw()

    # Light the world
    #
    # Input parameters are the x and y position of the avatar and the
    #    current radius of the torch.
    #    Calls the recursive lightDFS method to continue the lighting
    # Returns the total number of tiles lit
    def light(self, x, y, r):
        result = self.lightDFS(x, y, x, y, r)
        print("light(%d, %d, %.1f) = %d" % (x, y, r, result))
        return result
    
    # Recursively light from (x, y) limiting to radius r
    #
    # Input parameters are (x,y), the position of the avatar,
    #    (currX, currY), the position that we are currently looking
    #    to light, and r, the radius of the torch.
    # Returns the number of tiles lit
    def lightDFS(self, x, y, currentX, currentY, r):
        if currentX < 0 or currentY < 0 or \
           currentX >= self.width or currentY >= self.height or \
           self.tiles[currentX][currentY].getLit():
            return 0
        
        result = 0
        deltaX = x - currentX
        deltaY = y - currentY
        
        dist = math.sqrt(deltaX * deltaX + deltaY * deltaY)

        if dist < r:
            self.tiles[currentX][currentY].setLit(True)
            result += 1
                                                            
            if not self.tiles[currentX][currentY].isOpaque():
                result += self.lightDFS(x, y, currentX - 1, currentY, r)	# west		
                result += self.lightDFS(x, y, currentX + 1, currentY, r)	# east
                result += self.lightDFS(x, y, currentX, currentY - 1, r)	# north
                result += self.lightDFS(x, y, currentX, currentY + 1, r)	# south							
        return result
            
    # Turn all the lit values of the tiles to a given value. Used
    #    to reset lighting each time the avatar moves or the torch
    #    strength changes
    #
    # Input parameter is a boolean value, generally False, to turn off
    #    the light, but is flexible to turn the light on in some future
    #    version

    def setLit(self, value):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[x][y].setLit(value)

    
# Main code to test the world class
if __name__ == "__main__":
    world0 = World(sys.argv[1])
    world0.draw()
    StdDraw.show()
