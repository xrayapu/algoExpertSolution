# find the invert binary tree

#         1
  #    /    \
#     3      2 
#          /   \
#         5      9


# output
#         1
  #    /    \
#     2      3 
#   /   \
#  9     5     

def sol(tree):
  if not tree:
    return
  tree.left,tree.right=tree.right, tree.left
  sol(tree.left)
  sol(tree.right)
  return tree

# time O(n) | space O(d)
