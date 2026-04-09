class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_res = {}
        s_res = {}

        for i in range(len(s)):
            s_res[s[i]] = s_res.get(s[i], 0) + 1
            t_res[t[i]] = t_res.get(t[i], 0) + 1
        
        print(s_res, t_res)
        for key in s_res:
            if s_res[key] != t_res.get(key, 0):
                return False

        return True