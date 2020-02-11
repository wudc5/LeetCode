class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size == 0:
            return 0
        result = 0
        minPrice = 999999
        for i in range(size):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if result < prices[i] - minPrice:
                result = prices[i] - minPrice
        return result
