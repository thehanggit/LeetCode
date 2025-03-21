class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        heap = []
        heapq.heappush(heap, intervals[0])
        ans = []
        for i in range(1, len(intervals)):
            interval = heapq.heappop(heap)
            if interval[1] >= intervals[i][0]:
                new_interval = [interval[0], max(intervals[i][1], interval[1])]
                heapq.heappush(heap, new_interval)
            else:
                heapq.heappush(heap, intervals[i])
                ans.append(interval)
        while heap:
            ans.append(heapq.heappop(heap))
        
        return ans


