class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            sorted_Str = tuple(sorted(string))  
            if sorted_Str not in res:
                res[sorted_Str] = []
            res[sorted_Str].append(string)

        return list(res.values())

