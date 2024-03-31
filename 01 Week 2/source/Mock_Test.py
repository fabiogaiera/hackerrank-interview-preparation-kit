def reverse_row(matrix, row):
    max_index = len(matrix) - 1
    for i in range(len(matrix) // 2):
        aux = matrix[row][i]
        matrix[row][i] = matrix[row][max_index]
        matrix[row][max_index] = aux
        max_index -= 1


def reverse_col(matrix, col):
    max_index = len(matrix) - 1
    for i in range(len(matrix) // 2):
        aux = matrix[i][col]
        matrix[i][col] = matrix[max_index][col]
        matrix[max_index][col] = aux
        max_index -= 1


def flippingMatrix(matrix):
    result = 0
    length_matrix_top_left = len(matrix) // 2

    return result


input_matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]

total = flippingMatrix(input_matrix)

# print(total)

reverse_row(input_matrix, 0)
print(input_matrix)
