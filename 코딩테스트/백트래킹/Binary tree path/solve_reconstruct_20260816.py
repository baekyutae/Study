# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 걀과 저장용
        result = []
        # 탐색 경로 임시 저장용
        path = []

        # path 탐색
        def dfs(node, path):

            # 종료조건 = 하나의 경로 탐색 완료
            if node.left == None and node.right == None:
                path.append(node.val)
                str_path = "->".join(map(str, path))
                result.append(str_path)
                path.pop()
                return


            # 탐색중
            # 일단 현재 노드의 val을 path에 넣어야함
            path.append(node.val)


            # 그리고 좌우로 탐색을 해야함
            # tree가 root->left->right 순이니 왼쪽부터 탐색
            if node.left is not None:
                dfs(node.left, path)

            if not node.right == None:
                dfs(node.right, path)

            # 탐색 완료 했으면 한 부분만 되돌리기
            path.pop()


            return

        dfs(root,path)
        return result


'''
[restatement]
주어진 이진트리에서 모든 root to leaf 경로를 순서 상관없이 반환
반환 형태는 문자열에 "1 -> 2 -> 5" 와 같은 형태

[recall]
root 배열을 탐색
탐색과정에서 root to leaf 경로를 만들어감
leaf까지 탐색완료되면 result에 저장하고 한칸 위로 되돌려 우측에도 경로 있는지 확인
또 없으면 한칸 되돌리기
이런식으로 모든 경로를 탐색

[invariant]
leaf node까지 하나의 path 를 탐색후 path 의 상태는 다시 해당 경로를 탐색하기 전으로 돌아가야함

[edgecase]
1. root 가 [1]인 경우 : path에 1넣고 result에 추가후 전체 결과도 ["1"] 반환

[complexity_target]
항목               식          최악
시간               O(n + m)    O(n^2)
공간 (보조)        O(h)        O(n)
공간 (출력 포함)   O(n + m)    O(n^2)

m = result에 담긴 전체 글자 수 = 모든 leaf에 대한 경로 길이의 합
h = 트리 높이. 균형이 보장되지 않으므로 최악 n
'''
