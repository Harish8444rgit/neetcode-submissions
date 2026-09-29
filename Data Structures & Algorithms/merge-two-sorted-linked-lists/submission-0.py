# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1==None:
            return l2
        if l2==None:
            return l1
        dummy=ListNode()
        temp=dummy
        cur=l1
        curr=l2

        while(cur!=None and curr!=None):
            if cur.val<=curr.val:
                temp.next=ListNode(cur.val)
                temp=temp.next
                cur=cur.next
            else:
                temp.next=ListNode(curr.val)
                temp=temp.next
                curr=curr.next
        
        if curr:
            temp.next=curr
        if cur:
            temp.next=cur
        return dummy.next
        