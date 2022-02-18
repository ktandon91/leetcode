from typing import List


class Solution:
    def corpFlightBookingsNaive(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*n
        for start, end, seats in bookings:
            for i in range(start-1, end):
                ans[i]+=seats
        return ans
    
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n+1)
        for start, end, seats in bookings:
            ans[start-1]+=seats
            ans[end]-=seats
        for i in range(1, n):
            ans[i]+=ans[i-1]
        ans.pop()
        return ans
