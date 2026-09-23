# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0: return None
        
        # for every pair of list we do a lerge sort
        # keep doign this until we are a left with 1 sorted list

        # if a couple doesnty exist for 1 of the lists, just let it rest and append it to the merged lists

        while len(lists) > 1:

            # i + 1 is going to give us our duo
            # but we do run into the case where i + 1 doesnt exist too, so we just add it to the merged lists or whatever

            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                
                if list2:
                    mergedLists.append(self.mergeTwoLists(list1, list2))
                else:
                    mergedLists.append(list1)
            lists = mergedLists
        return lists[0]

    def mergeTwoLists(self, list1, list2):
        # do merge 2 lists here
        dummy = ListNode()
        cur = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur =  cur.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return dummy.next









