def sol(arr,tar):
    arr.sort()
    ans =[]
    
    for i in range(len(arr)-2):
        l=i+1
        r= len(arr)-1
        while l< r:
            total = arr[i]+arr[l]+arr[r]
            if total < tar:
                l+=1

            elif total > tar:
                r-=1
            else :
                ans.append([arr[i],arr[l],arr[r]])
                l+=1
                r-=1
    return ans

# a=[12,3,1,2,-6,5,-8,6]
# print(sol(a,0))


# time O(n^2) | space O(n)

#mid 1 in algoexpart

    
    
