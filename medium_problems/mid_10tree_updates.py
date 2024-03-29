# bst insert, search, delete

# tried to learn from programiz

# i got it at last , faceing some staggle but atlast at search i can see the subtree of searched value! 
class node:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.data = val


def minval(node):
    while node.left is not None: # while not node.left(same)
        return node.left


def inorder(root):
    if root is not None: # if not root
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def insert(root, val):
    if not root:
        return node(val)
    if root.data > val:
        root.left = insert(root.left, val)

    else:
        root.right = insert(root.right, val)

    return root


def search(root, val):
    if not root:
        return -1
    if root.data == val:
        # print("found", root.data)

        inorder(root)

    elif root.data > val:
        root.left = search(root.left, val)
    else:
        root.right = search(root.right, val)


def delete(root, val):
    if not root:
        return
    if root.data > val:
        root.left = delete(root.left, val)

    elif root.data < val:
        root.right = delete(root.right, val)

    else:
        if root.left is None: # if not root.left
            temp = root.right
            root = None
            return temp
        elif root.right is None: # if not root.right
            temp = root.left
            root = None
            return temp
        else:
            temp = minval(root.right)
            root.data = temp.data # root.data = temp
            delete(root.right, temp.data) # root.right = delete(root.right, temp)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=" ")
inorder(root)

print("\nDelete 11")
root = delete(root, 11)
print("Inorder traversal: ", end=" ")
inorder(root)
print("\n")
search(root, 6)
