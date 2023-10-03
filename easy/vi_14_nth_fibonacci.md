# fibonacci number
## naive recursion
```python
 def sol(n):
     if n==2: return 1
     elif n==1: return 0
     else: return sol(n-1) +sol(n-2)
```
## time : O(2^n) | space : O(n)

## 2nd approach using hashmaps :

```python
def sol(n):
    here= {1:0,2:1}
    if n in here:
        return here[n]
    else: 
        here[n] = sol(n-1) +sol(n-2)
        return here[n]
```    
## time : O(n) | space O(n) 

## iterative approach
```python
def sol(n):
    arr=[1,1]
    temp=3
    while temp <=n:
        it= arr[0] + arr[1]
        arr[0]= arr[1]
        arr[1] = it
        temp +=1
        #  temp over hobe jodio condition break down er jono ! 

    return arr[1] if n >= 1 else 0 

```

# time O(n) | space O(1)
