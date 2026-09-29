class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_data=set(nums)
        max_ans=1
        
        for i in nums:
            x=i
            if not x-1 in set_data:
                ans=1
                while(x+1 in set_data):
                    ans+=1
                    x+=1
                max_ans=max(max_ans,ans)
        return max_ans
                
                    


                    
        