class reverseWords:
    def reverseWords(self, s: str) -> str:
        split_s= s.split()
        split_s.reverse()
        answer = " ".join(split_s)
        return answer