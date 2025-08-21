class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit=float(-inf)
        small=prices[0]
        for i in range(len(prices)-1):
            if prices[i+1]<small:
                small=prices[i+1]
            else:
                profit=max(profit,prices[i+1]-small)

        return profit if profit!=float(-inf) else 0
