class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        def bisear(arr, x):
            left = 0
            right = len(arr) - 1
        
            while left <= right:
                mid  = (left + right)//2
                if arr[mid] >= x:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        htl = defaultdict(list)

        for l, h in rectangles:
            htl[h].append(l)
        
        for key, value in htl.items():
            value.sort()

        ans = []
        for px, py in points:
            count = 0
            for j in range(py, 101):
                if j in htl:
                    count += len(htl[j]) - bisear(htl[j], px)
            ans.append(count)
        
        return ans
            