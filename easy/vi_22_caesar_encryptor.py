# using ord function 
def sol(letter, n):
    arr= [] # ''
    n = n % 26 # for edge case 
    for num in letter:       
        new = ord(num) + key
        if new <=122:
            arr.append(chr(new)
        else :
            new = 96 + new %122
            arr.append(chr(new))
            
        
        
    return "".join(arr)
 #return arr
# time O(n) | space O(n)

# a='yz' 
# n=2
# print(sol(a,n))

