# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        ahead=head
        pre=None
        for i in range(n):
            ahead=ahead.next
        if ahead==None:
            return head.next
        cur=head
        while(ahead!=None):
            pre=cur
            ahead=ahead.next
            cur=cur.next


        pre.next=cur.next
        return head
    
        