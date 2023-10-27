class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_palindrome(s):
            return s == s[::-1]

        def find_lps_recursive(s):
            if len(s) <= 1:
                return s

            if is_palindrome(s):
                return s

            # Check both the left and right substrings
            left_lps = find_lps_recursive(s[1:])
            right_lps = find_lps_recursive(s[:-1])

            if len(left_lps) > len(right_lps):
                return left_lps
            else:
                return right_lps
            
        return find_lps_recursive(s)        
        