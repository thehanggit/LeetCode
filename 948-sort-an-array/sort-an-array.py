class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    #     if len(nums) <= 1:
    #         return nums
    #     mid_index = len(nums)//2
    #     left_sort = self.sortArray(nums[:mid_index])
    #     right_sort = self.sortArray(nums[mid_index:])
    #     return self.merge(left_sort, right_sort)
        
    # def merge(self, left_sort, right_sort):
    #     left = right = 0
    #     res = []
    #     while left < len(left_sort) and right < len(right_sort):
    #         if left_sort[left] < right_sort[right]:
    #             res.append(left_sort[left])
    #             left += 1

    #         else:
    #             res.append(right_sort[right])
    #             right += 1
    #     res.extend(left_sort[left:])
    #     res.extend(right_sort[right:])
    #     return res

        if len(nums) <= 1:
            return nums
        mid_index = len(nums)//2
        left_sort = self.sortArray(nums[:mid_index])
        right_sort = self.sortArray(nums[mid_index:])
        return self.merge(left_sort, right_sort)

    def merge(self, left_sort, right_sort):
        left = right = 0
        res = []
        while left < len(left_sort) and right < len(right_sort):
            if left_sort[left] < right_sort[right]:
                res.append(left_sort[left])
                left += 1
            else:
                res.append(right_sort[right])
                right+= 1
        res.extend(left_sort[left:])
        res.extend(right_sort[right:])
        return res
    # quick sort
    # pick a pivot, partition the array, and recursively sort left and right parts
        def quicksort(start, end):
            if start >= end:
                return
            pivot = partition(start, end)
            quicksort(start, pivot-1)
            quicksort(pivot+1, end)

        def partition(left, right):
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if pivot > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        quicksort(0, len(nums) - 1)
        return nums

    