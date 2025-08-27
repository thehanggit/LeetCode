class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum 
        

    def pickIndex(self) -> int:

        target = self.total_sum * random.random()
        # for i, prefix_sum in enumerate(self.prefix_sums):
        #     if target < prefix_sum:
        #         return i
        
        #binary search
        left = 0
        right = len(self.prefix_sums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()