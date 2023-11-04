# find the sucessor of the binary tree 
# just traverse the tree inorder fasion ! and give the next element from the array !!!

def sol(tree, tar):
    ans = []

    def inO(tree):
        if not tree:
            return
        inO(tree.left)
        ans.append(tree.val)
        inO(tree.right)

        return ans

    inO(tree)

    if tar in ans:
        idx = ans.index(tar)
    else:
        return None
        
    
    if idx == len(ans) - 1:
        return None
    else:
        return ans[idx + 1]


# time O(n) | space O(n)> list fact !!!
