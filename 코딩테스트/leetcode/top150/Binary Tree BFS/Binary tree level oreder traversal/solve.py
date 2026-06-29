from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level_result = []

            for _ in range(level_size):
                node = queue.popleft()
                level_result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level_result)

        return result

'''
levelOrder(root)

root가 None이면
    [] 반환

queue = deque 생성
result = 결과를 저장할 리스트

queue에 root를 넣는다

queue가 비어있지 않은 동안 반복
    현재 레벨의 노드 개수 = len(queue)
    level_result = 현재 레벨의 값을 저장할 리스트

    현재 레벨의 노드 개수만큼 반복
        node = queue에서 popleft

        level_result에 node.val 추가

        node.left가 있으면
            queue에 node.left 추가

        node.right가 있으면
            queue에 node.right 추가

    result에 level_result 추가

result 반환

'''