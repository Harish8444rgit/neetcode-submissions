class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq={}
        j=0
        ans=0
        count=0
        for i in range(len(s)):
            frq[s[i]]=frq.get(s[i],0)+1
            count=max(count,frq[s[i]])
            while((i-j+1)-count>k):
                frq[s[j]]-=1
                j+=1

            ans=max(ans,i-j+1)
        return ans
        
        