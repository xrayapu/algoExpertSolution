# longest peak
def sol(arr):
    long = 0
    i = 1
    while i < len(arr) - 1:
        ispeak = arr[i] > arr[i - 1] and arr[i] > arr[i + 1]
        if not ispeak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and arr[left] < arr[left + 1]:
            left -= 1

        hi = i + 2
        while hi < len(arr) and arr[hi] < arr[hi - 1]:
            hi += 1

        clong = hi - left - 1
        long = max(clong, long)
        i = hi

    return long


# a = [2, 1, 4, 7, 3, 2, 5]
# print(sol(a))
#time O(n)| space O(1)
