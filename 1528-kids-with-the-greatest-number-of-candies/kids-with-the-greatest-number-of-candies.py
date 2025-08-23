class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great = max(candies)
        res = []
        for candy in candies:
            if candy + extraCandies >= great:
                res.append(True)
            else:
                res.append(False)

        return res