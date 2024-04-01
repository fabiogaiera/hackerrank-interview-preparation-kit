def twoArrays(k, A, B):
    A = sorted(A)
    B = list(reversed(sorted(B)))
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


k = 10
lst_A = [2, 1, 3]
lst_B = [7, 8, 9]
print(twoArrays(k, lst_A, lst_B))
