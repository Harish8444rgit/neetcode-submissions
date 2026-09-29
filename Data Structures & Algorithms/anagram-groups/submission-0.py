class Solution:
    def hashgenrator(self,s):
        hash=''
        count=[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
        for x in count:
            hash+=str(x)+'#'
        return hash
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_list={}
        for i in strs:
            x=self.hashgenrator(i)
            if hash_list.get(x) is not None :
                hash_list.get(x).append(i)
            else:
                hash_list[x]=[i]
        ans=[]
        for a in hash_list.values():
            ans.append(a)
        return ans
        

        