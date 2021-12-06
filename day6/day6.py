import numpy as np


def task1(fish, days=80):
    """
    First approach used to solve task1. Memory intensive. 
    Inputs: 
      fish: numpy array representing initial fish
      days (int): Days of simulation 
    
    Returns: number of fish at end of simulation
    """
    #print("day 0", ":", len(fish), "|", fish)
    for _ in range(days):
        fish -= 1
        newbabies = np.array([8] * fish[fish == -1].shape[0])
        fish[fish == -1] = 6
        fish = np.concatenate([fish, newbabies])
        # print("day", t+1,  ":", len(fish), "|", fish)
        #print(freq_token(fish))
    
    return len(fish)

def task2(fish, days=256):
    """
    task1 was way too exhaustive of memory for task2. 
    Different approach using hashtables. 
    Inputs:
      fish: list representing initial fish
      days (int): days of simulation
    Returns: number of fish at end of simulation
    """

    # populate dictionary where each key is days left till birth
    # represents fish at time t
    fish_t0 = {} 
    for countdown in fish:
        fish_t0[countdown] = fish_t0.get(countdown, 0) + 1
    
    for _ in range(days):
        fish_t1 = {} # dictionary representing fish at t + 1
        for countdown, num_fish in fish_t0.items():
            if countdown == 0:
                fish_t1[8] = fish_t1.get(8, 0) + num_fish
                fish_t1[6] = fish_t1.get(6, 0) + num_fish
            else:
                fish_t1[countdown - 1] = fish_t1.get(countdown - 1, 0) + num_fish
                
        fish_t0 = fish_t1
        
    return sum(fish_t0.values())


def main():
    #file = input("Input text data filename here: ")
    with open("input.txt") as f:
        inputs = list(map(int, f.read().split(",")))
    ans1 = task2(inputs, 80) # using task2 since task1 alters input array
    ans2 = task2(inputs, 256)
    print("task1: ", ans1, "\ntask2: ", ans2)
    

if __name__ == "__main__":
    main()