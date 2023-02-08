class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        maxs = [float('-inf'), float('-inf'), float('-inf')] #max1, max2, max3
        for num in nums:
            if num > maxs[0]:
                maxs[2] = maxs[1]
                maxs[1] = maxs[0]
                maxs[0] = num
            elif num > maxs[1]:
                maxs[2] = maxs[1]
                maxs[1] = num
            elif num > maxs[2]:
                maxs[2] = num
        return maxs[2] if maxs[2] != float('-inf') else maxs[0]