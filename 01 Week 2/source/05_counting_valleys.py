def countingValleys(steps, path):
    count = 0
    sea_level = 0
    lst = []
    for i in range(steps):
        if path[i] == 'U':
            sea_level += 1
            lst.append(sea_level)
        elif path[i] == 'D':
            sea_level -= 1
            lst.append(sea_level)

    for i in range(len(lst)):
        if i + 1 < len(lst):
            if lst[i] == -1 and lst[i + 1] == 0:
                count += 1

    return count


counter = countingValleys(12, 'DDUUDDUDUUUD')
print(counter)
