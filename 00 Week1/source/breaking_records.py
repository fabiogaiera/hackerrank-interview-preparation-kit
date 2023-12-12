"""
                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

scores = [12, 24, 10, 24]

"""


# Index 0 is for breaking most points records, and index 1 is for breaking least points records.
def breaking_records(scores):
    maximum = scores[0]
    minimum = scores[0]
    count_max = 0
    count_min = 0
    for i in range(1, len(scores)):
        if scores[i] > maximum:
            maximum = scores[i]
            count_max += 1
        elif scores[i] < minimum:
            minimum = scores[i]
            count_min += 1

    lst = [0, 0]
    lst[0] = count_max
    lst[1] = count_min
    return lst
