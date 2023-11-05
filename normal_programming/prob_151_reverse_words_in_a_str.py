class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        cleaned_words = []
        for word in words:
            if word:
                cleaned_words.append(word)
        
        return " ".join(cleaned_words[::-1])

s = Solution()
test1 = "  hello world  "
print(s.reverseWords(test1))
