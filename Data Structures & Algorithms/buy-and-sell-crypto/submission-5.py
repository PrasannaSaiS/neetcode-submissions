class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0
        while l < r and r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, prices[r]-prices[l])
                r+=1
        return max_profit