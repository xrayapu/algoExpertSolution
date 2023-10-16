# array of products [5,1,4,2]=>[8,40,10,20]


# using division 
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
