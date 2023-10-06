# how to solve:
## using only sort function and just return the last 3 items
python :
```python
def sol(n):
    n.sort()
    

    return [n[-3],n[-2],n[-1]]

    
    
 ```
## use append option 
python:
```python
def sol(arr):
    arr.sort()
    ans = []
    ans.append(arr[-3])
    ans.append(arr[-2])
    ans.append(arr[-1])
    return ans

```
 
 ### time O(nlogn) | space O(1)
