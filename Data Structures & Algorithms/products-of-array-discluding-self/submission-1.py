class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodprfix=[1]*len(nums)
        pre_por=1
        for i in range(len(nums)-1,-1,-1):
            pre_por*=nums[i]
            prodprfix[i]=pre_por

        suf_pro=1
        ans=[]
        for i in range(len(nums)-1):
            ans.append(suf_pro*prodprfix[i+1])
            suf_pro*=nums[i]
        ans.append(suf_pro)
        return ans

