# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 탐색경로를 저장할 path
        path = []
        # 최종결과를 저장할
        result = []


        # 트리 경로 탐색 함수
        def dfs(node):
            if node is None:
                return

            if node.left is None and node.right is None:
                path.append(node.val)
                result.append("->".join(map(str,path)))
                path.pop()
                return

            path.append(node.val)

            # 좌우 자식 노드 탐색
            dfs(node.left)
            dfs(node.right)

            # 탐색했으면 한만큼 되돌리기
            path.pop()

        dfs(root)
        return result
