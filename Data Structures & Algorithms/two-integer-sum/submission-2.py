class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        numMap = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in seen:
                return [numMap[comp], i]
            else:
                numMap[n] = i
                seen.add(n)
