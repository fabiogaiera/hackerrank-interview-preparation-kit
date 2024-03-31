def marsExploration(s):
    count = 0
    length = len(s)
    for i in range(0, length, 3):

        substr = s[i:i + 3]

        if substr[0] != 'S':
            count += 1
        if substr[1] != 'O':
            count += 1
        if substr[2] != 'S':
            count += 1

    return count


counter = marsExploration('SOSTOT')
print(counter)
