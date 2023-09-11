# you are given some coin , return the minimum coin that can't created by all of this coins ! 

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
# a=[1, 4, 1] output: 3
# a=[1,1,3] output:6
# a=[1,2,3] output: 7
# a= [5,7,1,3,1,2,22] output: 20
# print(sol(a))
