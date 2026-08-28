class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eatbananas(piles: List[int], k: int) -> int:
            hr = 0
            for pile in piles:
                hr += math.ceil(pile/k)
            return hr
                
        low = 1
        high = max(piles)
        min_k = float('inf')

        while low <= high:
            mid = (low+high)//2
            if eatbananas(piles, mid) <= h:
                high = mid - 1
                min_k = min(min_k, mid)
            elif eatbananas(piles, mid) > h:
                low = mid + 1

        return min_k
