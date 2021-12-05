import numpy as np
import re

class Board():
    def __init__(self, twod_array):
        self.board = twod_array
        self.checks = np.zeros(self.board.shape)
        self.height, self.width = self.board.shape
        self.bingo_coordinates = None
    
    def check_row(self):
        bingo = False
        for i in range(self.height):
            checks_r = (self.checks[i] == 1)
            if np.all(checks_r):
                bingo = True
                break
        return bingo
    
    def check_col(self):
        bingo = False
        for i in range(self.width):
            checks_c = (self.checks[:,i] == 1)
            if np.all(checks_c):
                bingo = True
                break
        return bingo
    
    def sum_unmarked(self):
        sum = 0
        for i in range(self.height):
            for j in range(self.width):
                if not self.checks[i, j]:
                    sum += int(self.board[i, j])
        return sum
        
            
    def draw(self, num):
        res = False
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i, j] == num:
                    self.checks[i, j] = 1
        if self.check_row() or self.check_col():
            res = self.sum_unmarked() * int(num)
        
        return res
    
    def __str__(self):
        s = ""
        for i in range(self.height):
            s += "\n"
            for j in range(self.width):
                if self.checks[i, j]:
                    s += "<{}> ".format(self.board[i, j])
                else:
                    s += " {}  ".format(self.board[i, j])
        return s

    def __repr__(self):
        return self.__str__()


def parse_input(raw_inputs):
    draws = re.split(",|\n", raw_inputs[0].strip())
    rawboards = raw_inputs[2:]
    boards = []
    single_board = []
    for line in rawboards:
        if line == "\n":
            boards.append(Board(np.array(single_board)))
            single_board = []
        else:
            single_board.append(line.split())
    # append last 
    boards.append(Board(np.array(single_board)))

    return draws, boards

def task1(draws, boards):
    """
    Performs task1
    Inputs:
      draws: list of strings representing the drawed numbers
      boards: list of Board objects
    """
    for num in draws:
        for board in boards:
            res = board.draw(num)
            if res:
                return res

def task2(draws, boards):
    n = len(boards)
    bingoed = [0] * n
    num_bingoed = 0
    for num in draws:
        for i, board in enumerate(boards):
            res = board.draw(num)
            if res and not bingoed[i]:
                bingoed[i] = 1
                num_bingoed += 1
                if num_bingoed == n:
                    return res

def main():
    #file = input("Input text data filename here: ")
    with open("input.txt") as f:
        inputs = f.readlines()
    draws, boards = parse_input(inputs)
    ans1 = task1(draws, boards)
    ans2 = task2(draws, boards)
    print("task1: ", ans1, "\ntask2: ", ans2)
    

if __name__ == "__main__":
    main()


