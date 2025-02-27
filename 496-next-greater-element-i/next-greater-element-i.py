class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack = []
        # hashmap = {}
        # output = []
        
        # for num in reversed(nums2):
        #     while stack:
        #         if stack[-1] > num:
        #             hashmap[num] = stack[-1]
        #             stack.append(num)
        #             break
        #         else:
        #             stack.pop()
        #     if not stack:
        #         hashmap[num] = -1
        #         stack.append(num)
                
        # for num in nums1:
        #     output.append(hashmap[num])
        # return output

        stack = []
        hashmap = {}
        res = []

        for num in nums2:
            while stack and stack[-1] < num:
                item = stack.pop()
                hashmap[item] = num
            
            stack.append(num)
        
        while stack:
            hashmap[stack.pop()] = -1
        
        for num in nums1:
            res.append(hashmap[num])
        return res


        