def maximumPerimeterTriangle(sticks):
    sorted_sticks = sorted(sticks)
    length_sorted_sticks = len(sorted_sticks)

    triangles = []

    for i in range(length_sorted_sticks):
        for j in range(length_sorted_sticks):
            for k in range(length_sorted_sticks):
                if i < j < k and i < k:
                    if (sorted_sticks[i] + sorted_sticks[j] > sorted_sticks[k]) and (
                            sorted_sticks[i] + sorted_sticks[k] >
                            sorted_sticks[j]) and (sorted_sticks[j] + sorted_sticks[k] > sorted_sticks[i]):
                        triangles.append([sorted_sticks[i], sorted_sticks[j], sorted_sticks[k]])

    if len(triangles) == 0:
        return [-1]
    return triangles[-1]


sticks = [1, 2, 3, 4, 5, 10]
maximumPerimeterTriangle(sticks)
a = maximumPerimeterTriangle(sticks)
print(a)
