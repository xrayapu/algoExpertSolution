# longest peak
def sol(arr):
    ans=0
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i]> arr[i+1]:
            left= right= i
            while left >0 and arr[left] >arr[left-1]:
                left-=1
            while right < len(arr)-1 and arr[right] > arr[right+1]: # right+1 <len(arr) , comment code is ok but takes much time ! 
                right+=1
            val=right-left+1 # idx number from up and 1 for idx start with 0
            ans= max(ans, val)
    return ans

# a = [2, 1, 4, 7, 3, 2, 5]
# print(sol(a))
#time O(n)| space O(1)
