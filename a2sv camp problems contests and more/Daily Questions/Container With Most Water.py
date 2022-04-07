# LINK TO THE PROBLEM => https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Brut force
        #maxArea = 0
        #for i in range(len(height)):
        #    for j in range(len(height)):
        #        maxArea = max(maxArea, abs(j-i) * min(height[i], height[j]))
        #return maxArea
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left != right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea   