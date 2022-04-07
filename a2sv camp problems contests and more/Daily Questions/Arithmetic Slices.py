# LINK TO THE PROBLEM => https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:        
        if len(nums) < 3:
            return 0
        
        slices = []
        
        leftPointer = 0
        rightPointer = 1
        currDiff = None
        
        while rightPointer < len(nums):
            if currDiff == None:
                currDiff = nums[leftPointer] - nums[rightPointer]
                rightPointer += 1
            
            if rightPointer >= len(nums): break
                
            if nums[rightPointer - 1] - nums[rightPointer] == currDiff:
                rightPointer += 1
            elif leftPointer + 2 == rightPointer:
                leftPointer += 1
                currDiff = None
            else:
                slices.append(rightPointer-leftPointer)
                # checking if the last element of the previous slice can be part of the next slice
                if nums[rightPointer] - nums[rightPointer + 1] == nums[rightPointer - 1] - nums[rightPointer]:
                    leftPointer = rightPointer - 1
                else:
                    leftPointer = rightPointer
                    rightPointer += 1
                currDiff = None
        # recording the last slice's length
        slices.append(rightPointer-leftPointer)

        output = 0
        for item in slices:
            output += int(((item - 2)/2 ) * (item - 1))
           
        return output
