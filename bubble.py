def sol(arr):
    swap =False
    counter =0
    while not swap:
        swap = True 
        for i in range(len(arr)-1- counter):            
            if  arr[i] > arr[i+1]:
                arr[i],arr[i+1]=arr[i+1], arr[i]
                swap= False

        counter +=1

    return arr
a=[8,4,6,3,1,5,7]
print(sol(a))

# time O(n^2) | space O(1)

# lesson 18
