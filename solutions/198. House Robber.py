#top down
class Solution:
    def rob(self, nums: List[int]) -> int:

        memo=[-1]*len(nums)

        def find_profit(nums,curr):
            if curr>=len(nums):
                return 0

            if memo[curr]!=-1:
                return memo[curr]

            not_take=find_profit(nums,curr+1)
            take=nums[curr]+find_profit(nums,curr+2)

            memo[curr]=max(not_take,take)

            return memo[curr]
        return find_profit(nums,0)
    


### bottom up
class Solution:
    def rob(self, nums: List[int]) -> int:

        memo=[0]*(len(nums)+2)
        for i in range(len(nums)-1,-1,-1):
            memo[i]=max(nums[i]+memo[i+2],memo[i+1])
            # print(memo)

        return memo[0]

