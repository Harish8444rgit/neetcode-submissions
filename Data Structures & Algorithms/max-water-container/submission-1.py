class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans=0
        max_ans=0
        i=0
        j=len(heights)-1
        while(i<j):
            ans=min(heights[i],heights[j])*(j-i)
            max_ans=max(ans,max_ans)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_ans
        