# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans=[]
        for head in lists:
            cur=head
            while(cur!=None):
                ans.append(cur.val)
                cur=cur.next
        
        ans.sort()
        dummy=ListNode()
        temp=dummy
        for i in ans:
            temp.next=ListNode(i)
            temp=temp.next
        return dummy.next
        