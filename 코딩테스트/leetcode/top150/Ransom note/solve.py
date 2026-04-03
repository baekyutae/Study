class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        for i in ransomNote:
            if i in r:
                r[i] += 1
            else:
                r[i] = 1

        m = {}
        for i in magazine:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

        for check in r:
            if check in m:
                if m[check]>=r[check]:
                    continue
                else:
                    return False
            else:
                return False
        return True
        