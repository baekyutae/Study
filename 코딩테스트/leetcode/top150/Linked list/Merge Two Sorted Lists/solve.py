# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 헤드 부터 두 리스트의 노드들을 비교
        # 정렬된 리스트를 만들기 위한 임의의 링크드리스트를 하나 만듬
        # 비교해서 더큰쪽이 뒤로 가고 노드도 한칸 이동해서 다시비교

        temp = ListNode()
        tail = temp
        while list1 and list2:
            if list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next
                
        
            else:
                tail.next = list1
                list1 = list1.next
            
            tail = tail.next
        
        tail.next = list1 or list2

        return temp.next