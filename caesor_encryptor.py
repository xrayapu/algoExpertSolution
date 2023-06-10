# using ord function 
def sol(sr, n):
    arr= [] # ''
    if n > 26:
        n = n % 26 # for edge case 
    for i in sr:       
        nm = ord(i)        
        nm +=n
        if nm > 122:
            nm = 96 + nm %122           
        arr += chr(nm)
        
    return "".join(arr)
 #return arr
# time O(n) | space O(n)

# a='yz' 
# n=2
# print(sol(a,n))

