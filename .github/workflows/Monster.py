#
# Author: Michele Van Dyne
# Student/Editor: Michael Nelson
# ID#: 799056112
# Lab 7 - Ultima 0.1 (Topic: Threads)
# Referenced enumeration code from Tile.py provided in Lab06 Solutions
#
# Description: Monster class that holds all information about tiles and
#              characters in the Ultima 0.1 games

from enum import Enum, auto
import time
import StdDraw
import picture
import random
from Tile import Tile
import World
import Avatar
import threading
import random


class MonsterType(Enum):
    INVALID = auto()
    SKELETON = auto()
    ORC = auto()
    BAT = auto()
    SLIME = auto()


class Monster:

    # Construct a new monster
    # 
    # param world	- the world the monster moves about in
    # param code	- the string code that distinguishes types of monsters
    # param x		- the x position of the monster
    # param y		- the y position of the monster
    # param hp		- hit points - damage sustained by the monster
    # param damage	- damage the monster causes
    # param sleepMs	- delay between time monster moves
    def __init__(self, world, code, x, y, hp, damage, sleepMs):

        self.world = world
        self.x = int(x)
        self.y = int(y)
        self.hp = int(hp)
        self.damage = int(damage)
        self.sleepMs = int(sleepMs)
        self.counter = 0
        if code == "SK":
            self.type = MonsterType.SKELETON
        elif code == "OR":
            self.type = MonsterType.ORC
        elif code == "SL":
            self.type = MonsterType.SLIME
        elif code == "BA":
            self.type = MonsterType.BAT
        else:
            self.type = MonsterType.INVALID


    # The avatar has attacked a monster!
    #
    # param points	- number of hit points to be subtracted from monster
    def incurDamage(self, points):

        self.hp -= int(points)

    #
    # Draw this monster at its current location
    def draw(self):

        drawX = (self.x + 0.5) * Tile.SIZE          # Referenced code from Avatar.py
        drawY = (self.y + 0.5) * Tile.SIZE
        while self.counter < 3:
            StdDraw.setPenColor(StdDraw.RED)
            StdDraw.text(self.x + 0.5, self.y + 1.5, str(self.hp))           # Display remaining HP for 3 game cycles per API
        if self.type == MonsterType.SKELETON:
            StdDraw.picture(picture.Picture("skeleton.gif"), drawX, drawY)
        elif self.type == MonsterType.ORC:
            StdDraw.picture(picture.Picture("orc.gif"), drawX, drawY)
        elif self.type == MonsterType.SLIME:
            StdDraw.picture(picture.Picture("slime.gif"), drawX, drawY)
        elif self.type == MonsterType.BAT:
            StdDraw.picture(picture.Picture("bat.gif"), drawX, drawY)
        else:
            return

    #
    # Get the number of hit points the monster has remaining
    # 
    # return the number of hit points
    def getHitPoints(self):

        return self.hp

    #
    # Get the amount of damage a monster causes
    # 
    # return amount of damage monster causes
    def getDamage(self):
        if self.counter == 3:
            self.counter = 0
        else:
            self.counter += 1
        return self.damage

    #
    # Get the x position of the monster
    #
    # return x position
    def getX(self):

        return self.x       # The draw method handles offsetting the monster graphics so they are centered on tiles

    #
    # Get the y position of the monster
    #
    # return y position
    def getY(self):

        return self.y

    #
    # Set the new location of the monster
    # 
    # param x the new x location
    # param y the new y location
    def setLocation(self, x, y):

        self.x = int(x)
        self.y = int(y)

    #
    # Thread that moves the monster around periodically
    def run(self):

        while self.hp > 0:
            monster_bearing = random.randint(0,3)
            if monster_bearing == 0:
                y = self.y + 1
                x = self.x
            elif monster_bearing == 1:
                y = self.y
                x = self.x + 1
            elif monster_bearing == 2:
                y = self.y - 1
                x = self.x
            else:
                y = self.y
                x = self.x - 1

            self.world.monsterMove(x, y, self)
            time.sleep(self.sleepMS/1000)


