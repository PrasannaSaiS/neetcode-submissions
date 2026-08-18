class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        height = 0
        width = 0
        area = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = max(area, height*width)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return area        