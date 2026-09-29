class Solution:
    def one(self ,n):
        ans=0
        while(n):
            if n&1:
                ans+=1
            n=n >> 1 
        return ans
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            ans.append(self.one(i))
        return ans
            

        