class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        records = []
        for op in operations:
            if op == "+":
                records.append(records[-1]+records[-2])
            elif op == "C":
                records.pop()
            elif op == "D":
                records.append(records[-1]*2)
            else:
                records.append(int(op))
        return sum(records)

s = Solution()
print(s.calPoints(["5","2","C","D","+"]))
