def lonelyinteger(a):
    my_dict = {}
    for elem in a:
        if elem not in my_dict:
            my_dict[elem] = 1
        else:
            my_dict[elem] += 1

    for elem in my_dict:
        if my_dict[elem] == 1:
            return elem
    return None


el = lonelyinteger([1, 2, 3, 4, 3, 2, 1])
print(el)
