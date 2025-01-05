class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        hashmap = defaultdict(int)
        for trip in trips:
            num, start, end = trip
            for i in range(start, end):
                hashmap[i] += num
                if hashmap[i] > capacity:
                    return False
        
        return True