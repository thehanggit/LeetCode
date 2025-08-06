class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tor = hare = nums[0]
        while True:
            tor = nums[tor]
            hare = nums[nums[hare]]
            if tor == hare:
                break
        
        tor = nums[0]
        while tor != hare:
            tor = nums[tor]
            hare = nums[hare]
        
        return tor
            