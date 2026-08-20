import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res=[]
        for num in nums:
            if num != 0:
                prod *= num
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        elif zero_count == 0:
            for num in nums:
                num = prod//num
                res.append(num)
            return res

        else:
            for num in nums:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res
        