 #mid -4 monotonic array
# tring my code : done ! yep big claps to me !!!


def helper(num1, arr):
    for idx in range(1, len(arr)):
        num2 = arr[idx]
        if num1 != num2:
            return num2
    return True


def sol(arr):
    num1 = arr[0]
    top = 1
    num2 = helper(num1, arr)
    # used for [1,1,1,1] this type situation and if not >> [1,1,1,3,4] gives 3 and helping in the calculation
    if num2 == bool:
        return True
    else:
        diff = num1 - num2
       
        if diff > 0:
            for i in range(1, len(arr)):
                if arr[i] < arr[i - 1] or arr[i] == arr[i - 1]:
                    top += 1
                else:
                    return False

        else:
            for i in range(1, len(arr)):
                if arr[i] > arr[i - 1] or arr[i] == arr[i - 1]:
                    top += 1
                else:
                    return False

    return True  # return top == len(arr)


# a = [2, 2, 2, 2, 1, 3]
# print(sol(a))


# time O(n) | space O(1) #leetcode896
