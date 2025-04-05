class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for i in range(len(stones)):
        #     stones[i] = -stones[i]
        
        # heapq.heapify(stones)
        # while len(stones) > 1:
        #     first = abs(heapq.heappop(stones))
        #     second = abs(heapq.heappop(stones))
        #     if first != second:
        #         remain = abs(first - second)
        #         heapq.heappush(stones, -remain)
        
        # return -stones[0] if stones else 0

        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_y = -heapq.heappop(stones)
            stone_x = -heapq.heappop(stones)
            remain = stone_y - stone_x
            heapq.heappush(stones, -remain)
        return -stones[0] if stones else 0
        