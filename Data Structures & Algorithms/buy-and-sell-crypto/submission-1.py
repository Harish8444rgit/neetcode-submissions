class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_profit=0
        buy=nums[0]
        profit=0
        for i in range(len(nums)):
            buy=min(nums[i],buy)
            max_profit=max(max_profit,nums[i]-buy)
            profit=max(profit,max_profit)
        return profit
        