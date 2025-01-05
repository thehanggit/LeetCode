class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0] * 1000
        for trip in trips:
            num, start, end = trip
            for i in range(start, end):
                path[i] += num
                if path[i] > capacity:
                    return False
        
        return True