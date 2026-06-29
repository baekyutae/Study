# 풀이 1 방문 여부 기록방식

# 모든 노드들을 set에 저장하는 방식이므로 o(n) 공간복잡도 효율이 좋지 못함
# 시간복잡도 또한 모든 노드를 방문하므로 o(n)이다.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 방문한 노드의 '참조(주소값)'를 저장할 세트
        visited = set()
        
        curr = head
        while curr is not None:
            # 현재 노드가 이미 방문한 세트에 있다면 사이클이 존재함
            if curr in visited:
                return True
            
            # 처음 보는 노드라면 세트에 추가
            visited.add(curr)
            
            # 다음 노드로 이동 (포인터 이동 필수)
            curr = curr.next
            
        return False

