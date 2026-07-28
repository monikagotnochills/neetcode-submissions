class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return True, 0

            leftBalanced, leftHeight = dfs(node.left)
            rightBalanced, rightHeight = dfs(node.right)

            return (
                leftBalanced and
                rightBalanced and
                abs(leftHeight - rightHeight) <= 1,
                1 + max(leftHeight, rightHeight)
            )

        return dfs(root)[0]