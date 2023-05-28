# fibonacci number
# naive recursion
# def sol(n):
#     if n==2: return 1
#     elif n==1: return 0
#     else: return sol(n-1) +sol(n-2)

# a= 11
# print(sol(a))

# time : O(2^n) | space : O(n)

# def sol(n):
#     here= {1:0,2:1}
#     if n in here:
#         return here[n]
#     else: 
#         here[n] = sol(n-1) +sol(n-2)
#         return here[n]
    
# a =40
# print(sol(a))

# time : O(n) | space O(n) using hash table slow for call stack memory

def sol(n):
    arr=[0,1]
    temp=3
    while temp <=n:
        it= arr[0] + arr[1]
        arr[0]= arr[1]
        arr[1] = it
        temp +=1
        # print(it , arr[0], arr[1],temp) >> temp over hobe jodio condition break down er jono ! 

    return arr[1] if n > 1 else arr[0] # eade case n=1

print(sol(110))

# [0,1]
