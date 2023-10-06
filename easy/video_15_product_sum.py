def sol(arr , mul =1):
    sum = 0
    for num in arr:
        if type(num) is list:
            sum += sol(num , mul+1)  # handles the new list part . 

        else: sum +=num 

    return sum * mul # main part 

# a=[5,2,[7,-1],3,[6,[-13,8],4]]

# print(sol(a))

# time O(n) every elements + recursive elements | space O(d) largest depth of the subarray
