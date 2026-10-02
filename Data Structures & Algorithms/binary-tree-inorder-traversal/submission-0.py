# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # traverse left
    # visit node
    # traverse right
    def inOrder(self, root, ans):
        if root is None: return

        if root.left: 
            self.inOrder(root.left, ans)

        ans.append(root.val)

        if root.right:
            self.inOrder(root.right, ans)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        self.inOrder(root ,ans)

        return ans
