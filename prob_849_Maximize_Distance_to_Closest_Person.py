class Solution:
     def maxDistToClosest(self, seats):
        n = len(seats)
        lm = 0
        rm = n-1
        best_seat_distance = 0
        for i in range(n):
            curr_seat = seats[i]
            if curr_seat == 0:
                left = i
                right = i
                left_dis, right_dis = 0, 0
                while left >= lm and right <= rm:
                    if seats[left] == 0:
                        left_dis+=1
                        left-=1
                    else:
                        left = -1
                    if seats[right] == 0:
                        right_dis+=1
                        right+=1
                    else:
                        right = n
                    best_seat_distance = max(best_seat_distance,min(left_dis, right_dis))
        return best_seat_distance

test_case = [1,0,0,0,1,0,1]
print(Solution().maxDistToClosest(test_case))
