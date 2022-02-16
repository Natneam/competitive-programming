class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            if not stack:
                next_greater[nums2[i]] = -1
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                
                if not stack:
                    next_greater[nums2[i]] = -1
                else:
                    next_greater[nums2[i]] = stack[-1]
                
                stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(next_greater[num])
        
        return ans