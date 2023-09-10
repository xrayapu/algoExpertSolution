def sol(arr):
    ans = []
    for num in arr:
        num = num * num
        ans.append(num)

    ans.sort()
    return ans

# time O(nlogn) | space O(n)
  
# print(sol([-3, 1, 5]))



# optimal solution , if you get sorted array then you should try to solve it in O(n) time.

def sol(arr):
    i = 0
    j = len(arr) - 1
    ans = [0 for _ in arr] # created same array of length of the arr, but it is filled with 0.
    # print(len(ans))
    for idx in reversed(range(len(arr))):
        small = arr[i]
        large = arr[j]
        if abs(small) > abs(large):
            ans[idx] = small**2
            i += 1
        else:
            ans[idx] = large**2
            j -= 1

    return ans

# time O(n) | space O(n)
print(sol([-7, -3, 1, 5]))
