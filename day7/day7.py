import numpy as np
import math


def task1(array):
    # Constant only linear minimizer of least absolute deviation
    # = median 

    target_pos = round(np.median(array))
    moves = abs(array - target_pos)
    return sum(moves)

def task2(array):
    # loss function is cum_sum -> penalizes variance, much like least 
    # squares so minimizer is most likely mean 
    # - > (sure enough! the unrounded mean provides the global 
    # minimum, can be shown analytically)

    target_pos1 = math.ceil(np.mean(array))
    target_pos2 = math.floor(np.mean(array))
    moves1 = cum_sum(abs(array - target_pos1))
    moves2 = cum_sum(abs(array - target_pos2))
    return min(sum(moves1), sum(moves2))

def cum_sum(n):
    return n * (n+1) / 2

def main():
    #file = input("Input text data filename here: ")
    with open("input.txt") as f:
        inputs = np.array(list(map(int, f.read().split(","))))
    ans1 = task1(inputs)
    ans2 = task2(inputs)
    print("task1: ", ans1, "\ntask2: ", ans2)
    

if __name__ == "__main__":
    main()