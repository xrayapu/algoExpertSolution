# valid sequence , algo expert easy-2
def sol(arr, tar):
    i, j = 0, 0
    ans = []
    while i < len(arr) and j < len(tar):
        if arr[i] == tar[j]:
            ans.append(arr[i])
            i += 1
            j += 1

        else:
            i += 1

    return ans == tar


# print(sol([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 12]))

# time O(n) | space O(1)
