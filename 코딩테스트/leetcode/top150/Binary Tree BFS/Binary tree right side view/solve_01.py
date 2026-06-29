# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        각층에서
        가장우측에 있는 node.val을 []에 저장

        root.val 저장
        자식노드 있나?
        left, right 둘다 있으니 저장
        왼쪽부터 저장
        popleft해서 마지막 큐에 남은 node가 가장 오른쪽
        자식 여부 체크하면서 queue 에 저장
        또 queue 에서 popleft 해서 마지막 남은 node.val 저장

        '''
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                
                node = queue.popleft()
                # 현재 level에서 가장 우측 노드일때
                if i == level_size - 1 :
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result