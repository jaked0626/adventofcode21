
def steer_sub(inputs):
    hor = 0
    ver = 0
    for x in inputs:
        direc, mag = x.split()
        if direc == "down":
            ver += int(mag)
        elif direc == "up":
            ver -= int(mag)
        else:
            hor += int(mag)


def main():
    file = input("Input text data filename here: ")
    with open(file) as f:
        inputs = f.readlines()
    ans = depth_increases(inputs)
    ans2 = depth_increases3(inputs)
    print("task1: ", ans, "\ntask2: ", ans2)
    

if __name__ == "__main__":
    main()