def birthday(s, d, m):
    ways = 0
    i = 0
    while i < len(s):
        suma = 0
        j = i
        while j < m and j < len(s):
            suma += s[j]
            j += 1
        if suma == d:
            ways += 1
        m += m
        i = j

    return ways


lst = [2, 2, 1, 3, 2]
birth_day = 4
birth_month = 2
result = birthday(lst, birth_day, birth_month)
print(result)
