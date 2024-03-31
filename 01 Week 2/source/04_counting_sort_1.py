def countingSort(arr):
    output_array = [0 for _ in range(100)]
    for elem in arr:
        output_array[elem] += 1

    return output_array


input_array = [1, 2, 3, 4, 5, 6]

arr_result = countingSort(input_array)
print(arr_result)
