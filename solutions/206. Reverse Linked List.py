class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        else:
            curr=head
            left=None
            while True:
                if curr==None:
                    break
                if curr.next==None:
                    head=curr
                
                right=curr.next
                curr.next=left
                left=curr
                curr=right
            return  head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=head
        if temp==None or temp.next==None:
            return temp
        else:
            curr=temp
            reversed=self.reverseList(temp.next)
            curr.next.next=curr
            curr.next=None
            return reversed

        