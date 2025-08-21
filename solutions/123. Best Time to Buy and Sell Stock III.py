class Solution:                   
    def maxProfit(self, prices: List[int]) -> int:
        
        memo=[[[-1]*2 for j in range(2)] for i in prices]

        def find_profit(day:int,something_in_stock:bool,transaction:int)->int:
            if day==len(prices) or transaction==2:
                return 0            

            if memo[day][something_in_stock][transaction]!=-1:
                return  memo[day][something_in_stock][transaction]

            if something_in_stock==True:
                sell=prices[day]+find_profit(day+1,False,transaction+1)
                dont_sell=find_profit(day+1,True,transaction)
                memo[day][something_in_stock][transaction]=max(sell,dont_sell)
                return memo[day][something_in_stock][transaction]
            else:
                buy=-prices[day]+find_profit(day+1,True,transaction)
                dont_buy=find_profit(day+1,False,transaction)
                memo[day][something_in_stock][transaction]=max(buy,dont_buy)
                return memo[day][something_in_stock][transaction]
        return find_profit(0,False,0)
        