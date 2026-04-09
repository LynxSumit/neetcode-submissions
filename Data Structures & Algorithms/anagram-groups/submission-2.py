class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(m * nlogn) -> m number os strings and nlogn for sorting each item in the list 
        # res={}
        # for st in strs:
        #     sorted_str = tuple(sorted(st)) # used a tuple because a key in a hashmap can't be a list as it is mutable so we'll use tuple otherwise will get a invalid key error
        #    # print(sorted_str) # for visualisation 
        #     if sorted_str not in res:
        #         res[sorted_str] = []
        #     res[sorted_str].append(st)
        # return list(res.values())

        res = defaultdict(list)

        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(st)
        print(res.values()) # it returns dict_values but we need to return list of values 
        return list(res.values())



