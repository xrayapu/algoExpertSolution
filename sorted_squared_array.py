#solve 1: brute force
def sol(arr):
    ar=[]
    for val in arr:      
        val= val **2
        ar.append(val)

    ar.sort()
    return ar
    




# solve 2 : 2 pointer for time efficience 
def sol( arr):
    n_ar=[ 0 for _ in arr] # new jinis sikhlam 
    low, hi= 0,len(arr)-1
    i=hi
    while ( low <= hi):
        if abs(arr[low]) > abs(arr[hi]):
            n_ar[i] = arr[low] ** 2
            low +=1
        else :
            n_ar[i] = arr[hi] **2
            hi -=1
            
        i-= 1
    return n_ar
