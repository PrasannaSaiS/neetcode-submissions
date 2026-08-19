from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_list = sorted(count.keys(), key =count.get, reverse = True)
        return sorted_list[:k]
        