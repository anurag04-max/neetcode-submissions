class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = prices[0]
        max_profit = 0
        for price in prices:
            if price < b:
                b = price
            max_profit = max(max_profit,price - b)
        return max_profit         
        