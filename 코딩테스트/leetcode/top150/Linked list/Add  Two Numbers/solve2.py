'''
역순으로 주어진 링크드 리스트의 원래숫자를 복원

두 숫자를 더함

다시 역순으로 링크드 리스트를 만듬

'''

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def linked_list_to_int(node):
            num = 0
            place = 1

            while node:
                num += node.val * place
                place *= 10
                node = node.next

            return num

        n1 = linked_list_to_int(l1)
        n2 = linked_list_to_int(l2)

        total = n1 + n2

        dummy = ListNode(0)
        cur = dummy

        # total이 0인 경우도 처리해야 함
        if total == 0:
            return ListNode(0)

        while total > 0:
            digit = total % 10
            cur.next = ListNode(digit)
            cur = cur.next
            total //= 10

        return dummy.next