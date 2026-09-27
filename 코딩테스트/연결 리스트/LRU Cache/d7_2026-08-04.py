class Process:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # dummy head와 tail 생성
        self.head = Process()
        self.tail = Process()
        self.head.next = self.tail
        self.tail.prev = self.head

        # key값으로 프로세스를 꺼내 쓰기위한 dict
        self.cache_key = {}

    # 프로세스를 리스트에서 지우는 함수
    def remove(self, key):
        process = self.cache_key[key]
        process.prev.next = process.next
        process.next.prev = process.prev

    # 프로세스를 사용하여 리스트 맨뒤에 추가하는 함수
    def append_tail(self, key):
        process = self.cache_key[key]
        prev = self.tail.prev

        prev.next = process
        process.prev = prev
        process.next = self.tail
        self.tail.prev = process

    def get(self, key: int) -> int:
        # key값이 존재하지 않는다면
        if key not in self.cache_key:
            return -1

        # 존재한다면 프로세스의 val을 반환 및 리스트 뒤로 이동
        process = self.cache_key[key]
        self.remove(key)
        self.append_tail(key)

        return process.val

    def put(self, key: int, value: int) -> None:
        # key값이 존재한다면 갱신
        if key in self.cache_key:
            process = self.cache_key[key]
            process.val = value  # 갱신

            # 사용했으니 맨뒤로 이동
            self.remove(key)
            self.append_tail(key)

            return

        # capacity를 초과하려 한다면
        if len(self.cache_key) >= self.capacity:
            # 가장 오래된 프로세스를 식별후 리스트와 cache_key에서 제거
            old_process = self.head.next
            old_key = old_process.key

            self.remove(old_key)
            del self.cache_key[old_key]

        # 프로세스 생성 및 추가
        new_process = Process(key, value)
        self.cache_key[key] = new_process
        self.append_tail(key)
