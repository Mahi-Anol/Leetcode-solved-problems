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