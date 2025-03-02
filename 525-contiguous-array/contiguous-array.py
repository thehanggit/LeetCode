class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance_indicies_map = {0: -1}
        balance = 0
        length = 0
        for i in range(len(nums)):
            num = nums[i]
            if num == 1:
                balance += 1
            else:
                balance -= 1
            
            if balance in balance_indicies_map:
                length = max(length, i - balance_indicies_map[balance])
            else:
                balance_indicies_map[balance] = i
        
        return length