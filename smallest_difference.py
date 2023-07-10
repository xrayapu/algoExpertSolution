def sol(arr1,arr2):
    arr1.sort()
    arr2.sort()
    small= float('inf')   
    pair= []
    l=0
    r=0    
    while l<len(arr1) and r< len(arr2) :
        num1=arr1[l]
        num2=arr2[r]        
        diff= abs(num1-num2)
        small= min(diff, small)
        if  num1< num2:            
            l+=1
        elif num1 > num2 :
            r+=1
        else:
            return [num1,num2]
        if small == diff :
            pair = [num1, num2]
    return pair


#time O(nlogn + mlogm) | space O(1)

# a=[-1,5,17,20,28] 
# b=[15,17,134,135,26]
# print(sol(a,b))
    
            
