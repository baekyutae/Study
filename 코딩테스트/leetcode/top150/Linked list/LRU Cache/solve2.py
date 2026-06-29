# ---------------------------------------------------------------------------
# 파이썬에선 OrderedDict 하나로 끝낼 수도 있다.
# (OrderedDict 내부가 이미 "dict + 이중 링크드 리스트"로 구현돼 있기 때문)
# move_to_end / popitem(last=False) 가 O(1)인 이유가 바로 그 내부 구조다.
# ---------------------------------------------------------------------------
from collections import OrderedDict


class LRUCacheOrdered:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)          # 최근으로 이동 O(1)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)   # 가장 오래된 것 제거 O(1)


if __name__ == "__main__":
    # LeetCode 예제로 두 구현 모두 검증
    for Impl in (LRUCache, LRUCacheOrdered):
        c = Impl(2)
        c.put(1, 1)
        c.put(2, 2)
        assert c.get(1) == 1      # {1=1, 2=2} -> 1 반환, 1이 최근
        c.put(3, 3)               # capacity 초과 -> key 2 제거
        assert c.get(2) == -1
        c.put(4, 4)               # key 1 제거
        assert c.get(1) == -1
        assert c.get(3) == 3
        assert c.get(4) == 4
        print(f"{Impl.__name__}: 통과")
