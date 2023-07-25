# tree traversal history
# inorder, postorder, preorder
class node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


def postorder(val):
    if val is not None:
        postorder(val.left)
        postorder(val.right)
        print(val.data, end=" ")


root = node("f")
root.left = node("x")
root.right = node("g")
root.left.left = node("a")
root.left.right = node("d")
root.left.right.left = node("c")
root.left.right.right = node("e")
root.right.right = node("i")
root.right.right.left = node("h")

preorder(root)
print("")
inorder(root)
print("")
postorder(root)


