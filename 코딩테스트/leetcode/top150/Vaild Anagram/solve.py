class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_check = {}
        t_check = {}

        for i in s:
            if i in s_check:
                s_check[i] += 1

            else:
                s_check[i] = 1

        for i in t:
            if i in t_check:
                t_check[i] += 1

            else:
                t_check[i] = 1

        if s_check == t_check:
            return True
        
        else:
            return False
        