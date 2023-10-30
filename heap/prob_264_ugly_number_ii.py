import heapq

class Solution:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber1(self, n):
        return self.ugly[n-1]

    def nthUglyNumber(self, n):
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2.append(2 * u)
                q3.append(3 * u)
                q5.append(5 * u)


s = Solution()
print(s.nthUglyNumber(3))
