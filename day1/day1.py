

def depth_increases(lst):
    count = 0
    last_x = lst[0]
    for x in lst[1:]:
        x = x
        if x > last_x:
            count += 1
        last_x = x
    return count

def depth_increases3(lst):
    count = 0
    last_x = sum(lst[:3])
    for i, _ in enumerate(lst[1:-1]):
        x = sum(lst[i:i+3])
        if x > last_x:
            count += 1
        last_x = x
    return count


def main():
    file = input("Input text data filename here: ")
    with open(file) as f:
        inputs = list(map(int, f.readlines()))
    ans = depth_increases(inputs)
    ans2 = depth_increases3(inputs)
    print("task1: ", ans, "\ntask2: ", ans2)
    

if __name__ == "__main__":
    main()