# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        remain = targetSum - root.val

        if root.left is None and root.right is None:
            return remain == 0

        left_path = self.hasPathSum(root.left, remain)
        right_path = self.hasPathSum(root.right, remain)
        
        return left_path or right_path
    


'''
root가 None이면 false 반환

remain = 아래로 내려갈때마다 target-val

leaf 노드일 때 reamin 이 0인지 체크
    0이면 true 아니면 false 반환

좌측 경로로 탐색
우측 경로로 탐색

return 두경로중 하나라도 remain이 0이면 true 반환


'''