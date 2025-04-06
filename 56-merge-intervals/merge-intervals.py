class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()
        # heap = []
        # heapq.heappush(heap, intervals[0])
        # ans = []
        # for i in range(1, len(intervals)):
        #     interval = heapq.heappop(heap)
        #     if interval[1] >= intervals[i][0]:
        #         new_interval = [interval[0], max(intervals[i][1], interval[1])]
        #         heapq.heappush(heap, new_interval)
        #     else:
        #         heapq.heappush(heap, intervals[i])
        #         ans.append(interval)
        # while heap:
        #     ans.append(heapq.heappop(heap))
        
        # return ans
        # intervals.sort(key=lambda x:x[0])
        # merged = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     prev = merged[-1]
        #     if prev[1] >= intervals[i][0]:
        #         prev[1] = max(prev[1], intervals[i][1])
        #     else:
        #         merged.append(intervals[i])

        # return merged
        
        # sort based on the start time
        # intervals.sort(key=lambda x: x[0])
        # merged = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     prev = merged[-1]
        #     if prev[1] >= intervals[i][0]:
        #         prev[1] = max(prev[1], intervals[i][1])
        #     else:
        #         merged.append(intervals[i])
        
        # return merged


        # first sort the intervals based on start_date
        # second find out if the end date conflicts with the next interval's start date, if so, merge, otherwise, append it into result
        intervals.sort(key=lambda x:x[0])
        merge = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_end = merge[-1][1]
            next_start = intervals[i][0]
            if prev_end >= next_start:
                merge[-1][1] = max(intervals[i][1], prev_end)
            else:
                merge.append(intervals[i])
        return merge






