class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(k):
            total = 0
            for bus in time:
                total += k // bus

            return total >= totalTrips
        
        max_time = max(time)
        left = 0
        right = max_time * totalTrips

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

        