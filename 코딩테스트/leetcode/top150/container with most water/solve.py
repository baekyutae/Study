class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        current_max = 0
        while left < right:
            water = (right - left)*min(height[left],height[right])
            current_max = max(water, current_max)
            if height[left] > height[right]:
                right -=1

            else:
                left +=1

        return current_max