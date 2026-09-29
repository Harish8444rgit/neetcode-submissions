class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        already_contain=set()
        j=0
        ans=0
        for i in range(len(s)):
            while(s[i] in already_contain):
                already_contain.remove(s[j])
                j+=1
            already_contain.add(s[i])
            ans=max(ans,i-j+1)
        return ans


        