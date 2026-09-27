# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        temp = []

        def dfs(node):
            if node is None:
                return

            temp.append(node.val)

            if node.left is None and node.right is None:
                path = "->".join(map(str, temp))
                result.append(path)
            else:
                dfs(node.left)
                dfs(node.right)

            temp.pop()

        dfs(root)
        return result