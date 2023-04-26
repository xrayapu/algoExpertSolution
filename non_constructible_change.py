def sol(arr):
    cost = 0
    i=0
    arr.sort()
    if arr[0]!= 1 : return 1
    else:
       while i <len(arr):
            if cost +1 < arr[i]:
               return cost +1
            else:
                cost += arr[i]

            i+=1
        
    return cost+1
