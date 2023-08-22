import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price_ind = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[lowest_price_ind]:
                lowest_price_ind = i
            if prices[i] - prices[lowest_price_ind] > max_profit:
                max_profit = prices[i] - prices[lowest_price_ind]

        return max_profit
