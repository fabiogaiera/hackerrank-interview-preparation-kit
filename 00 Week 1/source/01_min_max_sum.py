def min_max_sum(arr):
    minimum = min(arr)
    maximum = max(arr)

    sum_total = 0
    for elem in arr:
        sum_total += elem

    print(sum_total - maximum, sum_total - minimum)


min_max_sum([1, 3, 5, 7, 9])
