'''
BST 규칙:
왼쪽 < 현재 < 오른쪽

중위 순회:
왼쪽 → 현재 → 오른쪽

따라서:
작은 값 → 중간 값 → 큰 값 순서로 방문됨

결과:
중위 순회 결과 = 오름차순 정렬 배열
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            array.append(node.val)
            inorder(node.right)

        inorder(root)

        return array[k-1]