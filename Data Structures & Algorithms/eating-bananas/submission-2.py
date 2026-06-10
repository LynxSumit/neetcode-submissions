class Solution:
    def satisfy(self, piles: List[int], h: int, k: int) -> bool:
        curr_hours = 0
        for pile in piles:
            curr_hours += math.ceil(pile / k)
            if curr_hours > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            k = (l+r) // 2
            if self.satisfy(piles, h, k):
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res