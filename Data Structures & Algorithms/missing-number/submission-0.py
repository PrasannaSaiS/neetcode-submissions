class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        pred_sum = (n*(n+1))//2
        act_sum = sum(nums)
        return int(pred_sum - act_sum)