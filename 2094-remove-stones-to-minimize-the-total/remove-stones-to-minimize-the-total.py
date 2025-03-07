class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # heap = [-pile for pile in piles]
        # heapq.heapify(heap)
        
        # steps = 0
        # while steps < k:
        #     steps += 1
        #     x = -heapq.heappop(heap)
        #     remain_x = x - floor(x / 2)
        #     heapq.heappush(heap, -remain_x)
        
        # return -sum(heap)

        total =  sum(piles)
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k > 0:
            k -= 1
            stones = -heapq.heappop(piles)
            total -= floor(stones/2)
            heapq.heappush(piles, -(stones - floor(stones/2)))
        
        return total