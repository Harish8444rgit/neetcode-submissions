class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        # row ri rj
        # column ci cj

        ri=0
        rj=len(m)
        ci=0
        cj=len(m[0])
        ans=[]
        while(ri<rj and ci<cj):

            for x in range(ci,cj):
                ans.append(m[ri][x])
            ri+=1

            for x in range(ri,rj):
                ans.append(m[x][cj-1])
            cj-=1

            if ri<rj:

                for x in range(cj-1,ci-1,-1):
                    ans.append(m[rj-1][x])

                rj-=1
            
            if ci<cj:

                for x in range(rj-1,ri-1,-1):
                    ans.append(m[x][ci])
                ci+=1

        return ans



        