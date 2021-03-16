#
# Author: Michele Van Dyne
# Student/Editor: Michael Nelson
# ID#: 799056112
# Code from Lab 6 Solution utilized for this program
# Lab 7 - Ultima 0.1 (Topic: Threads)
#
# Description: Avatar class that describes the data and operations of the
#              main player in the Ultima 0.1 games.
#
import StdDraw
from Tile import Tile
import picture
import numpy

minTorchRadius = float(2.0)     # Global variable here for better coding practice


class Avatar:

    # Constructor for the avatar class
    #
    # Input parameters x and y are the initial integer positions of the
    #    avatar within the world
    def __init__(self, x, y, hp, damage, torch):
        self.x = int(x)                 # current x location (integer)
        self.y = int(y)                 # current y location (integer)
        self.hp = int(hp)               # current hp (integer)
        self.damage = int(damage)       # current damage that the avatar inflicts on a monster per hit (integer)
        self.torch = numpy.double(torch)           # how powerful the torch is (default of 4.0) (double-precision float)
        self.TORCH_DELTA = numpy.double(0.5)     # increment/decrement of torch power (default of 0.5) (double)

    # Mutator method to set the avatar to a new location
    #
    # Input parameters are the new integer x and y position
    def setLocation(self, x, y):
        self.x = x
        self.y = y

    # Accessor (getter) method
    #
    # Returns the current hit points of the avatar (cast as an integer)
    def getHitPoints(self):
        StdDraw.setFontSize(12)         # This will adjust the font size for displaying the avatar's HP
        return int(self.hp)

    # Mutator (setter) method
    #
    # Reduces the avatar object's hit points by the given damage amount. Damage cast as an integer
    def incurDamage(self, damage):
        self.hp -= int(damage)

    # Accessor (getter) method
    #
    # Returns the damage output (per "hit") that the avatar causes to monsters
    def getDamage(self):
        return self.damage

    # Accessor method
    #
    # Returns the x position of the avatar
    def getX(self):
        return self.x
    
    # Accessor method
    #
    # Returns the y position of the avatar
    def getY(self):
        return self.y
    
    # Accessor method
    #
    # Returns the current radius of the torch
    def getTorchRadius(self):
        return self.torch

    # Make our torch more powerful
    #
    # Increases the radius of the torch
    def increaseTorch(self):
        self.torch += self.TORCH_DELTA
    
    # Make our torch less powerful
    #
    # Decreases the radius of the torch
    def decreaseTorch(self):
        self.torch -= self.TORCH_DELTA
        if self.torch < minTorchRadius:
            self.torch = minTorchRadius

    # Draw the avatar
    #
    # Uses the avatar's current position to place and draw the avatar
    #    on the canvas
    def draw(self):
        drawX = (self.x + 0.5) * Tile.SIZE
        drawY = (self.y + 0.5) * Tile.SIZE
        StdDraw.picture(picture.Picture("avatar.gif"), drawX, drawY)


# Main code to test the avatar class    
if __name__ == "__main__":
    # Create an avatar at 5,5
    avatar = Avatar(1, 2, 20, 3, 100.0)
    print("%d %d %.1f" % (avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Change the avatar's position
    avatar.setLocation(1, 4)
    print("%d %d %.1f" % (avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Increase the torch radius
    avatar.increaseTorch()
    print("%d %d %.1f" % (avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Decrease the torch radius 6 times to make sure it doesn't go below 2.0
    for i in range(0, 6):
        avatar.decreaseTorch()
        print("%d %d %.1f" % (avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
