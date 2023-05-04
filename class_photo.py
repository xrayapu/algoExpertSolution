# type 1

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

# type 2

def sol(ar1,ar2):
    ar1.sort()
    ar2.sort()
    check = 'red' if ar1[0] > ar2[0] else 'blue'
    if len(ar2) != len(ar1): return False
    else:
        i=1
        while(i < len(ar2)) :
            if check == 'red':
                if ar1[i] <= ar2[i]:
                    return False
                
            else :
                if ar1[i] >= ar2[i]:
                    return False
                
            i+=1

    return True
