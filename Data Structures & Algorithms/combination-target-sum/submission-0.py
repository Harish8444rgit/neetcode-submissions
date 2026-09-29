class Solution:
    def sum_checker(self,nums,ans,temp,i,target):
        if i>=len(nums):
            if target==0:
                ans.append(temp[:])
            return 

            return ans
        if nums[i]<=target:
            temp.append(nums[i])
            target-=nums[i]
            self.sum_checker(nums,ans,temp,i,target)

            target+=nums[i]
            temp.pop()
        self.sum_checker(nums,ans,temp,i+1,target)




    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        self.sum_checker(nums,ans,[],0,target)
        return ans
        