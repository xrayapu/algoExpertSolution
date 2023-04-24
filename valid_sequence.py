def sol(arr, tar):
    i,j=0,0
    while( i< len(arr) and j < len(tar)):
        if arr[i] == tar[j]:
            i+=1
            j+=1
        else :
            i+=1
    return j== len(tar)
    


