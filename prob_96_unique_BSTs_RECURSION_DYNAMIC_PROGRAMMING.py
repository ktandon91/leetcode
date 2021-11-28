class Solution:
    
    def numTrees(self, n: int) -> int:
        d = {}
        def recursive_solution(n):
            if n == 0 or n == 1:
                return 1
            
            if n in d:
                return d[n]

            total = 0
            for root in range(1, n+1):
                if (root-1) not in d:
                    d[root-1] = recursive_solution(root)
                if (n-root) not in d:
                    d[n-root] = recursive_solution(n-root)
                total += d[root-1]*d[n-root]
            d[n] = total
            return d[n]
        return recursive_solution(n)

s = Solution()
print(s.numTrees(4))
