# how to solve:
## using only sort function and just return the last 3 items
python :
```python
def sol(n):
    n.sort()

    return n[-3],n[-2],n[-1]
    
    
 ```
 
 ### time O(nlogn) | space O(1)
