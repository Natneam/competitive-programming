# LINK TO THE PROBLEM => https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = dict()
        
        for log in logs:
            if log[0] not in UAM.keys():
                UAM[log[0]] = set([log[1]])
            else:
                UAM[log[0]].add(log[1])
        
        output = [0 for _ in range(k)]
        
        for key in UAM.keys():
            output[len(UAM[key]) - 1] += 1
        
        return output