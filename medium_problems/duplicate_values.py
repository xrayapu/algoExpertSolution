# type: 1
def sol(nums):
    p = nums
    p.sort()
    for i in range(len(p)):
        if p[i] == p[i + 1]:
            return p[i]
#time: O(nlogn) | space O(n)
#type:2

from collections import Counter
def sol(nums):  
    x = Counter(nums)
    for num, val in x.items():
        if val > 1:
            return num


#time O(n) | space O(n)
