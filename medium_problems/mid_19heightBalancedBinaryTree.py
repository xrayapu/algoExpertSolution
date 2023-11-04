# a tree is given , return true if it is balanced binary tree otherwise false.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# leaf node always balanced and it's height is 0.


"""
              3
           /   \
          4     2
        /  \   / \
       1   5  7   9      output => true
                 / \
                8  11 

             3
           /   \
          4     2
               / \
              7   9    output => false
                   \
                   11 

"""

def balancedTree(root):
    def sol(root):
        if not root:
          return [True, 0]
        left = sol(root.left)
        right= sol(root.right)
        balanced= left[0] and right[0] and abs(left[1] - right[1])<= 1
        return [balanced , 1+max(left[1], right[1])]

    return sol(root)[0]







    



