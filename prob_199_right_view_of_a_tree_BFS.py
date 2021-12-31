# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideViewMyVersion(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        q = []
        q.append(root)
        nodes_left_in_layer = 1
        nodes_in_next_layer = 0
        layers = []
        result = []
        while q:
            node = q.pop(0)
            result.append(node.val)    
            
            if node.right is not None:
                q.append(node.right)
                nodes_in_next_layer+=1
            if node.left is not None:
                q.append(node.left)
                nodes_in_next_layer+=1
            
            nodes_left_in_layer-=1
            if nodes_left_in_layer == 0:
                nodes_left_in_layer = nodes_in_next_layer
                nodes_in_next_layer = 0
                layers.append(result)
                result = []
        result = []    
        for layer in layers:
            result.append(layer[0])
        return result
    
    def rightSideView(self, root):
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view
