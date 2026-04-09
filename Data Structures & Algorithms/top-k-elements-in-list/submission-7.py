class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for i, item in enumerate(nums):
            if item in occurences:
                occurences[item] += 1
            else:
                occurences[item] = 1
        sorted_occurences = list(dict(sorted(occurences.items(), key=lambda item: item[1], reverse=True)).items())
        res = []
        for i in range(k):
            res.append(sorted_occurences[i][0])
        return res