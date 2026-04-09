class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for st in strs:
            res_str += str(len(st)) + "#" + st
        return res_str

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            strs.append(s[j+1 : j + 1 + length])
            i  = j + 1 + length
        return strs




