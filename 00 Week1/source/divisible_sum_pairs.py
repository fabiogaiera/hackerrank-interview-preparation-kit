def divisible_sum_pairs(n, k, ar):
    count_pairs = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                if (ar[i] + ar[j]) % k == 0:
                    count_pairs += 1
    return count_pairs


divisible_sum_pairs(6, 5, [1, 2, 3, 4, 5, 6])
