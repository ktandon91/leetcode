class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        mapping = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for ch in key:
            if ch not in mapping and ch != " ":
                mapping[ch] = letters[i]
                i+=1

        res = ""
        for ch in message:
            new_ch = " "
            if ch != " ":
                new_ch = mapping[ch]
            res += new_ch

        return res 
