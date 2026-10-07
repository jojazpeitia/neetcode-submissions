# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.max_diameter = 0

        def bfs(curr):
            if not curr: return 0
            
            # code here
            left = bfs(curr.left)
            right = bfs(curr.right)

            # here we add the left and right trees to calculate diameter and just get whatever max we find
            self.max_diameter = max(self.max_diameter, left + right)

            # we only care about the longest height between left and right
            return 1 + max(left, right)


        bfs(root)
        return self.max_diameter
        