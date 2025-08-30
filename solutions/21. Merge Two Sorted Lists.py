# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist=None
        head=None
        tail=None
        while True:
            if list1==None or list2==None:
                break
            else:
                if list1.val>list2.val:
                    if newlist==None:
                        newlist=ListNode(list2.val,None)
                        head=newlist
                        tail=newlist
                    else:
                        tail.next=ListNode(list2.val,None)
                        tail=tail.next
                    list2=list2.next
                else:
                    if newlist==None:
                        newlist=ListNode(list1.val,None)
                        head=newlist
                        tail=newlist
                    else:
                        tail.next=ListNode(list1.val,None)
                        tail=tail.next
                    list1=list1.next

        if list1==None and list2!=None:
            if newlist!=None:
                tail.next=list2
            else:
                newlist=list2
                head=newlist
                tail=newlist
            
           

        elif list2==None and list1!=None:
            if newlist!=None:
                tail.next=list1
            else:
                newlist=list1
                head=newlist
                tail=newlist

        return head