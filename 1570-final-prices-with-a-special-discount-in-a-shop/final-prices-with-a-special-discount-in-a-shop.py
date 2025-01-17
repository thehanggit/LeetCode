class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = prices.copy()
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    ans[i] = prices[i] - prices[j]
                    break
        return ans