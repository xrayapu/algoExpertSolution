# leetcode 104 maximum depth of the bst tree
def sol(tree):
  if not tree:
    return 0
  left=sol(tree.left)
  right=sol(tree.right)
  return 1+max(left,right)


