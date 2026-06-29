# dfs로 푸는 방식
'''
오른쪽부터 DFS 한다
각 depth에서 처음 만난 노드만 저장한다
이미 그 depth 값이 result에 있으면 무시한다

'''
class Solution:
    def rightSideView(self, root):
        result = []

        def dfs(node, depth):
            if node is None:
                return

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result
