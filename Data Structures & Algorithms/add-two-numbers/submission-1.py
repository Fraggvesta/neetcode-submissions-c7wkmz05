# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        counter = 0
        while l1:
            num1 = num1 + l1.val * (10**counter)
            counter +=1
            l1 = l1.next
        num2 = 0
        counter = 0
        while l2:
            num2 = num2 + l2.val * (10**counter)
            counter +=1
            l2 = l2.next

        result = num1 + num2
        lsum = ListNode()
        head = lsum
        if result == 0:
            return lsum
        while result != 0:
            fract = result % 10
            result = result // 10
            head.val = fract
            head.next = ListNode()
            temp = head
            head = head.next
        temp.next = None

        return lsum