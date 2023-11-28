def plus_minus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    length = len(arr)

    for elem in arr:
        if elem > 0:
            positives += 1
        elif elem < 0:
            negatives += 1
        else:
            zeros += 1

    print(f"{positives / length:.6f}")
    print(f"{negatives / length:.6f}")
    print(f"{zeros / length:.6f}")


plus_minus([1, 1, 0, -1, -1])
