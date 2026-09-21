# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # just iterate backweards at nth position and do remove alg??
        # edge cases include empty lists?

        length = 0 

        cur = head

        while cur:
            cur = cur.next
            length += 1

        nth = length - n

        print(nth)

        new_cur = head
        prev = head
        for i in range(nth):
            prev = new_cur
            new_cur = new_cur.next

        if nth == 0:
            head = new_cur.next

        print(prev.val, new_cur.val)

        prev.next = new_cur.next

        return head

        
        