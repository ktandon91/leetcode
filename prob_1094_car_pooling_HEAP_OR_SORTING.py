from typing import List


class Solution:
    def carPoolingSorting(self, trips: List[List[int]], capacity: int) -> bool:
        bookings = []
        for curr_capacity, start, end in trips:
            bookings.append((start, curr_capacity))
            bookings.append((end, -curr_capacity))
        bookings.sort()
        curr_capacity = 0
        for booking in bookings:
            curr_capacity+=booking[1]
            if curr_capacity > capacity:
                return False
        return True

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops_capacity = [0] *(1000+1)
        for curr_capacity, start, end in trips:
            stops_capacity[start]+=curr_capacity
            stops_capacity[end]-=curr_capacity
        for stop_capacity in stops_capacity:
            if stop_capacity != 0:
                capacity-=stop_capacity
                if capacity < 0:
                    return False
        return True
    
    def carPoolingheap(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for n, i, j in trips:
            heapq.heappush(heap, (j, -n))
            heapq.heappush(heap, (i, n))
        while heap:
            capacity -= heapq.heappop(heap)[1]    
            if 0 > capacity:
                return False
        return True

trips = [[2,1,5],[3,3,7]]
capacity = 4

print(Solution().carPooling(trips, capacity))
