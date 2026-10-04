# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # BFS
        # We are going to use a queue for this!
        # First add root,
        # pop the queue, if queue is empty, it means that level has been fully visited 
        # and we can make a list for the output

        # then add whatever children it has to the queue

        # then from there every node u meet u pop(visit) it, (left most)

        if not root: return []

        q = collections.deque()

        q.append(root)

        output = []

        while q:

            sublist = []

            if q:
                for i in range(len(q)):

                    # visit
                    node = q.popleft()
                    sublist.append(node.val)

                    # add children
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)

                output.append(sublist)

        return output



            
            
            

                
                


        