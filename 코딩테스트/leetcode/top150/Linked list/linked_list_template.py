# 링크드 리스트 템플릿
'''
설계

1. head는 첫 번째 노드를 가리킨다.
2. head는 리스트의 시작점이라 함부로 움직이면 안 된다. (cur 사용)
3. Node는 val과 next를 가진다.
4. 순회할 때는 cur = self.head로 시작한다. => 탐색용 임시 포인터, 
5. cur = cur.next로 한 칸씩 이동한다.
6. 연결할 때는 어떤 노드.next = 다른 노드로 만든다.

'''

class Node:
    def __init__(self, val):
        self.val = val  
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    def append(self, val):
        
        new_node = Node(val)
        # 노드가 없는 경우
        if self.head is None:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next is not None:
            cur = cur.next

        cur.next = new_node

        
    def prepend(self, val):

        new_node = Node(val)

        new_node.next = self.head
        self.head = new_node


    def serach(self, val):
        cur = self.head

        while cur is not None:
            if cur.val == val:
                return True
            cur = cur.next

        return False

    def delete(self, val):
        
        # 노드가 없는경우
        if self.head is None:
            return

        # 삭제하려는 노드가 head인 경우
        if self.head.val == val:
            self.head = self.head.next
            return
        
        cur = self.head
        while cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
                return 
            
            cur = cur.next

    def to_list(self):
        result = []

        cur = self.head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next

        return result