import math
from typing import List

def construct_segment_tree_sum(inp, segment_tree, low, high, pos):
        if low == high:
            segment_tree[pos] = inp[low]
            return inp[low]
        mid = (low+high)//2  
        segment_tree[pos] = construct_segment_tree_sum(inp, segment_tree, low, mid, 2*pos+1) + \
                            construct_segment_tree_sum(inp, segment_tree, mid+1, high, 2*pos+2)
        return segment_tree[pos]

    
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segment_tree = self._create_segment_tree(nums)
    
    def _create_segment_tree(self, nums):
        sn = 2*(2**math.ceil(math.log2(len(nums)+1)))
        segment_tree = [0 for _ in range(sn-1)]
        construct_segment_tree_sum(nums, segment_tree, 0, len(nums)-1, 0)
        return segment_tree
    
    def sumRange(self, left: int, right: int) -> int:
        segment_tree = self.segment_tree
        def sum_range_query(qlow, qhigh, low, high, pos):
            if qlow <= low and qhigh>=high:
                return segment_tree[pos]
            if qlow > high or qhigh < low:
                return 0
            mid = (low+high)//2
            range_value = sum_range_query(qlow, qhigh, low, mid, 2*pos+1) + \
                            sum_range_query(qlow, qhigh, mid+1, high, 2*pos+2)

            return range_value
        range_value = sum_range_query(left, right, 0, len(self.nums)-1, 0)
        return range_value


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
