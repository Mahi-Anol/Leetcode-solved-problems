class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next==None or head==None:
            head=None
        else:
            slow=head
            fast=head
            for i in range(n):
                fast=fast.next
            
            while True:
                if fast==None or fast.next==None:
                    break
                else:
                    fast=fast.next
                    slow=slow.next
            if fast==None:
                head=slow.next
            else:
                slow.next=slow.next.next
            
        return head
        