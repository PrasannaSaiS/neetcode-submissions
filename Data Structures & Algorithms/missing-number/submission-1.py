class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n
        for i, num in enumerate(nums):
            xor = xor ^ i ^ num
        return xor