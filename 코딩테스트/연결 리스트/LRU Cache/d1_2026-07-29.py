class Node:
    def __init__(self, key=0, val=0):
        self.key = key  # 조회와 추가 모두 key값으로 이루어지므로 key 저장
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache_key = {}  # key: 해당 key를 가진 node

    def _append_tail(self, key):
        node = self.cache_key[key]
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, key):
        node = self.cache_key[key]
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache_key:
            return -1

        node = self.cache_key[key]
        self._remove(key)
        self._append_tail(key)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache_key:
            node = self.cache_key[key]
            node.val = value

            self._remove(key)
            self._append_tail(key)

            return

        if len(self.cache_key) >= self.capacity:
            del_node = self.head.next
            del_key = del_node.key
            self._remove(del_key)
            del self.cache_key[del_key]

        new_node = Node(key, value)
        self.cache_key[key] = new_node
        self._append_tail(key)
