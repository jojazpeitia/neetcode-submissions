# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preOrder(self, root, ans):
        if not root: return
        ans.append(root.val)
        self.preOrder(root.left, ans)
        self.preOrder(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # visit node
        # go left
        # go right

        ans = []
        self.preOrder(root, ans)
        return ans



        