# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        a = head
        num = 0
        
        while a:
            a = a.next
            num+=1

        todel = num - n + 1

        if todel == 1:
            return head.next

        counter = 0
        a = head
        while a:
            counter += 1
            if counter == todel - 1:
                a.next = a.next.next
                break
            a = a.next
        return head
