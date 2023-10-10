# video 25 :
# return the 1st non-repeated character's index number.
# leetcode 387 same question


def sol(arr):
    import collections

    x = collections.Counter(arr)

    for idx in range(len(arr)):
        if x[arr[idx]] == 1:
            return idx

    return -1


# print(sol("abcdacf"))  # output 1
