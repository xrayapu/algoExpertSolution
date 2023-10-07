# type 1(mycode):
```python
def palindrome(char):
    temp = "".join(reversed(char))
    
    i = 0
    while i < len(char):
        if char[i] == temp[i]:  
            i += 1
            
        else:
            return False
    return True
```
# type 2:
```python
def again(lets):
    i=0
    j=len(lets)-1
    while i<j:
        if lets[i] !=lets[j]:
            return False

        i+=1
        j-=1
    return True
```

##time O(n) | space O(1)
