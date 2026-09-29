class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq={}
        j=0
        ans=0
        count=0
        # logic is that in give string check max frq charter with how much can we replace charter in that move forword if replce charter frq<=k other wise we make move or j or srik untill the difrnt frq charter come under replacemnt
        for i in range(len(s)):
            frq[s[i]]=frq.get(s[i],0)+1
            count=max(count,frq[s[i]])
            while((i-j+1)-count>k):
                frq[s[j]]-=1
                j+=1

            ans=max(ans,i-j+1)
        return ans
        
        