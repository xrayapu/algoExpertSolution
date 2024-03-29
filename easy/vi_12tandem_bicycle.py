# def sol(red, blue, type):
#     red.sort()
#     blue.sort()
#     i=0
#     j=len(red)-1
#     temp=0
#     if type:
        
#         for num in red:
#             it= max(num, blue[j])
#             temp += it
#             #print(it, num, blue[j] ,i ,j)
#             #i+=1
#             j-=1

#         return temp
#     else : 
#         for num in red:
#             it= max(num, blue[i])
#             temp += it
#             #print(it, num, blue[j] ,i ,j)
#             i+=1
            

#         return temp 

# long code(by fully me )

def sol(red, blue, type):
    red.sort()
    if type:
        blue.sort(reverse=True)
    else: blue.sort()
    i=0
    
    temp=0
    
        
    for num in red:
        it= max(num, blue[i])
        temp += it
        
        i+=1
        
    return temp
    
# a=[5,5,9,2,3]
# b=[2,3,1,7,6]
# t=False

# print(sol(a,b,t))

# time: O(nlogn) | space: O(1)

def maxspeed(arr1, arr2, speed):
    total = 0
    arr1.sort()
    if speed:
        arr2.sort(reverse=True)
    else:
        arr2.sort()
    for idx in range(len(arr2)):
        
        temp = max(arr1[idx], arr2[idx])
        total += temp
        

    return total
# time: O(nlogn) | space: O(1)

    

