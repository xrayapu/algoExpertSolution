# video 23: run length encoding : aaaavv -> a4v2
# given a string , just compress it with number
def sol(lets):
    arr = []
    cnt = 1
    for i in range(1, len(lets)):
        clet = lets[i]
        nlet = lets[i - 1]
        
        if clet != nlet:
            arr.append(nlet)
            arr.append(str(cnt))
            cnt = 0

        cnt += 1
    arr.append(lets[len(lets) - 1])
    arr.append(str(cnt))
    
    return "".join(arr)


# print(sol("1111av"))

# time O(n) | space O(n)
