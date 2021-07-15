# Author: Cristime Cai
# -*- coding: utf-8 -*-
# 1 TODOs

import os
import platform
import sys
import time
import random

MAPSIZE = 4
FILENAME = r"score.txt"


class Game:
    data = []
    gameStatus = True
    score = 0

    def __init__(self):
        self.gameStatus = True
        self.score = 0
        random.seed(time.time())
        for i in range(0, MAPSIZE):
            tmpList = []
            for j in range(0, MAPSIZE):
                tmpList.append(0)
            self.data.append(tmpList)

    def updateGameStatus(self):
        self.gameStatus = False
        for x in range(0, MAPSIZE - 1):
            for y in range(0, MAPSIZE - 1):
                if not self.data[x][y] or self.data[x][y] == self.data[x][y + 1] or self.data[x][y] == self.data[x + 1][y]:
                    self.gameStatus = True
                    return

    # TODO: Finish this function defenition
    def move(self, direction):
        if direction == "w" or direction == "W":
            pass
        elif direction == "s" or direction == "S":
            pass
        elif direction == "a" or direction == "A":
            pass
        elif direction == "d" or direction == "D":
            pass

    def generateRandomNum(self):
        x = MAPSIZE
        y = MAPSIZE
        while x >= MAPSIZE or y >= MAPSIZE:  # Bug Fixed
            x = random.randint(0, MAPSIZE - 1)
            y = random.randint(0, MAPSIZE - 1)
        num = random.randint(0, 10)
        if num == 9:
            self.data[x][y] = 4
        else:
            self.data[x][y] = 2

    def printMap(self):
        # Add system check
        if platform.system() == "Windows":
            os.system("cls")  # 清屏(win)
        else:
            os.system("clear")  # 清屏(*nix)
        print()
        for eachLine in self.data:
            for eachNum in eachLine:
                print(eachNum, end="\t")
            print()
        print("\nScore: %d" % self.score)

    def exitGame(self):
        print("\nGame over!")
        if not os.path.exists(FILENAME):
            file = open(FILENAME, "w")
            file.write(str(self.score))
            file.close()
        else:
            file = open(FILENAME, "r")
            bestScore = int(file.readline())
            file.close()
            bestScore = max(bestScore, self.score)
            file = open(FILENAME, "w")
            print("Best score: %d" % bestScore)
            file.write(str(bestScore))
            file.close()

    def play(self):
        self.generateRandomNum()
        while True:
            self.generateRandomNum()
            self.updateGameStatus()
            if not self.gameStatus:
                break
            self.printMap()
            direction = sys.stdin.read(1)  # Bug fixed (but \n is needed)
            self.move(direction)
        self.exitGame()


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
