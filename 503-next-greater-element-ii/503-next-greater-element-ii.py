class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums + nums
        stack = []
        
        for i in range(len(nums) - 1, -1, -1 ):
            if not stack:
                nums[i] = -1
                stack.append(nums[i])
            else:
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                
                val = nums[i]
                if not stack:
                    nums[i] = -1
                else:
                    nums[i] = stack[-1]
                stack.append(val)
        return nums[:len(nums)//2]
                