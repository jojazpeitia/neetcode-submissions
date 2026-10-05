# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        # same idea as previous problem, where we created list for every level
        # instead we just return the right most of each level order

        q = collections.deque()

        q.append(root)

        level_lists = []
        ans = []

        while q:

            level = []
            for i in range(len(q)):
                # visit the node
                node = q.popleft()
                if node: level.append(node.val)

                # add its children if they exist
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level_lists.append(level)

        for level in level_lists:
            ans.append(level[-1])

        return ans

        
            