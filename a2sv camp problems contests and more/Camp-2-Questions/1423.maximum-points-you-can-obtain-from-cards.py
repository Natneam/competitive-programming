#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        possible_sum = sum(cardPoints[0:k])
        new_sum = possible_sum

        for i in range(k):
            new_sum = new_sum - cardPoints[k-i - 1]
            new_sum = new_sum + cardPoints[len(cardPoints) - i - 1]
            possible_sum = max(possible_sum, new_sum)
        return possible_sum

# @lc code=end

