class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []
        for i in range(len(trips)):
            arr.append((trips[i][1],1,trips[i][0]))
            arr.append((trips[i][2],-1,trips[i][0]))
        arr.sort()
        cap = 0
        for a in arr:
            if a[1] == 1:
                cap += a[2]
            else:
                cap -= a[2]
            if cap > capacity:
                return False
        return True