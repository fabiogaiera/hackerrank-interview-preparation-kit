def sockMerchant(n, ar):

    dct = {}
    pairs = 0

    for elem in ar:
        if elem in dct:
            dct[elem] += 1
        else:
            dct[elem] = 1

    for value in dct.values():
        pairs += value // 2

    return pairs


ar = [1, 2, 1, 2, 1, 3, 2]
n = 7

p = sockMerchant(7, ar)
print(p)
