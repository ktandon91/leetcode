from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0] )
        merged = intervals[0]
        start = 0
        end = len(merged)-1
        for interval in intervals[1:]:
            # interval 0
            if (interval[0]) < merged[start]:
                # merged[start] = interval[0]
                if (interval[1] < merged[start]):
                    merged = interval + merged
                    end += 2
                elif (interval[1] >= merged[start]) and (interval[1] <= merged[end]):
                    merged[start] = interval[0]
                else:
                    merged = interval

            elif (interval[0] >= merged[start]) and (interval[0] <= merged[end]):
                if interval[1] >= merged[end]:
                    merged[end] = interval[1]

            else:
                merged.extend(interval)
                end+=2
        result = []
        i = 0
        while i < len(merged):
            result.append([merged[i], merged[i+1]])
            i+=2
        return result

test_case = [[1,3],[2,6],[8,10],[15,18]]
test_case_2 = [[1,4],[4,5]]
test_case3=[[1,4],[1,5]]
test_case4 = [[1,4],[0,4]]
test_case5 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
test_case6 = [[2,3],[5,5],[2,2],[3,4],[3,4]]
s = Solution()
print(s.merge(test_case6))
