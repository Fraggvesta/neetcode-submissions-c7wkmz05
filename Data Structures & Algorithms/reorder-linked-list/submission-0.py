# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        a = head
        length = 0
        while a:
            a = a.next
            length += 1
        
        a = head
        for i in range(length // 2):
            a = a.next

        prev = None
        curr = a.next
        a.next = None  
        
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        

        a = prev
        b = head
        
        while a:
            temp1 = b.next
            temp2 = a.next
            
            b.next = a
            a.next = temp1
            
            b = temp1
            a = temp2

            
        
        