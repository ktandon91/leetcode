# class Solution:
#     def canJump(self, nums) -> bool:
#         print(nums)
#         print(nums[:-1])
#         for num in reversed(nums[:-1]):
#             print(num)
        
        # def can_jump(idx):
        #     if idx == len(nums) - 1:
        #         return True
        #     if idx >= len(nums) or nums[idx] == 0:
        #         return False
        #     val = nums[idx]
        #     for i in range(val, 0, -1):
        #         result = False or can_jump(idx+i)
        #         if result == True:
        #             break
        #     return result
        
        # return can_jump(0)

# class Solution:
#     def canJump(self, nums) -> bool:
#         if len(nums) == 1:
#             return True
        
#         answer = True
#         needed = 1

#         for num in reversed(nums[:-1]):
#             if num < needed:
#                 needed += 1
#                 answer = False
#             else:
#                 needed = 1
#                 answer = True
                
#         return answer

# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         n=len(nums)
#         opt=[False]*len(nums)

#         opt[n-1]=True

#         index=n-1

#         for i in range(n-2,-1,-1):
#             if(nums[i]+i>=index):
#                 index=i
#                 opt[i]=True


#         return(opt[0])
class Solution:
    def canJump(self, nums) -> bool:
        c, maxi = 0,0
        for r,x in enumerate(nums):
            maxi = max(maxi, x + r) 
            if r == c:
                c = maxi
        return c+1>=len(nums)
s = Solution()
example1 = [3,2,2,0,4]
print(s.canJump(example1))
