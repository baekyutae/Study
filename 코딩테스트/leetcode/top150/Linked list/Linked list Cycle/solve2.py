# floyd's cycle detection algorithm (토끼와 거북이 알고리즘)

# 포인터 2개를 서로 다른 속도로 움직여서, 사이클이 있으면 언젠가 반드시 같은 노드에서 만난다

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        # fast and fast.next 이 조건인 이유
        # 1. fast.next.next에서 에러 안 나게 하기 => fast.next 가 None이면 None.next가 되버려 None type 에러 발생
        # 2. fast가 끝에 도달하면 사이클이 없다고 판단하기
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False