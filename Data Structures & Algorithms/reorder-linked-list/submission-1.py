# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return 
        # simple solution make new with revres of that
        ans=[]
        cur=head
        while(cur!=None):
            ans.append(cur.val)
            cur=cur.next
        toggl=True
        i=0
        j=len(ans)-1
        cur=head
        while(i<=j and cur!=None):
            if toggl:
                cur.val=ans[i]
                i+=1
            else:
                cur.val=ans[j]
                j-=1
            cur=cur.next
            toggl=not toggl
        
            
        
        
        