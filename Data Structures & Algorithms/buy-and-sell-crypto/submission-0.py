class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l,r = 0,1
        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit= max(max_profit, prices[r]-prices[l])
                r += 1
            else:
                l = r
                r = l+1
        return max_profit
