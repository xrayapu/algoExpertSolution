# easy_> lesson 6

# recursion
# time O(logn) | space O(n)


def algo(root, tar):
    return sol(root, tar, closeval=float("inf"))


def sol(root, tar, closeval):
    if not root:
        return closeval
    if abs(tar - closeval) > abs(tar - root.val):
        closeval = root.val

    elif root.val > tar:
        return sol(root.left, tar, closeval)

    elif root.val < tar:
        return sol(root.right, tar, closeval)
    else:
        return closeval

# iterative implementation:
# 
#  time O(n)| space O(1) 
def sol(root, tar, closeval):
    close = root
    while close is not None:
        if abs(tar - closeval) > abs(tar - close.val):
            closeval = close.val

        elif close.val > tar:
            closeval = close.left

        elif root.val < tar:
            closeval = close.right

        else:
            break

    return closeval
