def sol(arr , mul =1):
    sum0 = 0
    for num in arr:
        if type(num) is list:
            sum0 += sol(num , mul+1) 

        else: sum0 +=num 

    return sum0 * mul

a=[5,2,[7,-1],3,[6,[-13,8],4]]

print(sol(a))

# time O(n) | space O(d)
