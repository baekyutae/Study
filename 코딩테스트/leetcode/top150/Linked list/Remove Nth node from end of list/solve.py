class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        check = head
        cur = head
        length = 0
        index = 0
        while check is not None:
            check = check.next
            length +=1

        if length == 1:
            return None
        x = length - n

        if x == 0:
            head = cur.next
            return head

        while cur is not None:
            if index == x-1:
                cur.next = cur.next.next
                return head
            else:
                index+=1
                cur = cur.next
