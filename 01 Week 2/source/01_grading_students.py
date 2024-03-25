def gradingStudents(grades):
    for i in range(len(grades)):
        elem = grades[i]
        if elem >= 38:
            count = 0
            while elem % 5 != 0:
                elem += 1
                count += 1
            if count < 3:
                grades[i] = elem
    return grades


rounded_array = gradingStudents([4, 73, 67, 38, 33])
print(rounded_array)
