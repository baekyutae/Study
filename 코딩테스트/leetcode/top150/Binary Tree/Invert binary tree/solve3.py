# 반복문 BFS — queue 사용

'''
queue에 root 넣기

queue가 빌 때까지:
    노드 하나 꺼냄
    그 노드의 left/right 바꿈
    바뀐 left가 있으면 queue에 넣음
    바뀐 right가 있으면 queue에 넣음
    
'''
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root