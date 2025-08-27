class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])
        
        p1 = p2 = 0
        # the intuition is: if two time slots intersect, we check if conditions met to have a meeting.
        while p1 < len(slots1) and p2 < len(slots2):
            s1, e1 = slots1[p1]
            s2, e2 = slots2[p2]
            start = max(s1, s2)
            end = min(e1, e2)
            if end - start >= duration:
                return [start, start + duration]

            if e1 < e2:
                p1 += 1
            else:
                p2 += 1
        return []