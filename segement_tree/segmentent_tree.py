# Conceptually Segment tree is a binary tree used for range query
# Physically Segment tree can be represented as a python list
# Given a of nums of size n. It's Segment tree list will have 
#  
import math

def construct_tree(input, segment_tree, low, high, pos):
    """Returns the segment_tree from a given input list.

        :param input: input python list, which has to be converted to segment
                    tree for range queries
        :param segment_tree: list with float('inf') elements to be converted to segment tree.
        :param low: to keep track of low index of input list
        :param high: to keep track of last index of input list
        :param pos: index to keep track while building segment tree 
    """
    if low == high:
        segment_tree[pos] = input[low]
        return input[low]
    mid = (low+high)//2  
    
    segment_tree[pos] = min(construct_tree(input, segment_tree, low, mid, 2*pos+1), 
                        construct_tree(input, segment_tree, mid+1, high, 2*pos+2))
    return segment_tree[pos]

def min_range_query(segment_tree, qlow, qhigh, low, high, pos):
    """Returns the range_query from a given interval

        :params segment_tree: tree on which range query will be performed
        :params qlow: lower range
        :params qhigh: higher range
        :params low: lower index of orginal input list
        :params high: higher index of original input list
        :params pos: pos to keep track of element of segment_tree

        Case 1: Total Overlap
        Case 2: No Overlap
        Case 3: Partial Overlap
    """
    if qlow <= low and qhigh>=high:
        return segment_tree[pos]
    if qlow > high or qhigh < low:
        return float('inf')
    mid = (low+high)//2
    range_value = min(min_range_query(segment_tree, qlow, qhigh, low, mid, 2*pos+1),
                    min_range_query(segment_tree, qlow, qhigh, mid+1, high, 2*pos+2))

    return range_value

def construct_segment_tree_sum(input, segment_tree, low, high, pos):
    if low == high:
        segment_tree[pos] = input[low]
        return input[low]
    mid = (low+high)//2  
    segment_tree[pos] = construct_segment_tree_sum(input, segment_tree, low, mid, 2*pos+1) + \
                        construct_segment_tree_sum(input, segment_tree, mid+1, high, 2*pos+2)
    return segment_tree[pos]

def sum_range_query(segment_tree, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh>=high:
        return segment_tree[pos]
    if qlow > high or qhigh < low:
        return 0
    mid = (low+high)//2
    range_value = sum_range_query(segment_tree, qlow, qhigh, low, mid, 2*pos+1) + \
                    sum_range_query(segment_tree, qlow, qhigh, mid+1, high, 2*pos+2)

    return range_value

def update_segment_tree_sum(pos, range_low, range_high, index, diff, segment_tree):
    if range_low > index or range_high < index:
        return
    segment_tree[pos]+=diff
    if range_low != range_high:
        mid = (range_low + range_high)//2
        update_segment_tree_sum(2*pos+1, range_low, mid, index, diff, segment_tree)
        update_segment_tree_sum(2*pos+1, mid+1, range_high, index, diff, segment_tree) 


def update_index(idx, val, input, segment_tree):
    diff = val - input[idx]
    update_segment_tree_sum(0, 0, len(input)-1, idx, diff, segment_tree)

def main():
    # nums = [-1,2,4,0]
    # n = len(nums)
    # segment_tree = [float('inf') for _ in range(2*n-1)]
    # construct_tree(nums, segment_tree, 0, len(nums)-1, 0)
    # print(segment_tree)
    # value = min_range_query(segment_tree, 1,3,0,3,0)
    # print(value)
    nums = [1,2,5,6,7,9]
    n = len(nums)
    sn = 2*(2**math.ceil(math.log2(n+1)))
    segment_tree = [0 for _ in range(sn-1)]
    construct_segment_tree_sum(nums, segment_tree, 0, n-1, 0)
    print(segment_tree)
    update_index(3,14, nums, segment_tree)
    print(segment_tree)
main()
