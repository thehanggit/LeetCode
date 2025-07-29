class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize != 0:
        #     return False
        # dic = Counter(hand)
        # while dic:
        #     min_value = min(dic.keys())
        #     for j in range(groupSize):
        #         if min_value in dic:
        #             dic[min_value] -= 1
        #             if dic[min_value] == 0:
        #                 del dic[min_value]
        #             min_value += 1
        #         else:
        #             return False
        # return True

        # consider using heap, which would have lower time complexity
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            for i in range(groupSize):
                if count[first + i] == 0:
                    return False
                count[first + i] -= 1
                if count[first + i] == 0 and first + i != min_heap[0]:
                    heapq.heappush(min_heap, first + i)
            while min_heap and count[min_heap[0]] == 0:
                heapq.heappop(min_heap)
        return True
                
                
        