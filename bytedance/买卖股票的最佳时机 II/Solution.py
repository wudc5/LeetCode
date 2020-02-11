class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        size = len(prices)
        i = 0
        while i < size - 1:
            while i < size - 1 and prices[i] >= prices[i+1]:
                i += 1
            minPrice = prices[i]
            while i < size - 1 and prices[i] <= prices[i+1]:
                i += 1
            maxPrice = prices[i]
            maxProfit += (maxPrice - minPrice)
        return maxProfit
