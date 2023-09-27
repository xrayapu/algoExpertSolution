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

    if root.val > tar:
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

# full code

# class node:
#     def __init__(self, val):
#         self.right = None
#         self.left = None
#         self.info = val


# def insert(tree, val):
#     if not tree:
#         return node(val)
#     if tree.info > val:
#         tree.left = insert(tree.left, val)

#     else:
#         tree.right = insert(tree.right, val)

#     return tree


# def helper(root, tar, comp):
#     if not root:
#         return comp
#     if abs(tar - comp) > abs(tar - root.info):
#         comp = root.info
#     if root.info == tar:
#         return comp
#     elif root.info > tar:
#         return helper(root.left, tar, comp)
#     else:
#         return helper(root.right, tar, comp)


# def sol(root, tar):
#     return helper(root, tar, comp=float("inf"))


# tree = node(10)

# tree = insert(tree, 5)
# tree = insert(tree, 2)
# tree = insert(tree, 5)
# tree = insert(tree, 1)
# tree = insert(tree, 15)
# tree = insert(tree, 13)
# tree = insert(tree, 22)
# tree = insert(tree, 14)

# print(sol(tree, 12))
