def birthday(s, d, m):
    length = 0  # equal to the m
    suma = 0
    count = 0
    left = 0
    for i in range(len(s)):
        suma += s[i]
        length += 1
        if length >= m:
            if suma == d:
                count += 1
            suma -= s[left]
            left += 1
            length -= 1

    return count


lst = [1, 2, 1, 3, 2]
birth_day = 3  # sum
birth_month = 2  # length
result = birthday(lst, birth_day, birth_month)
print(result)
