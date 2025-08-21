class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo=[[-1]*2 for i in range(len(prices))]

        def findout_max_profit(day:int,stock:bool) ->int:
            if day==len(prices):
                return 0

            if memo[day][stock]!=-1:
                return memo[day][stock]

            
            if stock==True:
                sell=prices[day]+findout_max_profit(day+1,False)
                dont_sell=findout_max_profit(day+1,True)
                memo[day][stock]=max(sell,dont_sell)
                return memo[day][stock]
            else:
                buy=-prices[day] + findout_max_profit(day+1,True)
                dont_buy=findout_max_profit(day+1,False)
                memo[day][stock]=max(buy,dont_buy)
                return memo[day][stock]

        return findout_max_profit(0,False)