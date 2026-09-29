class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        ans=nums[0]
        while(i<=j):
            mid= (j-i)//2 + i
            ans=min(ans,nums[mid])
            # sorted
            if nums[mid]>nums[i]:
                ans=min(ans,nums[i])
                i=mid+1
            else:
                ans=min(ans,nums[j])
                j=mid-1
        return ans


        