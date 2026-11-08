class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        for n in nums:
            if n == 0:
                zeroes += 1
        if zeroes > 1:
            return [0]*len(nums)

        if zeroes == 0:
            prod = 1
            for n in nums:
                prod *= n
            for i in range(len(nums)):
                nums[i] = prod // nums[i]
            return nums
        
        else:
            prod = 1
            for n in nums:
                if n != 0:
                    prod *= n
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            return nums
            
                