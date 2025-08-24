class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        ans = [[], []]
        for i in s1:
            if i not in s2:
                ans[0].append(i)
        for j in s2:
            if j not in s1:
                ans[1].append(j)

        return ans