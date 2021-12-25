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

def update_segment_tree_sum(pos, range_low, range_high, index, diff, segment_tree):
    if range_low > index or range_high < index:
        return
    segment_tree[pos]+=diff
    if range_low != range_high:
        mid = (range_low + range_high)//2
        update_segment_tree_sum(2*pos+1, range_low, mid, index, diff, segment_tree)
        update_segment_tree_sum(2*pos+2, mid+1, range_high, index, diff, segment_tree) 
    
    
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segment_tree = self._create_segment_tree(nums)
    
    def _create_segment_tree(self, nums):
        sn = 2*(2**math.ceil(math.log2(len(nums)+1)))
        segment_tree = [0 for _ in range(sn-1)]
        construct_segment_tree_sum(nums, segment_tree, 0, len(nums)-1, 0)
        return segment_tree
        
    def update(self, index: int, val: int) -> None:
        segment_tree = self.segment_tree
        diff = val - self.nums[index]
        self.nums[index] = val
        update_segment_tree_sum(0, 0, len(self.nums)-1, index, diff, segment_tree)
        
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


num_arr = NumArray([0,9,5,7,3])
print(num_arr.sumRange(4,4))
print(num_arr.sumRange(2,4))
print(num_arr.sumRange(3,3))
print(num_arr.update(4,5))
print(num_arr.update(1,7))
print(num_arr.update(0,8))
print(num_arr.sumRange(1,2))
print(num_arr.update(1,9))
print(num_arr.sumRange(4,4))
print(num_arr.update(3,4))
