class Solution:
    def topKFrequent(self, nums: List[int], t: int) -> List[int]:
        frq_count={}
        # make frq count
        # tuple frq,number 
        # sorted by freq 
        # find () k form left side elemnt return list of top k elemnt 

        for num in nums:
            frq_count[num]=frq_count.get(num,0)+1
        
        frq_list=[]
        for k,v in frq_count.items():
            frq_list.append((k,v))
        
        frq_list=sorted(frq_list,key=lambda x:x[1],reverse=True)

        ans=[]
        for i in range(t):
            ans.append(frq_list[i][0])
        return ans 

        