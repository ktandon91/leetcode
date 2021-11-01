class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def naive():
            # not a constant space
            d = set()
            for i in range(len(nums)):
                if nums[i] in d:
                    d.remove(nums[i])
                else:
                    d.add(nums[i])
            return d.pop()
        # return naive()
        
        def optimized():
            # constant space using XOR
            ans = 0
            for elem in nums:
                ans ^= elem # ans = ans ^ elem
            return ans
        return optimized()