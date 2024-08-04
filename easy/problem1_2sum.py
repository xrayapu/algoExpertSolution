#type 1:
def sol(arr, tar):
    m = {}

    for num in arr:
        temp = tar - num
        if temp not in m:
            m[num] = temp

        else:
            return temp, num

# time O(n) | space O(n)

#type 2:

def sol(arr, tar):
    arr.sort() # sort it
    i,j=0,len(arr)-1
    while i <j: # just 1st and last compaire !
        it=arr[i]+arr[j]
        if it < tar: # if it is smaller then target we just move i
            i+=1
        elif it> tar: # if it is greater then target we just move j
            j-=1
        else: # target= sum of 2 number
            return [arr[i], arr[j]]
        
    return [-1,-1]
    
# time o(nlogn) | space O(1)
print(sol([1,7,3,10],10))
