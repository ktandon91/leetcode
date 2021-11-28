# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        q = []
        result.append([root.val])
        q.append(root)
        q2, ans = [], []
        while q:
            node = q.pop(0)
            if node.left is not None:
                q2.append(node.left)
                ans.append(node.left.val)
            if node.right is not None:
                q2.append(node.right)
                ans.append(node.right.val)
            if not q  and q2:
                q = q2[:]
                result.append(ans)
                ans, q2 = [], []
        return result
    