class Bucket:
    __slots__ = ("count", "keys", "prev", "next")

    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Bucket(0)
        self.tail = Bucket(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.bucket_of_key = {}

    def _insert_after(self, node, count):
        bucket = Bucket(count)
        bucket.prev = node
        bucket.next = node.next
        node.next.prev = bucket
        node.next = bucket
        return bucket

    def _detach(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev

    def inc(self, key: str) -> None:
        if key in self.bucket_of_key:
            current = self.bucket_of_key[key]
            target = current.next
            if target is self.tail or target.count != current.count + 1:
                target = self._insert_after(current, current.count + 1)
        else:
            current = None
            target = self.head.next
            if target is self.tail or target.count != 1:
                target = self._insert_after(self.head, 1)

        target.keys.add(key)
        self.bucket_of_key[key] = target

        if current is not None:
            current.keys.remove(key)
            if not current.keys:
                self._detach(current)

    def dec(self, key: str) -> None:
        current = self.bucket_of_key[key]

        if current.count == 1:
            del self.bucket_of_key[key]
        else:
            target = current.prev
            if target is self.head or target.count != current.count - 1:
                target = self._insert_after(current.prev, current.count - 1)
            target.keys.add(key)
            self.bucket_of_key[key] = target

        current.keys.remove(key)
        if not current.keys:
            self._detach(current)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))
