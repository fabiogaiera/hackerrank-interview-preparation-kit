def find_median(arr):
    arr = sorted(arr)
    return arr[(len(arr) // 2)]


median = find_median([5, 3, 1, 2, 4])
print(median)
