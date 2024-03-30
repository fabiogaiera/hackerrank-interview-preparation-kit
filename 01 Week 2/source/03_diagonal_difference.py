#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    length = len(arr)

    # left to right diagonal
    sum_left_right_diagonal = 0
    i = 0
    while i <= length - 1:
        sum_left_right_diagonal += arr[i][i]
        i += 1

    # right to left diagonal
    sum_right_left_diagonal = 0
    i = 0
    j = length - 1
    while j >= 0:
        sum_right_left_diagonal += arr[i][j]
        i += 1
        j -= 1

    return abs(sum_left_right_diagonal - sum_right_left_diagonal)


number = diagonalDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(number)
