class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1 for i in range(len(nums))]
        stack = []
        
        for k in range(2):
            for i in range(len(nums)):
                while stack and stack[-1][1] < nums[i]:
                    index, val = stack.pop()
                    ans[index] = nums[i]
                stack.append((i, nums[i]))
        return ans
            
            
                