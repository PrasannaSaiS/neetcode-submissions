class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right= len(height) - 1
        l_max = 0
        r_max = 0
        amt = 0

        while left < right:
            if height[left] < height[right]:
                l_max = max(l_max, height[left])
                amt += l_max - height[left]
                left += 1
            else:
                r_max = max(r_max, height[right])
                amt += r_max - height[right]
                right -= 1 
        return amt