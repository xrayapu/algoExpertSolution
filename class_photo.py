def sol( arr1, arr2):
    arr1.sort()
    arr2.sort()
    i,j=0,0
    temp=0 
    if len(arr1) != len(arr2) : return False
    else:      
        if arr2[0] > arr1[0] :
            man =1
        else : man = 2
        while i< len(arr1) :
            if man ==1:
                if arr1[i] < arr2[j]:
                    temp +=1
                
            elif man==2 :
                if arr1[i] > arr2[j]:
                    temp +=1

            i+=1
            j+=1
            
        return temp == len(arr1)
    

# time O(nlogn) | space O(1)


# a=[5,1,3,4,6]
# b=[9,5,2,4,5]

# print(sol(a,b))
