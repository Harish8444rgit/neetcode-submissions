class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        x=31
        while(n):
            bit=n&1
            n=n>>1
            ans+= 0 if bit==0 else 2**x
            x-=1

        return ans

        