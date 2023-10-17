# merge overlapping intervals
def sol(arr):
    arr.sort()
    ans = []

    inta = arr[0]
    
    ans.append(inta)
    
    for next in arr:
        _, ans0 = inta

        ans1, ans2 = next
       
        if ans0 >= ans1:
            inta[1] = max(ans0, ans2)
        else:
            inta = next
            ans.append(inta)
    return ans


# print(sol([[1, 3], [2, 6], [8, 10], [15, 18]])) => [[1,6],[8,10],[15,18]]
#time O(nlogn) and space O(n)
