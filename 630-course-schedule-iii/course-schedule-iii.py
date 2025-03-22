class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        maxheap = []
        # sort by the course lastday
        courses.sort(key=lambda x: x[1])
        total_time = 0

        for duration, lastday in courses:
            total_time += duration
            heapq.heappush(maxheap, -duration)

            if total_time > lastday:
                total_time += heapq.heappop(maxheap)
        return len(maxheap)