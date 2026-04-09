class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        occurences_s = {}
        occurences_t = {}
        # storing occurences of s in disctionary_s
        for i, item in enumerate(s):
            if item in occurences_s:
                occurences_s[item] += 1
            else:
                occurences_s[item] = 1
        # storing occurences of t in disctionary_t
        for i, item in enumerate(t):
            if item in occurences_t:
                occurences_t[item] += 1
            else:
                occurences_t[item] = 1
        
        # matching the counts of dict_t and s if it is same then it is a valid annagram otherwise it's not

        for key, val in occurences_s.items():
            if occurences_t.get(key) != val:
                return False
        return True


