class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i, s in enumerate(strs):
            key = sorted(s)
            if res.get(tuple(key)):
                res.get(tuple(key)).append(s)
            else:
                res[tuple(key)] = [s]
        return list(res.values())