def permute(nums):
    result = []

    def backtrack(path, nums):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            backtrack(path + [nums[i]], nums[:i] + nums[i + 1:])

    backtrack([], nums)
    return result


def check_relationship_between_lists(k, list_a, list_b):
    for i in range(len(list_a)):
        if list_a[i] + list_b[i] < k:
            return False
    return True


def twoArrays(k, A, B):
    permutations_list_a = permute(A)
    permutations_list_b = permute(B)

    for elem_a in permutations_list_a:
        for elem_b in permutations_list_b:
            if check_relationship_between_lists(k, elem_a, elem_b):
                return "YES"
    return "NO"


k = 10
lst_A = [2, 1, 3]
lst_B = [7, 8, 9]
print(twoArrays(k, lst_A, lst_B))
