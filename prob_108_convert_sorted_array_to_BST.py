from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start, end = 0, len(nums)-1
        def recursive_solution(start, end):
            if start > end:
                return None
            
            middle = (start+end)//2
            
            root_node = TreeNode(nums[middle])
            
            root_node.left = recursive_solution(start, middle-1)
            root_node.right = recursive_solution(middle+1, end)
            
            return root_node
        return recursive_solution(start, end)

test_case = [-10,-3,0,5,9]
s = Solution()
print(s.sortedArrayToBST(test_case))
