# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':


        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
    

    '''
    함수 LCA(현재노드, p, q):

    1. 현재노드가 비어 있으면
        → None 반환

    2. 현재노드가 p 또는 q라면
        → 현재노드 반환

    3. 왼쪽 서브트리에서 p/q/LCA를 찾는다
        → left_result

    4. 오른쪽 서브트리에서 p/q/LCA를 찾는다
        → right_result

    5. 왼쪽과 오른쪽 둘 다 결과가 있다면
        → 현재노드가 p와 q가 갈라지는 지점
        → 현재노드 반환

    6. 왼쪽에만 결과가 있다면
        → left_result 반환

    7. 오른쪽에만 결과가 있다면
        → right_result 반환

    8. 둘 다 없으면
        → None 반환
    
    '''