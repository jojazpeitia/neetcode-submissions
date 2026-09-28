# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def getKth(self, groupPrev, k):
        # do cur alg here
        kth = groupPrev
        while kth and k > 0:
            kth = kth.next
            k -= 1
        return kth

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # main idea
        # find the window that we need to reverse!
        # then do the reversal on that window

        # we do this by initlaizing a cur and moving through the list k times
        # once its done k is at the end the group we need to reverse 
        # if cur becomes none when k is still going, we have reached the end, so we do nothing and just return the list!

        # problem 1, initializing the pointers to the correct spots
        # problem 2, reversing the list, and making sure it remains attached to the list

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:

            kth = self.getKth(groupPrev, k)
            if kth is None:
                break
            groupNext = kth.next

            # reverse the list!
            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                tmp = cur.next
                cur.next = prev
                prev = cur 
                cur = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp


        return dummy.next
