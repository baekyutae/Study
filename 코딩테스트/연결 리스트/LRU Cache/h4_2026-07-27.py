class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_key = {}

        # 더미 노드. head 쪽이 가장 오래된 쪽, tail 쪽이 가장 최근 쪽이다.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # 리스트에 이미 들어 있는 노드만 넘어온다.
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node):
        # 리스트에 없는 노드를 맨 뒤(tail 직전)에 붙인다.
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _move_to_back(self, node):
        self._remove(node)
        self._append(node)

    def get(self, key: int) -> int:
        if key not in self.cache_key:
            return -1

        node = self.cache_key[key]
        self._move_to_back(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache_key:
            node = self.cache_key[key]
            node.val = value
            self._move_to_back(node)
            return

        if len(self.cache_key) >= self.capacity:
            oldest = self.head.next
            self._remove(oldest)
            del self.cache_key[oldest.key]

        node = Node(key, value)
        self.cache_key[key] = node
        self._append(node)
