class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_nums = set(nums)

        return len(nums) != len(s_nums)
        