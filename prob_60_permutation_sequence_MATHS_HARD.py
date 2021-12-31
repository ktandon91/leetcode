""" 
    digits = [1,2,3,4]
    fact = [1,1,2,6,24,120.....] # till 9! since the constraint says n <= 9
    1. index = k % (n-1)!
    2. ans+=char(digits[index])
    3. erase used digit since each digit will be only used once.
    4. new k = k - (fact[n-1])*index
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1. Get all the digits
        digits = [(i+1) for i in range(n)]
        
        # 2. Compute factorial values of till n 
        fact = [1]*(n+1)
        for i in range(1,n+1): ###### Time Complexity O(n)
            fact[i] = i*fact[i-1]
        
        # 3. Initialize ans 
        ans = ""
        
        # 4. Iterate while we have a n digit kth permutation that we are looking for
        while n >= 1:
            # Mathematically at the most significant digit there will be n-1 permutations
            # and this permutation will reduce to n-1-i as we move along from right to left
            # eg. for n = 3, hundred's place can be filled in 6 ways. 2 each starting with 1, 2 and 3.
            # like 123, 132 starting with two 1s
            # Similary 213, 231 starting with two 2s and 312,321 starting with two 3s 
            # Considering example of 3 we realized that for n there can be n-1 possible ways a starting digit can fill the most significant digit
            # On the basis of this logic, we will find the starting digit of the ans
            
            # 5. Taking the quotient of k when divided with n-1 factorial will give us the required digit index
            index = k//fact[n-1]
            
            if k%fact[n-1] == 0:
                index -= 1
        
            # 6. add the digit to the ans.
            ans = ans+str(digits[index])
            
            # 7. remove the digit from digits since each digit will only occur once.
            digits.pop(index)
            
            # 8. Updated value of k for next iteration.
            # this is mathematical formula, by looking closer at the question
            # one may able to make sense out of this.
            k= k - (fact[n-1]*index)
            # 9. After filling one digit in the end result reduce the number and iterative fill all other digits
            n-=1
        return ans


class SolutionNaive:
    def getPermutation(self, n: int, k: int) -> str:
        def permute(nums):
            result = []
            if len(nums)==1:
                return [[nums[0]]]
            for i in range(len(nums)):
                element = nums.pop(i)
                perms = permute(nums)
                for perm in perms:
                    perm.insert(0,element)
                nums.insert(i, element)
                result.extend(perms)
            return result
        
        nums = [i+1 for i in range(n)]
        return permute(nums)

print(Solution().getPermutation(2,2))
