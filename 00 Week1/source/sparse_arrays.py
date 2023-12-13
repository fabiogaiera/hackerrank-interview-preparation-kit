def matching_strings(strings, queries):
    output = []
    for elem in queries:
        count = 0
        for string in strings:
            if elem == string:
                count += 1
        output.append(count)
    return output


s = ['ab', 'ab', 'abc']
q = ['ab', 'abc', 'bc']

lst = matching_strings(s, q)
print(lst)
