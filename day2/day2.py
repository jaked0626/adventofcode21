
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
    return hor * ver

def steer_sub2(inputs):
    hor = 0
    ver = 0
    aim = 0
    for x in inputs:
        direc, mag = x.split()
        if direc == "down":
            aim += int(mag)
        elif direc == "up":
            aim -= int(mag)
        else:
            hor += int(mag)
            ver += (aim * int(mag))
    return hor * ver


def main():
    file = input("Input text data filename here: ")
    with open(file) as f:
        inputs = f.readlines()
    ans1 = steer_sub(inputs)
    ans2 = steer_sub2(inputs)
    print("task1: ", ans1, "\ntask2: ", ans2)
    

if __name__ == "__main__":
    main()