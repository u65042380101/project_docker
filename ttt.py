import os
from getkey import getkey
import random


class Swapnumber():
  board = []
  col = 4
  row = 4
  cur = []

  def __init__(self):
    self.board = list(range(0, self.row))
    for i in range(0, self.row):
      self.board[i] = list(range(0, self.col))

    randombox = list(range(1, self.row * self.col))
    for i in range(self.row * self.col - 2, 0, -1):
      n = random.randrange(0, i + 1, 1)
      self.board[i // self.row][i % self.col] = randombox[n]
      randombox.remove(randombox[n])
    self.board[0][0] = randombox[0]

    self.cur = [self.row - 1, self.col - 1]
    self.board[self.cur[0]][self.cur[1]] = 0

  def showBoard(self):
    for i in range(0, self.row):
      for j in range(0, self.col):
        if(self.board[i][j]) == 0:
          print("     ", end="")
        else:
          print("%2d   " % (self.board[i][j]), end="")
      print("")
      print("")
  def checkBingo(self):
    e = 1
    for i in range(self.row):
        for j in range(self.col):
            if (i == self.row - 1 and j == self.col - 1):
                if self.board[i][j] != 0:
                    return False
            else:
                if self.board[i][j] != e:
                    return False
                e += 1

    print("Bingo !!!")
    return True
  def startGame(self):
    c = ""
    while c != "x":
      os.system('clear')
      self.showBoard()
      print("press w a s z (x = exit) : ")
      c = getkey()
      if c == "a" and self.cur[1] != self.col-1:
        self.board[self.cur[0]][self.cur[1]] = self.board[self.cur[0]][
            self.cur[1] + 1]
        self.board[self.cur[0]][self.cur[1] + 1] = 0
        self.cur[1] += 1
      elif c == "s" and self.cur[1] != 0:
        self.board[self.cur[0]][self.cur[1]] = self.board[self.cur[0]][
            self.cur[1] - 1]
        self.board[self.cur[0]][self.cur[1] - 1] = 0
        self.cur[1] -= 1
      elif c == "w" and self.cur[0] != self.row-1:
        self.board[self.cur[0]][self.cur[1]] = self.board[self.cur[0] +
                                                          1][self.cur[1]]
        self.board[self.cur[0] + 1][self.cur[1]] = 0
        self.cur[0] += 1
      elif c == "z" and self.cur[0] != 0:
        self.board[self.cur[0]][self.cur[1]] = self.board[self.cur[0] -
                                                          1][self.cur[1]]
        self.board[self.cur[0] - 1][self.cur[1]] = 0
        self.cur[0] -= 1
      if(self.checkBingo()):
       c = "x"

game = Swapnumber()
game.startGame()