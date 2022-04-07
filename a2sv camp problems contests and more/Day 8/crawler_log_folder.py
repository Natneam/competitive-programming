# LINK TO THE PROBLEM => https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        output = 0
        for i in logs:
            if i == '../':
                if output > 0:
                    output -= 1
            elif i == './':
                pass
            else:
                output += 1
        return output