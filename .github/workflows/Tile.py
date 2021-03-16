#
# Author: Michele Van Dyne
# Student/Editor: Michael Nelson
# ID#: 799056112
# Code from Lab 6 Solution utilized for this program
# Lab 7 - Ultima 0.1 (Topic: Threads)
#
# Description: Tile class that describes the data and operations of the
#              tiles that represent each available position and its terrain attributes in the Ultima 0.1 games.
#

from enum import Enum, auto
import picture
import StdDraw


# Enumeration class to handle different tile types
class TileType(Enum):
    INVALID = auto()
    FLOOR = auto()
    LAVA = auto()
    WATER = auto()
    FOREST = auto()
    GRASS = auto()
    MOUNTAIN = auto()
    WALL = auto()


# Class that handles all data and operations on tiles
class Tile:
    # Static variable associated with tiles to specify the size
    SIZE = 16

    # Constructor for a tile
    #
    # Parameter is a string or character that specifies the
    #   type of tile
    def __init__(self, code):
        self.lit = False                  # Is the tile lit?

        if code == "B":
            self.type = TileType.FLOOR
        elif code == "L":
            self.type = TileType.LAVA
        elif code == "W":
            self.type = TileType.WATER
        elif code == "F":
            self.type = TileType.FOREST
        elif code == "G":
            self.type = TileType.GRASS
        elif code == "M":
            self.type = TileType.MOUNTAIN
        elif code == "S":
            self.type = TileType.WALL
        else:
            self.type = TileType.INVALID

    # Accessor for the lit instance variable
    #
    # Returns a True if the tile is lit, False otherwise
    def getLit(self):
        return self.lit

    # Mutator for the lit instance variable
    #
    # Input parameter value is a boolean variable
    def setLit(self, value):
        self.lit = value

    # Does light pass through this tile
    #
    # Returns True if the tile is opaque, False otherwise
    def isOpaque(self):
        if self.type == TileType.FLOOR or \
           self.type == TileType.LAVA or \
           self.type == TileType.WATER or \
           self.type == TileType.GRASS or \
           self.type == TileType.INVALID:
            return False
        else:
            return True

    # Can the hero walk through this tile
    #
    # Returns True if the tile can be moved through,
    #    False otherwise
    def isPassable(self):
        if self.type == TileType.WATER or \
           self.type == TileType.MOUNTAIN or \
           self.type == TileType.WALL:
            return False
        else:
            return True

    # Does the hero receive damage when they step onto this tile?
    #
    # Returns 1 if the tile is lava, or 0 for any other tile type
    # Casting return values as integers since no decimals hit points in this version
    def getDamage(self):
        if self.type == TileType.LAVA:
            return int(1)
        else:
            return int(0)

    # Draw the tile at the given location
    #
    # Input parameters x and y are integers specifying
    #    the tile's position within the world grid
    def draw(self, x, y):
        drawX = float(x + 0.5) * self.SIZE      # Cast (x + 0.5) and (y + 0.5) to floats
        drawY = float(y + 0.5) * self.SIZE

        if self.lit:
            if self.type == TileType.FLOOR:
                StdDraw.picture(picture.Picture("brickfloor.gif"), drawX, drawY)
            elif self.type == TileType.LAVA:
                StdDraw.picture(picture.Picture("lava.gif"), drawX, drawY)
            elif self.type == TileType.WATER:
                StdDraw.picture(picture.Picture("water.gif"), drawX, drawY)
            elif self.type == TileType.GRASS:
                StdDraw.picture(picture.Picture("grasslands.gif"), drawX, drawY)
            elif self.type == TileType.FOREST:
                StdDraw.picture(picture.Picture("forest.gif"), drawX, drawY)
            elif self.type == TileType.MOUNTAIN:
                StdDraw.picture(picture.Picture("mountains.gif"), drawX, drawY)
            elif self.type == TileType.WALL:
                StdDraw.picture(picture.Picture("stonewall.gif"), drawX, drawY)
        else:
            StdDraw.picture(picture.Picture("blank.gif"), drawX, drawY)


#
# Main code for testing the Tile class
#
if __name__ == "__main__":
    # Set up test parameters
    SIZE 	= 16
    WIDTH 	= 7
    HEIGHT 	= 2

    # Set up a StdDraw canvas on which to draw the tiles
    StdDraw.setCanvasSize(WIDTH * SIZE, HEIGHT * SIZE)
    StdDraw.setXscale(0.0, WIDTH * SIZE)
    StdDraw.setYscale(0.0, HEIGHT * SIZE)

    # Create a list of codes to test tile creation
    codes = ["B", "L", "W", "F", "G", "M", "S"]
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            tile = Tile(codes[i])
            # Light every second tile
            if (i + j) % 2 == 0:
                tile.setLit(True)
            print("%d %d : lit %s\topaque %s\tpassable %s" % (i, j, tile.getLit(), tile.isOpaque(), tile.isPassable()))
            tile.draw(i, j)
    StdDraw.show(5000)
