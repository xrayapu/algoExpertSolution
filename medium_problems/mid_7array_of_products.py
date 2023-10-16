# array of products [5,1,4,2]=>[8,40,10,20]


# using division if input has no 0
# type 1: time O(n) | space O(1)

def sol(arr):
    ans = 1
    for i in arr:
        ans *= i

    for i in range(len(arr)):
        arr[i] = ans // arr[i]

    return arr

# brute force
# type 2 : time O(n^2) | space O(n)


def sol1(arr):
    p = []
    for i in range(len(arr)):
        ans = 1
        for j in range(len(arr)):
            if i != j:
                ans *= arr[j]

        p.append(ans)

    return p


# type 3: time O(n) | space O()

#left=[1,5,5,20]
#right=[8,8,2,1]
# ans=[8,40,10,20]
def sol(arr):
    ans = [1] * len(arr)
    left = [1] * len(arr)
    right = [1] * len(arr)
    leftval = 1
    for i in range(len(arr)):
        left[i] = leftval
        leftval *= arr[i]
    ritval = 1
    for i in reversed(range(len(arr))):
        right[i] = ritval
        ritval *= arr[i]
    for i in range(len(arr)):
        ans[i] = left[i] * right[i]

    return ans
