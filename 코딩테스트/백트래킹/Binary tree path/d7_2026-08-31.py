class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []

        def backtracking(node):
            # 호출한 노드가 none이면 다시 반환
            if node is None:
                return

            # leaf node에 도달하면
            if node.left == None and node.right == None:
                path.append(node.val)
                result.append("->".join(map(str,path)))
                path.pop()
                return

            path.append(node.val)

            backtracking(node.left)

            backtracking(node.right)

            path.pop()

            return
        backtracking(root)

        return result
