# # type: 1
# def sol(nums):
#     p = nums
#     p.sort()
#     for i in range(len(p)):
#         if p[i] == p[i + 1]:
#             return p[i]
# #time: O(nlogn) | space O(n)


# #type:2

from collections import Counter
def sol(nums):  
    x = Counter(nums)
    for num in range(len(nums)):
        if x[arr[num]]>1:
            return arr[num]

#time O(n) | space O(n)
# @ type 2 leetcode problem solutuion
