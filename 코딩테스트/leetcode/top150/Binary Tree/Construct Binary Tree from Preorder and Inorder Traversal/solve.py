# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder 값의 위치를 빠르게 찾기 위한 dict
        inorder_index = {}

        for i, val in enumerate(inorder):
            inorder_index[val] = i

        self.pre_idx = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            # inorder[left:right] 범위 안에서 트리를 만든다고 생각
            if left > right:
                return None

            # preorder에서 현재 위치의 값이 root
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            # inorder에서 root 위치 찾기
            mid = inorder_index[root_val]

            # inorder 기준으로 왼쪽은 left subtree
            root.left = build(left, mid - 1)

            # inorder 기준으로 오른쪽은 right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
    

    '''
    buildTree(preorder, inorder):

    inorder에서 각 값의 위치를 빠르게 찾을 수 있게 기록한다
    preorder에서 다음 root를 가리킬 포인터 pre_idx = 0 으로 둔다

    함수 build(left, right):
        # 의미:
        # inorder의 left ~ right 범위로 만들 수 있는 subtree를 만든다

        만약 left > right 라면:
            만들 노드가 없으므로 None 반환

        preorder[pre_idx]를 현재 subtree의 root 값으로 사용한다
        pre_idx를 1 증가시킨다

        root 노드를 만든다

        inorder에서 root 값의 위치 mid를 찾는다

        root의 왼쪽 자식 =
            inorder의 left ~ mid - 1 범위로 subtree 만들기

        root의 오른쪽 자식 =
            inorder의 mid + 1 ~ right 범위로 subtree 만들기

        root 반환

    전체 inorder 범위인 build(0, len(inorder) - 1)을 호출한다
    
    
    '''