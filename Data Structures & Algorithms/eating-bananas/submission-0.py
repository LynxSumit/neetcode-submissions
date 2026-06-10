class Solution:
    def greatest(self, piles: List[int]) -> int:
        curr_max = piles[0]
        for pile in piles:
            curr_max = max(pile, curr_max)
        return curr_max
    def satisfy(self, piles: List[int], h: int, k: int) -> bool:
        curr_hours = 0
        for pile in piles:
            curr_hours += -(pile // -k)
            if curr_hours > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float('inf')
        l = 1
        r = self.greatest(piles)
        while l <= r:
            mid = (l+r) // 2
            if self.satisfy(piles, h, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res