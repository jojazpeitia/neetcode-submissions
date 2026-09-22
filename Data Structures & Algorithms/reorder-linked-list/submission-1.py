# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # super simple in theory 
        # we find the middle
        # when we find the middle, we are actualy reveresing the stuff after it!
        # reverse 2nd half
        # merge the 2 lists/ends

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # print(slow.val)

        # slow will end up being the halfway point


        # reverse list starting from slow

        second = slow.next
        slow.next = None

        prev = None
        cur = second
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        # prev is the head of our 2nd list
        second = prev
        first = head

        # merge the two lists now

        first_nxt = None
        second_nxt = None
        while second:
            first_nxt = first.next
            first.next = second

            second_nxt = second.next
            second.next = first_nxt

            first = first_nxt
            second = second_nxt
