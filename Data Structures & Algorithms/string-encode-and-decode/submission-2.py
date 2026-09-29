class Solution:

    def encode(self, strs: List[str]) -> str:
        encode=''
        for x in strs:
            count=len(str(len(x)))
            encode+=str(count)+str(len(x))+x
        print(encode)
        return encode



    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while(i<len(s)):
            digit=int(s[i])
            step=int(s[i+1:i+1+digit])
            print(digit,)
            # ans.append(s[i+1:i+1+step])
            if step>0:
                print(s[i+digit+1:i+digit+1+step])
                ans.append(s[i+digit+1:i+digit+1+step])
            else:
                print('')
                ans.append('')
            i=i+step+digit+1
        return ans


