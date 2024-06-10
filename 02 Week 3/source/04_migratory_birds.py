def migratoryBirds(arr):
    dct = {}
    for elem in arr:
        if elem in dct:
            dct[elem] += 1
        else:
            dct[elem] = 1

    pair = (1, 1)
    for key, value in dct.items():
        if value > pair[1]:
            pair = (key, value)
        elif value == pair[1]:
            if key < pair[0]:
                pair = (key, value)

    return pair[0]


a = migratoryBirds([1, 1, 2, 2, 3])
print(a)
