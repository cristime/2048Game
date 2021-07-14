# -*- coding: utf-8 -*-

import os
import time
import msvcrt
import random


MAPSIZE = 4


class Game:
    data = []
    gameStatus = True

    def __init__(self):
        self.gameStatus = True
        random.seed(time.time())
        for i in range(0, MAPSIZE):
            tmpList = []
            for j in range(0, MAPSIZE):
                tmpList.append(0)
            self.data.append(tmpList)

    def updateGameStatus(self):
        pass

    def move(self):
        pass

    def generateRandomNum(self):
        x = MAPSIZE
        y = MAPSIZE
        while x and x < MAPSIZE and y and y < MAPSIZE:
            x = random.randint(0, MAPSIZE - 1)
            y = random.randint(0, MAPSIZE)
        num = random.randint(0, 10)
        if num == 9:
            self.data[x][y] = 4
        else:
            self.data[x][y] = 2

    def play(self):
        pass


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
