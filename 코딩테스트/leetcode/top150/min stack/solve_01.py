'''
    def getMin(self) -> int:
        return min(self.stack)

    이 시간복잡도 O(N)이라 모든 메서드 시간복잡도 O(1)을 보장하지 못함
'''


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
        