class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap:
        #         return [i, hashmap[complement]]
        #     else:
        #         hashmap[nums[i]] = i
        # return [-1, -1]
                
    
        # hashmap = {}
        # ans = []
        # for i, num in enumerate(nums):
        #     hashmap[num].append(i)
            
        # for num, indicies in hashmap.items():
        #     complement = target - num
        #     if complement in hashmap:
        #         if complement == num:
        #             for i in range(len(indicies)):
        #                 for j in range(i+1, len(indicies)):
        #                     ans.append([indicies[i], indicies[j]])
                
        #         elif complement < num:
        #             for i in indicies:
        #                 for j in hashmap[complement]:
        #                     ans.append([i, j])

        hashmap = defaultdict(int)
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in hashmap:
                return [i, hashmap[residual]]
            else:
                hashmap[nums[i]] = i
        return [-1, -1]
