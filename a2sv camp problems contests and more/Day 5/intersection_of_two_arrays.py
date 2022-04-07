#  LINK TO THE PROBLEM => https://leetcode.com/problems/intersection-of-two-arrays/submissions/
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) - (set(nums1) - set(nums2)))