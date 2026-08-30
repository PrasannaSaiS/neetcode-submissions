class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        csum = 0
        for num in nums:
            csum += num
            maxSum = max(maxSum , csum)
            if csum < 0:
                csum = 0
        return maxSum 