# class Solution:
#     def jump(self, nums) -> int:
#         # if len(nums) == 1 and nums[0] == 0:
#         #     return 0
#         if len(nums) == 1:
#             return 0
#         def get_minimum_jump(idx, curr_min):
#             if idx >= len(nums)-1:
#                 return 0
#             for i in range(idx+1, idx+nums[idx]+1):
#                 curr_min = min(curr_min, 1 + get_minimum_jump(i, curr_min))
#             return curr_min
#         return get_minimum_jump(0, float('inf'))

# class Solution:
#     def jump(self, nums) -> int:
#         # we are already at the last index
#         if len(nums) == 1:
#             return 0
        
#         last_idx = len(nums) - 1
        
#         # the range of our possible jump
#         # if there is always a solution the first element has to be >= 1
#         min_reach = 1
#         max_reach = nums[0] # we can jump as far as it is allowed
        
#         jumps = 1
#         # while the last index is not within reach 
#         while not min_reach <= last_idx <= max_reach:
            
#             # we go through each element in our current reach
#             # and update the positions towards we can reach
#             # this is necessary due to the fact that there can be elemets that are 0
#             for i in range(min_reach, max_reach + 1):
#                 if nums[i] == 0:
#                     # from a 0 element we can only go there
#                     min_reach = i
#                 else:
#                     # from a non zero elements we can always advance 1 step
#                     min_reach = i + 1
                
#                 # we greedily update the max reach as far as we can
#                 max_reach = max(max_reach, i + nums[i])
                
#             jumps += 1
            
#         return jumps 

class Solution:
    def jump(self, nums) -> int:
        left = right = 0
        jumps = 0
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])
            left = right+1
            right = farthest
            jumps += 1
        return jumps

s = Solution()
example1 = [2,3,0,1,4]
example2 = [1,1,1,1]
print(s.jump(example2))
