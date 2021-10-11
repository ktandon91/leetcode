class Solution:
    def threeSumClosest(self, nums, target) -> int:
        # Sort the num in ascending order
        nums.sort()

        # Get sum of top 3 lower valued elements
        minimum_sum = nums[0] + nums[1] + nums[2]

        # return minimum sum if it's equal to target
        if minimum_sum == target:
            return target

        # Iterate over array
        # First fix 1 element, then move second and third basis condition
        # Fixing one element using index i and since we need total of 3 elements
        # i will run from 0 to len(nums) - 2
        for i in range(0, len(nums) - 2):

            # After fixing i create two pointer j and k
            # j will track least valued element after i and k will track highest valued      element from last
            j = i + 1
            k = len(nums) - 1

            while j < k:
                # sum all 3 elements from i, j and k
                intermediate_sum = nums[i] + nums[j] + nums[k]

                # Check if intermediate_sum is equal to target then return target
                if intermediate_sum == target:
                    return target

                # If intermediate sum is not equal to target check whether minimum_sum is closer or intermediate_sum is closer to the target
                # if intermediate sum is closer then swap the value of minimum sum
                if abs(intermediate_sum - target) < abs(minimum_sum - target):
                    minimum_sum = intermediate_sum

                # move j, k based on conditions
                if intermediate_sum > target:
                    # means we have to reduce the value and since array is sorted right most element will be highest and it might be a good idea to replace that will lower valued element therefore move k.
                    k -= 1
                elif intermediate_sum < target:
                    # when intermediate_summ < target:
                    # it might be a good idea to try with bigger values
                    j += 1
        return minimum_sum


s = Solution()
print(s.threeSumClosest([0, 2, 1, -3], 1))
