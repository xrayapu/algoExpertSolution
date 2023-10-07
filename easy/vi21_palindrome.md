# type 1:
```python
def palindrome(char):
    temp = "".join(reversed(char))
    
    i = 0
    while i < len(char):
        if char[i] == temp[i]:  # char[j]:
            i += 1
            # j -= 1  # without temp
        else:
            return False
    return True
```
