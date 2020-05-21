class Solution(object):
    def maxProfit(self, prices):
        max_num = 0
        min_num = float('inf')
        opt = {}
        for i in range(len(prices)):
            if prices[i] < min_num:
                min_num = prices[i]
            elif prices[i] > min_num and prices[i] - min_num > max_num:
                max_num = prices[i] - min_num
        return max_num
        """
        :type prices: List[int]
        :rtype: int
        """
