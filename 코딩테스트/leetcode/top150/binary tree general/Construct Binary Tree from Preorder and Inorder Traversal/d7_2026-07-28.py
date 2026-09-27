# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # inorder에서의 idx 찾기 편하게 딕셔너리화
        inorder_idx = {val: idx for idx, val in enumerate(inorder)}

        # preorder idx
        self.pre_idx = 0

        # 트리 생성 함수 정의
        def build(left, right):
            # 트리 생성이 더이상 안될경우
            if left > right:
                return None

            # root 노드 생성
            val = preorder[self.pre_idx]
            node = TreeNode(val)
            self.pre_idx += 1
            mid = inorder_idx[val]

            # 좌,우측 서브트리 생성
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(inorder) - 1)
