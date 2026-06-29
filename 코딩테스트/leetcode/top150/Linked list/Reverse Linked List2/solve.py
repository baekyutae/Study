class Solution:
    def reverseBetween(
        self, 
        head: Optional[ListNode], 
        left: int, 
        right: int
    ) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        # prev: 뒤집을 구간 바로 앞 노드
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # start: 뒤집힐 구간의 첫 번째 노드
        start = prev.next

        # then: start 다음 노드
        then = start.next

        # right - left 번만큼 노드를 앞으로 빼기
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next

        return dummy.next


'''
함수 reverseBetween(head, left, right):

    dummy 노드를 만든다
    dummy.next = head

    prev = dummy

    # 1. prev를 뒤집을 구간 바로 앞 노드까지 이동
    left - 1번 반복:
        prev = prev.next

    # 2. start는 뒤집힐 구간의 첫 번째 노드
    start = prev.next

    # 3. then은 start 다음 노드
    then = start.next

    # 4. right - left번 반복하면서 then을 앞으로 뺀다
    right - left번 반복:

        # then을 원래 자리에서 제거
        start.next = then.next

        # then을 뒤집힌 구간의 맨 앞으로 연결
        then.next = prev.next

        # prev가 then을 가리키게 해서 진짜 맨 앞으로 붙임
        prev.next = then

        # 다음에 앞으로 뺄 노드 갱신
        then = start.next

    # 5. dummy.next가 최종 head
    return dummy.next

'''