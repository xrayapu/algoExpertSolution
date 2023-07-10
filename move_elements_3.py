# leetcode move zeros type problem 
# type 1
def sol(arr,tar):
    arr.sort()
    r= len(arr)-1
    l=0
    while (l<r):
       
        if  arr[l] != tar :
            l+=1

        elif arr[l] == tar :
            arr[l],arr[r]= arr[r],  arr[l]
            l+=1
            r-=1
    return arr


# time O(nlogn) | space O(1) 
# if order, time don't matter.



# a= [0,1,0,3,12]
# print(sol(a,0)) 




## optimal solution 



#type 2

def move_zeros(arr, tar):
    n=len(arr)
    i=0
    for num in arr:
        if num !=tar:
            arr[i] = num
            i+=1
    
    for k in range (i, n):
        arr[k]=tar

    return arr 
# a= [2,1,2,2,3,4,2]
# print(move_zeros(a, 2)) 

# time O(n)| space O(1)
    


