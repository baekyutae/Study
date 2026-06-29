class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, lower, upper):
            if node is None:
                return True

            if not (lower < node.val < upper):
                return False

            left_valid = validate(node.left, lower, node.val)
            right_valid = validate(node.right, node.val, upper)

            return left_valid and right_valid

        return validate(root, float("-inf"), float("inf"))
    

'''
isValidBST(root):

    검증용함수(node, lower, upper):

        만약 node가 None이면:
            return True

        만약 node.val이 lower보다 크고 upper보다 작은 조건을 만족하지 않으면:
            return False

        왼쪽검증 = 검증용함수(node.left, lower, node.val)
        오른쪽검증 = 검증용함수(node.right, node.val, upper)

        return 왼쪽검증 and 오른쪽검증


    return 검증용함수(root, -무한대, +무한대)

    
'''