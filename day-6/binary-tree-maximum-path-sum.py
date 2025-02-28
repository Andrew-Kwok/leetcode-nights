# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root) -> int:
        if root is None:
            return 0
        left_sum, right_sum = self.dfs(root.left), self.dfs(root.right)
        self.answer = max(self.answer, left_sum + root.val + right_sum)
        return max(0, root.val + max(left_sum, right_sum))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = -math.inf
        self.dfs(root)
        return self.answer

