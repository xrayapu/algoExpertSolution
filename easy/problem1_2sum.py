def sol(arr, tar):
    m = {}

    for num in arr:
        temp = tar - num
        if temp not in m:
            m[num] = temp

        else:
            return temp, num
