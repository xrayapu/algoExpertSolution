# type 1 : time : O(n^2)|space O(n) 

## use string concatination 

```python 

def sol(arr):
    st =''
    for i in arr : # n times
        st = i + st # time O(n) per opartion 

    return st == arr
```

# type 2: time : O(n)| space O(n)
## use list only 
``` python
def sol (arr):
    nre=[]
    for i in reversed(range(len(arr))):
        # for i in range(len(n)-1, -1, -1) same as above
        nre.append(arr[i])   
        #print(nre, i) 
    return ''.join(nre) == arr
```
# type 3 : 2 pointer 
``` python
def sol(arr):
    left =0
    right = len(arr)-1
    while left < right:
        if arr[left] != arr[right] :
            return False
        left +=1
        right -=1

    return True

  ```
 # time O(n) | space O(1)
    


