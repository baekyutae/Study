# lru cache를  double linked list로 구현

class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class Lrucache:
    def __init__(self, capacity=0):
        # lru 캐시를 구현하기 위한 링크드 리스트
        # 캐시를 조회하기 위한 딕셔너리
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def _add_to_tail(self, node):
        prev = self.tail.prev

        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    

    def _remove(self, node):
        node.prev.next= node.next
        node.next.prev = node.prev
        
        
    def put(self, key, value):
        # 이미 있던 key값이라면 
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._add_to_tail(node)

            return

        # 처음 capacity 용량 초과
        if len(self.cache) >= self.capacity:
            
            # 가장 오래된 노드를 링크드 리스트에서 제거, 
            # 캐시에서도 제거
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

        # capacity 초과도 아니고 이미 있지도 않음
        node = Node(key,value)
        self._add_to_tail(node)
        self.cache[key] = node


    def get(self, key):
        # 없는 key 값을 get 한경우
        if key not in self.cache:
            return -1
        
        # key값 반환
        # 사용했으니 맨뒤로 보내야함

        node = self.cache[key]
        self.remove(node)
        self._add_to_tail(node)
        return node.value

    