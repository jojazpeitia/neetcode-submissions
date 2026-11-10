# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not len(lists): return None
        
        # can be broken down to 2 steps!
        
        # grab a pair of lists
        # ^ if there is an odd grouping, the last list just gets added back to the bag of sorted lists
        # we create this bag of sorted lists, until it reaches a size of 1!
        # ^ then we can return that final bag
        # merge 2 sorted lists

        while len(lists) > 1:
            mergedLists = []
            # create the groupings
            # ^ low key forgot how to code this
            for i in range(0, len(lists), 2):
                if i + 1 == len(lists):
                    mergedLists.append(lists[i])
                else:
                    # perform merge 2 lists 
                    list1 = lists[i]
                    list2 = lists[i + 1]

                    dummy = ListNode()

                    # remember to have this lagging cur
                    # in order to have a poitner at end of list when run into situation
                    # where list1 or list2 dont exist
                    cur = dummy

                    while list1 and list2:
                        if list1.val <= list2.val:
                            cur.next = list1
                            cur = list1
                            list1 = list1.next
                        else:
                            cur.next = list2
                            cur = list2
                            list2 = list2.next

                    if list1:
                        cur.next = list1
                    elif list2:
                        cur.next = list2

                    mergedLists.append(dummy.next)
            lists = mergedLists

        return lists[0]











                
                    


