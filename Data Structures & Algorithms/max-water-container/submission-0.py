class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1      
        max_area = 0

        while left < right:            
            if heights[left] < heights[right]:
                area = (right - left) * heights[left]
                if area > max_area:
                    max_area = area
                left += 1    
            else:
                area = (right - left) * heights[right]
                if area > max_area:
                    max_area = area
                right -= 1
                    

        return max_area