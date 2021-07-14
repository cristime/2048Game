# Author: Cristime Cai
# -*- coding: utf-8 -*-
# 3 TODOs

import os
import time
import msvcrt
import random

MAPSIZE = 4


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
        os.system("cls")  # 清屏(win)
        print()
        for eachLine in self.data:
            for eachNum in eachLine:
                print(eachNum, end="\t")
            print()
        print("\nScore: %d" % self.score)

    # TODO: Finish this function defenition
    def exitGame(self):
        pass

    def play(self):
        self.generateRandomNum()
        while True:
            self.generateRandomNum()
            self.updateGameStatus()
            if not self.gameStatus:
                break
            self.printMap()
            ch = msvcrt.getch()  # TODO: Fix this bug (use msvcrt.kbhit())
            self.move(ch)
        self.exitGame()


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
