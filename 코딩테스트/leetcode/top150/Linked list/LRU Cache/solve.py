class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
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
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self._remove(node)
        self._add_to_tail(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._add_to_tail(node)

            return

        if len(self.cache) >= self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)


'''
class Node:
    key
    value
    prev
    next


class LRUCache:

    초기화(capacity):
        self.capacity = capacity
        self.cache = 빈 딕셔너리

        self.head = 더미 노드
        self.tail = 더미 노드

        head.next = tail
        tail.prev = head


    노드를_tail_앞에_추가(node):
        prev = tail.prev

        prev.next = node
        node.prev = prev

        node.next = tail
        tail.prev = node


    노드를_리스트에서_제거(node):
        앞노드 = node.prev
        뒷노드 = node.next

        앞노드.next = 뒷노드
        뒷노드.prev = 앞노드


    get(key):
        만약 key가 cache에 없다면:
            return -1

        node = cache[key]

        # 조회된 노드는 최근 사용된 노드가 됨
        노드를_리스트에서_제거(node)
        노드를_tail_앞에_추가(node)

        return node.value


    put(key, value):
        만약 key가 이미 cache에 있다면:
            node = cache[key]
            node.value = value

            # 수정된 노드도 최근 사용된 노드가 됨
            노드를_리스트에서_제거(node)
            노드를_tail_앞에_추가(node)

            return

        # 새로운 key를 넣어야 하는데 용량이 꽉 찬 경우
        만약 cache 크기 >= capacity 라면:
            lru = head.next

            # head.next는 가장 오래된 노드
            노드를_리스트에서_제거(lru)
            cache에서 lru.key 삭제

        # 새 노드 생성
        node = Node(key, value)

        # 딕셔너리는 key로 노드를 찾기 위한 주소록
        cache[key] = node

        # 새 노드는 최근 사용된 노드이므로 tail 앞에 추가
        노드를_tail_앞에_추가(node)

'''