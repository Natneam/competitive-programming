# LINK TO THE PROBELM => https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self._helper(0, n)
    
    def _helper(self, start, end):
        mid = (start + end)//2
        if isBadVersion(mid) and not isBadVersion(mid-1):
            return mid
        if not isBadVersion(mid):
            start = mid + 1
            return self._helper(start, end)
        if isBadVersion(mid):
            end = mid -1
            return self._helper(start, end)