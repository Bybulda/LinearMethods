def make_dict():
    size = int(input())
    data = dict()
    mx = 2
    position = 1
    for i in range(size):
        parent = input()
        if parent not in data.keys():
            data[str(i + 1)] = 2
        else:
            way_for = data[parent] + 1
            data[str(i + 1)] = way_for
            if way_for > mx:
                mx = way_for
                position = i + 1
    return position


if __name__ == '__main__':
    print(make_dict())
