class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            # 여는 괄호면 넣기
            if ch in '([{':
                stack.append(ch)
            # 닫는 괄호면 검사
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0