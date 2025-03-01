class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i]
            remain = target - nums[i]
            if remain in hashmap:
                return [i, hashmap[remain]]
            
            hashmap[num] = i
        return [-1, -1] 
                