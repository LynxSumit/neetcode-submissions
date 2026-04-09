class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        print(sorted(res.values()))
        sorted_list_based_on_values = list(dict(sorted(res.items(), key=lambda item: item[1], reverse=True)))
        return sorted_list_based_on_values[:k]
