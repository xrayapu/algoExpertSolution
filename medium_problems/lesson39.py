# largest value in the tree 

# time O(n) | space O(n)

def it(node, t):
    def tree_trvrsal(node):
        if not node:
            return

        tree_trvrsal(node.left)
        ans.append(node.val)
        tree_trvrsal(node.right)

        return ans

    ans = []
    tree_trvrsal(node)
    
    return ans[-t ]
