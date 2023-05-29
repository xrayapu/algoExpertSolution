# binary search using iterative way

### implementation
python :
```python
def sol(arr, tar):
    
    i,j=0, len(arr)-1
    while i<= j :
        mid = (i+j)//2
        if arr[mid] ==tar:
            return mid
        elif arr[mid] > tar:
            j = mid -1

        else : i = mid +1

    return -1
```

#  time O(logn) and space O(1)
