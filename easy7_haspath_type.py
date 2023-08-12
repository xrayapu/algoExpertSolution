# time O(n) and space O( n)



def sol(node, tar):
    ans = []
    cal(node, 0, ans)
    return ans


def cal(node, csum, ans):
    if not node:
        return
    csum = node.val + csum
    if node.left is None and node.right is None:
        ans.append(csum)
        return

    cal(node.left, csum, ans)
    cal(node.right, csum, ans)

# leetcode 112
# def cal(node, csum, ans):
#     if not node:
#         return
#     csum = node.val + csum
#     if node.left is None and node.right is None:
#         ans.append(csum)
#         return

#     cal(node.left, csum, ans)
#     cal(node.right,csum, ans)
# class Solution:
    
#     def hasPathSum(self, node: Optional[TreeNode], tar: int) -> bool:
#         #def sol(node, tar):
        
#         ans = []
#         cal(node, 0, ans)
#         for i in ans:
#             if i == tar:
#                 return True
#         return False
