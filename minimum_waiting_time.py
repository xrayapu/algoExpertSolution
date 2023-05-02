# minimum waiting time ! lesson 10
# time O(nlogn) | space O(1)
def sol(arr):
    time=0
    
    min_time=0
    arr.sort()
    for num in range(len(arr)-1):
        time += arr[num]                
        min_time +=time
        

                 
    return  min_time
