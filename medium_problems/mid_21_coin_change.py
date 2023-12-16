# how many ways to crate target value

def sol(arr, tar):
    n=len(arr)
    t=[[0] * (tar+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = 1

    for i in range(1,n+1):
        for j in range(1,tar+1):
            if arr[i-1] >j:
                t[i][j]= t[i-1][j]

            else: 
                t[i][j] = t[i-1][j] +  t[i][j- arr[i-1]]

  
    
    return t[n][tar]



#print(sol([1,2,4],6)) output: 6

#1+1+1+1+1+1
# 2+2+2
#4+2            they are the ways, total number is 6
#4+1+1
#2+2+1+1
#2+1+1+1+1

# time O(n*tar) | space O(n*tar)
