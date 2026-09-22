# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # create a window that shifts, when r falls off, that means we are at the nth node
        # from list

        # my issue at the moment is how to end the loop

        l, r = head, head

        nth = head
        prev = head



        while l:

            # sets the right boundary of window
            for i in range(n):
                r = r.next

            if r is None:
                return head.next
                
            # shift this window until r falls of to find nth 
            while r:
                prev = l
                l = l.next
                r = r.next

            # l should be at nth node now, so we shall delete
            prev.next = l.next
            l = None

        return head



