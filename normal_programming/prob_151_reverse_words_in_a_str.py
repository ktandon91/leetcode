class Solution(object):
    def reverseWordsInBuilt(self, s):
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

    def reverseWords(self, s):
        l = len(s) - 1
        reversed_str = ""
        start = None
        while l >= 0:
            if s[l] == ' ':
                if start:
                    reversed_str = reversed_str + " " + s[l+1:start+1]
                    start = None
            else:
                if not start:
                    start = l
            l-=1
        if start is not None:
            reversed_str = reversed_str + " " + s[l+1:start+1]
        return reversed_str[1::]
                    
s = Solution()
test1 = "a good   example"
print(s.reverseWords(test1))
