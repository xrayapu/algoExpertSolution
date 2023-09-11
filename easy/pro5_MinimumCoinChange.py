def sol(arr):
    arr.sort()
    make = 0
    if arr[0] != 1:
        return 1
    else:
        make += arr[0]  
        for idx in range(len(arr)):
            if make < arr[idx]:
                return make
            else:
                
                make += arr[idx]

    return make
