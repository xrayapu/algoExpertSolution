# does it satisfy bst properties? 

# time O(n) , n is all the node| space O(d),d is the length of the tree 
#leetcode type ! 
def bst_tree(node):
    return bst(node, float('-inf'), float('inf'))

def bst(node,minval, maxval):
    if not node:
        return True
    if node.val <= minval or node.val >=maxval: 
        return False
    left_tree= bst(node.left, minval, node.val)
    right_tree=bst(node.right,node.val, maxval)

    return left_tree and right_tree

