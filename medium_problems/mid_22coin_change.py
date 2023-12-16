# minimum number of coin needed to create target value 

def sol(arr, tar):
    n=len(arr)
    t=[[float('inf')] * (tar+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,tar+1):
            if arr[i-1] >j:
                t[i][j]= t[i-1][j]

            else: 
                t[i][j] = min(t[i-1][j] , 1+ t[i][j- arr[i-1]])

    if t[n][tar] == float('inf'):
        return -1
    
    return t[n][tar]



#print(sol([1,2,4],6))
