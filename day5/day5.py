import re
import numpy as np


def count_coordinates(lines, diagonals=False):
    """
    Counts number of times lines cross each coordinate.
    Inputs:
      lines: list of lines, each represented as [x1, y1, x2, y2]
      diagonals: boolean indicating whether to count diagonals 
    """
    coordinate_dic = {}

    for x1, y1, x2, y2 in lines:
        if x1 != x2 and y1 != y2 and not diagonals:
            continue
        
        # all diagonal lines have a slope of 1. So, coordinates will be 
        # incremented by either 1, 0, or -1
        delta_x = np.sign(x2 - x1)
        delta_y = np.sign(y2 - y1)
        line_len = max(abs(x2-x1), abs(y2-y1)) # for diagonals, this will be equal

        for i in range(line_len + 1):
            coordinate = (x1 + i * delta_x, y1 + i * delta_y)
            coordinate_dic[coordinate] = coordinate_dic.get(coordinate, 0) + 1

    return coordinate_dic


def task(lines, diagonals=False):
    """
    Returns number of coordinates with more than two lines crossing it. 
    Inputs:
      lines: list of lines, each represented as [x1, y1, x2, y2]
      diagonals: boolean indicating whether to count diagonals 
    """
    coordinate_dic = count_coordinates(lines, diagonals)

    n = 0
    for val in coordinate_dic.values():
        if val >= 2:
            n += 1
    return n

def parse_input(inputs):
    lines = []
    for line in inputs[:-1]:
        cleaned_line = re.split(",| -> ", line)
        lines.append(list(map(int, cleaned_line)))
    return lines

def main():
    #file = input("Input text data filename here: ")
    with open("input.txt") as f:
        inputs = f.read().split("\n")
    lines = parse_input(inputs)
    ans1 = task(lines)
    ans2 = task(lines, True)
    print("task1: ", ans1, "\ntask2: ", ans2)
    

if __name__ == "__main__":
    main()