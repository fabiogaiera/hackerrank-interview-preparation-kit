def pangrams(s):
    my_set = set()
    for elem in s:
        if elem.isalpha():
            my_set.add(elem.lower())

    result = len(my_set) == 26
    if result:
        return "pangram"
    else:
        return "not pangram"


is_pangram = pangrams('The quick brown fox jumps over the lazy dog')
print(is_pangram)
