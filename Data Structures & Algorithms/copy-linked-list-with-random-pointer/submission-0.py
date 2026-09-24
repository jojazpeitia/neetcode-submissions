"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # create a hashmap that links the floating nodes to their copy
        # not an exact link, but mentally this is how we are staying aware of the nodes and stuff

        # we need on first pass to create these nodes containing the copied values
        # we CANNOT copy the next, and random since those will be referenrece to the original list here
        
        # we instead on 2nd pass use the hashmap to connect the copied to nodes amongst each other
        # with the hashmap we can see what node goes into what other node
        
        oldToNew = { None : None }

        # 1st pass
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next

        # 2nd pass

        cur = head
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]

        