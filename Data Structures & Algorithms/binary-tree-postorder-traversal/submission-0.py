# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrder(self, root, ans):
        if not root: return

        self.postOrder(root.left, ans)
        self.postOrder(root.right, ans)
        ans.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # left 
        # right
        # visit if no left and no right

        # always takes left as priority, if right exists it will take it once no more left

        ans = []
        self.postOrder(root, ans)
        return ans


        